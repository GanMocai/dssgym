# Copyright 2021 Siemens Corporation
# Copyright 2025 Su Chenhui
# SPDX-License-Identifier: MIT

"""
`env_register.py` 模块是 PowerGym 项目中的环境注册中心，负责管理和创建电力系统仿真环境。主要包含以下功能：

1. 定义和存储各种电力系统的基本信息（`_SYS_INFO`），包括源节点、节点大小、标签偏移等显示参数
2. 维护不同环境配置（`_ENV_INFO`），提供多种预设环境，包括：
   - 不同规模的 IEEE 标准测试系统（13/34/123/8500节点）
   - 连续/离散电池控制变体（cbat 后缀）
   - 电池 SOC 优化变体（soc 后缀）
   - 各种奖励权重配置（power_w/cap_w/reg_w/soc_w/dis_w）

3. 提供核心功能：
   - `get_info_and_folder`：获取环境配置和系统文件路径
   - `make_env`：创建环境实例，支持并行环境创建
   - `remove_parallel_dss`：清理并行环境创建的临时文件

该模块作为 PowerGym 的入口点，简化了强化学习算法与电力系统仿真的对接，便于研究人员测试不同控制策略在各种电网拓扑下的性能。

Note: 比例因子 scale 为负载曲线倍数，缩放从csv读取得到的负载曲线数据。

Improve:
    1. 修改了最终的Env类的参数设置，最大步数改为96，移除了regulator和电容器的奖励权重

"""

import os
import inspect
import re
from powergym.powergym.env import Env

# map from system_name to fixed information of the system
# 系统名称到对应固定信息的映射，包括并网点、node数量、标签偏移等参数。
_SYS_INFO = {
    '13Bus': {
        'source_bus': 'sourcebus',
        'node_size': 500,
        'shift': 10,  # shift 是绘图上的标签偏离量
        'show_node_labels': True
    },

    '34Bus': {
        'source_bus': 'sourcebus',
        'node_size': 500,
        'shift': 80,
        'show_node_labels': True
    },

    '123Bus': {
        'source_bus': '150',
        'node_size': 400,
        'shift': 80,
        'show_node_labels': True
    },

    '8500-Node': {
        'source_bus': 'e192860',
        'node_size': 10,
        'shift': 0,
        'show_node_labels': False
    }
}

# map from env_name to the necessary information
# 环境名称到必要的系统信息的映射，包括系统名称、dss文件名、时间步数、变压器抽头和电池的动作数量、奖励函数权重等。
"""
{system name}_{use continuous battery}_{use soc penalty} 
标准版：平衡功率损耗和控制成本
cbat版：电池功率连续
soc版：使用soc_penalty，显著提高了 soc_w 值
cbat_soc版：结合cbat和soc

power_w 奖励函数powerloss_reward中的权重。较高的 power_w 值意味着环境会更重视降低功率损失。
cap_w 奖励函数ctrl_reward中控制成本中电容的权重。较高的 cap_w 值意味着环境会更重视少调整电容器。
reg_w 奖励函数ctrl_reward中控制成本中调压器的权重。较高的 reg_w 值意味着环境会更重视少调整调压器。
soc_w 奖励函数ctrl_reward中电池soc的权重。较高的 soc_w 值意味着环境会更重视不改变电池的SOC。
dis_w 奖励函数ctrl_reward中电池充放电的权重。较高的 dis_w 值意味着环境会更重视不充放电。
"""

