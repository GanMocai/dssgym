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
import pandas as pd
import matplotlib.pyplot as plt


def plot_training_reward(csv_path):
    df = pd.read_csv(csv_path)
    episodes = df["step"]  # 命名成step了，尴尬，太赶了
    rewards = df["reward"]
    # 使用窗口大小10计算移动平均奖励
    window = 10
    rewards_ma = rewards.rolling(window=window, min_periods=1).mean()

    plt.figure(figsize=(10, 6))
    plt.plot(episodes, rewards, label="Episode Reward")
    plt.plot(episodes, rewards_ma, label="Moving Average Reward")
    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.title("Training Reward Curve")
    plt.legend()
    plt.grid(True)
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
    plt.show()


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
    path = r'D:\LENOVO\Documents\Python\ML\powergym\results_20250501_021615_13Bus_cbat_1000000_01\rewards_in_training.csv'
    plot_training_reward(path)