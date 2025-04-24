# Copyright 2021 Siemens Corporation
# Copyright 2025 Su Chenhui
# SPDX-License-Identifier: MIT

"""
Todo:
    1. PV参考解博的实现，添加进去

Improve:
    1. 修改时间步长
    2. 绕开csv设置电池（使用circuit已有add_batteries），添加EV电池的接入和断开操作（参考EVChargingStaion）
    3. 各类适配

在python中定义各种元器件的特性，使用 OpenDSS 进行电力系统仿真。

Circuits 类：整个电力网络的核心管理类
    管理电力网络组件（线路、变压器、调节器等）
    编译和重置电路状态
    控制电容器、调节器和电池等设备的状态
    计算电压、电流和损耗等指标
    添加电力系统组件
边缘组件：
    Edge：连接两个母线的基类
    Line：电力线路，具有电阻、电抗和电容矩阵
    Transformer：标准变压器
    Regulator：电压调节器，具有分接头设置
节点组件：
    Node：连接到母线的基类
    Load：负载节点，具有电压、有功和无功功率属性
    Capacitor：可控电容器组，具有开关状态
    Battery：电池设备，具有充放电控制功能 Note: 电池分为储能电池和EV电池
"""

import dss as opendss
import networkx as nx
import numpy as np
import os
import pandas as pd
from pathlib import Path
from collections import deque