_ENV_INFO = {
    '13Bus': {
        'system_name': '13Bus',
        'dss_file': 'IEEE13Nodeckt_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': 33,
        'power_w': 10.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 0.0 / 33,
        'dis_w': 6.0 / 33
    },

    '13Bus_cbat': {
        'system_name': '13Bus',
        'dss_file': 'IEEE13Nodeckt_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': float('inf'),
        'power_w': 10.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 0.0 / 33,
        'dis_w': 6.0 / 33,
    },

    '13Bus_soc': {
        'system_name': '13Bus',
        'dss_file': 'IEEE13Nodeckt_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': 33,
        'power_w': 10.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 20.0 / 33,
        'dis_w': 1.0 / 33
    },

    '13Bus_cbat_soc': {
        'system_name': '13Bus',
        'dss_file': 'IEEE13Nodeckt_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': float('inf'),
        'power_w': 10.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 20.0 / 33,
        'dis_w': 1.0 / 33,
    },

    '34Bus': {
        'system_name': '34Bus',
        'dss_file': 'ieee34Mod1_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': 33,
        'power_w': 1.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 0.0 / 33,
        'dis_w': 10.0 / 33,
    },

    '34Bus_cbat': {
        'system_name': '34Bus',
        'dss_file': 'ieee34Mod1_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': float('inf'),
        'power_w': 1.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 0.0 / 33,
        'dis_w': 10.0 / 33,
    },

    '34Bus_soc': {
        'system_name': '34Bus',
        'dss_file': 'ieee34Mod1_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': 33,
        'power_w': 1.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 500.0 / 33,
        'dis_w': 4.0 / 33,
    },

    '34Bus_cbat_soc': {
        'system_name': '34Bus',
        'dss_file': 'ieee34Mod1_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': float('inf'),
        'power_w': 1.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 500.0 / 33,
        'dis_w': 4.0 / 33,
    },

    '123Bus': {
        'system_name': '123Bus',
        'dss_file': 'IEEE123Master_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': 33,
        'power_w': 10.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 0.0 / 33,
        'dis_w': 7.0 / 33,
    },

    '123Bus_cbat': {
        'system_name': '123Bus',
        'dss_file': 'IEEE123Master_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': float('inf'),
        'power_w': 10.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 0.0 / 33,
        'dis_w': 7.0 / 33,
    },

    '123Bus_soc': {
        'system_name': '123Bus',
        'dss_file': 'IEEE123Master_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': 33,
        'power_w': 10.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 500.0 / 33,
        'dis_w': 5.0 / 33,
    },

    '123Bus_cbat_soc': {
        'system_name': '123Bus',
        'dss_file': 'IEEE123Master_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': float('inf'),
        'power_w': 10.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 500.0 / 33,
        'dis_w': 5.0 / 33,
    },

    '8500Node': {
        'system_name': '8500-Node',
        'dss_file': 'Master_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': 33,
        'power_w': 1.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 0.0 / 33,
        'dis_w': 200.0 / 33,
    },

    '8500Node_cbat': {
        'system_name': '8500-Node',
        'dss_file': 'Master_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': float('inf'),
        'power_w': 1.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 0.0 / 33,
        'dis_w': 200.0 / 33,
    },

    '8500Node_soc': {
        'system_name': '8500-Node',
        'dss_file': 'Master_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': 33,
        'power_w': 1.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 10000 / 33,
        'dis_w': 100 / 33,
    },

    '8500Node_cbat_soc': {
        'system_name': '8500-Node',
        'dss_file': 'Master_daily.dss',
        'max_episode_steps': 24,
        'reg_act_num': 33,
        'bat_act_num': float('inf'),
        'power_w': 1.0,
        'cap_w': 1.0 / 33,
        'reg_w': 1.0 / 33,
        'soc_w': 10000 / 33,
        'dis_w': 100 / 33,
    }
}

# 充电站信息 连接的母线名称、充电枪数目
_STATION_INFO = {
    '13Bus': {
        'bus_name': '680',  # 充电站连接的母线名称
        'num_chargers': 10,  # 充电桩数量
        'transformer_kVA': 800, # 设定专变的容量
        # 'ev_price': '13Bus_ev_price.csv',  # 电价文件
    },
    '34Bus': {
        'bus_name': '',  # 充电站连接的母线名称
        'num_chargers': 10,  # 充电桩数量
        'transformer_kVA': 800, # 设定专变的容量
        # 'ev_price': '13Bus_ev_price.csv',  # 电价文件
    },
    '123Bus': {
        'bus_name': '',  # 充电站连接的母线名称
        'num_chargers': 10,  # 充电桩数量
        'transformer_kVA': 800,  # 设定专变的容量
        # 'ev_price': '13Bus_ev_price.csv',  # 电价文件
    },
    '8500-Node': {
        'bus_name': '',  # 充电站连接的母线名称
        'num_chargers': 10,  # 充电桩数量
        'transformer_kVA': 800,  # 设定专变的容量
        # 'ev_price': '13Bus_ev_price.csv',  # 电价文件
    }
}

# 充电需求队列信息
_EV_INFO = {
    '13Bus': {
        'ev_demand': r'D:\LENOVO\Documents\Python\ML\powergym\ev_demand\ev_demand-public_parking-general-250-A95.csv',  # 充电需求文件
    },
    '34Bus': {
        'ev_demand': '34Bus_ev_demand.csv',  # 充电需求文件
    },
    '123Bus': {
        'ev_demand': '123Bus_ev_demand.csv',  # 充电需求文件
    },
    '8500-Node': {
        'ev_demand': '8500Node_ev_demand.csv',  # 充电需求文件
    }
}

