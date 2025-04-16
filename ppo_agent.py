# -*- coding = utf-8 -*-
# @Time : 2025/3/12 下午6:24
# @Author : Gan Mocai
# @FIle : ppo_agent.py
# @Software : PyCharm

"""
用SB3的PPO算法作为智能体进行训练，主程序
note: 统一设置各种随机seed为27
note: 在代码执行过程中，保存模型时，未使用cwd则会保存到对应dss文件所在目录；保存图片在powergym文件夹下的plots目录中
note: 目前使用了monkey patch临时替换函数reset，参考自 https://yuanbao.tencent.com/chat/naQivTmsDa/26ca9f85-b738-4e39-8d3d-7550578fdb25
note: 自定义网络参数的方式可见 https://kimi.moonshot.cn/chat/cv8ol6kchmtsrgk9q630
"""

from stable_baselines3 import PPO
from powergym.powergym.env_register import make_env, remove_parallel_dss
from RL.SB3.reward_monitor_callback import RewardMonitorCallback

import matplotlib.pyplot as plt
import numpy as np
import imageio.v2 as imageio  # 兼容旧版接口
import glob

import argparse
import random
import itertools
import os
import multiprocessing as mp


def parse_arguments():
    parser = argparse.ArgumentParser(description='Argument Parser')
    parser.add_argument('--env_name', default='13Bus')
    parser.add_argument('--seed', type=int, default=27, metavar='N', help='random seed')
    parser.add_argument('--model_seed', type=int, default=27, metavar='N',
                        help='random seed for model initialization')
    parser.add_argument('--num_steps', type=int, default=10000, metavar='N',
                        help='maximum number of steps')
    parser.add_argument('--mode', type=str, default='ppo',
                        help="running mode, ppo, parallel_ppo, episodic_ppo or dss")
    parser.add_argument('--num_workers', type=int, default=3, metavar='N',
                        help='number of parallel processes')
    parser.add_argument('--use_plot', type=lambda x: str(x).lower() == 'true', default=False)
    parser.add_argument('--plot_path', type=str, default=r'plots\ppo_model', )
    parser.add_argument('--do_testing', type=lambda x: str(x).lower() == 'true', default=False)
    parser.add_argument('--model_path', type=str, default=r'models\ppo_model',  # 纯粹使用该相对路径时，实际会转到对应dss文件所在目录下
                        help="path to save or load the model")
    parser.add_argument('--learning_rate', type=float, default=3e-6,  # 3e-4
                        help="learning rate for PPO")
    parser.add_argument('--n_steps', type=int, default=2048,
                        help="number of steps to run for each environment per update")
    parser.add_argument('--batch_size', type=int, default=64,
                        help="mini-batch size for optimization")
    arguments = parser.parse_args()
    return arguments


def seeding(seed) -> None:
    """
    统一设置随机种子，包括numpy、random和os环境变量
    Args:
        seed: 随机种子
    """
    np.random.seed(seed)
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)


def seeding_all(seed) -> None:
    """
    统一设置随机种子，包括numpy、random、os环境变量和PyTorch
    Args:
        seed: 随机种子
    """
    import torch

    np.random.seed(seed)
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