class Circuits:
    """Circuits 类：电力系统的核心管理类

    管理电力系统元件（线路、变压器、变压器抽头等）

    1. 编译和重置电路状态
    2. 获取电容器、调节器和电池等设备的状态
    3. 获取电压、电流、损耗、总功率
    4. 添加lines、transformers、regulators、loads、capacitors和batteries
    """

    def __init__(self, dss_file, batt_file='Battery.csv', RB_act_num=(33, 33), dss_act=False):
        # DSS
        self.dss = opendss.DSS  # the dss simulator object
        self.dss_file = dss_file  # path to the dss file for the whole circuit
        self.dss_act = dss_act  # whether to use OpenDSS controllers defined in the circuit file

        # 电池文件路径 which is used to initialize the battery objects
        self.batt_file = os.path.join(Path(self.dss_file).parent, batt_file)
        if not os.path.exists(self.batt_file):
            self.batt_file = ''

        self.topology = nx.Graph()
        self.edge_obj = dict()  # map from frozenset({bus1, bus2}) to the (active) object on the edge
        self.dup_edges = dict()  # map from duplicate edge (if any) to the objects on the edge
        self.edge_weight = dict()  # map from edge to Ymatrix. Ymatrix is symmetric/tall if the number of phases is equal/different
        self.bus_phase = dict()  # map from bus name to the number of phases.
        self.bus_obj = dict()  # map from bus name to the objects(load,capacitor,batteries) on the bus

        # circuit element
        self.lines = dict()
        self.transformers = dict()
        self.regulators = dict()
        self.loads = dict()
        self.capacitors = dict()
        self.batteries = dict()   # 存储所有电池
        # 添加以示区分
        self.storage_batteries = dict()  # storage batteries
        self.ev_batteries = dict()  # EV batteries

        # regulator and battery action dim
        self.reg_act_num, self.bat_act_num = RB_act_num

        # initialization
        self.initialize()  # 初始化过程使用 _gen_bat_obj 从csv文件添加
        self.storage_batteries.update(self.batteries)  # 对初始电池字典进行浅拷贝

        # 添加对EV充电站的可引用性
        self.ev_controller = None
        self.ev_station = None

    def set_all_batteries_before_solve(self, nkws_or_states, change_dss=True):
        """
        设置所有电池（包括储能电池和EV电池）的状态
        ( Run this function before each solve() )
        Args:
            nkws_or_states: array of nkws or states
                 nkw: continuous battery's normalized discharge power in [-1, 1]
                 state: discrete battery's discharge state in [0, len(avail_kw)-1]
            change_dss: 是否在dss中修改电池的kw和kvar
        Returns:
            the absolute change of states in integers
        """
        # 原校验过程
        # assert len(nkws_or_states) > 0 and len(nkws_or_states) == len(self.batteries), 'inconsistent states'

        # 将智能体的输出转换为合法的电池功率控制
        if self.bat_act_num == np.inf:  # 连续空间
            nkws_or_states = np.array(nkws_or_states, dtype=np.float32)
        else:
            nkws_or_states = np.array(nkws_or_states, dtype=int)

        # 为适配场景（EV连接点未满），添加额外处理
        # 初始化电池功率字典
        bat2kwkvar = dict()
        # 1. 先处理静态储能电池
        for i, bat_name in enumerate(self.storage_batteries.keys()):
            if bat_name in self.batteries:  # 确保电池存在
                batt = self.batteries[bat_name]
                kw = batt.state_projection(nkws_or_states[i])  # projection
                kvar = kw / batt.pf
                bat2kwkvar[batt.name[8:]] = (kw, kvar)  # remove the header 'Battery.'

        # 2. 处理EV电池
        if hasattr(self, 'ev_station') and self.ev_station is not None:
            static_battery_count = len(self.storage_batteries)

            # 遍历所有EV连接点位置
            for j in range(self.ev_station.num_connection_points):
                idx_in_nkws_or_states = static_battery_count + j

                # 跳过超出动作空间的部分
                if idx_in_nkws_or_states >= len(nkws_or_states):
                    continue

                # 查找连接到此连接点的EV
                ev_idx = None
                for battery_idx, connection_id in self.ev_station.battery_connection_points.items():
                    if connection_id == j and battery_idx in self.ev_station.connected_batteries:
                        ev_idx = battery_idx
                        break

                if ev_idx is not None:  # 如果有EV连接到此连接点
                    ev_name = self.ev_station.connected_batteries[ev_idx]
                    full_name = f"Battery.{ev_name}" if not ev_name.startswith("Battery.") else ev_name

                    if full_name in self.batteries:
                        batt = self.batteries[full_name]
                        kw = batt.state_projection(nkws_or_states[idx_in_nkws_or_states])
                        kvar = kw / batt.pf
                        bat2kwkvar[batt.name[8:]] = (kw, kvar)
        # # 原设置电池对象
        # bat2kwkvar = dict()
        # for i, bat in enumerate(self.batteries.keys()):  # 索引，key
        #     batt = self.batteries[bat]
        #     kw = batt.state_projection(nkws_or_states[i])  # projection
        #     kvar = kw / batt.pf
        #     bat2kwkvar[batt.name[8:]] = (kw, kvar)  # remove the header 'Battery.'

        # 在dss中修改kw和kvar，遍历顺序接近创建顺序，但似乎无明确定义
        if change_dss:
            dssGen = self.dss.ActiveCircuit.Generators
            if dssGen.First == 0:  # 没有这类对象
                return
            while True:
                if dssGen.Name in bat2kwkvar:
                    kw, kvar = bat2kwkvar[dssGen.Name]
                    dssGen.kW = kw
                    dssGen.kvar = kvar
                    print(dssGen.Name, dssGen.kW, dssGen.kvar)
                if dssGen.Next == 0:  # 没有下一个这类对象
                    break

        # run solve() afterward

    def set_all_batteries_after_solve(self):
        """
        更新所有电池(储能电池和EV电池)的kwh和soc，基于DSS对象中的实际功率。
        ( Run this function after each solve() )

        Args: None
        Returns: soc 变化 和 discharge 变化
        """
        # 为适配场景（EV连接点未满），添加额外处理
        # 使用storage_batteries获取初始化时存储的静态电池
        total_actions = len(self.storage_batteries)

        if hasattr(self, 'ev_station') and self.ev_station is not None:
            total_actions += self.ev_station.num_connection_points  # 添加固定数量的EV连接点

        # 初始化状态变化数组，固定大小
        soc_errs = np.zeros(total_actions)
        discharge_errs = np.zeros(total_actions)

        # 1. 更新静态储能电池err状态并记录变化
        for i, bat_name in enumerate(self.storage_batteries.keys()):
            if bat_name in self.batteries:  # 确保电池存在
                batt = self.batteries[bat_name]
                batt.kwh += batt.actual_power() * batt.duration
                batt.kwh = round(max(0.0, min(batt.max_kwh, batt.kwh)))
                batt.soc = batt.kwh / batt.max_kwh
                soc_errs[i] = abs(batt.soc - batt.initial_soc)

                if self.bat_act_num == np.inf:
                    discharge_errs[i] = max(0.0, batt.kw) / batt.max_kw
                else:
                    discharge_errs[i] = max(0.0, batt.avail_kw[batt.state]) / batt.max_kw

        # 2. 更新EV电池err状态
        if hasattr(self, 'ev_station') and self.ev_station is not None:
            static_battery_count = len(self.storage_batteries)

            # 对所有EV连接点位置，无论是否有EV连接，都更新对应位置的状态变化数组
            for j in range(self.ev_station.num_connection_points):
                idx_in_bat_errs = static_battery_count + j

                # 查找连接到此连接点的EV
                ev_idx = None
                for battery_idx, connection_id in self.ev_station.battery_connection_points.items():
                    if connection_id == j and battery_idx in self.ev_station.connected_batteries:
                        ev_idx = battery_idx
                        break

                if ev_idx is not None:  # 如果有EV连接到此连接点
                    ev_name = self.ev_station.connected_batteries[ev_idx]
                    full_name = f"Battery.{ev_name}" if not ev_name.startswith("Battery.") else ev_name

                    if full_name in self.batteries:  # 确保电池存在
                        batt = self.batteries[full_name]
                        batt.kwh += batt.actual_power() * batt.duration
                        batt.kwh = round(max(0.0, min(batt.max_kwh, batt.kwh)))
                        batt.soc = batt.kwh / batt.max_kwh
                        soc_errs[idx_in_bat_errs] = abs(batt.soc - batt.initial_soc)

                        if self.bat_act_num == np.inf:
                            discharge_errs[idx_in_bat_errs] = max(0.0, batt.kw) / batt.max_kw
                        else:
                            discharge_errs[idx_in_bat_errs] = max(0.0, batt.avail_kw[batt.state]) / batt.max_kw
                # 如果没有EV连接，这个位置的soc_errs和discharge_errs保持为0

        # 原处理过程
        # soc_errs, discharge_errs = np.zeros(len(self.batteries)), np.zeros(len(self.batteries))
        # for i, bat in enumerate(self.batteries):
        #     batt = self.batteries[bat]
        #     batt.kwh += batt.actual_power() * batt.duration
        #     # enforce capacity constraint and round to integer
        #     batt.kwh = round(max(0.0, min(batt.max_kwh, batt.kwh)))
        #     batt.soc = batt.kwh / batt.max_kwh
        #     soc_errs[i] = abs(batt.soc - batt.initial_soc)
        #
        #     if self.bat_act_num == np.inf:
        #         discharge_errs[i] = max(0.0, batt.kw) / batt.max_kw
        #     else:
        #         discharge_errs[i] = max(0.0, batt.avail_kw[batt.state]) / batt.max_kw
        return soc_errs, discharge_errs

    def set_regulator_parameters(self, tap=1.1, mintap=0.9, maxtap=1.1):
        """
        Set all regulator parameters to the same predefined values

        Args:
           tap: tap value in between mintap and maxtap
           maxtap: max tap value
           mintap: min tap value

        Returns: None
        """
        # run this after Text.Command = "compile" and before ActiveCircuit.Solution.Solve()

        ## numtaps: number of tap values between mintap and maxtap.
        ##          reg_act_num = numtaps + 1
        numtaps = self.reg_act_num - 1
        fea = [mintap, maxtap, numtaps]
        transet = set()
        for regname in self.regulators.keys():
            self.regulators[regname].tap_feature = fea.copy()
            self.regulators[regname].tap = tap
            transet.add(regname[10:])

        dssTrans = self.dss.ActiveCircuit.Transformers
        if dssTrans.First == 0:
            return  # no such kind of object
        while True:
            if dssTrans.Name in transet:
                dssTrans.Tap = tap
                dssTrans.MinTap = mintap
                dssTrans.MaxTap = maxtap
                dssTrans.NumTaps = numtaps
            if dssTrans.Next == 0:
                break

    def compile(self, disable=False):
        """
        Compile the main dss file

        Args:
            disable: disable sources and loads during solve.
                     This is used when computing the admittance matrix (Ymat)

        Returns: None
        """
        self.dss.Text.Command = "compile " + self.dss_file
        self.dss.Text.Command = "Set Maxiterations=50"
        self.dss.Text.Command = "Set Maxcontroliter=100"

        if disable:
            self.dss.Text.Command = 'vsource.source.enabled=no'
            self.dss.Text.Command = 'batchedit load..* enabled=no'
        else:
            self.dss.Text.Command = 'vsource.source.enabled=yes'
            self.dss.Text.Command = 'batchedit load..* enabled=yes'

        if not self.dss_act:
            self.dss.Text.Command = "Set ControlMode = off"

    def reset(self):
        """
        Reset the circuit to the original state. This includes:
        """
        self.compile()  # this includes resetting regulators in dss
        # capacitors in dss and batteries in dss
        # reset regulator, capacitors and batteries in objects
        self.set_regulator_parameters()
        self.set_all_capacitor_statuses([1] * len(self.capacitors), change_dss=False)
        for bat in self.batteries.keys():
            self.batteries[bat].reset()
        # self.dss.ActiveCircuit.Solution.Solve()
        self.dss.ActiveCircuit.Solution.SolveNoControl()

    def initialize(self, noWei=True):
        """
        Compile and generate all data members.

        Args:
            noWei: don't compute the admittance matrix (Ymat), stored as self.edge_weight

        Returns: None
        """

        if not noWei:
            self.compile(disable=True)
            self.__cal_edgeWei_busPhase(noWei=noWei)
            self.compile(disable=False)
        else:
            self.compile(disable=False)
            self.__cal_edgeWei_busPhase(noWei=noWei)

        # edges
        regulators, valid_trans2edge, line2edge = self._get_edge_name()
        self._gen_reg_obj(regulators)
        self._gen_trans_obj(valid_trans2edge)
        self._gen_line_obj(line2edge)
        self.set_regulator_parameters()

        # nodes
        self._gen_load_cap_obj()
        if self.batt_file != '':
            self._gen_bat_obj()

        # self.dss.ActiveCircuit.Solution.Solve()
        self.dss.ActiveCircuit.Solution.SolveNoControl()

    def get_all_capacitor_statuses(self):
        """
        Get taps of all regulators

        Returns:
            capacitor statuses (dict)
        """
        states = dict()
        dssCap = self.dss.ActiveCircuit.Capacitors
        if dssCap.First == 0:
            return  # no such object
        while True:
            states['Capacitor.' + dssCap.Name] = dssCap.States[0]
            if dssCap.Next == 0: break
        return states

    def set_all_capacitor_statuses(self, statuses, change_dss=True):
        """
        Set statuses of all capacitors

        Args:
            statuses: array of 0-1 integers

        Returns:
            the absolute change of statuses
        """
        assert len(statuses) > 0 and len(statuses) == len(self.capacitors), 'inconsistent statuses'
        statuses = np.array(statuses, dtype=int)

        # set capacitor objects
        diff = np.zeros(len(statuses))
        cap2st = dict()
        for i, cap in enumerate(self.capacitors.keys()):
            capa = self.capacitors[cap]
            diff[i] = abs(capa.status - statuses[i])
            capa.status = statuses[i]
            cap2st[capa.name[10:]] = statuses[i]

        # set dss object
        if change_dss:
            dssCap = self.dss.ActiveCircuit.Capacitors
            if dssCap.First == 0: return  # no such object
            while True:
                if dssCap.Name in cap2st:
                    dssCap.States = [cap2st[dssCap.Name]]
                if dssCap.Next == 0: break
        return diff

    def get_all_regulator_tapnums(self):
        """
        Get tapnums of all regulators

        Returns:
            regulator tapnums (dict)
        """
        mintap, maxtap, numtaps = self.regulators[next(iter(self.regulators))].tap_feature
        step = (maxtap - mintap) / numtaps

        # get trans name
        trans = {regname[10:] for regname in self.regulators.keys()}

        # get taps from dss
        tapnums = dict()
        dssTrans = self.dss.ActiveCircuit.Transformers
        if dssTrans.First == 0:
            return  # no such kind of object
        while True:
            if dssTrans.Name in trans:
                tapnums['Regulator.' + dssTrans.Name] = int((dssTrans.Tap - mintap) / step)
            if dssTrans.Next == 0: break

        return tapnums

    def set_all_regulator_tappings(self, tapnums, change_dss=True):
        """
        Set tap values of all regulators

        Args:
            tapnums: array of integers in [0, numtaps]

        Returns:
            the absolute change of tapnums
        """
        assert len(tapnums) > 0 and len(tapnums) == len(self.regulators), 'inconsistent tapnums'
        mintap, maxtap, numtaps = self.regulators[next(iter(self.regulators))].tap_feature
        step = (maxtap - mintap) / numtaps
        tapnums = np.maximum(0, np.minimum(numtaps, np.array(tapnums, dtype=int)))
        taps = tapnums * step + mintap

        # set regulator objects
        diff = np.zeros(len(taps))
        trans2tap = dict()
        for i, reg in enumerate(self.regulators.keys()):
            regu = self.regulators[reg]
            diff[i] = abs((regu.tap - taps[i]) / step)
            regu.tap = taps[i]
            # remove 'Regulator.' from the head of the name
            trans2tap[reg[10:]] = (taps[i], tapnums[i])

        # set dss
        if change_dss:
            dssTrans = self.dss.ActiveCircuit.Transformers
            if dssTrans.First == 0: return  # no such kind of object
            while True:
                if dssTrans.Name in trans2tap:
                    tap, tapnum = trans2tap[dssTrans.Name]
                    dssTrans.NumTaps = tapnum
                    dssTrans.Tap = tap
                if dssTrans.Next == 0:
                    break
        return diff

    def _get_edge_name(self):
        """
        Compute the object names on all edges.

        Args: None

        Returns:
            regulators [dict]: map from edge to all transformers and regcontrols of a regulator.
            valid_trans2edge [dict]: map from non-regulator transformers to edge
            line2edge [dict]: map from line to edge
        """

        def get_edge(type_name, ignore_duplicate=False):
            self.dss.ActiveCircuit.SetActiveElement(type_name)
            buses = self.dss.ActiveCircuit.ActiveElement.BusNames

            # transformer may have >2 buses
            if type_name.startswith('Transformer'):
                assert len(buses) in [2, 3], type_name + ' has invalid number of terminals'
            else:
                assert len(buses) == 2, type_name + ' has more than two terminals'

            if len(buses) == 2:
                bus1, bus2 = map(lambda x: x.lower().split('.'), buses)
                bus1, bus2 = bus1[0], bus2[0]
                edge = frozenset({bus1, bus2})
            else:
                bus1, bus2, bus3 = map(lambda x: x.lower().split('.'), buses)
                bus1, bus2, bus3 = bus1[0], bus2[0], bus3[0]
                edge = frozenset({bus1, bus2, bus3})

            if ignore_duplicate:
                return edge, False
            else:
                return edge, (edge in self.edge_obj)

        # deal with RegControls as an exception first        
        regulators = set()  # names of transformers acting as a regulator
        dssReg = self.dss.ActiveCircuit.RegControls
        if dssReg.First == 0: return  # no such kind of object
        while True:
            # reg_name = dssReg.Name
            trans_name = dssReg.Transformer
            regulators.add(trans_name)
            if dssReg.Next == 0: break

        # run for line and transformer
        valid_trans2edge = dict()
        line2edge = dict()
        for type in ['Transformer', 'Line']:
            if type == 'Line':
                names = self.dss.ActiveCircuit.Lines.AllNames
            elif type == 'Transformer':
                names = self.dss.ActiveCircuit.Transformers.AllNames

            for name in names:
                # ignore regulators since they have been processed
                if type == 'Transformer' and name in regulators: continue
                type_name = type + '.' + name
                edge, has_dup = get_edge(type_name)

                # handle duplicate
                if not has_dup:
                    self.edge_obj[edge] = type_name
                else:
                    if type == 'Line':  # allow jump circuit
                        dup_name = self.edge_obj[edge]
                        # assert not dup_name.startswith('Line'), 'Duplicated lines: {} {}'.format(dup_name, type_name)
                        self.edge_obj[edge] = type_name

                    if edge not in self.dup_edges:
                        self.dup_edges[edge] = [dup_name, type_name]
                    else:
                        self.dup_edges[edge].append(type_name)

                if type == 'Transformer':
                    valid_trans2edge[name] = edge
                else:
                    line2edge[name] = edge
        return regulators, valid_trans2edge, line2edge

    def _gen_reg_obj(self, regulators):
        '''
        Generate all regulator objects:

        Args: 
            regulators (set): names of regulators acting as a regulator

        Returns: None
        '''
        if len(regulators) == 0: return
        dssTrans = self.dss.ActiveCircuit.Transformers
        if dssTrans.First == 0: return  # no such kind of object
        while True:
            name = dssTrans.Name
            if name in regulators:
                tap = [dssTrans.Tap, dssTrans.MinTap, dssTrans.MaxTap, dssTrans.NumTaps]
                fea = [dssTrans.Xhl, dssTrans.R]
                for wdg in range(1, 1 + dssTrans.NumWindings):
                    dssTrans.Wdg = wdg
                    fea = fea + [dssTrans.kV, dssTrans.kVA]
                if dssTrans.NumWindings == 3:
                    fea = fea + [dssTrans.Xht, dssTrans.Xlt]

                # get the correct bus order
                self.dss.ActiveCircuit.SetActiveElement('Transformer.' + name)
                buses = self.dss.ActiveCircuit.ActiveElement.BusNames

                self.add_regulators('Regulator.' + name, buses, fea, tap)
            if dssTrans.Next == 0: break

    def _gen_trans_obj(self, valid_trans2edge):
        """
        Generate all transformer objects:

        Args:
            valid_trans2edge [dict]: one of the returned objects of self._get_edge_name()

        Returns: None
        """
        dssTrans = self.dss.ActiveCircuit.Transformers
        if dssTrans.First == 0: return  # no such kind of object
        while True:
            name = dssTrans.Name
            if name in valid_trans2edge:
                # tap = [dssTrans.Tap, dssTrans.MinTap, dssTrans.MaxTap, dssTrans.NumTaps]
                fea = [dssTrans.Xhl, dssTrans.R]
                for wdg in range(1, 1 + dssTrans.NumWindings):
                    dssTrans.Wdg = wdg
                    fea = fea + [dssTrans.kV, dssTrans.kVA]
                if dssTrans.NumWindings == 3:
                    fea = fea + [dssTrans.Xht, dssTrans.Xlt]

                # get the correct bus order
                self.dss.ActiveCircuit.SetActiveElement('Transformer.' + name)
                buses = self.dss.ActiveCircuit.ActiveElement.BusNames

                self.add_transformers('Transformer.' + name, buses, fea)
            if dssTrans.Next == 0: break

    def _gen_line_obj(self, line2edge):
        '''
        Generate all line objects:

        Args: 
            line2edge [dict]: one of the returned objects of self._get_edge_name()

        Returns: None
        '''
        dssLine = self.dss.ActiveCircuit.Lines
        if dssLine.First == 0: return  # no such kind of object
        while True:
            name = dssLine.Name
            assert name in line2edge, 'missing line for Line.{}'.format(name)
            self.dss.ActiveCircuit.SetActiveElement('Line.' + name)
            buses = self.dss.ActiveCircuit.ActiveElement.BusNames
            mats = [dssLine.Rmatrix, dssLine.Xmatrix, dssLine.Cmatrix]
            self.add_lines('Line.' + name, buses, mats)
            if dssLine.Next == 0: break

    def _gen_load_cap_obj(self):
        '''
        Generate all load and capacitor objects

        Args: None

        Returns: None
        '''
        for type in ['Load', 'Capacitor']:
            if type == 'Load':
                dssObj = self.dss.ActiveCircuit.Loads
            else:
                dssObj = self.dss.ActiveCircuit.Capacitors
            if dssObj.First == 0: break  # no such kind of object
            while True:
                objname = self.dss.ActiveCircuit.CktElements.Name
                BusNames = self.dss.ActiveCircuit.CktElements.BusNames[0].split('.')
                bus = BusNames[0]
                if len(BusNames) > 1:
                    phases = BusNames[1:]
                else:
                    # if not specifying the phases, use all phases at the bus
                    phases = self.bus_phase[bus]

                if type == 'Load':
                    fea = [dssObj.kV, dssObj.kW, dssObj.kvar]
                    self.add_loads(objname, bus, phases, fea)
                else:
                    fea = [dssObj.States[0], dssObj.kV, dssObj.kvar]
                    self.add_capacitors(objname, bus, phases, fea)
                if dssObj.Next == 0: break

    def _gen_bat_obj(self):
        '''
        Generate all battery objects defined in self.batt_file

        Args: None

        Returns: None
        '''
        batt = pd.read_csv(self.batt_file, sep=',', header=0)
        batt = batt.set_index('name')
        batts = {name: feature for name, feature in batt.iterrows()}

        dssGen = self.dss.ActiveCircuit.Generators
        if dssGen.First == 0: return  # no such kind of object
        while True:
            name = dssGen.Name
            if name in batts:
                feature = batts[name]
                dssGen.kW = 0.0  # initialize in disconnected mode
                dssGen.PF = feature.pf
                dssGen.kvar = feature.max_kw / feature.pf

                BusNames = self.dss.ActiveCircuit.CktElements.BusNames[0].split('.')
                bus = BusNames[0]
                if len(BusNames) > 1:
                    phases = BusNames[1:]
                else:
                    # if not specifying the phases, use all phases at the bus
                    phases = self.bus_phase[bus]
                self.add_batteries('Battery.' + name, bus, phases, feature)
            if dssGen.Next == 0: break

    def __cal_edgeWei_busPhase(self, noWei=True):
        """
        Calculate edge weights (admittance matrix, Ymat) and number of phases on each bus

        Args:
            noWei: don't compute edge weights

        Returns: None
        """
        # sort y nodes in alphabetical order
        YNodeOrder = np.array(self.dss.Circuits.YNodeOrder)
        order = np.argsort(YNodeOrder)
        YNodeOrder = YNodeOrder[order]

        # find the range and bus phase
        bus_range = dict()
        for i, node_name in enumerate(YNodeOrder):
            bus_name = node_name.split('.', 1)[0].lower()
            if bus_name not in bus_range:
                bus_range[bus_name] = [i, i + 1]
            else:
                bus_range[bus_name][1] = i + 1

        for bus_name in bus_range.keys():
            self.dss.Circuits.SetActiveBus(bus_name)
            self.bus_phase[bus_name] = [str(i) for i in self.dss.Circuits.Buses.Nodes]
        # self.bus_phase = {bus:r[1]-r[0] for bus, r in bus_range.items()}

        if noWei: return
        bus_length = len(YNodeOrder)
        Y = self.dss.Circuits.SystemY
        Y = Y.reshape((bus_length, 2 * bus_length))
        Y = Y[:, ::2] + 1j * Y[:, 1::2]
        Y = Y[order, :][:, order]

        # extract the submatrix of edge weight from Y
        for edge in self.edge_obj.keys():
            bus1, bus2 = tuple(edge)
            range1, range2 = bus_range[bus1], bus_range[bus2]
            nphase1, nphase2 = range1[1] - range1[0], range2[1] - range2[0]

            if nphase1 == nphase2:
                # symmetric matrix if same number of phases
                self.edge_weight[edge] = Y[range1[0]:range1[1], range2[0]:range2[1]]
            else:
                # store as a tall matrix
                if nphase1 < nphase2:
                    self.edge_weight[edge] = Y[range2[0]:range2[1], range1[0]:range1[1]]
                else:
                    self.edge_weight[edge] = Y[range1[0]:range1[1], range2[0]:range2[1]]

    def bus_voltage(self, bus_name):
        """
        Get voltage of a bus

        Args:
            bus_name [str]: the bus name

        Returns:
            per-unit voltages and angles
        """
        return self.dss.ActiveCircuit.Buses(bus_name).puVmagAngle

    def edge_current(self, edge_obj_name):
        """
        Get current on an edge object

        Args:
            edge_obj_name [str]: the name of an edge object

        Returns:
            currents values represented in real and imaginary parts.
        """
        return self.dss.ActiveCircuit.CktElements(edge_obj_name).Currents

    def total_loss(self):
        # get loss in [kw, kvar]
        return self.dss.ActiveCircuit.Losses / 1000

    def total_power(self):
        # get power in [kw, kvar]
        return self.dss.ActiveCircuit.TotalPower

    ########## object addition functions called by  ############
    ###           _gen_reg_obj()
    ###           _gen_trans_obj()
    ###           _gen_line_obj()
    ###           _gen_load_cap_obj()
    ###           _gen_bat_obj()
    def add_lines(self, linename, buses, mats):
        self.lines[linename] = Line(linename, buses, mats)

    def add_transformers(self, transname, buses, feature):
        self.transformers[transname] = Transformer(transname, buses, feature)

    def add_regulators(self, regname, buses, feature, tap):
        self.regulators[regname] = Regulator(self.dss, regname, buses, feature, tap)

    def add_capacitors(self, capname, bus, phases, feature):
        self.capacitors[capname] = Capacitor(self.dss, capname, bus, phases, feature)
        if bus not in self.bus_obj:
            self.bus_obj[bus] = [capname]
        else:
            self.bus_obj[bus].append(capname)

    def add_loads(self, loadname, bus, phases, feature):
        self.loads[loadname] = Load(loadname, bus, phases, feature)
        if bus not in self.bus_obj:
            self.bus_obj[bus] = [loadname]
        else:
            self.bus_obj[bus].append(loadname)

    def add_batteries(self, batname, bus, phases, feature):
        self.batteries[batname] = Battery(self.dss, batname, bus, phases, feature,
                                          bat_act_num=self.bat_act_num)
        if bus not in self.bus_obj:
            self.bus_obj[bus] = [batname]
        else:
            self.bus_obj[bus].append(batname)

    ######### object addition functions end  ############