# 添加系统信息和充电站信息到环境ENV信息
for env in _ENV_INFO.keys():
    sys = _ENV_INFO[env]['system_name']
    _ENV_INFO[env].update(_SYS_INFO[sys])  # 将对应_SYS_INFO中的所有配置项添加到环境的配置字典中
    # 将所有的max_episode_steps从24改为96
    _ENV_INFO[env]['max_episode_steps'] = 96
    # 场景不涉及regulator操作，将所有环境的reg_w置零，禁用regulator奖励权重
    _ENV_INFO[env]['reg_w'] = 0.0
    # 汽车充电站较少配置电容，将所有环境的cap_w置零，禁用电容奖励权重
    _ENV_INFO[env]['cap_w'] = 0.0
    # 暂时不考虑由SOC构成的奖励项
    _ENV_INFO[env]['soc_w'] = 0.0
    # 暂时不考虑对放电的限制
    _ENV_INFO[env]['dis_w'] = 0.0
    # 在info中添加充电站信息，包括母线、连接点数量
    _ENV_INFO[env].update(_STATION_INFO[sys])
    # 在info中ev充电需求队列文件路径
    _ENV_INFO[env].update(_EV_INFO[sys])
    # 在info中添加充电站相关充电完成率的权重
    _ENV_INFO[env]['completion_w'] = 15  # 常用值10
    _ENV_INFO[env]['connection_w'] =2 * 10/250  # 按EV总数目归一化，同时又突出重要性
    _ENV_INFO[env]['energy_w'] = 10
    # 显式设置电压越限惩罚权重
    _ENV_INFO[env]['voltage_w'] = 10
    _ENV_INFO[env]['tf_capacity_w'] = 10


# %% 函数
def get_info_and_folder(env_name):
    """
    获取系统信息和环境的文件夹路径，会根据env_name的后缀(_s 数值)【在ENV信息里修改key】，设置对应的scale，同时调整soc_w
    Args:
        env_name: the name of the env, such as '13Bus', '34Bus', '123Bus', '8500Node'
    Returns:
        base_info: the basic information of the env
        folder_path: the path of the env
    """
    scale = 1.0
    # 通过env_name的后缀判断是否需要进行缩放并提取scale
    is_scaled = re.match(pattern='.*(_s)([0-9]*[.])?[0-9]+?', string=env_name)  # match example: 13Bus_s2.0
    if is_scaled:
        matched_str = is_scaled.group(0)
        idx = matched_str.rfind('_s')
        env_name = matched_str[:idx]
        scale = float(matched_str[idx + 2:])  # 取出匹配到的字符串中的数字部分
    # 检查基础环境是否存在
    assert env_name in _ENV_INFO, env_name + ' not implemented'

    # get base_info
    base_info = _ENV_INFO[env_name].copy()
    if is_scaled:
        base_info['scale'] = scale
        base_info['soc_w'] = base_info['soc_w'] * (scale ** 2)

    # get folder path
    folder_path = os.path.join(os.path.dirname(os.path.abspath(inspect.getsourcefile(Env))), '..', 'systems')
    folder_path = os.path.abspath(folder_path)
    return base_info, folder_path


def make_env(env_name, dss_act=False, worker_idx=None):
    """
    根据信息创建环境实例
    Args:
        env_name: env名称, '13Bus', '34Bus', '123Bus', '8500Node' 可直接给字符串添加后缀_s和数值进行负载曲线缩放(也可直接添加字典，在env初始化中有处理)
        dss_act: 是否使用dss，如果为True，则使用dss的动作
        worker_idx: 进程的索引号，默认为None
    Returns:
        env: 环境实例
    """
    base_info, folder_path = get_info_and_folder(env_name)

    if worker_idx is None:
        return Env(folder_path, base_info, dss_act)
    else:
        base_file = os.path.join(folder_path, base_info['system_name'], base_info['dss_file'])
        assert os.path.exists(base_file), base_file + ' does not exist'
        fin = open(base_file, 'r')

        with open(base_file[:-4] + '_' + str(worker_idx) + '.dss', 'w') as fout:
            for line in fin:
                if line.strip() == 'redirect loadshape.dss':
                    fout.write('redirect loadshape_' + str(worker_idx) + '.dss\n')
                else:
                    fout.write(line)
        info = base_info.copy()
        info['dss_file'] = info['dss_file'][:-4] + '_' + str(worker_idx) + '.dss'
        info['worker_idx'] = worker_idx
        return Env(folder_path, info, dss_act)


def remove_parallel_dss(env_name, num_workers):
    """移除并行env训练生成的dss文件
    Args:
        env_name: 待删除的env名称
        num_workers: 并行训练的worker数量
    """
    base_info, folder_path = get_info_and_folder(env_name)
    base_main = os.path.join(folder_path, base_info['system_name'], base_info['dss_file'])
    base_loadshape = os.path.join(folder_path, base_info['system_name'], 'loadshape.dss')

    bases = [base_main, base_loadshape]
    for base in bases:
        for i in range(num_workers):
            fname = base[:-4] + '_' + str(i) + '.dss'
            if os.path.exists(fname):
                os.remove(fname)
