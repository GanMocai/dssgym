# -*- coding = utf-8 -*-
# @Time : 2025/4/27 00:36
# @Author : Gan Mocai
# @FIle : ev_bms.py
# @Software : PyCharm

"""
模拟EV的BMS，根据电池的SOC，最大功率（和温度）与充电桩所给的容量设置功率。灵感源自调研反馈与宇航设想。
不依赖于已有的其他模块，所以单独搞一个文件。
https://claudeonline.top/chat/a08557ae-6984-4343-a7cf-4d948ce4c531
"""
from typing import List, Dict, Any, Optional, Union, Tuple


class EVBMS:
    """
    电动汽车电池管理系统 (EVBMS)
    根据当前SOC、电池支持的最大充电功率、充电桩容量和充电协议，计算并控制充电功率.
    其核心函数只有两个，set_soc, calculate_charge_power，is_charging状态不影响后者计算并返回一个值。
    """

    # 充电协议类型定义
    PROTOCOL_MCC = 0  # 多段恒流充电 (对应curve_type=0)
    PROTOCOL_Decay = 1  # 上升-平台-衰减 (对应curve_type=1)
    PROTOCOL_CC_CV = 2  # 恒功率充电 (对应curve_type=2)

    def __init__(self,
                 battery_capacity: float = 60.0,
                 max_battery_charge_power: float = 60.0,
                 initial_soc: float = 20.0,
                 charge_protocol: int = 0):
        """
        初始化EVBMS

        参数:
            battery_capacity: 电池容量(kWh)
            max_battery_charge_power: 电池支持的最大充电功率(kW)
            initial_soc: 初始SOC百分比(0-100)
            charge_protocol: 充电协议类型(0=多段恒流, 1=上升-平台-衰减, 2=恒功率)
        """
        # 基础参数
        self.battery_capacity = battery_capacity  # 电池容量(kWh)
        self.max_battery_charge_power = max_battery_charge_power  # 最大充电功率(kW)
        self.current_soc = initial_soc  # 当前电量百分比
        self.charge_protocol = charge_protocol  # 充电协议

        # 充电历史记录
        self.charging_history = []
        self.time_segment_counter = 0  # 时间段序号计数器

        # 环境因素
        self.battery_temperature = 25.0  # 默认电池温度25°C

        # 内部状态
        self.current_charge_power = 0.0  # 当前充电功率
        self.is_charging = False  # 是否正在充电
        self.charging_duration = 0  # 充电持续时间(秒)

    def start_charging(self, charger_power: float) -> float:
        """
        开始充电

        参数:
            charger_power: 充电桩提供的最大功率(kW)

        返回:
            实际充电功率(kW)
        """
        if self.is_charging:
            print("已经在充电中")
            return self.current_charge_power

        self.is_charging = True
        self.charging_duration = 0

        # 计算初始充电功率
        power = self.calculate_charge_power(charger_power)
        self.set_charge_power(power)

        return self.current_charge_power

    def stop_charging(self) -> Optional[Dict[str, Any]]:
        """
        停止充电

        返回:
            充电会话统计
        """
        if not self.is_charging:
            print("没有正在进行的充电")
            return None

        start_soc = self.charging_history[0]['soc'] if self.charging_history else self.current_soc

        charging_session = {
            "duration": self.charging_duration,
            "start_soc": start_soc,
            "end_soc": self.current_soc,
            "total_segments": self.time_segment_counter,
            "power_history": self.charging_history.copy()
        }

        self.is_charging = False
        self.current_charge_power = 0.0
        self.charging_history = []
        self.time_segment_counter = 0  # 重置时间段计数器

        return charging_session

    def update_charging_status(self, charger_power: float, elapsed_seconds: float) -> float:
        """
        更新充电状态

        参数:
            charger_power: 充电桩当前提供的最大功率(kW)
            elapsed_seconds: 已经充电的时间(秒)

        返回:
            更新后的充电功率(kW)
        """
        if not self.is_charging:
            print("没有正在进行的充电")
            return 0.0

        # 更新充电时间
        self.charging_duration = elapsed_seconds

        # 模拟SOC增加 (简化模型)
        # 假设在当前功率下，每小时充入的电量相当于电池容量的 currentPower/batteryCapacity 比例
        hours_fraction = elapsed_seconds / 3600
        energy_charged = self.current_charge_power * hours_fraction
        soc_increase = (energy_charged / self.battery_capacity) * 100

        # 更新SOC (不考虑充电效率损失，实际应该有系数)
        self.current_soc = min(100.0, self.current_soc + soc_increase)

        # 根据新SOC重新计算充电功率
        new_power = self.calculate_charge_power(charger_power)
        self.set_charge_power(new_power)

        return self.current_charge_power

    def set_charge_power(self, power: float) -> None:
        """
        直接设置充电功率，绕开BMS的处理

        参数:
            power: 充电功率(kW)
        """
        self.current_charge_power = power

        # 递增时间段序号
        self.time_segment_counter += 1

        # 记录到历史
        self.charging_history.append({
            "segment": self.time_segment_counter,
            "soc": self.current_soc,
            "power": power,
            "temperature": self.battery_temperature
        })

    def calculate_charge_power(self, charger_power: float) -> float:
        """
        计算合适的充电功率

        参数:
            charger_power: 充电桩提供的最大功率(kW)

        返回:
            计算后的充电功率(kW)
        """
        # 考虑充电桩功率限制与电池最大接受功率的较小值
        power = min(charger_power, self.max_battery_charge_power)

        # 根据充电协议和SOC调整充电功率
        if self.charge_protocol == self.PROTOCOL_MCC:  # 多段恒流充电
            if self.current_soc < 30:
                # 第一阶段: 最大功率充电
                pass  # 保持当前功率不变
            elif self.current_soc < 50:
                # 第二阶段: 80%功率
                power = power * 0.8
            elif self.current_soc < 70:
                # 第三阶段: 60%功率
                power = power * 0.6
            elif self.current_soc < 85:
                # 第四阶段: 40%功率
                power = power * 0.4
            else:
                # 最后阶段: 25%功率
                power = power * 0.25

        elif self.charge_protocol == self.PROTOCOL_Decay:  # 上升-平台-衰减
            if self.current_soc < 30:
                # 上升阶段: 功率随SOC线性增加
                power = power * (0.5 + self.current_soc / 60)  # 从50%额定功率开始线性增加
            elif self.current_soc < 70:
                # 平台阶段: 保持最大功率
                pass  # 保持当前功率不变
            else:
                # 衰减阶段: 功率随SOC增加而双曲线下降
                k = 0.15  # 衰减系数
                reduce_factor = 1 / (1 + k * (self.current_soc - 70))
                power = power * reduce_factor

        elif self.charge_protocol == self.PROTOCOL_CC_CV:  # 恒功率充电
            # 恒功率模式下功率不变，但在SOC很高时略微降低以保护电池
            if self.current_soc > 90:
                power = power * 0.9  # 轻微降低功率

        else:  # 未知充电协议，默认退化到多段恒流模式
            if self.current_soc < 30:
                pass  # 保持当前功率不变
            elif self.current_soc < 50:
                power = power * 0.8
            elif self.current_soc < 70:
                power = power * 0.6
            elif self.current_soc < 85:
                power = power * 0.4
            else:
                power = power * 0.25

        # 考虑温度影响 (简化模型)
        if self.battery_temperature < 0:
            # 低温时减少充电功率
            power = power * 0.5
        elif self.battery_temperature > 40:
            # 高温时减少充电功率
            power = power * 0.7

        # 限制最小充电功率为1kW
        return max(1.0, power)

    def set_battery_temperature(self, temperature: float) -> None:
        """
        设置电池温度

        参数:
            temperature: 电池温度(°C)
        """
        self.battery_temperature = temperature

        # 如果正在充电，重新计算功率
        if self.is_charging:
            new_power = self.calculate_charge_power(self.current_charge_power)
            self.set_charge_power(new_power)

    def get_charging_history(self) -> List[Dict[str, Any]]:
        """
        获取充电历史记录

        返回:
            充电历史记录
        """
        return self.charging_history

    def get_charging_status(self) -> Dict[str, Any]:
        """
        获取当前充电状态

        返回:
            充电状态
        """
        # 协议名称映射
        protocol_names = {
            self.PROTOCOL_MCC: "多段恒流充电",
            self.PROTOCOL_Decay: "上升-平台-衰减",
            self.PROTOCOL_CC_CV: "恒功率充电"
        }

        return {
            "is_charging": self.is_charging,
            "current_soc": self.current_soc,
            "current_power": self.current_charge_power,
            "protocol": self.charge_protocol,
            "protocol_name": protocol_names.get(self.charge_protocol, "Unknown"),
            "duration": self.charging_duration,
            "temperature": self.battery_temperature
        }

    def set_soc(self, new_soc: float) -> bool:
        """
        直接设置电池SOC值

        参数:
            new_soc: 新的SOC值(0-100)

        返回:
            操作是否成功
        """
        # 验证SOC值是否在有效范围内
        if not (0 <= new_soc <= 100):
            print(f"错误: SOC值 {new_soc} 超出有效范围(0-100)")
            return False

        # 更新SOC
        old_soc = self.current_soc
        self.current_soc = new_soc

        # 如果正在充电，根据新SOC重新计算充电功率
        if self.is_charging:
            # 计算功率前获取当前充电桩功率上限
            charger_power = self.current_charge_power
            new_power = self.calculate_charge_power(charger_power)
            self.set_charge_power(new_power)
            print(f"SOC从 {old_soc:.2f}% 更新为 {new_soc:.2f}%, 充电功率调整为 {new_power:.2f} kW")
        else:
            print(f"SOC从 {old_soc:.2f}% 更新为 {new_soc:.2f}%")

        return True