# %% Edge Objects
class Edge:
    """
    定义了电力系统的边界对象，包括变压器、线路和调节器等。其中，边界对象
    """

    def __init__(self, name, bus1, bus2):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2

    def __repr__(self):
        return f"Edge {self.name} at ({self.bus1}, {self.bus2}),"


class Line(Edge):
    """
    定义了电力系统的线路对象，包括单相和三相线路。
    """

    def __init__(self, name, buses, mats):
        bus1, bus2 = map(lambda x: x.lower().split('.'), buses)
        self.phase1, self.phase2 = map(lambda b: b[1:] if len(b) > 1 else ['1', '2', '3'], [bus1, bus2])
        bus1, bus2 = bus1[0], bus2[0]
        super().__init__(name, bus1, bus2)

        # The matrices are symmetric if both buses are of the same number of phases; 
        # Otherwise, the matrices are represented as a tall matrix.
        self.rmat = mats[0]  # resistance matrix
        self.xmat = mats[1]  # reactance matrix
        self.cmat = mats[2]  # capacitance matrix


class Transformer(Edge):
    """
    定义了电力系统的变压器对象，包括两端或三端变压器。
    """

    def __init__(self, name, buses, feature):
        if len(buses) == 2:
            bus1, bus2 = map(lambda x: x.lower().split('.'), buses)
            phase1, phase2 = map(lambda b: b[1:] if len(b) > 1 else ['1', '2', '3'], [bus1, bus2])
            bus1, bus2 = bus1[0], bus2[0]
        else:
            bus1, bus2, bus3 = map(lambda x: x.lower().split('.'), buses)
            phase1, phase2, phase3 = map(lambda b: b[1:] if len(b) > 1 else ['1', '2', '3'],
                                         [bus1, bus2, bus3])
            bus1, bus2, bus3 = bus1[0], bus2[0], bus3[0]
            self.bus3 = bus3
            self.phase3 = phase3
        super().__init__(name, bus1, bus2)
        self.phase1 = phase1
        self.phase2 = phase2

        # 2 windings: [xhl, r, kv_wdg1, kva_wdg1, kv_wdg2, kva_wdg2]
        # 3 windings: [xhl, r, kv_wdg1, kva_wdg1, kv_wdg2, kva_wdg2, kv_wdg3, kva_wdg3, xht, xlt]
        self.trans_feature = feature


