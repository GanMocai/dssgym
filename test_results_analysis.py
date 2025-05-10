# -*- coding = utf-8 -*-
# @Time : 2025/5/6 15:49
# @Author : Gan Mocai
# @FIle : test_results_analysis.py
# @Software : PyCharm

"""
对测试结果进行分析，包括根据测试结果绘制调度图（参考历史实现），读取测试结果记录并进行简单统计分析。
"""
import datetime
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import re
import glob

from sympy.matrices.expressions.kronecker import rules

# 定义中英文字体映射
plt.rcParams['font.family'] = ['sans-serif', 'serif']
# 设置英文和数字字体为 Times New Roman
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
# 设置中文字体为宋体
plt.rcParams['font.sans-serif'] = ['SimSun'] + plt.rcParams['font.sans-serif']
# 解决坐标轴负数的负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 其他字体属性设置
# plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 16

# 如果要对特定元素单独设置字体，可以用以下方式
# 例如：设置标题
# plt.title('标题中文 English 123', fontproperties=fm.FontProperties(fname='SimSun.ttf'), fontname='Times New Roman')


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

    # 完全满足的车辆数
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
        if rewards_data['Transformer_reward'][i] <= 10.0/200 * 200:
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
        # 提取数字部分作为标签
        formatted_ids = [re.search(r'\d+', ev_id).group() if re.search(r'\d+', ev_id) else ev_id for ev_id in ev_ids]
        plt.yticks(np.arange(len(ev_ids)), formatted_ids)
    else:
        # 如果EV数量过多，只显示部分标签
        step = len(ev_ids) // 10
        formatted_ids = [re.search(r'\d+', ev_ids[i]).group() if re.search(r'\d+', ev_ids[i]) else ev_ids[i]
                        for i in range(0, len(ev_ids), step)]
        plt.yticks(np.arange(0, len(ev_ids), step), formatted_ids)

    # plt.title('电动汽车充电调度')

    return plt.gcf()