# 使用示例
if __name__ == "__main__":
    # 创建BMS实例
    bms = EVBMS(
        battery_capacity=60.0,  # 电池容量60kWh
        max_battery_charge_power=120.0,  # 电池最大接受充电功率120kW
        initial_soc=20.0,  # 初始SOC 20%
        charge_protocol=EVBMS.PROTOCOL_MCC  # 充电协议: 多段恒流 (0)
    )

    # 开始充电，充电桩提供60kW功率
    print(f"开始充电, 功率: {bms.start_charging(60.0):.2f} kW")
    print(f"当前状态: {bms.get_charging_status()}")

    # 模拟充电10分钟
    print(f"\n充电10分钟后, 功率: {bms.update_charging_status(60.0, 600):.2f} kW")
    print(f"当前SOC: {bms.current_soc:.2f}%")

    # 模拟充电1小时
    print(f"\n充电1小时后, 功率: {bms.update_charging_status(60.0, 3600):.2f} kW")
    print(f"当前SOC: {bms.current_soc:.2f}%")

    # 模拟电池温度变化
    bms.set_battery_temperature(5.0)
    print(f"\n电池温度降至5°C, 功率调整为: {bms.current_charge_power:.2f} kW")

    # 创建使用不同充电协议的BMS实例
    print("\n测试不同充电协议:")

    # 上升-平台-衰减
    cc_cv_bms = EVBMS(
        battery_capacity=60.0,
        max_battery_charge_power=120.0,
        initial_soc=20.0,  # 从20%开始，观察上升阶段
        charge_protocol=EVBMS.PROTOCOL_Decay  # 上升-平台-衰减 (1)
    )
    cc_cv_bms.start_charging(60.0)
    print(f"上升-平台-衰减协议(20% SOC)功率: {cc_cv_bms.current_charge_power:.2f} kW")

    # 让SOC增加到50%，观察平台阶段
    cc_cv_bms.set_soc(50.0)
    print(f"上升-平台-衰减协议(50% SOC)功率: {cc_cv_bms.current_charge_power:.2f} kW")

    # 让SOC增加到85%，观察衰减阶段
    cc_cv_bms.set_soc(85.0)
    print(f"上升-平台-衰减协议(85% SOC)功率: {cc_cv_bms.current_charge_power:.2f} kW")

    # 恒功率充电
    constant_bms = EVBMS(
        battery_capacity=60.0,
        max_battery_charge_power=120.0,
        initial_soc=50.0,
        charge_protocol=EVBMS.PROTOCOL_CC_CV  # 恒功率充电 (2)
    )
    constant_bms.start_charging(60.0)
    print(f"恒功率协议(50% SOC)功率: {constant_bms.current_charge_power:.2f} kW")

    # 让SOC增加到95%，观察高SOC时的行为
    constant_bms.set_soc(95.0)
    print(f"恒功率协议(95% SOC)功率: {constant_bms.current_charge_power:.2f} kW")

    # 继续使用原BMS充电直到SOC达到85%
    print("\n继续多段恒流充电:")
    while bms.current_soc < 85.0:
        bms.update_charging_status(60.0, 600)  # 每次充电10分钟

    print(f"充电至85% SOC, 当前功率: {bms.current_charge_power:.2f} kW")

    # 测试直接设置SOC
    print("\n测试直接设置SOC:")
    # 设置有效的SOC
    result = bms.set_soc(90.0)
    print(f"设置SOC为90%: {'成功' if result else '失败'}")
    print(f"当前功率: {bms.current_charge_power:.2f} kW")

    # 设置无效的SOC
    result = bms.set_soc(120.0)
    print(f"设置SOC为120%: {'成功' if result else '失败'}")
    print(f"当前SOC: {bms.current_soc:.2f}%")

    # 打印历史记录，查看时间段序号
    print("\n充电历史记录:")
    for record in bms.get_charging_history():
        print(f"时间段: {record['segment']}, SOC: {record['soc']:.2f}%, 功率: {record['power']:.2f} kW")

    # 停止充电并查看充电会话
    session = bms.stop_charging()
    print(f"\n充电会话总结:")
    print(f"持续时间: {session['duration'] / 60:.2f} 分钟")
    print(f"SOC变化: {session['start_soc']:.2f}% -> {session['end_soc']:.2f}%")
    print(f"时间段总数: {session['total_segments']}")
    print(f"功率历史记录数: {len(session['power_history'])}")