class Regulator(Edge):
    """
    定义了电力系统的调节器对象，包括两端或三端调节器。
    """

    def __init__(self, dss, name, buses, feature, tapfea):
        assert len(buses) == 2, 'invalid number of buses for ' + name
        bus1, bus2 = map(lambda x: x.lower().split('.'), buses)
        phase1, phase2 = map(lambda b: b[1:] if len(b) > 1 else ['1', '2', '3'], [bus1, bus2])
        bus1, bus2 = bus1[0], bus2[0]
        super().__init__(name, bus1, bus2)
        self.phase1 = phase1
        self.phase2 = phase2

        self.trans_feature = feature  # [xhl, r, kv_wdg1, kva_wdg1, kv_wdg2, kva_wdg2]
        self.dss = dss  # the circuit's dss simulator object
        self.tap = tapfea[0]  # tap value
        self.tap_feature = tapfea[1:]  # [mintap, maxtap, numtaps]


# %% Node Objects
class Node:
    def __init__(self, name, bus1, phases):
        """
        初始化仅赋值属性
        Args:
            name:
            bus1:
            phases: names of the active phases; e.g., ['1','2','3']
        """
        self.name = name
        self.bus1 = bus1
        self.phases = phases  # names of the active phases; e.g., ['1','2','3']

    def __repr__(self):
        return f"Node {self.name} at {self.bus1}"


class Load(Node):
    def __init__(self, loadname, bus1, phases, feature):
        super().__init__(loadname, bus1, phases)
        self.feature = feature  # [kV, kW, kvar]


class Capacitor(Node):
    def __init__(self, dss, capname, bus1, phases, feature):
        super().__init__(capname, bus1, phases)
        self.dss = dss  # the circuit's dss simulator object
        self.status = feature[0]  # close: 1,  open: 0
        self.feature = feature[1:]  # [kV, kvar]

    def __repr__(self):
        return f'Capacitor status: {self.status!r},\
               Voltage at Bus: {self.bus1!r}, {self.dss.ActiveCircuit.Buses[self.bus1].puVmagAngle}'

    def set_status(self, status):
        """
        设置电容状态

        Args:
            status: the status to be set

        Returns:
            the absolute change of status in integer
        """
        diff = abs(self.status - status)  # record state difference
        dssCap = self.dss.ActiveCircuit.Capacitors
        if dssCap.First == 0: return  # no such object
        while True:
            if self.name.endswith(dssCap.Name):
                self.status = status
                dssCap.States = [self.status]
                break
            if dssCap.Next == 0: break
        return diff
        # should re-solve self.dss later


class Battery(Node):
    """
    继承自Node，通过Load定义了电力系统的电池对象，包括单相和三相电池。
    """

    def __init__(self, dss, batname, bus1, phases, feature, bat_act_num=33):
        super().__init__(batname, bus1, phases)
        self.dss = dss  # the circuit's dss simulator object
        self.max_kw = feature.max_kw  # maximum power magnitude
        self.pf = feature.pf  # power factor
        self.max_kwh = feature.max_kwh  # capacity
        self.kwh = feature.initial_kwh  # current charge
        self.soc = self.kwh / self.max_kwh  # state of charge
        self.initial_soc = self.soc  # initial soc
        self.duration = self.dss.ActiveCircuit.Solution.StepSize / 3600.0  # time step in hour
        if self.duration < 1e-5: self.duration = 1.0
        self.enabled = True  # 默认启用 Todo: 添加相关逻辑

        # battery states
        self.bat_act_num = bat_act_num
        if bat_act_num == np.inf:
            ## continuous discharge state
            self.kw = 0.0
        else:
            ## finite discharge state
            ## current kw = avail_kw[state]
            ## kw > 0 means discharging
            mode_num = bat_act_num // 2
            diff = self.max_kw / mode_num
            ## avail_kw: a discrete range from -max_kw to max_kw
            self.avail_kw = [n * diff for n in range(-mode_num, mode_num + 1)]
            self.state = len(self.avail_kw) // 2  # initialize as disconnected mode

    def __repr__(self):
        return f'Battery Available kW: {self.avail_kw!r}, \
        Status: {self.state!r}, kWh: {self.kwh!r}, SOC: {self.soc!r}, \
        Actual kW: {-self.actual_power()!r}'

    def state_projection(self, nkw_or_state):
        """
        Project to the valid state

        Args:
            nkw_or_state: nkw: continuous battery's normalized discharge power in [-1, 1]
                          state: discrete battery's discharge state in [0, len(avail_kw)-1]
        Returns:
            the valid discharge kw
        """
        # Todo: 目前是按照Battery初始化时的额定功率作为基准值，后续将映射处理改为统一基准值，但应该会影响训练收敛，先不动。
        if self.bat_act_num == np.inf:
            kw = max(-1.0, min(1.0, nkw_or_state)) * self.max_kw
            if kw > 0:
                kw = min(self.kwh / self.duration, kw)
            else:
                kw = max((self.kwh - self.max_kwh) / self.duration, kw)
            self.kw = kw
            return kw
        else:
            state = max(0, min(len(self.avail_kw) - 1, nkw_or_state))
            mid = len(self.avail_kw) // 2
            if state > mid:  # discharging
                allowed_kw = self.kwh / self.duration  # max kw
                if self.avail_kw[state] > allowed_kw:
                    state = int(state - np.ceil((self.avail_kw[state] - allowed_kw) / \
                                                (self.avail_kw[1] - self.avail_kw[0]) - 1e-8))
            elif state < mid:  # charging
                allowed_kw = (self.kwh - self.max_kwh) / self.duration  # min kw
                if self.avail_kw[state] < allowed_kw:
                    state = int(state + np.ceil((allowed_kw - self.avail_kw[state]) / \
                                                (self.avail_kw[1] - self.avail_kw[0]) - 1e-8))
            self.state = state
            return self.avail_kw[state]

    def step_before_solve(self, nkw_or_state):
        """
        未在circuit.set_all_batteries_before_solve()中调用，是其子集，可暂时忽略。
        Set the state of this battery
        ( Run this function before each solve() )

        Args:
            nkw_or_state: nkw: continuous battery's normalized discharge power in [-1, 1]
                          state: discrete battery's discharge state in [0, len(avail_kw)-1]

        Returns: None
        """
        kw = self.state_projection(nkw_or_state)

        # change kw in dss
        name = self.name[8:]  # remove the header 'Battery.'
        dssGen = self.dss.ActiveCircuit.Generators
        if dssGen.First == 0:  # no such kind of object
            return
        while True:
            if dssGen.Name == name:
                dssGen.kW = kw
                dssGen.kvar = kw / self.pf
                break
            if dssGen.Next == 0:
                break

        # run solve() afterward

    def step_after_solve(self):
        """
        根据dss对象展示的实际功率更新kwh和soc，同时返回soc的变化的绝对值和
        ( Run this function after each solve() )

        Returns: soc变化和放电功率 soc error and discharge error
        """
        self.kwh += self.actual_power() * self.duration
        # 实现容量限制并将kwh的值截断为整数
        self.kwh = round(max(0.0, min(self.max_kwh, self.kwh)))  # Fixme: 可能不需要进行截断，但是截断可能利于训练收敛
        self.soc = self.kwh / self.max_kwh
        soc_err = abs(self.soc - self.initial_soc)

        # discharge_err 只返回正值，负值不属于discharge
        if self.bat_act_num == np.inf:
            discharge_err = max(0.0, self.kw) / self.max_kw
        else:
            discharge_err = max(0.0, self.avail_kw[self.state]) / self.max_kw
        return soc_err, discharge_err

    def actual_power(self):
        # get the actual power computed by dss in [-kw, -kvar] in dss, the minus means power generation
        # actual_power < 0 means discharging （和 opendss 内置的 storage 相反）
        try:
            name = 'Generator.' + self.name[8:]
            return self.dss.ActiveCircuit.CktElements(name).TotalPowers[0]
        except Exception as e:
            print(e)
            return 0.0

    def reset(self):
        # reset the charge
        self.soc = self.initial_soc
        self.kwh = self.soc * self.max_kwh

        # reset to zero discharge mode
        if self.bat_act_num == np.inf:
            self.kw = 0.0
        else:
            self.state = len(self.avail_kw) // 2