def run_ppo_agent(args, load_profile_idx=0, worker_idx=None, use_plot=False, print_step=False):
    """
    运行PPO智能体
    Args:
        args: 命令行参数
        load_profile_idx: 负载配置索引
        worker_idx: 进程ID
        use_plot: 是否绘图
        print_step: 是否打印每步信息
    """
    cwd = os.getcwd()
    print('当前工作目录:', cwd)  # 工作目录在powergym

    # 获取环境
    env = make_env(args.env_name, worker_idx=worker_idx)
    env.seed(args.seed + 0 if worker_idx is None else worker_idx)

    if print_step:
        print('This system has {} capacitors, {} regulators and {} batteries'.format(env.cap_num, env.reg_num,
                                                                                     env.bat_num))
        print('reg, bat action nums: ', env.reg_act_num, env.bat_act_num)
        print('-' * 80)

    # 创建回调
    reward_monitor = RewardMonitorCallback(log_freq=1)  # 每10步记录一次

    # 创建PPO模型并显式设置随机种子
    model = PPO("MlpPolicy", env,  # 默认策略网络，两层隐藏层的全连接网络，每层包含64个神经元
                learning_rate=args.learning_rate,
                n_steps=args.n_steps,
                batch_size=args.batch_size,
                seed=args.model_seed,
                verbose=1)

    # 训练模型
    model.learn(total_timesteps=args.num_steps, callback=reward_monitor)  # 使用回调进行训练

    # 保存模型
    model_path = args.model_path
    if worker_idx is not None:
        # 为并行工作进程添加唯一标识符
        model_path = f"{model_path}_{worker_idx}"

    model_path = os.path.join(cwd, model_path)  # 统一一下目录

    model_dir = os.path.dirname(model_path)
    if model_dir and not os.path.exists(model_dir):
        os.makedirs(model_dir)
    model.save(model_path)  # 根据实际情况，好像不必额外检查目录是否存在，会自动创建？
    print(f"模型已保存至 {model_path}")

    # 评估模型性能
    # obs = env.reset(load_profile_idx=load_profile_idx)
    obs, info = env.reset(seed=args.seed, options={'load_profile_idx': load_profile_idx})  # 显式传递种子

    # 创建保存图像的目录
    if use_plot and not os.path.exists(os.path.join(cwd, args.plot_path)):
        os.makedirs(os.path.join(cwd, args.plot_path))

    episode_reward = 0.0
    for i in range(env.horizon):
        action, _ = model.predict(obs, deterministic=True)
        # obs, reward, done, info = env.step(action)
        # 上方改成下方两行，以适配API要求
        obs, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        episode_reward += reward
        print(worker_idx, i, reward)

        if print_step:
            print('\nStep:{}\n'.format(i))
            print('Action:', action)
            print('Next Obs: {} R: {} Done: {} Info: {}'.format(obs, reward, done, info))

        if use_plot:
            # node_bound参数用于决定为具有多相的节点绘制最大或最小节点电压
            fig, _ = env.plot_graph()
            fig.tight_layout(pad=0.1)
            fig.savefig(os.path.join(cwd, args.plot_path, 'node_voltage_' + str(i).zfill(4) + '.png'))
            plt.close()

    print(f'load_profile: {load_profile_idx}, episode_reward: {episode_reward}')

    # 根据保存的png图像生成GIF
    if use_plot:
        fig, _ = env.plot_graph(show_voltages=False)
        fig.tight_layout(pad=0.1)
        fig.savefig(os.path.join(cwd, args.plot_path, 'system_layout.pdf'))

        # 改进GIF动画生成
        images = []
        filenames = sorted(glob.glob(os.path.join(cwd, args.plot_path, "node_voltage_*.png")))
        for filename in filenames:
            images.append(imageio.imread(filename))

        if images:  # 确保有图像才生成GIF
            # 使用更好的参数设置来确保动画效果
            imageio.mimsave(
                os.path.join(cwd, args.plot_path, 'node_voltage.gif'),
                images,
                fps=2,  # 提高帧率使动画更流畅
                loop=0,  # 0表示无限循环
                duration=500  # 每帧显示500毫秒
            )
            print(f"已生成GIF动画，包含{len(images)}帧")


def run_parallel_ppo_agent(args):
    """
    并行运行多个PPO智能体
    """
    workers = []
    for i in range(0, args.num_workers):
        p = mp.Process(target=run_ppo_agent, args=(args, i, i))
        p.start()
        workers.append(p)
    for p in workers:
        p.join()

    remove_parallel_dss(args.env_name, args.num_workers)


def ppo_evaluate(model, env, profiles, episodes=None):
    """
    使用PPO模型评估性能

    Args:
        model: PPO模型
        env: 环境
        profiles: 负载配置列表
        episodes: 评估的回合数量

    Returns:
        评估回合的平均回报和标准差
    """
    returns = np.zeros(len(profiles)) if episodes is None else np.zeros(min(episodes, len(profiles)))
    for i in range(len(returns)):
        pidx = profiles[i] if episodes is None else random.choice(profiles)
        obs = env.reset(seed=args.seed, load_profile_idx=pidx)  # 显式传递种子
        episode_reward = 0
        episode_steps = 0
        done = False
        while not done:
            action, _ = model.predict(obs, deterministic=True)
            next_obs, reward, done, _ = env.step(action)
            episode_reward += reward
            episode_steps += 1
            mask = 1 if episode_steps == env.horizon else float(not done)
            obs = next_obs
        returns[i] = episode_reward
    return returns.mean(), returns.std()