def visualize_ev_schedule_revised(charging_powers, ev_ids):
    """
    可视化EV充电调度
    Args:
        charging_powers (ndarray): 充电功率数据
        ev_ids (list): EV ID列表
    Returns:
        Figure: Matplotlib图形对象
    """
    # 创建共享X轴的两个子图
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(22 / 2.54, (22 / 2.54) * (8 / 12)), sharex=True)

    # 自定义颜色映射
    custom_cmap = ListedColormap(['white'] + [plt.cm.YlOrRd(i) for i in np.linspace(0, 1, 100)])

    # 在主图中绘制热图
    im = ax1.imshow(charging_powers, aspect='auto', cmap=custom_cmap,
                    vmin=0, vmax=120, interpolation='nearest')

    # 配置第一个子图
    ax1.set_ylabel('车辆编号')
    ax1.set_title('电动汽车实际充电功率')

    # 添加颜色条
    cbar_ax = fig.add_axes([0.06, 0.15, 0.02, 0.7])  # [左, 下, 宽, 高]
    cbar = fig.colorbar(im, cax=cbar_ax, label='充电功率 (kW)')

    # 设置纵轴标签为EV ID
    n_evs = len(ev_ids)
    if n_evs <= 20:
        # 提取数字部分作为标签
        formatted_ids = [re.search(r'\d+', ev_id).group() if re.search(r'\d+', ev_id) else ev_id for ev_id in ev_ids]
        ax1.set_yticks(np.arange(len(ev_ids)))
        ax1.set_yticklabels(formatted_ids)
    else:
        # 如果EV数量过多，只显示部分标签
        step = max(1, n_evs // 10)
        positions = np.arange(0, n_evs, step)
        formatted_ids = [re.search(r'\d+', ev_ids[i]).group() if re.search(r'\d+', ev_ids[i]) else ev_ids[i]
                         for i in positions]
        ax1.set_yticks(positions)
        ax1.set_yticklabels(formatted_ids)

    # 在下方子图中绘制总功率曲线
    total_power = np.sum(charging_powers, axis=0)
    ax2.plot(np.arange(charging_powers.shape[1]), total_power, 'b-', linewidth=2)
    ax2.set_xlim(0, charging_powers.shape[1] - 1)
    ax2.set_ylabel('总充电功率 (kW)')
    ax2.set_xlabel('时间 (时:分)')
    ax2.grid(True, linestyle='--', alpha=0.7)

    # 设置横轴为实际时刻（每个时间步为15分钟）
    T = charging_powers.shape[1]
    tick_positions = np.arange(0, T, 4)
    tick_labels = [f"{j // 4 :02d}:00" if j % 4 == 0 else "" for j in tick_positions]
    ax2.set_xticks(tick_positions)
    ax2.set_xticklabels(tick_labels, fontsize=8)

    # 添加垂直分隔线表示每6小时
    for hour in range(6, 24, 6):
        ax1.axvline(x=hour * 4, color='gray', linestyle='--', alpha=0.5)
        ax2.axvline(x=hour * 4, color='gray', linestyle='--', alpha=0.5)

    # 调整布局，为左侧的颜色条留出更多空间
    plt.subplots_adjust(right=0.95, left=0.2, bottom=0.15, top=0.90)

    return plt.gcf()


def visualize_charging_schedule_with_batteries(results, title=None):
    """
    可视化充电计划以及PV、储能数据，使用统一的显示风格，标注使用中文。

    Args:
        results (dict): 优化结果字典，包含ev_schedule、pv_power、battery_charge等信息
        title (str, optional): 自定义图表标题
    """
    # 提取结果数据
    charging_data = results['ev_schedule']
    pv_power = results['pv_power']
    battery_charge = results['battery_charge']
    battery_discharge = results['battery_discharge']
    # 可以直接从ev_power中取出充电站功率，也可以从charging_data.sum计算
    station_active_power = results['ev_power']['CS1'] if 'ev_power' in results else charging_data.sum(axis=0)

    # 获取数据维度
    Num_EVs = charging_data.shape[0]
    T = charging_data.shape[1]

    # 如果有station_net_load_p和station_net_load_q，计算视在功率
    if 'station_net_load_p' in results and 'station_net_load_q' in results:
        station_apparent_power = [np.sqrt(p ** 2 + q ** 2) for p, q in
                                  zip(results['station_net_load_p'], results['station_net_load_q'])]
    else:
        # 根据结果重新计算视在功率
        ev = results['ev_power']['CS1']
        pv = results['pv_power']
        bc = results['battery_charge']
        bd = results['battery_discharge']
        phi_ev = math.acos(-0.98)
        phi_b = math.acos(0.95)
        station_apparent_power = []
        for p_ev, p_pv, bc_t, bd_t in zip(ev, pv, bc, bd):
            p_net = p_ev - p_pv + bc_t - bd_t
            q_net = p_ev * math.tan(phi_ev) + (bc_t - bd_t) * math.tan(phi_b)
            station_apparent_power.append(math.sqrt(p_net ** 2 + q_net ** 2))

    # 将MW转换为kW显示
    if max(station_active_power) < 1.0:
        pv_power = [p * 1000 for p in pv_power]
        battery_charge = [b * 1000 for b in battery_charge]
        battery_discharge = [b * 1000 for b in battery_discharge]
        station_apparent_power = [s * 1000 for s in station_apparent_power]

    # 获取充电站功率限制
    Power_Station = 800  # 默认值800kVA，如果在结果中有定义则使用结果中的值

    # 设置图表尺寸
    width_inches = 22 / 2.54  # 转换为英寸
    height_inches = width_inches * (8 / 12)

    # 创建共享X轴的两个子图
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(width_inches, height_inches), sharex=True)

    # 自定义颜色映射
    custom_cmap = ListedColormap(['white'] +
                                 [plt.cm.YlOrRd(i) for i in np.linspace(0, 1, 100)])

    # 绘制热图
    im = ax1.imshow(charging_data, aspect='auto', cmap=custom_cmap,
                    vmin=0, vmax=120, interpolation='nearest')

    # 配置第一个子图
    if title:
        ax1.set_title(title)
    ax1.set_ylabel('车辆编号')

    # 添加颜色条
    cbar_ax = fig.add_axes([0.06, 0.15, 0.02, 0.7])  # [左, 下, 宽, 高]
    cbar = fig.colorbar(im, cax=cbar_ax, label='充电功率 (kW)')

    # 绘制功率曲线
    ax2.plot(station_active_power, color='blue', label='充电站有功功率')
    ax2.plot(station_apparent_power, color='purple', linestyle='-.', label='充电站视在功率')
    ax2.plot(pv_power, color='green', label='PV有功功率')

    # 绘制EV充电有功功率
    ev_only_power = np.array(results['ev_power']['CS1']) * 1000 if max(station_active_power) < 1.0 else np.array(results['ev_power']['CS1'])
    ax2.plot(ev_only_power, color='red', linestyle=':', label='EV充电有功功率')

    # 绘制储能充放电功率
    battery_power = np.array(battery_discharge) - np.array(battery_charge)
    ax2.plot(battery_power, color='orange', label='储能净功率\n(正值为放电)')

    # 添加充电站功率限制线
    ax2.axhline(y=Power_Station, color='red', linestyle='--', label='充电站专变容量')

    # 配置第二个子图
    ax2.set_ylabel('功率 (kW)')
    # 设置Y轴范围，确保所有曲线都能显示
    all_powers = np.concatenate([station_active_power, pv_power, battery_power, station_apparent_power])
    y_min = min(min(all_powers) - 10, -10)
    y_max = max(max(station_apparent_power) + 10, Power_Station + 10)
    ax2.set_ylim(y_min, y_max)

    # 设置横轴为实际时刻（每个时间步为15分钟）
    tick_positions = np.arange(0, T, 4)
    tick_labels = [f"{j // 4 :02d}:00" if j % 4 == 0 else "" for j in tick_positions]
    ax2.set_xticks(tick_positions)
    ax2.set_xticklabels(tick_labels, fontsize=8)
    ax2.set_xlabel('时间 (时:分)')

    # 将第二个子图的图例移到图表内部
    ax2.legend(loc='upper right', borderaxespad=0, fontsize=8)

    # 调整布局，为左侧的颜色条留出更多空间
    plt.subplots_adjust(right=0.95, left=0.2, bottom=0.15, top=0.90)

    return fig, (ax1, ax2)


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
    print(f"最大EV总充电功率: {stats['max_charging_power']:.2f} kW")
    print(f"超专变容量运行时长: {stats['overload_hours']:.2f} 小时")
    print(f"总PV发电量: {stats['total_pv_energy']:.2f} kWh")
    print(f"电压低于0.95标幺值比例: {stats['undervoltage_ratio']:.2f}%")
    print(f"电压高于1.05标幺值比例: {stats['overvoltage_ratio']:.2f}%")
    print("==========================")

    # 读取充电调度文件
    charging_files =os.path.join(results_dir, 'schedule.csv')
    ev_ids, charging_powers = load_schedule_data(charging_files)

    # 生成调度矩阵图
    plt.figure()
    fig = visualize_ev_schedule_revised(charging_powers, ev_ids)
    # plt.tight_layout()

    # 保存图形
    output_file = os.path.join(os.getcwd(), f'charging_schedule_{index:02}_{datetime.datetime.now().strftime("%Y%m%d")}.png')
    fig.savefig(output_file)
    print(f"充电调度图已保存至: {output_file}")

    return stats