class BatteryController:
    """
    EV电池的连接/断开和功率控制类，也控制储能电池。定位上脱离
    """

    def __init__(self, circuit):
        """初始化控制器"""
        self.circuit = circuit  # 引用电力系统Circuits实例
        self.dss = circuit.dss  # 引用OpenDSS接口
        self.active_batteries = {}  # 当前激活的电池 {name: Battery对象}
        self.battery_configs = {}  # 所有电池配置信息 {name: pd.Series}
        self.battery_history = {}  # 电池运行历史记录

        # 添加对已有电池的管理
        for bat_name, battery in circuit.batteries.items():
            self.active_batteries[bat_name] = battery
            self.battery_history[bat_name] = []

    def connect_battery(self, name, bus, max_kw=100, max_kwh=100, initial_soc=0.2, pf=0.95):
        """连接指定的电池或创建新电池，借助 circuit.add_batteries
        Args:
            name (str): 电池名称，或者说电动汽车编号
            bus (str): 连接的母线名称
            max_kw (float): 最大功率（kW）
            max_kwh (float): 最大能量（kWh）
            initial_soc (float): 初始SOC（0-1之间）
            pf (float): 功率因数
        Returns:
            str: 电池名称
        """
        # 如果电池已激活，先断开
        if f"Battery.{name}" in self.active_batteries:
            self.disconnect_battery(name)

        # 创建OpenDSS中的实际对象——电压等级等和dss中创建的储能保持一致
        self.dss.Text.Commands(f"""
            New Generator.{name}
            ~ phases=3
            ~ bus1={bus}
            ~ kV=4.16
            ~ kW=0.0
            ~ conn=Delta
            ~ PF={pf}
            ~ model=1
            ~ enabled=True
        """)

        # 创建Battery配置对象
        bat_config = pd.Series({
            'max_kw': max_kw,
            'pf': pf,
            'max_kwh': max_kwh,
            'initial_kwh': max_kwh * initial_soc,
            'initial_soc': initial_soc
        })
        # 添加到配置列表
        self.battery_configs[name] = bat_config

        # 获取相位信息，用于初始化
        self.dss.ActiveCircuit.SetActiveBus(bus)
        phases = [str(i) for i in self.dss.ActiveCircuit.Buses.Nodes]

        # 创建Battery对象，OpenDSS的实际对象的对应抽象
        bat_name = f"Battery.{name}"
        self.circuit.add_batteries(bat_name, bus, phases, bat_config)

        # 添加到管理列表
        self.active_batteries[bat_name] = self.circuit.batteries[bat_name]
        self.battery_history[bat_name] = []

        print(f"已连接电池: {name}, 初始SOC: {initial_soc * 100}%, 最大功率: {max_kw}kW, 电池容量: {max_kwh}kWh")
        return name

    def disconnect_battery(self, name):
        """断开指定的电池并移除
        Args:
            name (str): 电池名称（默认情况下电动汽车编号evxxx）
        Returns:
            bool: 是否成功断开
        """
        bat_name = f"Battery.{name}" if not name.startswith("Battery.") else name

        if bat_name in self.active_batteries:
            # 在OpenDSS中禁用
            gen_name = bat_name[8:]  # 移除"Battery."前缀
            self.dss.Text.Commands(f'Generator.{gen_name}.enabled=False')

            # 从circuit.batteries中移除
            if bat_name in self.circuit.batteries:
                del self.circuit.batteries[bat_name]

            # 从管理列表中移除
            del self.active_batteries[bat_name]
            print(f"已断开电池: {name}")
            return True
        else:
            print(f"电池 {name} 不存在或已断开")
            return False

    def set_battery_power(self, name, power_kw):
        """直接设置电池功率 (正值表示放电，负值表示充电)
        Args:
            name (str): 电池名称
            power_kw (float): 功率（kW）

        Returns:
            bool: 是否成功设置功率
        """
        bat_name = f"Battery.{name}" if not name.startswith("Battery.") else name

        if bat_name not in self.active_batteries:
            print(f"电池 {name} 不存在或已断开")
            return False

        battery = self.active_batteries[bat_name]

        # 限制功率在额定范围内
        if abs(power_kw) > battery.max_kw:
            original_power = power_kw
            power_kw = battery.max_kw if power_kw > 0 else -battery.max_kw
            print(f"功率设置{original_power}kW超出额定值{battery.max_kw}kW，已调整为{power_kw}kW")

        # 设置功率
        if battery.bat_act_num == np.inf:
            # 连续模式
            nkw = power_kw / battery.max_kw  # 归一化功率
            battery.step_before_solve(nkw)
        else:
            # 离散模式
            # 找到最接近请求功率的离散级别
            closest_idx = min(range(len(battery.avail_kw)),
                              key=lambda i: abs(battery.avail_kw[i] - power_kw))
            battery.step_before_solve(closest_idx)

        print(f"已设置{name}的功率为{power_kw}kW")
        return True

    def get_battery_status(self, name):
        """获取电池的当前状态"""
        bat_name = f"Battery.{name}" if not name.startswith("Battery.") else name

        if bat_name not in self.active_batteries:
            return None

        battery = self.active_batteries[bat_name]

        # 获取基本信息
        stored_energy = battery.kwh
        soc_percent = battery.soc * 100

        # 获取实际功率
        actual_power = battery.actual_power()

        # 获取电压信息
        self.dss.ActiveCircuit.SetActiveBus(battery.bus1)
        voltages = self.dss.ActiveCircuit.Buses.puVmagAngle
        voltage_pu = np.mean(voltages[::2]) if len(voltages) > 0 else 1.0

        # 构建状态对象
        status = {
            'battery_name': bat_name,
            'stored_energy': stored_energy,
            'soc_percent': soc_percent,
            'charging_power': -actual_power,  # 转换为充电功率表示（负为放电）
            'actual_power': actual_power,
            'voltage_pu': voltage_pu,
            'rated_power': battery.max_kw,
            'timestamp': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        return status

    def update_all_before_solve(self):
        """更新所有电池状态(求解前)，未实际实现"""
        # 这个方法用于与circuit.set_all_batteries_before_solve协同工作
        # 不需要实际操作，因为每个电池的功率设置已在set_battery_power中完成
        pass

    def update_all_after_solve(self):
        """更新所有电池状态(求解后)并记录历史"""
        for bat_name, battery in self.active_batteries.items():
            # 更新电池状态
            battery.step_after_solve()

            # 获取当前状态
            status = self.get_battery_status(bat_name)
            if not status:
                continue

            # 更新历史记录
            history = self.battery_history[bat_name]

            # 计算变化(如果有历史记录)
            if history:
                prev_status = history[-1]['status']
                energy_diff = status['stored_energy'] - prev_status['stored_energy']
                soc_diff = status['soc_percent'] - prev_status['soc_percent']

                # 记录到历史
                self.battery_history[bat_name].append({
                    'battery_name': bat_name,
                    'timestamp': status['timestamp'],
                    'status': status,
                    'energy_change': energy_diff,
                    'soc_change': soc_diff
                })

                # print(f"电池 {bat_name} 状态变化: SOC {prev_status['soc_percent']:.2f}% → {status['soc_percent']:.2f}%, "
                #      f"能量 {prev_status['stored_energy']:.2f}kWh → {status['stored_energy']:.2f}kWh")
            else:
                # 首次记录
                self.battery_history[bat_name].append({
                    'battery_name': bat_name,
                    'timestamp': status['timestamp'],
                    'status': status,
                    'energy_change': 0,
                    'soc_change': 0
                })

                # print(f"电池 {bat_name} 首次记录状态: SOC {status['soc_percent']:.2f}%, 能量 {status['stored_energy']:.2f}kWh")

    def export_battery_history(self, filename=None):
        """导出电池历史数据
        Args:
            filename(str): 输出文件名，缺省时，自动命名为为"battery_history.csv"
        Returns:
            bool: 是否成功导出
        """
        if not self.battery_history:
            print("没有电池历史数据可以导出")
            return False

        try:
            data = []
            for bat_name, history in self.battery_history.items():
                for entry in history:
                    status = entry['status']
                    record = {
                        'timestamp': entry['timestamp'],
                        'battery_name': bat_name,
                        'soc_percent': status['soc_percent'],
                        'stored_energy_kwh': status['stored_energy'],
                        'charging_power_kw': status['charging_power'],
                        'voltage_pu': status['voltage_pu'],
                        'energy_change_kwh': entry['energy_change'],
                        'soc_change_percent': entry['soc_change']
                    }
                    data.append(record)

            df = pd.DataFrame(data)
            output_file = filename if filename else "battery_history.csv"
            df.to_csv(output_file, index=False)
            print(f"电池历史数据已导出到 {output_file}")
            return True
        except Exception as e:
            print(f"导出数据失败: {e}")
            return False


def load_ev_from_csv(csv_path):
    """从路径加载csv文件并解包出BatteryStationManager所需的参数

    CSV文件应包含以下列：
    - arrive_time: 到达时间步
    - depart_time: 离开时间步
    - power_support: 最大充电功率(kW)
    - battery_capacity: 电池最大容量(kWh)
    - start_soc: 初始荷电状态(0-1)
    - end_soc: 目标荷电状态(0-1)

    Args:
        csv_path (str): ev充电需求信息的csv文件路径

    Returns:
        dict: 包含BatteryStationManager初始化所需的参数，SOC将四舍五入为二位小数
            - arrival: 到达时间列表
            - departure: 离开时间列表
            - max_power: 最大功率列表
            - capacity: 最大容量列表
            - initial_soc: 初始SOC列表
            - target_soc: 目标SOC列表
    """
    try:
        import pandas as pd

        # 读取CSV文件
        df = pd.read_csv(csv_path)

        # 检查必要的列是否存在
        required_columns = ['arrive_time', 'depart_time', 'power_support',
                            'battery_capacity', 'start_soc', 'end_soc']

        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"CSV文件缺少必要的列: {', '.join(missing_columns)}")

        # 提取数据并映射到BatteryStationManager需要的参数名
        result = {
            'arrival': df['arrive_time'].tolist(),
            'departure': df['depart_time'].tolist(),
            'max_power': df['power_support'].tolist(),
            'capacity': df['battery_capacity'].tolist(),
            'initial_soc': [round(x, 2) for x in df['start_soc'].tolist()],
            'target_soc': [round(x, 2) for x in df['end_soc'].tolist()],
        }

        # 添加可选列
        if 'battery_name' in df.columns:
            result['battery_names'] = df['battery_name'].tolist()

        if 'priority' in df.columns:
            result['priority'] = df['priority'].tolist()

        # 进行数据校验
        for i, (arrival, departure) in enumerate(zip(result['arrival'], result['departure'])):
            if arrival == departure:
                print(f"警告: 第{i+1}行的到达时间等于离开时间")
            elif arrival > departure:
                print(f"警告: 第{i+1}行的到达时间晚于离开时间")

        for i, soc in enumerate(result['initial_soc']):
            if not 0 <= soc <= 1:
                print(f"警告: 第{i+1}行的初始SOC值 {soc} 不在有效范围[0,1]内")

        for i, soc in enumerate(result['target_soc']):
            if not 0 <= soc <= 1:
                print(f"警告: 第{i+1}行的目标SOC值 {soc} 不在有效范围[0,1]内")

        return result

    except Exception as e:
        print(f"加载EV数据失败: {str(e)}")
        return None


