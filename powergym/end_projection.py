# -*- coding = utf-8 -*-
# @Time : 2025/5/9 15:07
# @Author : Gan Mocai
# @FIle : end_projection.py
# @Software : PyCharm

"""
为适应不对称空间出现的连续动作空间收缩（导致储能不放电影响），添加动作后处理映射。
对于离散动作空间不做处理。
"""

import gymnasium as gym
import numpy as np


class CustomActionWrapper(gym.ActionWrapper):
    def __init__(self, env, sto_num):
        super().__init__(env)
        self.sto_num = sto_num
        self.bat_num = env.action_space.shape[0]

        # 判断是连续动作空间还是离散动作空间
        self.is_discrete = isinstance(env.action_space, gym.spaces.Discrete)

        if not self.is_discrete:
            # 修改动作空间为统一的[0,1]区间
            self.action_space = gym.spaces.Box(
                low=0.0, high=1.0,
                shape=(self.bat_num,),
                dtype=np.float32
            )

    def action(self, action):
        """将[0,1]范围的动作映射到原始的不均匀范围"""
        mapped_action = np.zeros_like(action)

        if not self.is_discrete:
            # 前sto_num个动作映射到[-1,1]
            mapped_action[:self.sto_num] = 2.0 * action[:self.sto_num] - 1.0
            # 剩余动作映射到[-1,0]
            mapped_action[self.sto_num:] = action[self.sto_num:] * (-1.0)
            return mapped_action
        else:
            return action
