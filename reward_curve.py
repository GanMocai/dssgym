# -*- coding = utf-8 -*-
# @Time : 2025/5/4 19:53
# @Author : Gan Mocai
# @FIle : reward_curve.py
# @Software : PyCharm

"""
根据历史奖励数据的csv绘制奖励曲线，包括：
    1. 训练奖励曲线——回合奖励和历史平均奖励，数据来源csv文件，路径示例：D:\LENOVO\Documents\Python\ML\powergym\results_20250503_165005_13Bus_1000000\rewards_in_training.csv
    2. 测试奖励曲线——各奖励函数子项曲线和总曲线，数据来源csv文件，路径示例：D:\LENOVO\Documents\Python\ML\powergym\results_20250503_165005_13Bus_1000000\test_results_20250504_011214\rewards.csv
"""

import argparse
import datetime

import pandas as pd
import matplotlib.pyplot as plt

# 定义中英文字体映射
plt.rcParams['font.family'] = ['serif', 'sans-serif']
# # 设置英文和数字字体为 Times New Roman
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
# 设置中文字体为宋体
plt.rcParams['font.sans-serif'] = ['SimSun'] + plt.rcParams['font.sans-serif']
# 解决坐标轴负数的负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 其他字体属性设置
# plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 12

def plot_training_reward(csv_path, index:int=0):
    df = pd.read_csv(csv_path)
    # episodes = df["step"]  # 命名成step了，尴尬，太赶了
    # rewards = df["reward"]

    # 确保数据类型正确（将step和reward列转换为数值类型）
    df["step"] = pd.to_numeric(df["step"], errors="coerce")
    df["reward"] = pd.to_numeric(df["reward"], errors="coerce")

    # 使用窗口大小100计算移动平均奖励，使曲线更平滑
    window = 100
    # 在DataFrame上直接计算移动平均
    df['rewards_ma'] = df['reward'].rolling(window=window, min_periods=1).mean()

    episodes = df["step"].tolist()  # 需要时再转换为列表
    rewards = df["reward"].tolist()
    rewards_ma = df["rewards_ma"].tolist()

    # print(episodes, rewards, rewards_ma)

    plt.figure(figsize=(16/2.54, 10/2.54))
    plt.plot(episodes, rewards, 'b-', alpha=0.3, label="单回合奖励")
    plt.plot(episodes, rewards_ma, 'r-', linewidth=2, label="移动平均奖励")
    # 自动调整Y轴范围，使图像更清晰
    # 设置合理的Y轴范围，排除极端值的影响——1-3需要
    reward_q1 = pd.Series(rewards).quantile(0.000005)  # 5%分位数
    reward_q3 = pd.Series(rewards).quantile(1)  # 95%分位数
    y_min = max(reward_q1 / 1.5, min(rewards_ma) / 1.2)  # 确保能显示移动平均线
    y_max = min(reward_q3 * 1.5, max(rewards_ma) * 1.2)  # 确保能显示移动平均线
    plt.ylim(y_min, y_max)

    plt.xlabel("回合")
    plt.ylabel("奖励")
    plt.title("训练过程奖励曲线")
    plt.legend(loc='upper left', borderaxespad=0)
    plt.grid(True)
    plt.savefig(f'training_reward_curve_{index:02d}_{datetime.datetime.now().strftime("%Y%m%d")}.png', dpi=300)  # 保存图像
    plt.show()


def plot_test_reward(csv_path):
    df = pd.read_csv(csv_path)
    plt.figure(figsize=(10, 6))
    # 假设CSV包含各奖励函数分项及总奖励数据，绘制所有曲线
    for col in df.columns:
        plt.plot(df.index, df[col], label=col)
    plt.xlabel("Step")
    plt.ylabel("Reward")
    plt.title("Test Reward Curve")
    plt.legend()
    plt.grid(True)
    # plt.show()


def main():
    parser = argparse.ArgumentParser(description="根据CSV数据绘制奖励曲线")
    parser.add_argument("mode", choices=["train", "test"], help="选择绘制训练或测试奖励曲线")
    parser.add_argument("csv_path",
                        help="奖励数据CSV文件的路径，例如：D:\\LENOVO\\Documents\\Python\\ML\\powergym\\results_20250503_165005_13Bus_1000000\\rewards_in_training.csv")
    args = parser.parse_args()

    if args.mode == "train":
        plot_training_reward(args.csv_path)
    elif args.mode == "test":
        plot_test_reward(args.csv_path)


if __name__ == "__main__":
    # main()
    path = ['0']
    # path_1 = r'D:\LENOVO\Documents\Python\ML\powergym\results_20250501_021615_13Bus_cbat_1000000_01\rewards_in_training.csv'
    # path_2 = r'D:\LENOVO\Documents\Python\ML\powergym\results_20250502_005245_13Bus_cbat_s2_1000000_02\rewards_in_training.csv'
    # path_3 = r'D:\LENOVO\Documents\Python\ML\powergym\results_20250502_125646_13Bus_1000000_03\rewards_in_training.csv'
    # path_4 = r'D:\LENOVO\Documents\Python\ML\powergym\results_20250503_091058_13Bus_cbat_1000000_04\rewards_in_training.csv'
    # path_5 = r'D:\LENOVO\Documents\Python\ML\powergym\results_20250503_124337_13Bus_cbat_s2_1000000_05\rewards_in_training.csv'
    # path_6 = r'D:\LENOVO\Documents\Python\ML\powergym\results_20250503_165005_13Bus_1000000_06\rewards_in_training.csv'
    # path_7 = r'D:\LENOVO\Documents\Python\ML\powergym\results_20250504_012306_13Bus_cbat_1000000_07\rewards_in_training.csv'
    # path_8 = r'D:\LENOVO\Documents\Python\ML\powergym\results_20250504_055308_13Bus_cbat_1000000_08\rewards_in_training.csv'
    # path.append(path_1)
    # path.append(path_2)
    # path.append(path_3)
    # path.append(path_4)
    # path.append(path_5)
    # path.append(path_6)
    # path.append(path_7)
    # path.append(path_8)
    path_list = [
        r'D:\LENOVO\Documents\Python\ML\powergym\results_20250509_213723_13Bus_cbat_1000000\rewards_in_training.csv',
        r'D:\LENOVO\Documents\Python\ML\powergym\results_20250510_132849_13Bus_cbat_1000000\rewards_in_training.csv',
        r'D:\LENOVO\Documents\Python\ML\powergym\results_20250510_194947_13Bus_cbat_1000000\rewards_in_training.csv',
        r'D:\LENOVO\Documents\Python\ML\powergym\results_20250513_224309_13Bus_1000000\rewards_in_training.csv',
        r'D:\LENOVO\Documents\Python\ML\powergym\results_20250511_121502_13Bus_cbat_s2_1000000\rewards_in_training.csv',
        r'D:\LENOVO\Documents\Python\ML\powergym\results_20250512_143129_13Bus_cbat_1000000\rewards_in_training.csv',
        r'D:\LENOVO\Documents\Python\ML\powergym\results_20250514_092650_13Bus_1000000\rewards_in_training.csv',
        r'D:\LENOVO\Documents\Python\ML\powergym\results_20250513_002728_13Bus_cbat_s2_1000000\rewards_in_training.csv',
    ]
    for index, path in enumerate(path_list):
        plot_training_reward(path, index+1)