# 示例用法
if __name__ == "__main__":
    # 旧测试结果
    # path_list = [
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250501_021615_13Bus_cbat_1000000_01\test_results_20250501_073028',
    #
    #
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250502_005245_13Bus_cbat_s2_1000000_02\test_results_20250502_065405',
    #
    #
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250502_125646_13Bus_1000000_03\test_results_20250502_214808',
    #
    #
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250503_091058_13Bus_cbat_1000000_04\test_results_20250503_123842',
    #
    #
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250503_124337_13Bus_cbat_s2_1000000_05\test_results_20250503_164645',
    #
    #
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250503_165005_13Bus_1000000_06\test_results_20250504_011214',
    #
    #
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250504_012306_13Bus_cbat_1000000_07\test_results_20250504_052230',
    #
    #
    #     r'D:\LENOVO\Documents\Python\ML\powergym\results_20250504_055308_13Bus_cbat_1000000_08\test_results_20250504_093552',
    #
    #
    # ]
    # rules_agent_path = r'D:\LENOVO\Documents\Python\ML\powergym\test_results_rules_20250506_200736_13Bus_cbat'

    path_list = [
        r'',
        r'',
    ]
    rules_agent_path = r''
    for i in range(len(path_list)):
        test_results_analysis(path_list[i], i+1)
    test_results_analysis(rules_agent_path, 0)
    pass