class BatteryStationManager:
    """EV电池排队管理器，处理EV电池的接入/断开和排队逻辑

    Attributes:
        circuit (Circuits): 电力系统仿真对象
        battery_count (int): 电池总数量
        initial_data (dict): 保存初始输入数据的字典
        arrival (list): 每个电池的到达时间步
        departure (list): 每个电池的离开时间步
        max_power (list): 每个电池的最大功率(kW)
        initial_soc (list): 每个电池的初始荷电状态(0-1)
        target_soc (list): 每个电池的目标荷电状态(0-1)
        capacity (list): 每个电池的容量(kWh)
        battery_names (list): 电池名称列表
        bus (str): 充电站连接的母线名称
        num_connection_points (int): 充电桩数量
        waiting_queue (deque): 等待接入的电池队列，每项为(idx, arrival_time)
        connected_batteries (dict): 已在连接中的电池，{idx: battery_name}
        connection_next_avail (list): 各接入点下次可用的时间步
        total_steps (int): 总时间步数
        current_step (int): 当前时间步
        schedule (np.ndarray): 电池功率排程矩阵，形状为(battery_count, total_steps)
        controller (BatteryController): 电池控制器实例
        sorted_indices (np.ndarray): 按到达时间排序的电池索引
        stats (dict): 性能统计数据，可能还需要包括等待时间、拒绝数量、实时充电满足率等，已经包括实时充电满足率
    """

    def __init__(self, circuit, bus, num_connection_points, arrival, departure,
                 max_power, initial_soc, target_soc, capacity,
                 battery_names=None, total_steps=96):
        """
        Args:
            circuit: Circuits对象，电力系统实例
            bus: 接入点母线名称  （本来想改，但是pycharm重构对于这种大众名比较麻烦）
            num_connection_points: 电网可用接入点数量
            arrival: 到达时间步列表
            departure: 离开时间步列表
            max_power: 最大功率列表(kW)
            initial_soc: 初始SOC列表(0-1)
            target_soc: 目标SOC列表(0-1)
            capacity: 最大容量列表(kWh)
            battery_names: 电池名称列表，若不提供则自动按照索引生成
            total_steps: 总时间步数，默认96（即24小时每15分钟一个时间步）
        """
        # 保存电力系统仿真对象引用
        self.circuit = circuit

        # 验证输入参数
        self.battery_count = len(arrival)
        assert len(departure) == self.battery_count, "到达和离开时间步列表长度必须一致"
        assert len(max_power) == self.battery_count, "最大功率列表长度必须一致"
        assert len(initial_soc) == self.battery_count, "初始SOC列表长度必须一致"
        assert len(capacity) == self.battery_count, "容量列表长度必须一致"

        # 如果没有提供target_soc，则默认为1.0
        if target_soc is None:
            target_soc = [1.0] * self.battery_count
        else:
            assert len(target_soc) == self.battery_count, "目标SOC列表长度必须一致"

        # 如果未提供电池名称，则自动生成
        self.battery_count = len(arrival)
        if battery_names is None:
            battery_names = [f"batt_ev_{i:03d}" for i in range(self.battery_count)]

        # 保存初始输入数据
        self.initial_data = {
            'arrival': arrival.copy(),
            'departure': departure.copy(),
            'max_power': max_power.copy(),
            'initial_soc': initial_soc.copy(),
            'target_soc': target_soc.copy(),
            'capacity': capacity.copy(),
            'battery_names': battery_names.copy(),
            'num_connection_points': num_connection_points
        }

        # 电池基本信息
        self.arrival = arrival
        self.departure = departure
        self.max_power = max_power
        self.initial_soc = initial_soc
        self.target_soc = target_soc
        self.capacity = capacity
        self.battery_names = battery_names

        # 充电站参数
        self.bus = bus  # 接入点母线名称
        self.num_connection_points = num_connection_points

        # 运行时状态
        self.waiting_queue = deque()  # 等待队列 (idx, arrival_time)
        self.connected_batteries = {}  # 已连接电池 {idx: battery_name}，当前连接的电池
        self.connection_next_avail = [0] * num_connection_points  # 各接入点下次可用时间
        # 添加一个新字典来记录当前的电池与连接点的对应关系
        self.battery_connection_points = {}  # {battery_idx: connection_point_id}，会自动清理
        self.battery_connection_points_history = {}  # {battery_idx: connection_point_id}，用于记录电池与连接点的对应关系

        # 时间和调度
        self.total_steps = total_steps
        self.current_step = 0
        self.schedule = np.zeros((self.battery_count, self.total_steps))  # 电池功率调度

        # 确保电池控制器存在  Fixme: 实际最初是想需要将这部分和控制器相互嵌入
        if circuit.ev_controller is not None:
            circuit.ev_controller = BatteryController(circuit)
        self.controller = circuit.ev_controller

        # 按到达时间对EV电池进行排序
        self.sorted_indices = np.argsort(arrival)

        # 性能统计
        self.stats = {
            # 基本连接统计
            'connected_count': 0,  # 已连接的EV电池数【原计划用于统计已连接过的EV数，在断开时计数】
            'rejected_count': 0,  # 未能连接的EV电池数
            'waiting_count': 0,  # 进入等待队列的EV电池数
            'active_count': 0,  # 当前连接的EV电池数

            # 能量统计
            'total_discharge': 0,  # 总放电量(kWh)
            'total_charge': 0,  # 总充电量(kWh)
            'net_energy': 0,  # 净能量交换(kWh)

            # 充电满足度统计
            'completed_count': 0,  # 完成充电的EV电池数【原计划用于统计满足需求的EV数】
            'completed_soc': 0,  # 完成充电的EV电池的SOC增加总和
            'avg_completed_soc': 0,  # 完成充电的EV电池的平均增加的SOC
            'charge_satisfaction_ratio': 0,  # EV电池能量满足率之和（单个EV电池的满足率离开时的充电能量比所需的充电能量）
            'target_achieved_count': 0,  # 达到目标SOC（能量满足率为1，完全满足）的EV电池数
            'avg_target_achieved': 0,  # 充电满足率平均值(满足率之和/总连接数)

            # 服务质量统计
            'avg_waiting_time': 0,  # 平均等待时间(时间步)
            'total_waiting_time': 0,  # 总等待时间
            'max_waiting_time': 0,  # 最长等待时间

            # 时间利用率统计
            'total_connection_time': 0,  # 总连接时长
            'charger_utilization': 0,  # 充电桩利用率(总连接时长/(当前时段*充电桩数))

            # 实时指标
            'current_connection_rate': 0,  # 当前连接率(当前连接数/总连接点数)
            'current_charging_power': 0,  # 当前总充电功率(电池状态的charging_power累加)
            'current_success_rate': 0  # 当前服务成功率(完全满足数/总连接数)
        }

    def check_arrivals(self, print_details=False) -> None:
        """检查并处理当前时刻到达的电池。

        当电池到达时，根据接入点可用性进行处理：
        1. 如果有接入点可用，直接连接电池
        2. 如果没有接入点可用，将电池加入等待队列

        Returns:
            None
        """
        for idx in self.sorted_indices:
            if self.arrival[idx] == self.current_step:
                # 找到最早可用的接入点
                earliest_avail_time = min(self.connection_next_avail)
                connection_point_id = self.connection_next_avail.index(earliest_avail_time)

                if earliest_avail_time <= self.current_step:
                    # 有接入点可用，直接连接电池
                    name = self.battery_names[idx]
                    self.controller.connect_battery(
                        name=name,
                        bus=self.bus,
                        max_kw=self.max_power[idx],
                        max_kwh=self.capacity[idx],
                        initial_soc=self.initial_soc[idx]
                    )
                    # 更新已连接电池列表
                    self.connected_batteries[idx] = name
                    # 更新该连接点的下次可用时间
                    self.connection_next_avail[connection_point_id] = self.departure[idx]
                    # 记录电池与连接点的对应关系
                    self.battery_connection_points[idx] = connection_point_id
                    self.battery_connection_points_history[idx] = connection_point_id
                    # 更新统计数据
                    self.update_statistics('arrival', connected=True)
                    if print_details:
                        print(f"时间步 {self.current_step} 执行前: 电池 {name} 已接入")
                else:
                    # 无接入点可用，加入等待队列
                    self.waiting_queue.append((idx, self.current_step))
                    # 更新等待队列统计
                    self.update_statistics('arrival', waiting=True)
                    if print_details:
                        print(f"时间步 {self.current_step} 执行前: 电池 {self.battery_names[idx]} 加入等待队列")

    def check_departures(self, print_details=True) -> None:
        """检查当前时刻离开的已连接电池并断开连接。

        检查电池是否达到目标SOC（达到则提前断开，并更新连接点可用信息）。
        注意：等待队列中EV电池的离开由process_waiting_queue()处理。

        Returns:
            None
        """
        disconnected_indices = []

        for idx, name in list(self.connected_batteries.items()):
            # 1. 先检查是否达到目标SOC
            bat_status = self.controller.get_battery_status(name)
            initial_soc = self.initial_soc[idx]
            target_soc = self.target_soc[idx]
            if bat_status and bat_status['soc_percent'] / 100 >= self.target_soc[idx]:  # 达到目标SOC
                self.controller.disconnect_battery(name)
                disconnected_indices.append(idx)
                # 更新统计：成功达到目标SOC的电池
                self.update_statistics('departure',
                                       idx=idx,
                                       final_soc=bat_status['soc_percent'] / 100,
                                       is_target_achieved=True,
                                       arrival_time=self.arrival[idx])
                if print_details:
                    print(f"时间步 {self.current_step} 执行前: 电池 {name} 已充满 (SOC: {bat_status['soc_percent']:.1f}%)，离开")

                # # Deprecated: 相应更新连接点可用信息——添加电池-桩的对应关系后已经不需要
                # # 1. 充满时间正好和离开时间一致则不需要更新信息
                # # 2. 提前充满则空出一个可用时间为离开时间的连接点，保持其他连接点的可用时间不变，无论是否同一连接点，效果一致
                # if self.current_step == self.departure[idx]:  # 巧合
                #     pass
                # else:  # 提前充满
                #     # 遍历连接点列表
                #     for i, next_avail in enumerate(self.connection_next_avail):
                #         if self.current_step < next_avail == self.departure[idx]:
                #             self.connection_next_avail[i] = self.current_step
                #             break

                continue  # 已断开连接，无需继续检查

            # 2. 检查是否到达离开时间
            if self.departure[idx] == self.current_step:
                final_soc = bat_status['soc_percent'] / 100 if bat_status['soc_percent'] > 0 else 0
                target_ratio = min(1.0, (final_soc - initial_soc) / (target_soc - initial_soc))
                # 记录统计信息
                self.update_statistics('departure',
                                       idx=idx,
                                       final_soc=bat_status['soc_percent'] / 100 if bat_status else 0,
                                       is_target_achieved=False,
                                       arrival_time=self.arrival[idx])

                # 断开连接
                self.controller.disconnect_battery(name)
                disconnected_indices.append(idx)
                if print_details:
                    print(f"时间步 {self.current_step}: 电池 {name} 已离开，当前SOC: {final_soc * 100:.1f}%，能量满足率: {target_ratio * 100:.1f}%")

        # 从已连接电池列表中移除断开的电池
        for idx in disconnected_indices:
            # 释放对应的接入点（使用记录的连接点ID）
            if idx in self.battery_connection_points:
                connection_id = self.battery_connection_points[idx]
                self.connection_next_avail[connection_id] = self.current_step
                del self.battery_connection_points[idx]  # 删除连接点记录

            del self.connected_batteries[idx]

    def process_waiting_queue(self) -> None:
        """处理等待队列中的电池。

        从队列中取出等待的电池，并尝试为它们分配可用的充电接入点。
        处理流程：
        1. 如果有接入点可用，连接电池
        2. 如果没有接入点可用，保持在队列中
        3. 若电池已超过预定离开时间，从队列中移除并记录为拒绝服务

        Returns:
            None
        """
        while self.waiting_queue and min(self.connection_next_avail) <= self.current_step:
            earliest_avail_time = min(self.connection_next_avail)
            connection_point_id = self.connection_next_avail.index(earliest_avail_time)

            # 取出队列中第一个电池
            idx, arrival_time = self.waiting_queue.popleft()

            # 检查电池是否还在站内时间范围内
            if self.current_step >= self.departure[idx]:
                # 借用到达统计更新拒绝服务信息
                self.update_statistics('arrival', rejected=True)
                print(f"时间步 {self.current_step}: 电池 {self.battery_names[idx]} 已错过离开时间，无法接入")
                continue

            # 连接电池
            bus = self.bus
            name = self.battery_names[idx]
            self.controller.connect_battery(
                name=name,
                bus=bus,
                max_kw=self.max_power[idx],
                max_kwh=self.capacity[idx],
                initial_soc=self.initial_soc[idx]
            )

            # 计算等待时间并更新统计
            wait_time = self.current_step - arrival_time
            self.update_statistics('waiting', wait_time=wait_time)

            # 借用到达统计更新连接统计信息
            self.update_statistics('arrival', connected=True)

            # 更新已连接电池列表
            self.connected_batteries[idx] = name
            # 更新该连接点的下次可用时间
            self.connection_next_avail[connection_point_id] = self.departure[idx]
            # 记录电池与连接点的对应关系
            self.battery_connection_points[idx] = connection_point_id
            self.battery_connection_points_history[idx] = connection_point_id

            print(f"时间步 {self.current_step} 执行前: 排队电池 {name} 已接入")


    def update_statistics(self, update_type, **kwargs) -> None:
        """统一更新统计信息的函数

        Args:
            update_type (str): 更新类型，可以是'arrival', 'departure', 'waiting', 'connection', 'energy', 'summary'
            **kwargs: 根据更新类型提供的参数
        """
        if update_type == 'arrival':  # 更新到达相关统计
            if kwargs.get('connected', False):
                # 电池成功连接
                self.stats['active_count'] += 1
            elif kwargs.get('waiting', False):
                # 电池进入等待队列
                self.stats['waiting_count'] += 1
            if kwargs.get('rejected', False):
                # 电池被拒绝（预计无法在停留时间内连接）
                self.stats['rejected_count'] += 1

            # 更新当前连接率
            self.stats['current_connection_rate'] = self.stats['active_count'] / self.num_connection_points

        elif update_type == 'departure':  # 更新离开相关统计
            idx = kwargs.get('idx')
            final_soc = kwargs.get('final_soc', 0)
            initial_soc = kwargs.get('initial_soc', self.initial_soc[idx] if idx is not None else 0)
            target_soc = kwargs.get('target_soc', self.target_soc[idx] if idx is not None else 1.0)
            arrival_time = kwargs.get('arrival_time', self.arrival[idx] if idx is not None else 0)
            departure_time = kwargs.get('departure_time', self.current_step)
            is_target_achieved = kwargs.get('is_target_achieved', False)

            # 更新已连接电池计数 Checked
            self.stats['connected_count'] += 1
            self.stats['active_count'] -= 1

            # 更新完成充电统计 Checked
            self.stats['completed_count'] += 1
            self.stats['completed_soc'] += final_soc - initial_soc

            # 更新目标达成率 - 充电进度/目标进度
            if is_target_achieved:
                self.stats['target_achieved_count'] += 1
                target_ratio = 1.0
            elif target_soc > initial_soc:  # 避免分母为0
                target_ratio = min(1.0, (final_soc - initial_soc) / (target_soc - initial_soc))
            else:
                target_ratio = 1.0  # 如果初始SOC已经达到或超过目标SOC

            self.stats['charge_satisfaction_ratio'] += target_ratio

            # 更新连接时间
            connection_time = departure_time - arrival_time
            self.stats['total_connection_time'] += connection_time

            # 更新平均SOC
            if self.stats['completed_count'] > 0:
                self.stats['avg_completed_soc'] = self.stats['completed_soc'] / self.stats['completed_count']

            # 更新目标达成平均值
            if self.stats['connected_count'] > 0:
                self.stats['avg_target_achieved'] = self.stats.get('charge_satisfaction_ratio', 0) / self.stats[
                    'connected_count']

            # 更新充电桩利用率
            if self.current_step > 0:
                self.stats['charger_utilization'] = self.stats['total_connection_time'] / (
                            self.current_step * self.num_connection_points)

            # 更新当前连接率
            self.stats['current_connection_rate'] = self.stats['active_count'] / self.num_connection_points

            # 更新当前服务成功率
            if self.stats['connected_count'] > 0:
                self.stats['current_success_rate'] = self.stats['target_achieved_count'] / self.stats['connected_count']

        elif update_type == 'waiting':  # 更新等待队列相关统计
            wait_time = kwargs.get('wait_time', 0)
            self.stats['total_waiting_time'] += wait_time
            self.stats['max_waiting_time'] = max(self.stats['max_waiting_time'], wait_time)

            # 更新平均等待时间
            if self.stats['waiting_count'] > 0:
                self.stats['avg_waiting_time'] = self.stats['total_waiting_time'] / self.stats['waiting_count']

        elif update_type == 'energy':  # 更新能量相关统计
            power = kwargs.get('power', 0)
            duration = kwargs.get('duration', 0.25)  # 默认15分钟，转为小时为0.25

            if power > 0:  # 放电
                self.stats['total_discharge'] += power * duration
            else:  # 充电
                self.stats['total_charge'] += abs(power) * duration

            # 更新净能量
            self.stats['net_energy'] = self.stats['total_discharge'] - self.stats['total_charge']

        elif update_type == 'summary':  # 更新总体统计数据，通常在时间步结束时调用
            # 更新当前充电功率
            total_charging_power = 0
            for idx, name in self.connected_batteries.items():
                bat_status = self.controller.get_battery_status(name)
                if bat_status and bat_status['actual_power'] < 0:  # 充电为负值
                    total_charging_power += abs(bat_status['actual_power'])
            self.stats['current_charging_power'] = total_charging_power

    def update_schedule(self):
        """更新电池功率调度记录"""
        # total_charging_power = 0
        for idx, name in self.connected_batteries.items():
            if self.arrival[idx] <= self.current_step < self.departure[idx]:
                bat_status = self.controller.get_battery_status(name)
                if bat_status:
                    # 记录EV视角的功率，正值表示充电
                    self.schedule[idx, self.current_step] = bat_status['charging_power']
                # total_charging_power += bat_status['charging_power']
        # 更新当前充电功率
        # self.stats['current_charging_power'] = total_charging_power

    def update_before_solve(self):
        """在OpenDSS求解前更新，处理电池到达、队列和离开
        Todo: 未启用，待检查和其余地方的冲突"""
        # 1. 处理到达的电池
        self.check_arrivals()

        # 2. 处理等待队列中的电池
        self.process_waiting_queue()

        # 3. 设置电池功率（如果需要根据需求调整功率，可在此处添加）

        # 4. 更新所有电池的状态
        self.controller.update_all_before_solve()

    def update_after_solve(self):
        """在OpenDSS解后更新，记录数据并处理电池离开
        Todo: 未启用，待检查和其余地方的冲突"""
        # 1. 更新所有电池的状态
        self.controller.update_all_after_solve()

        # 2. 更新电池排程记录
        self.update_schedule()

        # 3. 断开离开的电池
        self.check_departures()

        # 4. 更新计数器
        self.current_step += 1

    def get_connection_status(self):
        """获取当前所有接入点和电池连接状态，需要调整结构，按照电池连接点的方式或者补齐长度
        Returns:
            dict: 包含接入点状态和电池连接状态的字典
        """
        status = {
            'connected_batteries': {idx: {
                'name': name,
                'connection_point': self._find_connection_point(idx),
                'arrival': self.arrival[idx],
                'departure': self.departure[idx],
                'current_soc': self._get_battery_soc(name)
            } for idx, name in self.connected_batteries.items()},
            'waiting_queue': list(self.waiting_queue),
            'connection_points_status': [
                {'id': i, 'next_available': time}
                for i, time in enumerate(self.connection_next_avail)
            ],
            'current_step': self.current_step
        }
        return status

    def get_all_statuses(self):
        """返回所有充电桩位置的状态

        Returns:
            list: 包含所有充电桩状态的列表，每个充电桩返回[soc, power_ratio]
                  未连接的充电桩位置返回[0.0, 0.0]
        """
        statuses = []

        # 按顺序遍历所有充电桩位置
        for i in range(self.num_connection_points):
            # 查找是否有电池连接到该充电桩
            pt_idx = None
            for idx, point_id in self.battery_connection_points.items():
                if point_id == i:
                    pt_idx = idx
                    break

            if pt_idx is not None:
                # 如果有电池连接，获取其SOC和功率信息
                battery_name = self.connected_batteries.get(pt_idx)
                if battery_name:
                    # 获取电池状态
                    bat_name = f"Battery.{battery_name}" if not battery_name.startswith("Battery.") else battery_name
                    battery = self.circuit.batteries.get(bat_name)

                    if battery:
                        # 使用Battery对象的数据
                        soc = battery.soc  # 已归一化的SOC (0-1)
                        power_ratio = -1 * battery.actual_power() / battery.max_kw  # 充电功率/最大功率
                        statuses.append([soc, power_ratio])
                    else:
                        # 电池对象不存在，返回零状态——经输出检查，实际不存在这种情况
                        statuses.append([0.0, 0.0])
                        # print("电池对象不存在，返回零状态")
                else:
                    # 连接索引存在但电池名称不存在，返回零状态——经输出检查，实际不存在这种情况
                    statuses.append([0.0, 0.0])
                    # print("连接索引存在但电池名称不存在，返回零状态")
            else:
                # 充电桩未连接电池，返回零状态
                statuses.append([0.0, 0.0])
        # print(f"从函数get_all_statuses中返回的状态长度为 {len(statuses)}")  # 通过输出检查
        return statuses

    def _find_connection_point(self, idx):
        """查找指定电池的接入点编号"""
        # 直接从记录中获取连接点ID
        if idx in self.battery_connection_points:
            return self.battery_connection_points[idx]

        # 如果没有记录，则尝试查找（旧的兼容方法）
        for point_id, avail_time in enumerate(self.connection_next_avail):
            if avail_time == self.departure[idx]:
                return point_id
        return -1  # 未找到

    def _get_battery_soc(self, name):
        """获取电池的当前SOC"""
        status = self.controller.get_battery_status(name)
        return status['soc_percent'] if status else 0

    def step(self):
        """执行一个完整的时间步的方法调用示例，并不实际运行"""
        self.update_before_solve()

        # 默认使用SolveNoControl方法
        self.circuit.dss.ActiveCircuit.Solution.SolveNoControl()

        self.update_after_solve()

        # 返回当前状态信息
        return {
            'current_step': self.current_step - 1,
            'connected_batteries': len(self.connected_batteries),
            'waiting_queue': len(self.waiting_queue)
        }

    def reset(self):
        """重置电池站状态"""
        # 断开所有连接的电池
        for _, name in self.connected_batteries.items():
            self.controller.disconnect_battery(name)

        # 恢复初始状态
        self.waiting_queue = deque()
        self.connected_batteries = {}
        self.connection_next_avail = [0] * self.initial_data['num_connection_points']
        self.current_step = 0
        self.schedule = np.zeros((self.battery_count, self.total_steps))

        # 重置性能统计
        self.stats = {
            # 基本连接统计
            'connected_count': 0,  # 已连接的EV电池数【原计划用于统计已连接过的EV数，在断开时计数】
            'rejected_count': 0,  # 未能连接的EV电池数
            'waiting_count': 0,  # 进入等待队列的EV电池数
            'active_count': 0,  # 当前连接的EV电池数

            # 能量统计
            'total_discharge': 0,  # 总放电量(kWh)
            'total_charge': 0,  # 总充电量(kWh)
            'net_energy': 0,  # 净能量交换(kWh)

            # 充电满足度统计
            'completed_count': 0,  # 完成充电的EV电池数【原计划用于统计满足需求的EV数】
            'completed_soc': 0,  # 完成充电的EV电池的SOC增加总和
            'avg_completed_soc': 0,  # 完成充电的EV电池的平均增加的SOC
            'charge_satisfaction_ratio': 0,  # EV电池能量满足率之和（单个EV电池的满足率离开时的充电能量比所需的充电能量）
            'target_achieved_count': 0,  # 达到目标SOC（能量满足率为1，完全满足）的EV电池数
            'avg_target_achieved': 0,  # 充电满足率平均值(满足率之和/总连接数)

            # 服务质量统计
            'avg_waiting_time': 0,  # 平均等待时间(时间步)
            'total_waiting_time': 0,  # 总等待时间
            'max_waiting_time': 0,  # 最长等待时间

            # 时间利用率统计
            'total_connection_time': 0,  # 总连接时长
            'charger_utilization': 0,  # 充电桩利用率(总连接时长/(当前时段*充电桩数))

            # 实时指标
            'current_connection_rate': 0,  # 当前连接率(当前连接数/总连接点数)
            'current_charging_power': 0,  # 当前总充电功率(电池状态的charging_power累加)
            'current_success_rate': 0  # 当前服务成功率(完全满足数/总连接数)
        }

        print("BatteryStationManager已重置")
        return True

    def get_statistics(self):
        """计算并返回整体的性能统计"""
        # 计算已连接过的电池数量
        connected_count = np.count_nonzero(self.schedule.sum(axis=1))

        # Note: 满足充电需求的电池数量改为实时计算，并放置于 check_departures 中

        # 计算总放电量和充电量
        discharge_mask = self.schedule > 0
        charge_mask = self.schedule < 0
        total_discharge = self.schedule[discharge_mask].sum() * 0.25  # 每15分钟乘以0.25小时
        total_charge = -self.schedule[charge_mask].sum() * 0.25

        # 更新统计信息
        self.stats.update({
            'connected_count': connected_count,
            'total_discharge': total_discharge,
            'total_charge': total_charge,
            'net_energy': total_discharge - total_charge
        })

        # 打印性能指标
        print(f"电池站调度结果：")
        print(f"    接入的电池数量: {int(connected_count)}")
        print(f"    总放电量: {total_discharge:.2f} kWh")
        print(f"    总充电量: {total_charge:.2f} kWh")
        print(f"    净能量支持: {total_discharge - total_charge:.2f} kWh")
        print(f"    被拒绝的电池数量: {self.stats['rejected_count']}")

        return self.stats


