# -*- coding = utf-8 -*-
# @Time : 2025/5/6 15:49
# @Author : Gan Mocai
# @FIle : test_results_analysis.py
# @Software : PyCharm

"""
对测试结果进行分析，包括根据测试结果绘制调度图（参考历史实现），读取测试结果记录并进行简单统计分析。
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import re
import glob


# 中文绘图参数设置，显示中文，负号显示
font = {'family': 'SimSun',  # 宋体
        'weight': 'bold',
        'size': '16'}
plt.rc('font', **font)  # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）


def load_schedule_data(file_path):
    """
    加载充电数据文件

    参数:
        file_path: 充电数据文件的路径

    返回:
        ev_ids: 电动汽车ID列表
        charging_powers: 充电功率数组，形状为(n_evs, n_timesteps)
    """
    # 检查第一行是否为表头
    with open(file_path, 'r') as f:
        first_line = f.readline().strip()
        has_header = 'step_0' in first_line

    if has_header:
        df = pd.read_csv(file_path)
        # 获取第一列的电动汽车ID
        ev_ids = df.iloc[:, 0].tolist()
        # 获取除第一列外的所有数据列
        charging_powers = df.iloc[:, 1:].astype(float).values
    else:
        df = pd.read_csv(file_path, header=None)
        # 提取EV ID和充电功率
        ev_ids = df[0].tolist()
        charging_powers = df.iloc[:, 1:].astype(float).values
    return ev_ids, charging_powers


def load_ev_stats_data(file_path):
    """
    加载电动汽车统计数据文件最后一行数据

    Args:
        file_path (str): 统计数据文件路径

    Returns:
        dict: 包含电动汽车统计信息的字典
    """
    if not os.path.exists(file_path):
        return None

    df = pd.read_csv(file_path, header=None)
    if len(df) == 0:
        return None

    # 获取最后一行数据
    last_row = df.iloc[-1]

    # 解析数据并存入字典
    stats_dict = {
        'step': int(last_row[0]),
        'connection_rate': float(last_row[1]),
        'charging_power': float(last_row[2]),
        'total_connections': int(last_row[3]),
        'success_rate': float(last_row[4]),
        'avg_satisfaction': float(last_row[5])
    }

    return stats_dict


def load_summary_data(file_path):
    """
    加载总结数据

    Args:
        file_path (str): 总结文件路径

    Returns:
        dict: 总结数据
    """
    summary = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if '总奖励:' in line:
                summary['total_reward'] = float(line.split(':')[1].strip())
            elif '步数:' in line:
                summary['steps'] = int(line.split(':')[1].strip())
            elif '电压低于0.95标幺值比例:' in line:
                summary['undervoltage_ratio'] = float(line.split(':')[1].strip().replace('%', ''))
            elif '电压高于1.05标幺值比例:' in line:
                summary['overvoltage_ratio'] = float(line.split(':')[1].strip().replace('%', ''))
    return summary


def load_rewards_data(file_path):
    """
    加载奖励数据文件并解析为字典

    Args:
        file_path (str): 奖励数据文件路径

    Returns:
        dict: 包含奖励数据的字典，可通过rewards['key'][index]方式查询值
    """
    if not os.path.exists(file_path):
        print(f"警告: 没有找到{file_path}文件")
        return None

    rewards = {}
    df = pd.read_csv(file_path)

    # 将列名作为字典的键
    for column in df.columns:
        rewards[column] = df[column].values

    return rewards


def analyze_schedule_and_stats(schedule, ev_stats):
    """
    分析充电调度，提取性能统计数据。

    Args:
        schedule (ndarray): 充电功率数据
        ev_stats (dict): 统计信息

    Returns:
        dict: 分析结果
    """
    # 服务车辆数（总连接数）：有充电功率>0的车辆
    served_vehicles = np.sum(np.any(schedule > 0, axis=1))

    # 计算每个车辆的充电总量 (kWh)
    # 假设每个时间段为15分钟(0.25小时)
    ev_total_energy = np.sum(schedule, axis=1) * 0.25

    # 完全满足的车辆数 (完全满足率)
    success_vehicles = ev_stats['success_rate'] * ev_stats['total_connections']

    # 平均满足率
    average_satisfaction = ev_stats['avg_satisfaction']

    # 总充电电量 (kWh)
    total_charging_energy = np.sum(ev_total_energy)

    # 平均单车充电量 (kWh)
    avg_ev_energy = total_charging_energy / served_vehicles if served_vehicles > 0 else 0

    # 最大总充电功率 (kW)：所有车辆在某一时刻的总充电功率最大值
    max_charging_power = np.max(np.sum(schedule, axis=0))

    return {
        'served_vehicles': served_vehicles,
        'success_vehicles': success_vehicles,
        'average_satisfaction': average_satisfaction,
        'total_charging_energy': total_charging_energy,
        'avg_ev_energy': avg_ev_energy,
        'max_charging_power': max_charging_power
    }


def generate_summary_stats(results_dir):
    """
    生成结果目录的统计数据

    Args:
        results_dir (str): 结果目录路径

    Returns:
        dict: 统计数据
    """
    # 查找充电调度文件
    schedule_file = os.path.join(results_dir, 'schedule.csv')

    # 查找充电站统计文件
    ev_stats_file = os.path.join(results_dir, 'ev_stats.csv')

    # 查找summary文件
    summary_file = os.path.join(results_dir, 'summary.txt')

    # 查找奖励记录文件
    rewards_file = os.path.join(results_dir, 'rewards.csv')

    # 加载充电数据
    if os.path.exists(schedule_file):
        ev_ids, charging_powers = load_schedule_data(schedule_file)
    else:
        raise FileNotFoundError("没找到schedule.csv")

    # 加载统计数据
    ev_stats = load_ev_stats_data(ev_stats_file)
    if ev_stats is None:
        print("警告: 没有找到有效的ev_stats.csv文件或文件为空")

    # 加载总结数据
    if os.path.exists(summary_file):
        summary_data = load_summary_data(summary_file)
    else:
        raise FileNotFoundError("没找到summary.txt")

    # 加载奖励数据
    rewards_data = load_rewards_data(rewards_file)

    # 分析充电调度
    charging_analysis = analyze_schedule_and_stats(charging_powers, ev_stats)

    # 计算超专变容量运行时间
    # 假设每检测到总奖励函数负值则增加0.25小时
    overload_hours = 0.0
    for i in range(96):
        if rewards_data['Transformer_reward'][i] <= -150 * 10:
            overload_hours += 0.25

    # 总PV发电量(kWh)
    # 保持为常数一致就行
    total_pv_energy = 460.17

    # 合并结果
    results = {
        **charging_analysis,
        'steps': summary_data['steps'],
        'overload_hours': overload_hours,
        'total_pv_energy': total_pv_energy,
        'undervoltage_ratio': summary_data['undervoltage_ratio'],
        'overvoltage_ratio': summary_data['overvoltage_ratio']
    }

    return results


def visualize_ev_schedule(charging_powers, ev_ids):
    """
    可视化EV充电调度

    Args:
        charging_powers (ndarray): 充电功率数据
        ev_ids (list): EV ID列表

    Returns:
        Figure: Matplotlib图形对象
    """
    # 设置图表尺寸
    plt.figure(figsize=(14, 10))

    # 自定义颜色映射
    custom_cmap = ListedColormap(['white'] + [plt.cm.YlOrRd(i) for i in np.linspace(0, 1, 100)])

    # 绘制热图
    plt.imshow(charging_powers, aspect='auto', cmap=custom_cmap,
               vmin=0, vmax=120, interpolation='nearest')

    # 添加颜色条
    cbar = plt.colorbar(label='充电功率 (kW)')

    # 设置坐标轴
    plt.ylabel('车辆编号')
    plt.xlabel('时间段')

    # 设置横轴为实际时刻（每个时间步为15分钟）
    T = charging_powers.shape[1]
    tick_positions = np.arange(0, T, 4)
    tick_labels = [f"{j // 4 :02d}:00" if j % 4 == 0 else "" for j in tick_positions]
    plt.xticks(tick_positions, tick_labels, fontsize=8)

    # 设置纵轴标签为EV ID
    if len(ev_ids) <= 20:
        plt.yticks(np.arange(len(ev_ids)), ev_ids)
    else:
        # 如果EV数量过多，只显示部分标签
        step = len(ev_ids) // 10
        plt.yticks(np.arange(0, len(ev_ids), step), [ev_ids[i] for i in range(0, len(ev_ids), step)])

    plt.title('电动汽车充电调度')

    return plt.gcf()


def test_results_analysis(results_dir, index=0):
    """
    分析测试结果并生成报告

    Args:
        results_dir (str): 结果目录路径
        index (int): 图片后缀
    """
    # 生成统计数据
    stats = generate_summary_stats(results_dir)

    # 打印统计结果
    print("===== 充电站性能统计 =====")
    print(f"服务车辆数: {stats['served_vehicles']}")
    print(f"完全满足数: {stats['success_vehicles']}")
    print(f"平均满足率: {stats['average_satisfaction']:.2%}")
    print(f"总充电电量: {stats['total_charging_energy']:.2f} kWh")
    print(f"平均单车充电量: {stats['avg_ev_energy']:.2f} kWh")
    print(f"最大EV充电功率: {stats['max_charging_power']:.2f} kW")
    print(f"超专变容量运行时间: {stats['overload_hours']:.2f} 小时")
    print(f"总PV发电量: {stats['total_pv_energy']:.2f} kWh")
    print(f"电压低于0.95标幺值比例: {stats['undervoltage_ratio']:.2f}%")
    print(f"电压高于1.05标幺值比例: {stats['overvoltage_ratio']:.2f}%")
    print("==========================")

    # 如果是基于字符串的数据，需要解析为充电功率矩阵
    if isinstance(results_dir, str) and 'batt_ev_' in results_dir:
        charging_data = []
        ev_ids = []
        for line in results_dir.split('\n'):
            if line.startswith('batt_ev_'):
                parts = line.split(',')
                ev_id = parts[0]
                ev_ids.append(ev_id)
                powers = [float(x) for x in parts[1:]]
                charging_data.append(powers)
        charging_powers = np.array(charging_data)
    else:
        # 查找充电调度文件
        charging_files = glob.glob(os.path.join(results_dir, 'schedule.csv'))
        if charging_files:
            ev_ids, charging_powers = load_schedule_data(charging_files[0])
        else:
            print("未找到充电调度数据文件，无法生成可视化")
            return

    # 生成调度矩阵图
    plt.figure()
    fig = visualize_ev_schedule(charging_powers, ev_ids)
    plt.tight_layout()

    # 保存图形
    output_file = os.path.join(os.getcwd(), f'charging_schedule_{index:02}.png')
    fig.savefig(output_file)
    print(f"充电调度图已保存至: {output_file}")

    return stats


# 示例用法
if __name__ == "__main__":
    # 使用结果目录路径
    # path_list = [
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250501_021615_13Bus_cbat_1000000_01\test_results_20250501_073028',
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250502_005245_13Bus_cbat_s2_1000000_02\test_results_20250502_065405',
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250502_125646_13Bus_1000000_03\test_results_20250502_214808',
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250503_091058_13Bus_cbat_1000000_04\test_results_20250503_123842',
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250503_124337_13Bus_cbat_s2_1000000_05\test_results_20250503_164645',
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250503_165005_13Bus_1000000_06\test_results_20250504_011214',
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250504_012306_13Bus_cbat_1000000_07\test_results_20250504_052230',
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250504_055308_13Bus_cbat_1000000_08\test_results_20250504_093552'
    # ]
    # for i in range(8):
    #     test_results_analysis(path_list[i], i+1)

    # rules_agent_path = r'D:\LENOVO\Documents\Python\ML\powergym\test_results_rules_20250506_200736_13Bus_cbat'
    # test_results_analysis(rules_agent_path, 0)
    pass