def run_episodic_ppo_agent(args, worker_idx=None):
    """运行基于回合的PPO智能体，包含训练-测试分割

    Args:
        args: 命令行参数
        worker_idx: 工作进程ID
    """
    test_profiles = None
    fout = None
    # 输出文件
    if args.do_testing:
        fout = open("result/{}_ppo_{}.csv".format(args.env_name, args.seed), 'w')

    # 获取环境
    env = make_env(args.env_name, worker_idx=worker_idx)
    env.seed(args.seed + 0 if worker_idx is None else worker_idx)

    # 获取观察和动作空间
    obs_dim = env.observation_space.shape[0]
    CRB_num = (env.cap_num, env.reg_num, env.bat_num)
    CRB_dim = (2, env.reg_act_num, env.bat_act_num)
    print('NumCap, NumReg, NumBat: {}'.format(CRB_num))
    print('ObsDim, ActDim: {}, {}'.format(obs_dim, sum(CRB_num)))
    print('-' * 80)

    # 训练-测试分割
    if args.do_testing:
        train_profiles = random.sample(range(env.num_profiles), k=env.num_profiles // 2)
        test_profiles = [i for i in range(env.num_profiles) if i not in train_profiles]
    else:
        train_profiles = list(range(env.num_profiles))

    # 创建PPO模型并显式设置随机种子
    model = PPO("MlpPolicy", env,
                learning_rate=args.learning_rate,
                n_steps=args.n_steps,
                batch_size=args.batch_size,
                seed=args.model_seed,
                verbose=1)

    # 训练循环
    total_num_steps = 0

    for i_episode in itertools.count(start=1):
        # 每个回合训练模型一定步数
        model.learn(total_timesteps=env.horizon)
        total_num_steps += env.horizon

        # 评估当前回合的性能
        load_profile_idx = random.choice(train_profiles)
        obs = env.reset(seed=args.seed, load_profile_idx=load_profile_idx)  # 显式传递种子
        episode_reward = 0
        episode_steps = 0
        done = False

        while not done:
            action, _ = model.predict(obs, deterministic=True)
            next_obs, reward, done, info = env.step(action)
            episode_steps += 1
            episode_reward += reward
            obs = next_obs

        print(f"episode: {i_episode}, profile: {load_profile_idx},"
              f" total num steps: {total_num_steps}, episode steps: {episode_steps},"
              f" reward: {episode_reward:.2f}")

        if total_num_steps >= args.num_steps:
            # 保存最终模型
            model.save(args.model_path)
            print(f"模型已保存至 {args.model_path}")
            break

        # 定期在测试集上评估
        if args.do_testing and i_episode % 5 == 0:
            avg_reward, std = ppo_evaluate(model, env, test_profiles)
            fout.write('{},{},{}\n'.format(total_num_steps, avg_reward, std))
            fout.flush()
            print("----------------------------------------")
            print("Avg., Std. Reward: {}, {}".format(round(avg_reward, 2), round(std, 2)))
            print("----------------------------------------")


def run_dss_agent(args):
    """

    """
    # 获取环境
    env = make_env(args.env_name, dss_act=True)
    env.seed(args.seed)

    profiles = list(range(env.num_profiles))

    # 训练循环
    total_num_steps = 0  # 追踪所有回合的累计步数

    for i_episode in itertools.count(start=1):
        episode_reward = 0
        episode_steps = 0
        done = False
        load_profile_idx = random.choice(profiles)
        obs = env.reset(seed=args.seed,load_profile_idx=load_profile_idx)

        while not done:
            next_obs, reward, done, info = env.dss_step()
            episode_steps += 1
            total_num_steps += 1
            episode_reward += reward
            obs = next_obs

        print(f"episode: {i_episode}, profile: {load_profile_idx}, total num steps: {total_num_steps}, "
              f"episode steps: {episode_steps}, reward: {episode_reward:.2f}")
        if total_num_steps >= args.num_steps:
            break


# %% EV数据从文件中读取
pass


if __name__ == '__main__':
    args = parse_arguments()
    seeding(args.seed)
    if args.mode.lower() == 'ppo':
        run_ppo_agent(args, worker_idx=None, use_plot=args.use_plot, print_step=False)
    elif args.mode.lower() == 'parallel_ppo':
        run_parallel_ppo_agent(args)
    elif args.mode.lower() == 'episodic_ppo':
        run_episodic_ppo_agent(args)
    elif args.mode.lower() == 'dss':
        run_dss_agent(args)
    else:
        raise NotImplementedError("运行模式未实现")