# %% 弃用 Deprecated
class MergedRegulator(Edge):
    def __init__(self, dss, name, ori_names, edge, feature):
        bus1, bus2 = tuple(edge)
        super().__init__(name, bus1, bus2)
        self.dss = dss  # the circuit's dss simulator object
        self.tap = feature[0][0]  # tap value
        self.tap_feature = feature[0][1:]  # [mintap, maxtap, numtaps]
        self.trans_feature = feature[1]  # [xhl, r, kv_wdg1, kva_wdg1, kv_wdg2, kva_wdg2]
        self.regctr_feature = feature[2]  # [ForwardR, ForwardX, ForwardBand, ForwardVreg, CTPrimary, PTratio]
        self.ori_trans = []  # the transformer names associated with this regulator
        self.ori_regctr = []  # the regulator names associated with this regulator
        for trans, regctr in ori_names:
            self.ori_trans.append(trans)
            self.ori_regctr.append(regctr)

    def __repr__(self):
        return f'Reg Current Tapping: {self.tap!r}, Reg(mintap, maxtap, numtaps): {self.tap_feature!r} \
        Voltage at Bus: {self.bus1, self.dss.ActiveCircuit.Buses[self.bus1].puVmagAngle!r}, \
        Voltage at Bus: {self.bus2, self.dss.ActiveCircuit.Buses[self.bus2].puVmagAngle!r}'

    def set_tapping(self, numtap):
        """
        Set the tap value of this regulator as mintap + tapnum * (maxtap-mintap)/numtaps

        Args:
            numtap: integer value in [0, numtaps]

        Returns:
            the absolute change of numtap in integers
        """
        numtap = min(self.tap_feature[2], max(0, numtap))
        step = (self.tap_feature[1] - self.tap_feature[0]) / self.tap_feature[2]
        new_tap = numtap * step + self.tap_feature[0]
        diff = abs((self.tap - new_tap) / step)  # record tap difference
        self.tap = new_tap

        dssTrans = self.dss.ActiveCircuit.Transformers
        dssTrans.First
        while True:
            if dssTrans.Name in self.ori_trans:
                dssTrans.NumTaps = numtap
                dssTrans.Tap = self.tap
            if dssTrans.Next == 0: break

        return diff
        # should re-solve self.dss later
