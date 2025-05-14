

## 测试信息

### 原始控制台输出


```text
环境初始化中，充电站母线为 680.
There are 17 edges and 15 unique edges. Overlapping transformer edges
BatteryStationManager已重置

电压边界维度: 41
电容边界维度: 2
Regulator边界维度: 3
电池边界维度: 22
EV station metrics dimension: 5
Load 边界维度: 16
观察空间维度设置为: 89
Wrapping the env with a `Monitor` wrapper
Wrapping the env in a DummyVecEnv.
已从D:\LENOVO\Documents\Python\ML\powergym\results_20250513_224309_13Bus_1000000\model\ppo_model加载模型
BatteryStationManager已重置
智能体的动作为: [25  0  1  0  2  1  1  1  0  1  0]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -56.25, -18.488480916311055
奖励各项的值：powerloss=-0.1169978157314658, voltage=-0.1774549801676062, ctrl=-0.0, connection=0.0, completion=0.0, energy=0.0, transformer=0.
已连接电池 batt_ev_030, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 90kWh，并创BMS。
已连接电池 batt_ev_149, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 69kWh，并创BMS。
已连接电池 batt_ev_126, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 68kWh，并创BMS。
已连接电池 batt_ev_064, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_123, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
已连接电池 batt_ev_239, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 92kWh，并创BMS。
已连接电池 batt_ev_039, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 52kWh，并创BMS。
已连接电池 batt_ev_242, 初始SOC: 38.0%, 最大功率: 120kW, 电池容量: 93kWh，并创BMS。
已连接电池 batt_ev_042, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
已连接电池 batt_ev_045, 初始SOC: 12.0%, 最大功率: 120kW, 电池容量: 72kWh，并创BMS。
智能体的动作为: [25  0  1  0  2  1  1  1  0  1  0]
初次设置charger_power=58.18181818181818。
功率需求: 120.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=50.90909090909091。
功率需求: 60.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 120.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -56.25, -18.488480916311055
已在 set_all_batteries_before_solve 中设置 batt_ev_030 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.18 更新为 0.34。
SOC从 0.32 更新为 0.52。
SOC从 0.18 更新为 0.39。
SOC从 0.12 更新为 0.33。
SOC从 0.22 更新为 0.49。
SOC从 0.28 更新为 0.43。
SOC从 0.12 更新为 0.38。
SOC从 0.38 更新为 0.54。
SOC从 0.22 更新为 0.52。
SOC从 0.12 更新为 0.32。
奖励各项的值：powerloss=-0.14609522335414532, voltage=-0.238679976549252, ctrl=-0.0, connection=0.0, completion=0.0, energy=0.0, transformer=0.
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=58.18181818181818，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 72.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=47.27272727272727失败。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -43.75, -14.379929601575267
已在 set_all_batteries_before_solve 中设置 batt_ev_030 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.34 更新为 0.50。
SOC从 0.52 更新为 0.69。
SOC从 0.39 更新为 0.57。
SOC从 0.33 更新为 0.52。
SOC从 0.49 更新为 0.72。
SOC从 0.43 更新为 0.58。
SOC从 0.38 更新为 0.64。
SOC从 0.54 更新为 0.69。
SOC从 0.52 更新为 0.72。
SOC从 0.32 更新为 0.52。
已断开电池: batt_ev_030
时间步 3 执行前: 电池 batt_ev_030 已充满 (SOC: 50.3%)，离开
已断开电池: batt_ev_064
时间步 3 执行前: 电池 batt_ev_064 已充满 (SOC: 51.9%)，离开
已断开电池: batt_ev_039
时间步 3: 电池 batt_ev_039 已离开，当前SOC: 64.5%，能量满足率: 61.0%
已断开电池: batt_ev_045
时间步 3: 电池 batt_ev_045 已离开，当前SOC: 52.4%，能量满足率: 47.0%
奖励各项的值：powerloss=-0.14046184236672166, voltage=-0.2878761753567183, ctrl=-0.0, connection=0.32, completion=5.0, energy=7.699947823494337, transformer=0.
已连接电池 batt_ev_224, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_224 已接入
时间步 3: 电池 batt_ev_092 已错过离开时间，无法接入
已连接电池 batt_ev_081, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 50kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_081 已接入
已连接电池 batt_ev_076, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_076 已接入
已连接电池 batt_ev_235, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_235 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=50.90909090909091。
功率需求: 80.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=54.54545454545455失败。
功率需求: 72.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=47.27272727272727失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=47.27272727272727。
功率需求: 36.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_235 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.28 更新为 0.58。
SOC从 0.69 更新为 0.87。
SOC从 0.57 更新为 0.70。
SOC从 0.12 更新为 0.37。
SOC从 0.72 更新为 0.84。
SOC从 0.58 更新为 0.72。
SOC从 0.28 更新为 0.51。
SOC从 0.69 更新为 0.85。
SOC从 0.72 更新为 0.86。
SOC从 0.62 更新为 0.81。
已断开电池: batt_ev_126
时间步 4: 电池 batt_ev_126 已离开，当前SOC: 70.3%，能量满足率: 65.3%
已断开电池: batt_ev_239
时间步 4 执行前: 电池 batt_ev_239 已充满 (SOC: 72.5%)，离开
已断开电池: batt_ev_242
时间步 4 执行前: 电池 batt_ev_242 已充满 (SOC: 84.9%)，离开
奖励各项的值：powerloss=-0.13715009778586068, voltage=-0.3007088465287522, ctrl=-0.0, connection=0.56, completion=5.7142857142857135, energy=8.19067396636651, transformer=0.
时间步 4: 电池 batt_ev_104 已错过离开时间，无法接入
已连接电池 batt_ev_018, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_018 已接入
已连接电池 batt_ev_062, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_062 已接入
时间步 4: 电池 batt_ev_200 已错过离开时间，无法接入
时间步 4: 电池 batt_ev_163 已错过离开时间，无法接入
已连接电池 batt_ev_014, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_014 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=25.454545454545453失败。
功率需求: 20.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 64.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=29.09090909090909失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=21.818181818181817失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=32.72727272727273失败。
功率需求: 24.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_235 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_062 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_014 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.58 更新为 0.78。
SOC从 0.87 更新为 0.94。
SOC从 0.32 更新为 0.52。
SOC从 0.37 更新为 0.63。
SOC从 0.84 更新为 0.96。
SOC从 0.57 更新为 0.75。
SOC从 0.51 更新为 0.66。
SOC从 0.28 更新为 0.46。
SOC从 0.86 更新为 0.94。
SOC从 0.81 更新为 0.94。
已断开电池: batt_ev_123
时间步 5: 电池 batt_ev_123 已离开，当前SOC: 95.8%，能量满足率: 97.1%
已断开电池: batt_ev_042
时间步 5: 电池 batt_ev_042 已离开，当前SOC: 94.0%，能量满足率: 94.7%
已断开电池: batt_ev_076
时间步 5: 电池 batt_ev_076 已离开，当前SOC: 65.7%，能量满足率: 53.9%
已断开电池: batt_ev_235
时间步 5 执行前: 电池 batt_ev_235 已充满 (SOC: 93.9%)，离开
已断开电池: batt_ev_062
时间步 5: 电池 batt_ev_062 已离开，当前SOC: 74.7%，能量满足率: 43.2%
奖励各项的值：powerloss=-0.13380953472482596, voltage=-0.31399193620843535, ctrl=-0.0, connection=0.96, completion=4.166666666666667, energy=8.018962832659216, transformer=0.
已连接电池 batt_ev_180, 初始SOC: 8.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
时间步 5 执行前: 排队电池 batt_ev_180 已接入
已连接电池 batt_ev_036, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
时间步 5 执行前: 排队电池 batt_ev_036 已接入
已连接电池 batt_ev_231, 初始SOC: 8.0%, 最大功率: 80kW, 电池容量: 62kWh，并创BMS。
时间步 5 执行前: 排队电池 batt_ev_231 已接入
已连接电池 batt_ev_067, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 5 执行前: 排队电池 batt_ev_067 已接入
已连接电池 batt_ev_248, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
时间步 5 执行前: 排队电池 batt_ev_248 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=36.36363636363636失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=10.909090909090908失败。
功率需求: 20.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 64.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=47.27272727272727。
功率需求: 60.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_014 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_231 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_248 充电的有无功功率为 47.27272727272727, -9.599136684516559
SOC从 0.78 更新为 0.92。
SOC从 0.94 更新为 1.00。
SOC从 0.52 更新为 0.66。
SOC从 0.63 更新为 0.87。
SOC从 0.08 更新为 0.35。
SOC从 0.57 更新为 0.75。
SOC从 0.08 更新为 0.30。
SOC从 0.46 更新为 0.65。
SOC从 0.32 更新为 0.52。
SOC从 0.22 更新为 0.41。
已断开电池: batt_ev_149
时间步 6 执行前: 电池 batt_ev_149 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_014
时间步 6: 电池 batt_ev_014 已离开，当前SOC: 64.8%，能量满足率: 61.4%
已断开电池: batt_ev_231
时间步 6: 电池 batt_ev_231 已离开，当前SOC: 30.0%，能量满足率: 24.4%
已断开电池: batt_ev_248
时间步 6: 电池 batt_ev_248 已离开，当前SOC: 41.4%，能量满足率: 25.5%
奖励各项的值：powerloss=-0.14645592928262502, voltage=-0.3435887717754471, ctrl=-0.0, connection=1.28, completion=3.75, energy=7.335053167308615, transformer=0.
已连接电池 batt_ev_240, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_240 已接入
时间步 6: 电池 batt_ev_119 已错过离开时间，无法接入
已连接电池 batt_ev_158, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_158 已接入
已连接电池 batt_ev_157, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_157 已接入
已连接电池 batt_ev_096, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_096 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=14.545454545454545失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=18.18181818181818失败。
功率需求: 20.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=36.36363636363636失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=47.27272727272727。
功率需求: 60.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_157 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 47.27272727272727, -9.599136684516559
SOC从 0.92 更新为 1.00。
SOC从 0.48 更新为 0.67。
SOC从 0.66 更新为 0.81。
SOC从 0.87 更新为 0.97。
SOC从 0.35 更新为 0.58。
SOC从 0.75 更新为 0.90。
SOC从 0.28 更新为 0.57。
SOC从 0.12 更新为 0.38。
SOC从 0.52 更新为 0.67。
SOC从 0.18 更新为 0.41。
已断开电池: batt_ev_224
时间步 7 执行前: 电池 batt_ev_224 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_018
时间步 7: 电池 batt_ev_018 已离开，当前SOC: 81.2%，能量满足率: 74.5%
已断开电池: batt_ev_036
时间步 7: 电池 batt_ev_036 已离开，当前SOC: 90.3%，能量满足率: 81.2%
已断开电池: batt_ev_157
时间步 7: 电池 batt_ev_157 已离开，当前SOC: 38.5%，能量满足率: 30.8%
奖励各项的值：powerloss=-0.15979648282723372, voltage=-0.3813499871808279, ctrl=-0.0, connection=1.6, completion=3.5, energy=7.300507995261238, transformer=0.
时间步 7: 电池 batt_ev_187 已错过离开时间，无法接入
已连接电池 batt_ev_106, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 92kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_106 已接入
已连接电池 batt_ev_055, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_055 已接入
已连接电池 batt_ev_216, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_216 已接入
已连接电池 batt_ev_247, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 87kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_247 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=43.63636363636363失败。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 100.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=3.6363636363636362失败。
功率需求: 20.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 120.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 48.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_106 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_216 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.32 更新为 0.47。
SOC从 0.67 更新为 0.87。
SOC从 0.28 更新为 0.43。
SOC从 0.97 更新为 1.00。
SOC从 0.58 更新为 0.76。
SOC从 0.42 更新为 0.65。
SOC从 0.57 更新为 0.76。
SOC从 0.18 更新为 0.35。
SOC从 0.67 更新为 0.82。
SOC从 0.41 更新为 0.63。
已断开电池: batt_ev_081
时间步 8 执行前: 电池 batt_ev_081 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_180
时间步 8: 电池 batt_ev_180 已离开，当前SOC: 75.9%，能量满足率: 75.5%
已断开电池: batt_ev_067
时间步 8: 电池 batt_ev_067 已离开，当前SOC: 82.0%，能量满足率: 75.8%
已断开电池: batt_ev_240
时间步 8: 电池 batt_ev_240 已离开，当前SOC: 87.0%，能量满足率: 77.9%
已断开电池: batt_ev_158
时间步 8 执行前: 电池 batt_ev_158 已充满 (SOC: 76.2%)，离开
已断开电池: batt_ev_106
时间步 8: 电池 batt_ev_106 已离开，当前SOC: 46.8%，能量满足率: 22.5%
已断开电池: batt_ev_216
时间步 8: 电池 batt_ev_216 已离开，当前SOC: 64.6%，能量满足率: 40.4%
奖励各项的值：powerloss=-0.17639162999718797, voltage=-0.38218113203345894, ctrl=-0.0, connection=2.16, completion=3.333333333333333, energy=7.230242505559409, transformer=0.
时间步 8: 电池 batt_ev_244 已错过离开时间，无法接入
已连接电池 batt_ev_090, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
时间步 8 执行前: 排队电池 batt_ev_090 已接入
已连接电池 batt_ev_128, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 80kWh，并创BMS。
时间步 8 执行前: 排队电池 batt_ev_128 已接入
已连接电池 batt_ev_220, 初始SOC: 72.0%, 最大功率: 120kW, 电池容量: 85kWh，并创BMS。
时间步 8 执行前: 排队电池 batt_ev_220 已接入
已连接电池 batt_ev_016, 初始SOC: 22.0%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
时间步 8 执行前: 排队电池 batt_ev_016 已接入
已连接电池 batt_ev_173, 初始SOC: 56.99999999999999%, 最大功率: 100kW, 电池容量: 65kWh，并创BMS。
时间步 8 执行前: 排队电池 batt_ev_173 已接入
已连接电池 batt_ev_132, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
时间步 8 执行前: 排队电池 batt_ev_132 已接入
已连接电池 batt_ev_150, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 78kWh，并创BMS。
时间步 8 执行前: 排队电池 batt_ev_150 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=43.63636363636363。
功率需求: 48.00 kW, 充电桩功率: 43.64 kW, 最终充电功率: 43.64 kW。
初次设置charger_power=54.54545454545455。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 36.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_128 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 43.63636363636363, -8.86074155493836
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_173 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_132 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.48 更新为 0.62。
SOC从 0.42 更新为 0.59。
SOC从 0.43 更新为 0.59。
SOC从 0.72 更新为 0.85。
SOC从 0.22 更新为 0.36。
SOC从 0.57 更新为 0.78。
SOC从 0.18 更新为 0.44。
SOC从 0.35 更新为 0.51。
SOC从 0.08 更新为 0.25。
SOC从 0.63 更新为 0.81。
已断开电池: batt_ev_055
时间步 9: 电池 batt_ev_055 已离开，当前SOC: 58.6%，能量满足率: 43.8%
已断开电池: batt_ev_247
时间步 9: 电池 batt_ev_247 已离开，当前SOC: 51.4%，能量满足率: 41.8%
已断开电池: batt_ev_090
时间步 9: 电池 batt_ev_090 已离开，当前SOC: 61.6%，能量满足率: 27.3%
已断开电池: batt_ev_128
时间步 9: 电池 batt_ev_128 已离开，当前SOC: 59.1%，能量满足率: 30.4%
已断开电池: batt_ev_173
时间步 9: 电池 batt_ev_173 已离开，当前SOC: 78.0%，能量满足率: 51.2%
已断开电池: batt_ev_132
时间步 9: 电池 batt_ev_132 已离开，当前SOC: 43.7%，能量满足率: 32.2%
奖励各项的值：powerloss=-0.1986712168562219, voltage=-0.4728363272483893, ctrl=-0.0, connection=2.64, completion=2.727272727272727, energy=6.602464995333378, transformer=0.
时间步 9: 电池 batt_ev_002 已错过离开时间，无法接入
已连接电池 batt_ev_191, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 87kWh，并创BMS。
时间步 9 执行前: 排队电池 batt_ev_191 已接入
已连接电池 batt_ev_193, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 67kWh，并创BMS。
时间步 9 执行前: 排队电池 batt_ev_193 已接入
时间步 9: 电池 batt_ev_024 已错过离开时间，无法接入
已连接电池 batt_ev_161, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 72kWh，并创BMS。
时间步 9 执行前: 排队电池 batt_ev_161 已接入
已连接电池 batt_ev_186, 初始SOC: 82.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
时间步 9 执行前: 排队电池 batt_ev_186 已接入
已连接电池 batt_ev_194, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 86kWh，并创BMS。
时间步 9 执行前: 排队电池 batt_ev_194 已接入
已连接电池 batt_ev_078, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 85kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=43.63636363636363，设置charger_power=21.818181818181817失败。
功率需求: 48.00 kW, 充电桩功率: 43.64 kW, 最终充电功率: 43.64 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=21.818181818181817。
功率需求: 48.00 kW, 充电桩功率: 21.82 kW, 最终充电功率: 21.82 kW。
初次设置charger_power=54.54545454545455。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=36.36363636363636失败。
功率需求: 24.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 43.63636363636363, -8.86074155493836
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_191 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_161 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 21.818181818181817, -4.43037077746918
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.18 更新为 0.34。
SOC从 0.22 更新为 0.42。
SOC从 0.22 更新为 0.42。
SOC从 0.85 更新为 0.98。
SOC从 0.36 更新为 0.51。
SOC从 0.82 更新为 0.90。
SOC从 0.28 更新为 0.44。
SOC从 0.38 更新为 0.55。
SOC从 0.25 更新为 0.43。
SOC从 0.81 更新为 0.92。
已断开电池: batt_ev_096
时间步 10 执行前: 电池 batt_ev_096 已充满 (SOC: 92.3%)，离开
已断开电池: batt_ev_220
时间步 10 执行前: 电池 batt_ev_220 已充满 (SOC: 97.7%)，离开
已断开电池: batt_ev_150
时间步 10: 电池 batt_ev_150 已离开，当前SOC: 43.0%，能量满足率: 38.9%
已断开电池: batt_ev_191
时间步 10: 电池 batt_ev_191 已离开，当前SOC: 33.7%，能量满足率: 19.6%
已断开电池: batt_ev_161
时间步 10: 电池 batt_ev_161 已离开，当前SOC: 42.2%，能量满足率: 26.6%
奖励各项的值：powerloss=-0.20872074198052257, voltage=-0.4539547095755547, ctrl=-0.0, connection=3.04, completion=2.8947368421052633, energy=6.483797857622998, transformer=0.
已连接电池 batt_ev_000, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 80kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_000 已接入
已连接电池 batt_ev_008, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 60kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_008 已接入
已连接电池 batt_ev_162, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_162 已接入
已连接电池 batt_ev_170, 初始SOC: 42.0%, 最大功率: 120kW, 电池容量: 99kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_170 已接入
已连接电池 batt_ev_085, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_085 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=50.90909090909091。
功率需求: 60.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=21.818181818181817，设置charger_power=10.909090909090908失败。
功率需求: 30.00 kW, 充电桩功率: 21.82 kW, 最终充电功率: 21.82 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=47.27272727272727。
功率需求: 36.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 21.818181818181817, -4.43037077746918
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_008 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_085 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.18 更新为 0.35。
SOC从 0.42 更新为 0.63。
SOC从 0.68 更新为 0.88。
SOC从 0.28 更新为 0.48。
SOC从 0.51 更新为 0.65。
SOC从 0.90 更新为 0.98。
SOC从 0.44 更新为 0.60。
SOC从 0.55 更新为 0.72。
SOC从 0.42 更新为 0.56。
SOC从 0.62 更新为 0.84。
已断开电池: batt_ev_016
时间步 11: 电池 batt_ev_016 已离开，当前SOC: 65.1%，能量满足率: 56.7%
已断开电池: batt_ev_193
时间步 11: 电池 batt_ev_193 已离开，当前SOC: 62.7%，能量满足率: 53.6%
已断开电池: batt_ev_186
时间步 11: 电池 batt_ev_186 已离开，当前SOC: 97.6%，能量满足率: 86.5%
已断开电池: batt_ev_008
时间步 11 执行前: 电池 batt_ev_008 已充满 (SOC: 88.0%)，离开
已断开电池: batt_ev_085
时间步 11 执行前: 电池 batt_ev_085 已充满 (SOC: 84.0%)，离开
奖励各项的值：powerloss=-0.22012131224105314, voltage=-0.4908397260824504, ctrl=-0.0, connection=3.44, completion=3.0232558139534884, energy=6.652561062265997, transformer=0.
时间步 11: 电池 batt_ev_222 已错过离开时间，无法接入
已连接电池 batt_ev_114, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_114 已接入
已连接电池 batt_ev_009, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_009 已接入
已连接电池 batt_ev_113, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_065, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_203, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=14.545454545454545。
功率需求: 15.00 kW, 充电桩功率: 14.55 kW, 最终充电功率: 14.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 120.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 120.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=54.54545454545455失败。
功率需求: 40.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=47.27272727272727。
功率需求: 60.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 14.545454545454543, -2.953580518312787
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 47.27272727272727, -9.599136684516559
SOC从 0.35 更新为 0.52。
SOC从 0.92 更新为 0.99。
SOC从 0.18 更新为 0.32。
SOC从 0.48 更新为 0.66。
SOC从 0.28 更新为 0.46。
SOC从 0.62 更新为 0.79。
SOC从 0.60 更新为 0.76。
SOC从 0.72 更新为 0.84。
SOC从 0.56 更新为 0.70。
SOC从 0.28 更新为 0.55。
已断开电池: batt_ev_194
时间步 12: 电池 batt_ev_194 已离开，当前SOC: 75.6%，能量满足率: 68.0%
已断开电池: batt_ev_170
时间步 12: 电池 batt_ev_170 已离开，当前SOC: 69.6%，能量满足率: 49.2%
奖励各项的值：powerloss=-0.22204294104810132, voltage=-0.5083579083573464, ctrl=-0.0, connection=3.6, completion=2.8888888888888884, energy=6.617291173128085, transformer=0.
已连接电池 batt_ev_011, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 12 执行前: 排队电池 batt_ev_011 已接入
已连接电池 batt_ev_041, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=14.545454545454545，设置charger_power=-0.0失败。
功率需求: 15.00 kW, 充电桩功率: 14.55 kW, 最终充电功率: 14.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 36.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=43.63636363636363失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=29.09090909090909失败。
功率需求: 40.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 36.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 14.545454545454543, -2.953580518312787
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_011 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.52 更新为 0.67。
SOC从 0.99 更新为 1.00。
SOC从 0.32 更新为 0.46。
SOC从 0.66 更新为 0.80。
SOC从 0.46 更新为 0.63。
SOC从 0.79 更新为 0.90。
SOC从 0.32 更新为 0.51。
SOC从 0.84 更新为 0.96。
SOC从 0.12 更新为 0.37。
SOC从 0.55 更新为 0.75。
已断开电池: batt_ev_078
时间步 13: 电池 batt_ev_078 已离开，当前SOC: 95.7%，能量满足率: 96.2%
已断开电池: batt_ev_000
时间步 13: 电池 batt_ev_000 已离开，当前SOC: 67.1%，能量满足率: 61.4%
已断开电池: batt_ev_162
时间步 13: 电池 batt_ev_162 已离开，当前SOC: 79.9%，能量满足率: 74.1%
已断开电池: batt_ev_114
时间步 13 执行前: 电池 batt_ev_114 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_011
时间步 13: 电池 batt_ev_011 已离开，当前SOC: 51.5%，能量满足率: 29.5%
奖励各项的值：powerloss=-0.22479766944661994, voltage=-0.5474928272665358, ctrl=-0.0, connection=4.0, completion=2.8000000000000003, energy=6.678093999361927, transformer=0.
已连接电池 batt_ev_232, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_232 已接入
已连接电池 batt_ev_237, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_237 已接入
已连接电池 batt_ev_052, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_052 已接入
已连接电池 batt_ev_206, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 62kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_206 已接入
已连接电池 batt_ev_172, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=50.90909090909091。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=18.18181818181818失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=40.0失败。
功率需求: 24.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_052 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_206 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.38 更新为 0.56。
SOC从 0.78 更新为 0.87。
SOC从 0.46 更新为 0.60。
SOC从 0.38 更新为 0.58。
SOC从 0.63 更新为 0.81。
SOC从 0.90 更新为 0.97。
SOC从 0.22 更新为 0.44。
SOC从 0.38 更新为 0.68。
SOC从 0.37 更新为 0.63。
SOC从 0.75 更新为 0.89。
已断开电池: batt_ev_065
时间步 14: 电池 batt_ev_065 已离开，当前SOC: 96.7%，能量满足率: 96.5%
已断开电池: batt_ev_203
时间步 14: 电池 batt_ev_203 已离开，当前SOC: 89.0%，能量满足率: 87.1%
已断开电池: batt_ev_206
时间步 14: 电池 batt_ev_206 已离开，当前SOC: 44.0%，能量满足率: 36.7%
奖励各项的值：powerloss=-0.22291234824598535, voltage=-0.5435401952415897, ctrl=-0.0, connection=4.24, completion=2.641509433962264, energy=6.715551331527364, transformer=0.
已连接电池 batt_ev_229, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_229 已接入
已连接电池 batt_ev_164, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_164 已接入
已连接电池 batt_ev_134, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=32.72727272727273失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 72.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 36.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=25.454545454545453失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=47.27272727272727失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=47.27272727272727。
功率需求: 64.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_052 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 47.27272727272727, -9.599136684516559
SOC从 0.56 更新为 0.70。
SOC从 0.87 更新为 0.92。
SOC从 0.60 更新为 0.75。
SOC从 0.58 更新为 0.73。
SOC从 0.81 更新为 0.97。
SOC从 0.38 更新为 0.58。
SOC从 0.42 更新为 0.63。
SOC从 0.68 更新为 0.91。
SOC从 0.63 更新为 0.85。
SOC从 0.32 更新为 0.54。
已断开电池: batt_ev_009
时间步 15: 电池 batt_ev_009 已离开，当前SOC: 74.5%，能量满足率: 70.6%
已断开电池: batt_ev_113
时间步 15 执行前: 电池 batt_ev_113 已充满 (SOC: 96.7%)，离开
已断开电池: batt_ev_232
时间步 15: 电池 batt_ev_232 已离开，当前SOC: 70.3%，能量满足率: 53.8%
已断开电池: batt_ev_052
时间步 15 执行前: 电池 batt_ev_052 已充满 (SOC: 73.0%)，离开
奖励各项的值：powerloss=-0.221396873087112, voltage=-0.5372326591544518, ctrl=-0.0, connection=4.5600000000000005, completion=2.807017543859649, energy=6.813542855292669, transformer=0.
已连接电池 batt_ev_214, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 80kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_214 已接入
已连接电池 batt_ev_143, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_143 已接入
已连接电池 batt_ev_245, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_245 已接入
已连接电池 batt_ev_098, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_098 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=18.18181818181818失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 64.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=50.90909090909091。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=14.545454545454545失败。
功率需求: 15.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=21.818181818181817失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 48.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.48 更新为 0.65。
SOC从 0.92 更新为 0.98。
SOC从 0.48 更新为 0.73。
SOC从 0.38 更新为 0.56。
SOC从 0.42 更新为 0.61。
SOC从 0.58 更新为 0.73。
SOC从 0.63 更新为 0.79。
SOC从 0.91 更新为 1.00。
SOC从 0.85 更新为 1.00。
SOC从 0.54 更新为 0.76。
已断开电池: batt_ev_041
时间步 16 执行前: 电池 batt_ev_041 已充满 (SOC: 99.6%)，离开
已断开电池: batt_ev_237
时间步 16: 电池 batt_ev_237 已离开，当前SOC: 97.6%，能量满足率: 97.8%
已断开电池: batt_ev_172
时间步 16 执行前: 电池 batt_ev_172 已充满 (SOC: 99.9%)，离开
奖励各项的值：powerloss=-0.21909463389726355, voltage=-0.5308811247614398, ctrl=-0.0, connection=4.8, completion=3.0, energy=6.969242524122238, transformer=0.
已连接电池 batt_ev_190, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 63kWh，并创BMS。
时间步 16 执行前: 排队电池 batt_ev_190 已接入
已连接电池 batt_ev_069, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 56kWh，并创BMS。
已连接电池 batt_ev_071, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=43.63636363636363失败。
功率需求: 32.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 36.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=43.63636363636363失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=36.36363636363636失败。
功率需求: 32.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.65 更新为 0.82。
SOC从 0.18 更新为 0.40。
SOC从 0.73 更新为 0.86。
SOC从 0.56 更新为 0.70。
SOC从 0.61 更新为 0.79。
SOC从 0.73 更新为 0.83。
SOC从 0.79 更新为 0.89。
SOC从 0.38 更新为 0.59。
SOC从 0.42 更新为 0.56。
SOC从 0.76 更新为 0.91。
已断开电池: batt_ev_214
时间步 17: 电池 batt_ev_214 已离开，当前SOC: 82.1%，能量满足率: 68.2%
已断开电池: batt_ev_245
时间步 17: 电池 batt_ev_245 已离开，当前SOC: 69.8%，能量满足率: 53.0%
奖励各项的值：powerloss=-0.22282645061048797, voltage=-0.5072046606129721, ctrl=-0.0, connection=4.96, completion=2.903225806451613, energy=6.939960995973625, transformer=0.
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=21.818181818181817失败。
功率需求: 20.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=40.0失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=36.36363636363636失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=21.818181818181817失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=14.545454545454545失败。
功率需求: 20.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 20.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.40 更新为 0.61。
SOC从 0.86 更新为 0.95。
SOC从 0.79 更新为 0.90。
SOC从 0.83 更新为 0.93。
SOC从 0.89 更新为 0.96。
SOC从 0.59 更新为 0.76。
SOC从 0.56 更新为 0.70。
SOC从 0.91 更新为 1.00。
已断开电池: batt_ev_229
时间步 18 执行前: 电池 batt_ev_229 已充满 (SOC: 93.0%)，离开
已断开电池: batt_ev_134
时间步 18 执行前: 电池 batt_ev_134 已充满 (SOC: 99.9%)，离开
已断开电池: batt_ev_143
时间步 18: 电池 batt_ev_143 已离开，当前SOC: 94.7%，能量满足率: 93.4%
已断开电池: batt_ev_098
时间步 18: 电池 batt_ev_098 已离开，当前SOC: 90.1%，能量满足率: 85.8%
已断开电池: batt_ev_071
时间步 18 执行前: 电池 batt_ev_071 已充满 (SOC: 70.4%)，离开
奖励各项的值：powerloss=-0.22107973091161873, voltage=-0.3415448077393801, ctrl=-0.0, connection=5.36, completion=3.1343283582089554, energy=7.13728652916826, transformer=0.
已连接电池 batt_ev_083, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_174, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_167, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=47.27272727272727。
功率需求: 48.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=50.90909090909091。
功率需求: 80.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=7.2727272727272725失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=50.90909090909091失败。
功率需求: 24.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_083 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.68 更新为 0.90。
SOC从 0.61 更新为 0.83。
SOC从 0.32 更新为 0.56。
SOC从 0.18 更新为 0.37。
SOC从 0.96 更新为 1.00。
SOC从 0.76 更新为 0.86。
已断开电池: batt_ev_164
时间步 19 执行前: 电池 batt_ev_164 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_083
时间步 19 执行前: 电池 batt_ev_083 已充满 (SOC: 89.9%)，离开
奖励各项的值：powerloss=-0.21396766778986612, voltage=-0.21418460058636457, ctrl=-0.0, connection=5.5200000000000005, completion=3.333333333333333, energy=7.220263731221354, transformer=0.
已连接电池 batt_ev_115, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
已连接电池 batt_ev_181, 初始SOC: 56.99999999999999%, 最大功率: 80kW, 电池容量: 69kWh，并创BMS。
已连接电池 batt_ev_182, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 95kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=21.818181818181817失败。
功率需求: 40.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 64.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=29.09090909090909失败。
功率需求: 15.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 120.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.83 更新为 0.99。
SOC从 0.56 更新为 0.73。
SOC从 0.37 更新为 0.57。
SOC从 0.12 更新为 0.42。
SOC从 0.57 更新为 0.74。
SOC从 0.86 更新为 0.93。
SOC从 0.28 更新为 0.42。
已断开电池: batt_ev_190
时间步 20 执行前: 电池 batt_ev_190 已充满 (SOC: 98.8%)，离开
奖励各项的值：powerloss=-0.20841280682944818, voltage=-0.15759094724185685, ctrl=-0.0, connection=5.6000000000000005, completion=3.428571428571429, energy=7.2599742493467625, transformer=0.
已连接电池 batt_ev_037, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_138, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
已连接电池 batt_ev_095, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=50.90909090909091失败。
功率需求: 24.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=50.90909090909091失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=14.545454545454545失败。
功率需求: 15.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=47.27272727272727。
功率需求: 64.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_138 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.48 更新为 0.76。
SOC从 0.73 更新为 0.85。
SOC从 0.57 更新为 0.75。
SOC从 0.42 更新为 0.68。
SOC从 0.74 更新为 0.86。
SOC从 0.12 更新为 0.40。
SOC从 0.93 更新为 1.00。
SOC从 0.42 更新为 0.57。
SOC从 0.32 更新为 0.50。
已断开电池: batt_ev_069
时间步 21 执行前: 电池 batt_ev_069 已充满 (SOC: 99.6%)，离开
已断开电池: batt_ev_138
时间步 21 执行前: 电池 batt_ev_138 已充满 (SOC: 75.9%)，离开
奖励各项的值：powerloss=-0.21075214310415075, voltage=-0.11436906102970434, ctrl=-0.0, connection=5.76, completion=3.611111111111111, energy=7.336086075753797, transformer=0.
已连接电池 batt_ev_197, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 75kWh，并创BMS。
已连接电池 batt_ev_026, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 102kWh，并创BMS。
已连接电池 batt_ev_212, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=29.09090909090909失败。
功率需求: 24.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=47.27272727272727失败。
功率需求: 32.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=25.454545454545453失败。
功率需求: 20.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 48.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_212 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.32 更新为 0.45。
SOC从 0.52 更新为 0.68。
SOC从 0.85 更新为 0.97。
SOC从 0.75 更新为 0.87。
SOC从 0.68 更新为 0.87。
SOC从 0.86 更新为 0.93。
SOC从 0.40 更新为 0.65。
SOC从 0.22 更新为 0.49。
SOC从 0.57 更新为 0.71。
SOC从 0.50 更新为 0.68。
已断开电池: batt_ev_174
时间步 22: 电池 batt_ev_174 已离开，当前SOC: 86.9%，能量满足率: 86.1%
已断开电池: batt_ev_167
时间步 22: 电池 batt_ev_167 已离开，当前SOC: 96.7%，能量满足率: 98.0%
已断开电池: batt_ev_115
时间步 22 执行前: 电池 batt_ev_115 已充满 (SOC: 87.3%)，离开
已断开电池: batt_ev_181
时间步 22 执行前: 电池 batt_ev_181 已充满 (SOC: 93.2%)，离开
已断开电池: batt_ev_182
时间步 22: 电池 batt_ev_182 已离开，当前SOC: 71.1%，能量满足率: 61.5%
奖励各项的值：powerloss=-0.20216680187194525, voltage=-0.1010001258802018, ctrl=-0.0, connection=6.16, completion=3.6363636363636367, energy=7.438511051511635, transformer=0.
已连接电池 batt_ev_010, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 71kWh，并创BMS。
时间步 22 执行前: 排队电池 batt_ev_010 已接入
已连接电池 batt_ev_241, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 68kWh，并创BMS。
已连接电池 batt_ev_084, 初始SOC: 78.0%, 最大功率: 100kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_038, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
已连接电池 batt_ev_040, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=50.90909090909091。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=29.09090909090909。
功率需求: 40.00 kW, 充电桩功率: 29.09 kW, 最终充电功率: 29.09 kW。
初次设置charger_power=54.54545454545455。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=47.27272727272727。
功率需求: 24.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 48.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_212 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_084 充电的有无功功率为 29.090909090909086, -5.907161036625574
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.45 更新为 0.59。
SOC从 0.68 更新为 0.84。
SOC从 0.48 更新为 0.68。
SOC从 0.48 更新为 0.66。
SOC从 0.78 更新为 0.90。
SOC从 0.42 更新为 0.66。
SOC从 0.65 更新为 0.84。
SOC从 0.49 更新为 0.71。
SOC从 0.78 更新为 0.89。
SOC从 0.68 更新为 0.87。
已断开电池: batt_ev_212
时间步 23: 电池 batt_ev_212 已离开，当前SOC: 71.2%，能量满足率: 64.7%
奖励各项的值：powerloss=-0.18587400957681183, voltage=-0.11551508786018072, ctrl=-0.0, connection=6.24, completion=3.58974358974359, energy=7.42608524630782, transformer=0.
已连接电池 batt_ev_046, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_046 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=32.72727272727273失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=40.0失败。
功率需求: 72.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 36.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=29.09090909090909，设置charger_power=14.545454545454545失败。
功率需求: 25.00 kW, 充电桩功率: 29.09 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=29.09090909090909失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=21.818181818181817失败。
功率需求: 15.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=21.818181818181817失败。
功率需求: 20.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 20.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_084 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_046 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.59 更新为 0.72。
SOC从 0.84 更新为 0.95。
SOC从 0.68 更新为 0.89。
SOC从 0.66 更新为 0.79。
SOC从 0.90 更新为 1.00。
SOC从 0.66 更新为 0.86。
SOC从 0.84 更新为 0.97。
SOC从 0.42 更新为 0.66。
SOC从 0.89 更新为 0.95。
SOC从 0.87 更新为 0.94。
已断开电池: batt_ev_037
时间步 24: 电池 batt_ev_037 已离开，当前SOC: 94.2%，能量满足率: 94.3%
已断开电池: batt_ev_197
时间步 24: 电池 batt_ev_197 已离开，当前SOC: 94.7%，能量满足率: 92.8%
已断开电池: batt_ev_010
时间步 24 执行前: 电池 batt_ev_010 已充满 (SOC: 89.0%)，离开
已断开电池: batt_ev_084
时间步 24 执行前: 电池 batt_ev_084 已充满 (SOC: 99.8%)，离开
已断开电池: batt_ev_038
时间步 24: 电池 batt_ev_038 已离开，当前SOC: 86.2%，能量满足率: 78.9%
奖励各项的值：powerloss=-0.1639329857811744, voltage=-0.18630535074889654, ctrl=-0.0, connection=6.640000000000001, completion=3.6144578313253013, energy=7.540184766651045, transformer=0.
已连接电池 batt_ev_050, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_050 已接入
已连接电池 batt_ev_125, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_125 已接入
已连接电池 batt_ev_137, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 84kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_137 已接入
已连接电池 batt_ev_221, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 75kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_221 已接入
已连接电池 batt_ev_109, 初始SOC: 88.0%, 最大功率: 100kW, 电池容量: 70kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_109 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 24.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 120.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=3.6363636363636362失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=7.2727272727272725失败。
功率需求: 15.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=18.18181818181818。
功率需求: 25.00 kW, 充电桩功率: 18.18 kW, 最终充电功率: 18.18 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_046 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_050 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_125 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 18.18181818181818, -3.6919756478909838
SOC从 0.72 更新为 0.84。
SOC从 0.28 更新为 0.56。
SOC从 0.28 更新为 0.50。
SOC从 0.79 更新为 0.88。
SOC从 0.52 更新为 0.66。
SOC从 0.28 更新为 0.46。
SOC从 0.97 更新为 1.00。
SOC从 0.66 更新为 0.85。
SOC从 0.95 更新为 1.00。
SOC从 0.88 更新为 0.95。
已断开电池: batt_ev_095
时间步 25 执行前: 电池 batt_ev_095 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_026
时间步 25: 电池 batt_ev_026 已离开，当前SOC: 83.9%，能量满足率: 78.6%
已断开电池: batt_ev_241
时间步 25: 电池 batt_ev_241 已离开，当前SOC: 87.7%，能量满足率: 90.2%
已断开电池: batt_ev_040
时间步 25 执行前: 电池 batt_ev_040 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_046
时间步 25: 电池 batt_ev_046 已离开，当前SOC: 84.9%，能量满足率: 76.5%
已断开电池: batt_ev_050
时间步 25: 电池 batt_ev_050 已离开，当前SOC: 56.4%，能量满足率: 47.4%
已断开电池: batt_ev_125
时间步 25: 电池 batt_ev_125 已离开，当前SOC: 49.7%，能量满足率: 33.9%
奖励各项的值：powerloss=-0.14043441663901757, voltage=-0.2412478077501623, ctrl=-0.0, connection=7.2, completion=3.555555555555556, energy=7.538919166712366, transformer=0.
已连接电池 batt_ev_034, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 68kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_034 已接入
已连接电池 batt_ev_141, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 75kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_141 已接入
已连接电池 batt_ev_101, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 68kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_101 已接入
已连接电池 batt_ev_075, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_075 已接入
已连接电池 batt_ev_093, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_093 已接入
已连接电池 batt_ev_047, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 56kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_047 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 120.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=50.90909090909091。
功率需求: 80.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=18.18181818181818，设置charger_power=7.2727272727272725失败。
功率需求: 25.00 kW, 充电桩功率: 18.18 kW, 最终充电功率: 18.18 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 18.18181818181818, -3.6919756478909838
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_141 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_075 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.22 更新为 0.42。
SOC从 0.28 更新为 0.46。
SOC从 0.22 更新为 0.43。
SOC从 0.42 更新为 0.56。
SOC从 0.66 更新为 0.81。
SOC从 0.46 更新为 0.64。
SOC从 0.38 更新为 0.56。
SOC从 0.38 更新为 0.59。
SOC从 0.95 更新为 1.00。
已断开电池: batt_ev_109
时间步 26 执行前: 电池 batt_ev_109 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.1390259632577468, voltage=-0.2619539843371843, ctrl=-0.0, connection=7.28, completion=3.6263736263736264, energy=7.565964011034208, transformer=0.
已连接电池 batt_ev_031, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_057, 初始SOC: 8.0%, 最大功率: 80kW, 电池容量: 73kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 64.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 60.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=47.27272727272727失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=50.90909090909091失败。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=47.27272727272727。
功率需求: 80.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_141 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_075 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_031 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 47.27272727272727, -9.599136684516559
SOC从 0.42 更新为 0.62。
SOC从 0.46 更新为 0.64。
SOC从 0.43 更新为 0.65。
SOC从 0.56 更新为 0.70。
SOC从 0.81 更新为 0.90。
SOC从 0.64 更新为 0.83。
SOC从 0.56 更新为 0.74。
SOC从 0.59 更新为 0.76。
SOC从 0.42 更新为 0.67。
SOC从 0.08 更新为 0.24。
已断开电池: batt_ev_141
时间步 27: 电池 batt_ev_141 已离开，当前SOC: 64.4%，能量满足率: 52.0%
已断开电池: batt_ev_075
时间步 27 执行前: 电池 batt_ev_075 已充满 (SOC: 70.0%)，离开
已断开电池: batt_ev_031
时间步 27 执行前: 电池 batt_ev_031 已充满 (SOC: 67.3%)，离开
奖励各项的值：powerloss=-0.1398529328549379, voltage=-0.29699502441949743, ctrl=-0.0, connection=7.5200000000000005, completion=3.723404255319149, energy=7.59254165404578, transformer=0.
已连接电池 batt_ev_111, 初始SOC: 68.0%, 最大功率: 100kW, 电池容量: 83kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_111 已接入
已连接电池 batt_ev_006, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_006 已接入
已连接电池 batt_ev_225, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 94kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_225 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=50.90909090909091。
功率需求: 36.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=21.818181818181817失败。
功率需求: 20.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=21.818181818181817失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=43.63636363636363失败。
功率需求: 40.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=50.90909090909091失败。
功率需求: 24.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 80.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_006 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_225 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.62 更新为 0.80。
SOC从 0.68 更新为 0.84。
SOC从 0.65 更新为 0.82。
SOC从 0.57 更新为 0.72。
SOC从 0.90 更新为 0.96。
SOC从 0.83 更新为 0.99。
SOC从 0.74 更新为 0.87。
SOC从 0.76 更新为 0.86。
SOC从 0.52 更新为 0.67。
SOC从 0.24 更新为 0.40。
已断开电池: batt_ev_137
时间步 28: 电池 batt_ev_137 已离开，当前SOC: 96.0%，能量满足率: 95.8%
已断开电池: batt_ev_221
时间步 28 执行前: 电池 batt_ev_221 已充满 (SOC: 98.6%)，离开
已断开电池: batt_ev_047
时间步 28: 电池 batt_ev_047 已离开，当前SOC: 86.2%，能量满足率: 80.4%
已断开电池: batt_ev_006
时间步 28: 电池 batt_ev_006 已离开，当前SOC: 72.0%，能量满足率: 71.4%
奖励各项的值：powerloss=-0.1329581283005673, voltage=-0.2796985652040207, ctrl=-0.0, connection=7.84, completion=3.673469387755102, energy=7.637276084357682, transformer=0.
已连接电池 batt_ev_054, 初始SOC: 82.0%, 最大功率: 120kW, 电池容量: 85kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_054 已接入
已连接电池 batt_ev_129, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 94kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_129 已接入
已连接电池 batt_ev_088, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 50kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_088 已接入
已连接电池 batt_ev_007, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 84kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_007 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=40.0失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=29.09090909090909失败。
功率需求: 40.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=32.72727272727273失败。
功率需求: 32.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=29.09090909090909。
功率需求: 48.00 kW, 充电桩功率: 29.09 kW, 最终充电功率: 29.09 kW。
初次设置charger_power=54.54545454545455。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=21.818181818181817失败。
功率需求: 25.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 64.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_225 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 29.090909090909086, -5.907161036625574
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_007 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.80 更新为 0.92。
SOC从 0.84 更新为 0.96。
SOC从 0.82 更新为 0.94。
SOC从 0.82 更新为 0.91。
SOC从 0.28 更新为 0.43。
SOC从 0.38 更新为 0.62。
SOC从 0.87 更新为 0.95。
SOC从 0.32 更新为 0.49。
SOC从 0.67 更新为 0.81。
SOC从 0.40 更新为 0.57。
已断开电池: batt_ev_034
时间步 29: 电池 batt_ev_034 已离开，当前SOC: 91.5%，能量满足率: 91.5%
已断开电池: batt_ev_101
时间步 29: 电池 batt_ev_101 已离开，当前SOC: 94.2%，能量满足率: 95.0%
已断开电池: batt_ev_093
时间步 29: 电池 batt_ev_093 已离开，当前SOC: 95.3%，能量满足率: 95.5%
已断开电池: batt_ev_057
时间步 29: 电池 batt_ev_057 已离开，当前SOC: 56.6%，能量满足率: 65.6%
已断开电池: batt_ev_225
时间步 29: 电池 batt_ev_225 已离开，当前SOC: 81.0%，能量满足率: 63.1%
奖励各项的值：powerloss=-0.13507131328264688, voltage=-0.28231448677661364, ctrl=-0.0, connection=8.24, completion=3.4951456310679614, energy=7.665259207232218, transformer=0.
已连接电池 batt_ev_142, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_142 已接入
已连接电池 batt_ev_147, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_147 已接入
已连接电池 batt_ev_079, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 78kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_079 已接入
时间步 29: 电池 batt_ev_156 已错过离开时间，无法接入
已连接电池 batt_ev_053, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_053 已接入
已连接电池 batt_ev_211, 初始SOC: 62.0%, 最大功率: 120kW, 电池容量: 106kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_211 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=3.6363636363636362失败。
功率需求: 25.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=29.09090909090909，设置charger_power=14.545454545454545失败。
功率需求: 30.00 kW, 充电桩功率: 29.09 kW, 最终充电功率: 29.09 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=47.27272727272727。
功率需求: 72.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 29.090909090909086, -5.907161036625574
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_007 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_147 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 47.27272727272727, -9.599136684516559
SOC从 0.32 更新为 0.46。
SOC从 0.96 更新为 1.00。
SOC从 0.52 更新为 0.67。
SOC从 0.91 更新为 0.99。
SOC从 0.43 更新为 0.57。
SOC从 0.62 更新为 0.80。
SOC从 0.08 更新为 0.25。
SOC从 0.49 更新为 0.67。
SOC从 0.32 更新为 0.46。
SOC从 0.62 更新为 0.73。
已断开电池: batt_ev_111
时间步 30 执行前: 电池 batt_ev_111 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_007
时间步 30: 电池 batt_ev_007 已离开，当前SOC: 66.6%，能量满足率: 52.5%
已断开电池: batt_ev_147
时间步 30: 电池 batt_ev_147 已离开，当前SOC: 66.8%，能量满足率: 70.3%
奖励各项的值：powerloss=-0.1466310694874981, voltage=-0.3004066725505372, ctrl=-0.0, connection=8.48, completion=3.490566037735849, energy=7.658456388848659, transformer=0.
已连接电池 batt_ev_017, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_017 已接入
已连接电池 batt_ev_087, 初始SOC: 62.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_087 已接入
时间步 30: 电池 batt_ev_021 已错过离开时间，无法接入
已连接电池 batt_ev_209, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_209 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=29.09090909090909，设置charger_power=-0.0失败。
功率需求: 30.00 kW, 充电桩功率: 29.09 kW, 最终充电功率: 29.09 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=36.36363636363636失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 48.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 29.090909090909086, -5.907161036625574
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.46 更新为 0.59。
SOC从 0.28 更新为 0.49。
SOC从 0.62 更新为 0.78。
SOC从 0.99 更新为 1.00。
SOC从 0.57 更新为 0.72。
SOC从 0.80 更新为 0.92。
SOC从 0.25 更新为 0.43。
SOC从 0.38 更新为 0.59。
SOC从 0.46 更新为 0.60。
SOC从 0.73 更新为 0.84。
已断开电池: batt_ev_054
时间步 31 执行前: 电池 batt_ev_054 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_142
时间步 31: 电池 batt_ev_142 已离开，当前SOC: 59.3%，能量满足率: 45.5%
奖励各项的值：powerloss=-0.16533089272252557, voltage=-0.25627617123214375, ctrl=-0.0, connection=8.64, completion=3.5185185185185186, energy=7.65132448041319, transformer=0.
已连接电池 batt_ev_178, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 93kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_178 已接入
已连接电池 batt_ev_110, 初始SOC: 22.0%, 最大功率: 100kW, 电池容量: 65kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_110 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=43.63636363636363失败。
功率需求: 40.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=50.90909090909091。
功率需求: 100.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 40.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=14.545454545454545失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=29.09090909090909失败。
功率需求: 48.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_178 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_110 充电的有无功功率为 50.90909090909091, -10.337531814094755
SOC从 0.42 更新为 0.57。
SOC从 0.49 更新为 0.67。
SOC从 0.78 更新为 0.89。
SOC从 0.22 更新为 0.42。
SOC从 0.72 更新为 0.82。
SOC从 0.92 更新为 0.99。
SOC从 0.43 更新为 0.60。
SOC从 0.59 更新为 0.74。
SOC从 0.60 更新为 0.75。
SOC从 0.84 更新为 0.95。
已断开电池: batt_ev_129
时间步 32: 电池 batt_ev_129 已离开，当前SOC: 82.2%，能量满足率: 90.3%
已断开电池: batt_ev_088
时间步 32 执行前: 电池 batt_ev_088 已充满 (SOC: 99.5%)，离开
已断开电池: batt_ev_079
时间步 32: 电池 batt_ev_079 已离开，当前SOC: 60.5%，能量满足率: 58.3%
已断开电池: batt_ev_053
时间步 32: 电池 batt_ev_053 已离开，当前SOC: 74.6%，能量满足率: 64.6%
已断开电池: batt_ev_211
时间步 32 执行前: 电池 batt_ev_211 已充满 (SOC: 95.5%)，离开
已断开电池: batt_ev_087
时间步 32: 电池 batt_ev_087 已离开，当前SOC: 89.0%，能量满足率: 89.9%
已断开电池: batt_ev_178
时间步 32: 电池 batt_ev_178 已离开，当前SOC: 56.7%，能量满足率: 26.2%
已断开电池: batt_ev_110
时间步 32: 电池 batt_ev_110 已离开，当前SOC: 41.6%，能量满足率: 32.6%
奖励各项的值：powerloss=-0.18126424676303599, voltage=-0.23921733985001303, ctrl=-0.0, connection=9.28, completion=3.4482758620689657, energy=7.608025577702629, transformer=0.
已连接电池 batt_ev_112, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 71kWh，并创BMS。
时间步 32 执行前: 排队电池 batt_ev_112 已接入
已连接电池 batt_ev_223, 初始SOC: 22.0%, 最大功率: 100kW, 电池容量: 81kWh，并创BMS。
时间步 32 执行前: 排队电池 batt_ev_223 已接入
已连接电池 batt_ev_207, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
时间步 32 执行前: 排队电池 batt_ev_207 已接入
已连接电池 batt_ev_198, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 88kWh，并创BMS。
时间步 32 执行前: 排队电池 batt_ev_198 已接入
已连接电池 batt_ev_152, 初始SOC: 68.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
时间步 32 执行前: 排队电池 batt_ev_152 已接入
时间步 32: 电池 batt_ev_192 已错过离开时间，无法接入
已连接电池 batt_ev_171, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
时间步 32 执行前: 排队电池 batt_ev_171 已接入
已连接电池 batt_ev_022, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 68kWh，并创BMS。
时间步 32 执行前: 排队电池 batt_ev_022 已接入
已连接电池 batt_ev_028, 初始SOC: 82.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 32 执行前: 排队电池 batt_ev_028 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 100.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=50.90909090909091。
功率需求: 60.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
初次设置charger_power=54.54545454545455。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=54.54545454545455失败。
功率需求: 24.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=36.36363636363636。
功率需求: 24.00 kW, 充电桩功率: 36.36 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_223 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_198 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.22 更新为 0.41。
SOC从 0.67 更新为 0.80。
SOC从 0.22 更新为 0.40。
SOC从 0.28 更新为 0.55。
SOC从 0.08 更新为 0.23。
SOC从 0.68 更新为 0.86。
SOC从 0.12 更新为 0.44。
SOC从 0.74 更新为 0.85。
SOC从 0.32 更新为 0.50。
SOC从 0.82 更新为 0.93。
已断开电池: batt_ev_017
时间步 33: 电池 batt_ev_017 已离开，当前SOC: 80.5%，能量满足率: 75.0%
已断开电池: batt_ev_209
时间步 33: 电池 batt_ev_209 已离开，当前SOC: 84.6%，能量满足率: 77.6%
已断开电池: batt_ev_112
时间步 33: 电池 batt_ev_112 已离开，当前SOC: 41.2%，能量满足率: 32.0%
已断开电池: batt_ev_223
时间步 33: 电池 batt_ev_223 已离开，当前SOC: 40.0%，能量满足率: 35.9%
已断开电池: batt_ev_198
时间步 33: 电池 batt_ev_198 已离开，当前SOC: 23.5%，能量满足率: 18.5%
奖励各项的值：powerloss=-0.19940844814352832, voltage=-0.3102569640626629, ctrl=-0.0, connection=9.68, completion=3.3057851239669422, energy=7.491133320852055, transformer=0.
时间步 33: 电池 batt_ev_168 已错过离开时间，无法接入
时间步 33: 电池 batt_ev_070 已错过离开时间，无法接入
已连接电池 batt_ev_155, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 76kWh，并创BMS。
时间步 33 执行前: 排队电池 batt_ev_155 已接入
时间步 33: 电池 batt_ev_089 已错过离开时间，无法接入
已连接电池 batt_ev_094, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 56kWh，并创BMS。
时间步 33 执行前: 排队电池 batt_ev_094 已接入
已连接电池 batt_ev_140, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 67kWh，并创BMS。
时间步 33 执行前: 排队电池 batt_ev_140 已接入
已连接电池 batt_ev_068, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 62kWh，并创BMS。
时间步 33 执行前: 排队电池 batt_ev_068 已接入
已连接电池 batt_ev_185, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
时间步 33 执行前: 排队电池 batt_ev_185 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 36.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=25.454545454545453失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=36.36363636363636，设置charger_power=14.545454545454545失败。
功率需求: 15.00 kW, 充电桩功率: 36.36 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_155 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_094 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_068 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_185 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.52 更新为 0.68。
SOC从 0.28 更新为 0.52。
SOC从 0.38 更新为 0.60。
SOC从 0.55 更新为 0.73。
SOC从 0.18 更新为 0.40。
SOC从 0.86 更新为 0.93。
SOC从 0.44 更新为 0.72。
SOC从 0.48 更新为 0.78。
SOC从 0.50 更新为 0.67。
SOC从 0.93 更新为 0.99。
已断开电池: batt_ev_207
时间步 34: 电池 batt_ev_207 已离开，当前SOC: 73.3%，能量满足率: 64.7%
已断开电池: batt_ev_152
时间步 34 执行前: 电池 batt_ev_152 已充满 (SOC: 93.0%)，离开
已断开电池: batt_ev_171
时间步 34: 电池 batt_ev_171 已离开，当前SOC: 71.6%，能量满足率: 74.5%
已断开电池: batt_ev_022
时间步 34: 电池 batt_ev_022 已离开，当前SOC: 67.3%，能量满足率: 53.5%
已断开电池: batt_ev_028
时间步 34: 电池 batt_ev_028 已离开，当前SOC: 99.1%，能量满足率: 95.0%
已断开电池: batt_ev_068
时间步 34: 电池 batt_ev_068 已离开，当前SOC: 40.0%，能量满足率: 36.7%
奖励各项的值：powerloss=-0.21490653786601202, voltage=-0.33065675616283263, ctrl=-0.0, connection=10.16, completion=3.228346456692913, energy=7.4713784750087875, transformer=0.
已连接电池 batt_ev_049, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
已连接电池 batt_ev_023, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=50.90909090909091。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=14.545454545454545。
功率需求: 15.00 kW, 充电桩功率: 14.55 kW, 最终充电功率: 14.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=32.72727272727273失败。
功率需求: 24.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_155 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_094 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_185 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_049 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_023 充电的有无功功率为 14.545454545454543, -2.953580518312787
SOC从 0.68 更新为 0.84。
SOC从 0.52 更新为 0.68。
SOC从 0.60 更新为 0.81。
SOC从 0.32 更新为 0.55。
SOC从 0.92 更新为 0.99。
SOC从 0.78 更新为 0.93。
已断开电池: batt_ev_155
时间步 35: 电池 batt_ev_155 已离开，当前SOC: 83.6%，能量满足率: 68.6%
已断开电池: batt_ev_094
时间步 35: 电池 batt_ev_094 已离开，当前SOC: 68.4%，能量满足率: 57.8%
已断开电池: batt_ev_185
时间步 35 执行前: 电池 batt_ev_185 已充满 (SOC: 93.0%)，离开
奖励各项的值：powerloss=-0.2144866231715364, voltage=-0.30209608069020844, ctrl=-0.0, connection=10.4, completion=3.230769230769231, energy=7.473119731450385, transformer=0.
已连接电池 batt_ev_121, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=58.18181818181818，设置charger_power=25.454545454545453失败。
功率需求: 40.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 36.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=14.545454545454545，设置charger_power=-0.0失败。
功率需求: 15.00 kW, 充电桩功率: 14.55 kW, 最终充电功率: 14.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_049 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_023 充电的有无功功率为 14.545454545454543, -2.953580518312787
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.81 更新为 0.96。
SOC从 0.55 更新为 0.72。
SOC从 0.99 更新为 1.00。
SOC从 0.48 更新为 0.71。
已断开电池: batt_ev_140
时间步 36: 电池 batt_ev_140 已离开，当前SOC: 96.4%，能量满足率: 97.3%
已断开电池: batt_ev_049
时间步 36: 电池 batt_ev_049 已离开，当前SOC: 71.6%，能量满足率: 60.0%
已断开电池: batt_ev_023
时间步 36 执行前: 电池 batt_ev_023 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.21462250513526193, voltage=-0.38432039606963064, ctrl=-0.0, connection=10.64, completion=3.233082706766917, energy=7.498010253981101, transformer=0.
智能体的动作为: [25  0  1  0  2  1  1  0  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=47.27272727272727失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 32.0, -6.497877140288132
SOC从 0.71 更新为 0.85。
奖励各项的值：powerloss=-0.21143178563734066, voltage=-0.4179644299486296, ctrl=-0.0, connection=10.64, completion=3.233082706766917, energy=7.498010253981101, transformer=0.
已连接电池 batt_ev_015, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
已连接电池 batt_ev_201, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [30  3  2  1  2  8  0  3 14  9  0]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=25.454545454545453失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=47.27272727272727。
功率需求: 36.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=25.454545454545453。
功率需求: 120.00 kW, 充电桩功率: 25.45 kW, 最终充电功率: 25.45 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 25.454545454545453, -5.168765907047377
SOC从 0.85 更新为 0.98。
SOC从 0.52 更新为 0.67。
SOC从 0.18 更新为 0.24。
已断开电池: batt_ev_121
时间步 38 执行前: 电池 batt_ev_121 已充满 (SOC: 98.2%)，离开
奖励各项的值：powerloss=-0.21241908980944135, voltage=-0.44626244829367057, ctrl=-0.0, connection=10.72, completion=3.283582089552239, energy=7.516681819249898, transformer=0.
已连接电池 batt_ev_080, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_204, 初始SOC: 2.0%, 最大功率: 80kW, 电池容量: 81kWh，并创BMS。
智能体的动作为: [25  0  1  1  2  1  1  0  0  1  3]
初次设置charger_power=58.18181818181818。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=25.454545454545453，设置charger_power=54.54545454545455失败。
功率需求: 120.00 kW, 充电桩功率: 25.45 kW, 最终充电功率: 25.45 kW。
初次设置charger_power=47.27272727272727。
功率需求: 36.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 25.454545454545453, -5.168765907047377
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.02 更新为 0.20。
SOC从 0.67 更新为 0.82。
SOC从 0.24 更新为 0.30。
SOC从 0.57 更新为 0.74。
奖励各项的值：powerloss=-0.21430424161362227, voltage=-0.44782308173485275, ctrl=-0.0, connection=10.72, completion=3.283582089552239, energy=7.516681819249898, transformer=0.
已连接电池 batt_ev_183, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 71kWh，并创BMS。
已连接电池 batt_ev_230, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [25  0  1  0  2  1  1  0  0  1  3]
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=43.63636363636363失败。
功率需求: 24.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=25.454545454545453，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 25.45 kW, 最终充电功率: 25.45 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 24.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 25.454545454545453, -5.168765907047377
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_183 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.20 更新为 0.38。
SOC从 0.38 更新为 0.57。
SOC从 0.82 更新为 0.91。
SOC从 0.52 更新为 0.66。
SOC从 0.30 更新为 0.37。
SOC从 0.74 更新为 0.85。
已断开电池: batt_ev_183
时间步 40 执行前: 电池 batt_ev_183 已充满 (SOC: 57.2%)，离开
奖励各项的值：powerloss=-0.21249155459300478, voltage=-0.47275993544421135, ctrl=-0.0, connection=10.8, completion=3.333333333333333, energy=7.535076768736937, transformer=0.
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=58.18181818181818，设置charger_power=54.54545454545455失败。
功率需求: 64.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=18.18181818181818失败。
功率需求: 15.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=25.454545454545453，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 25.45 kW, 最终充电功率: 25.45 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=29.09090909090909失败。
功率需求: 24.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 25.454545454545453, -5.168765907047377
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.38 更新为 0.56。
SOC从 0.91 更新为 0.97。
SOC从 0.66 更新为 0.80。
SOC从 0.37 更新为 0.43。
SOC从 0.85 更新为 0.96。
已断开电池: batt_ev_201
时间步 41: 电池 batt_ev_201 已离开，当前SOC: 42.7%，能量满足率: 35.3%
已断开电池: batt_ev_080
时间步 41 执行前: 电池 batt_ev_080 已充满 (SOC: 95.9%)，离开
已断开电池: batt_ev_204
时间步 41: 电池 batt_ev_204 已离开，当前SOC: 55.9%，能量满足率: 56.1%
已断开电池: batt_ev_230
时间步 41: 电池 batt_ev_230 已离开，当前SOC: 79.7%，能量满足率: 60.2%
奖励各项的值：powerloss=-0.20861999877459433, voltage=-0.381103245301484, ctrl=-0.0, connection=11.120000000000001, completion=3.3093525179856114, energy=7.49926107429756, transformer=0.
智能体的动作为: [25  0  1  0  2  1  1  0  0  1  3]
已有历史设置self.charger_power=47.27272727272727，设置charger_power=3.6363636363636362失败。
功率需求: 15.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.97 更新为 1.00。
已断开电池: batt_ev_015
时间步 42 执行前: 电池 batt_ev_015 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.20460858873946328, voltage=-0.22858646353187462, ctrl=-0.0, connection=11.200000000000001, completion=3.3571428571428568, energy=7.517123495195435, transformer=0.
已连接电池 batt_ev_148, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_215, 初始SOC: 62.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_210, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [21  3  2  1  6  8  8  9 14  9  0]
初次设置charger_power=54.54545454545455。
功率需求: 120.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=36.36363636363636。
功率需求: 72.00 kW, 充电桩功率: 36.36 kW, 最终充电功率: 36.36 kW。
初次设置charger_power=29.09090909090909。
功率需求: 36.00 kW, 充电桩功率: 29.09 kW, 最终充电功率: 29.09 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 36.36363636363636, -7.3839512957819675
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 29.090909090909086, -5.907161036625574
SOC从 0.28 更新为 0.43。
SOC从 0.62 更新为 0.74。
SOC从 0.57 更新为 0.70。
奖励各项的值：powerloss=-0.20425138483708377, voltage=-0.11738059667547374, ctrl=-0.0, connection=11.200000000000001, completion=3.3571428571428568, energy=7.517123495195435, transformer=0.
智能体的动作为: [25  0  1  1  2  1  1  0  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=36.36363636363636，设置charger_power=36.36363636363636失败。
功率需求: 48.00 kW, 充电桩功率: 36.36 kW, 最终充电功率: 36.36 kW。
已有历史设置self.charger_power=29.09090909090909，设置charger_power=54.54545454545455失败。
功率需求: 24.00 kW, 充电桩功率: 29.09 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 36.36363636363636, -7.3839512957819675
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.43 更新为 0.58。
SOC从 0.74 更新为 0.86。
SOC从 0.70 更新为 0.81。
已断开电池: batt_ev_210
时间步 44: 电池 batt_ev_210 已离开，当前SOC: 81.1%，能量满足率: 58.8%
奖励各项的值：powerloss=-0.19657849043570483, voltage=-0.1102872018429557, ctrl=-0.0, connection=11.28, completion=3.333333333333333, energy=7.505546028315953, transformer=0.
已连接电池 batt_ev_146, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
已连接电池 batt_ev_027, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 107kWh，并创BMS。
智能体的动作为: [25  0  1  1  2  1  1  0  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=36.36363636363636，设置charger_power=18.18181818181818失败。
功率需求: 30.00 kW, 充电桩功率: 36.36 kW, 最终充电功率: 30.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.32 更新为 0.45。
SOC从 0.58 更新为 0.73。
SOC从 0.86 更新为 0.96。
SOC从 0.42 更新为 0.59。
已断开电池: batt_ev_215
时间步 45 执行前: 电池 batt_ev_215 已充满 (SOC: 95.8%)，离开
奖励各项的值：powerloss=-0.19689207446282467, voltage=-0.06035964357912427, ctrl=-0.0, connection=11.36, completion=3.380281690140845, energy=7.523112605581334, transformer=0.
已连接电池 batt_ev_135, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_127, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 88kWh，并创BMS。
已连接电池 batt_ev_165, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 105kWh，并创BMS。
智能体的动作为: [25  0  1  0  2  1  1  0  0  1  3]
初次设置charger_power=58.18181818181818。
功率需求: 64.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=47.27272727272727失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 100.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 120.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.32 更新为 0.59。
SOC从 0.45 更新为 0.57。
SOC从 0.73 更新为 0.86。
SOC从 0.59 更新为 0.74。
SOC从 0.18 更新为 0.35。
SOC从 0.18 更新为 0.31。
已断开电池: batt_ev_148
时间步 46: 电池 batt_ev_148 已离开，当前SOC: 86.2%，能量满足率: 96.9%
已断开电池: batt_ev_027
时间步 46: 电池 batt_ev_027 已离开，当前SOC: 57.5%，能量满足率: 42.5%
奖励各项的值：powerloss=-0.19257453927953205, voltage=-0.06954104957621166, ctrl=-0.0, connection=11.52, completion=3.333333333333333, energy=7.515441103254568, transformer=0.
已连接电池 batt_ev_003, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_001, 初始SOC: 38.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
已连接电池 batt_ev_086, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=58.18181818181818，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=47.27272727272727。
功率需求: 80.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.59 更新为 0.81。
SOC从 0.12 更新为 0.35。
SOC从 0.74 更新为 0.85。
SOC从 0.38 更新为 0.57。
SOC从 0.35 更新为 0.51。
SOC从 0.31 更新为 0.44。
SOC从 0.42 更新为 0.57。
已断开电池: batt_ev_146
时间步 47: 电池 batt_ev_146 已离开，当前SOC: 84.6%，能量满足率: 76.0%
已断开电池: batt_ev_135
时间步 47: 电池 batt_ev_135 已离开，当前SOC: 81.2%，能量满足率: 74.5%
奖励各项的值：powerloss=-0.17648161556635, voltage=-0.13434683052607754, ctrl=-0.0, connection=11.68, completion=3.287671232876712, energy=7.515595836426941, transformer=0.
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 60.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.35 更新为 0.55。
SOC从 0.57 更新为 0.77。
SOC从 0.51 更新为 0.68。
SOC从 0.44 更新为 0.57。
SOC从 0.57 更新为 0.73。
已断开电池: batt_ev_165
时间步 48: 电池 batt_ev_165 已离开，当前SOC: 57.0%，能量满足率: 48.7%
奖励各项的值：powerloss=-0.15274696825820247, voltage=-0.17582262489575173, ctrl=-0.0, connection=11.76, completion=3.265306122448979, energy=7.497608304011986, transformer=0.
已连接电池 batt_ev_043, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_051, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
已连接电池 batt_ev_144, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=50.90909090909091。
功率需求: 64.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=29.09090909090909失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 40.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 40.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_144 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.48 更新为 0.62。
SOC从 0.22 更新为 0.51。
SOC从 0.42 更新为 0.61。
SOC从 0.55 更新为 0.70。
SOC从 0.77 更新为 0.94。
SOC从 0.68 更新为 0.84。
SOC从 0.73 更新为 0.86。
已断开电池: batt_ev_003
时间步 49: 电池 batt_ev_003 已离开，当前SOC: 85.7%，能量满足率: 78.0%
已断开电池: batt_ev_001
时间步 49: 电池 batt_ev_001 已离开，当前SOC: 94.1%，能量满足率: 93.5%
奖励各项的值：powerloss=-0.1338672600007078, voltage=-0.22670258450486314, ctrl=-0.0, connection=11.92, completion=3.221476510067114, energy=7.512095878336903, transformer=0.
已连接电池 batt_ev_188, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
已连接电池 batt_ev_107, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 60kWh，并创BMS。
已连接电池 batt_ev_131, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 120.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=29.09090909090909失败。
功率需求: 40.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_144 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.18 更新为 0.34。
SOC从 0.62 更新为 0.76。
SOC从 0.51 更新为 0.74。
SOC从 0.61 更新为 0.79。
SOC从 0.70 更新为 0.85。
SOC从 0.28 更新为 0.51。
SOC从 0.84 更新为 0.96。
SOC从 0.22 更新为 0.52。
已断开电池: batt_ev_127
时间步 50: 电池 batt_ev_127 已离开，当前SOC: 95.5%，能量满足率: 96.9%
已断开电池: batt_ev_086
时间步 50: 电池 batt_ev_086 已离开，当前SOC: 84.7%，能量满足率: 90.9%
已断开电池: batt_ev_051
时间步 50: 电池 batt_ev_051 已离开，当前SOC: 76.4%，能量满足率: 83.6%
已断开电池: batt_ev_144
时间步 50 执行前: 电池 batt_ev_144 已充满 (SOC: 74.1%)，离开
奖励各项的值：powerloss=-0.13138268722809268, voltage=-0.2606413056815815, ctrl=-0.0, connection=12.24, completion=3.202614379084967, energy=7.558426769124969, transformer=0.
已连接电池 batt_ev_136, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
已连接电池 batt_ev_116, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 52kWh，并创BMS。
已连接电池 batt_ev_196, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=36.36363636363636失败。
功率需求: 32.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=47.27272727272727。
功率需求: 64.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.34 更新为 0.50。
SOC从 0.18 更新为 0.49。
SOC从 0.79 更新为 0.92。
SOC从 0.51 更新为 0.71。
SOC从 0.42 更新为 0.59。
SOC从 0.52 更新为 0.71。
SOC从 0.42 更新为 0.65。
已断开电池: batt_ev_131
时间步 51: 电池 batt_ev_131 已离开，当前SOC: 71.2%，能量满足率: 64.8%
奖励各项的值：powerloss=-0.12386746823852002, voltage=-0.29053440269725783, ctrl=-0.0, connection=12.32, completion=3.1818181818181817, energy=7.55139784555952, transformer=0.
已连接电池 batt_ev_005, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_063, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
已连接电池 batt_ev_033, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
已连接电池 batt_ev_077, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=14.545454545454545失败。
功率需求: 20.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=50.90909090909091失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 48.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.50 更新为 0.66。
SOC从 0.49 更新为 0.76。
SOC从 0.38 更新为 0.60。
SOC从 0.92 更新为 0.99。
SOC从 0.52 更新为 0.74。
SOC从 0.71 更新为 0.84。
SOC从 0.59 更新为 0.73。
SOC从 0.32 更新为 0.47。
SOC从 0.18 更新为 0.35。
SOC从 0.65 更新为 0.87。
已断开电池: batt_ev_043
时间步 52 执行前: 电池 batt_ev_043 已充满 (SOC: 99.2%)，离开
奖励各项的值：powerloss=-0.12994068024337263, voltage=-0.28801359925099357, ctrl=-0.0, connection=12.4, completion=3.225806451612903, energy=7.5671952788139745, transformer=0.
已连接电池 batt_ev_082, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
时间步 52 执行前: 排队电池 batt_ev_082 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=40.0失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=50.90909090909091。
功率需求: 64.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=36.36363636363636失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=25.454545454545453失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=18.18181818181818失败。
功率需求: 20.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 20.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 50.90909090909091, -10.337531814094755
SOC从 0.66 更新为 0.81。
SOC从 0.76 更新为 0.90。
SOC从 0.60 更新为 0.77。
SOC从 0.38 更新为 0.63。
SOC从 0.74 更新为 0.89。
SOC从 0.84 更新为 0.97。
SOC从 0.73 更新为 0.83。
SOC从 0.47 更新为 0.62。
SOC从 0.35 更新为 0.53。
SOC从 0.87 更新为 0.97。
已断开电池: batt_ev_116
时间步 53: 电池 batt_ev_116 已离开，当前SOC: 97.1%，能量满足率: 98.4%
已断开电池: batt_ev_077
时间步 53: 电池 batt_ev_077 已离开，当前SOC: 52.5%，能量满足率: 43.2%
奖励各项的值：powerloss=-0.1267461405346652, voltage=-0.26201104031254197, ctrl=-0.0, connection=12.56, completion=3.184713375796178, energy=7.560935597118047, transformer=0.
已连接电池 batt_ev_159, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 53kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_159 已接入
时间步 53: 电池 batt_ev_097 已错过离开时间，无法接入
已连接电池 batt_ev_105, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_105 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=29.09090909090909失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=14.545454545454545失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=47.27272727272727失败。
功率需求: 24.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=14.545454545454545失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=3.6363636363636362失败。
功率需求: 20.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=40.0失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 72.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=47.27272727272727。
功率需求: 48.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
初次设置charger_power=47.27272727272727。
功率需求: 48.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_105 充电的有无功功率为 47.27272727272727, -9.599136684516559
SOC从 0.81 更新为 0.95。
SOC从 0.90 更新为 0.98。
SOC从 0.77 更新为 0.88。
SOC从 0.63 更新为 0.86。
SOC从 0.89 更新为 0.99。
SOC从 0.97 更新为 1.00。
SOC从 0.83 更新为 0.93。
SOC从 0.62 更新为 0.77。
SOC从 0.68 更新为 0.90。
SOC从 0.42 更新为 0.65。
已断开电池: batt_ev_188
时间步 54: 电池 batt_ev_188 已离开，当前SOC: 95.4%，能量满足率: 96.7%
已断开电池: batt_ev_107
时间步 54 执行前: 电池 batt_ev_107 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_136
时间步 54: 电池 batt_ev_136 已离开，当前SOC: 92.8%，能量满足率: 90.7%
已断开电池: batt_ev_196
时间步 54 执行前: 电池 batt_ev_196 已充满 (SOC: 98.4%)，离开
已断开电池: batt_ev_063
时间步 54 执行前: 电池 batt_ev_063 已充满 (SOC: 98.9%)，离开
已断开电池: batt_ev_033
时间步 54: 电池 batt_ev_033 已离开，当前SOC: 77.0%，能量满足率: 68.2%
已断开电池: batt_ev_105
时间步 54: 电池 batt_ev_105 已离开，当前SOC: 64.7%，能量满足率: 40.6%
奖励各项的值：powerloss=-0.13239020271997995, voltage=-0.26795798245158764, ctrl=-0.0, connection=13.120000000000001, completion=3.231707317073171, energy=7.601746947288436, transformer=0.
已连接电池 batt_ev_058, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_058 已接入
已连接电池 batt_ev_118, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 90kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_118 已接入
已连接电池 batt_ev_199, 初始SOC: 52.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_199 已接入
已连接电池 batt_ev_153, 初始SOC: 2.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_153 已接入
已连接电池 batt_ev_169, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 85kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_169 已接入
已连接电池 batt_ev_059, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
已连接电池 batt_ev_175, 初始SOC: 88.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=21.818181818181817失败。
功率需求: 15.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=18.18181818181818失败。
功率需求: 20.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=14.545454545454545失败。
功率需求: 20.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=21.818181818181817。
功率需求: 30.00 kW, 充电桩功率: 21.82 kW, 最终充电功率: 21.82 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_058 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 21.818181818181817, -4.43037077746918
SOC从 0.28 更新为 0.48。
SOC从 0.57 更新为 0.72。
SOC从 0.88 更新为 0.95。
SOC从 0.86 更新为 0.96。
SOC从 0.52 更新为 0.70。
SOC从 0.02 更新为 0.23。
SOC从 0.28 更新为 0.44。
SOC从 0.18 更新为 0.45。
SOC从 0.90 更新为 1.00。
SOC从 0.88 更新为 0.94。
已断开电池: batt_ev_005
时间步 55: 电池 batt_ev_005 已离开，当前SOC: 94.9%，能量满足率: 94.9%
已断开电池: batt_ev_082
时间步 55: 电池 batt_ev_082 已离开，当前SOC: 96.3%，能量满足率: 97.2%
已断开电池: batt_ev_159
时间步 55 执行前: 电池 batt_ev_159 已充满 (SOC: 99.7%)，离开
奖励各项的值：powerloss=-0.15125094840161385, voltage=-0.2569418370499599, ctrl=-0.0, connection=13.36, completion=3.2335329341317367, energy=7.640077403416492, transformer=0.
已连接电池 batt_ev_029, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_195, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
已连接电池 batt_ev_213, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=47.27272727272727失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 64.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=50.90909090909091。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=50.90909090909091失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=21.818181818181817，设置charger_power=10.909090909090908失败。
功率需求: 30.00 kW, 充电桩功率: 21.82 kW, 最终充电功率: 21.82 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_058 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 21.818181818181817, -4.43037077746918
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.48 更新为 0.65。
SOC从 0.72 更新为 0.85。
SOC从 0.42 更新为 0.65。
SOC从 0.38 更新为 0.67。
SOC从 0.70 更新为 0.88。
SOC从 0.23 更新为 0.44。
SOC从 0.44 更新为 0.60。
SOC从 0.45 更新为 0.68。
SOC从 0.28 更新为 0.49。
SOC从 0.94 更新为 0.99。
已断开电池: batt_ev_058
时间步 56 执行前: 电池 batt_ev_058 已充满 (SOC: 65.2%)，离开
已断开电池: batt_ev_213
时间步 56 执行前: 电池 batt_ev_213 已充满 (SOC: 48.7%)，离开
奖励各项的值：powerloss=-0.1744661345000925, voltage=-0.23185684878106239, ctrl=-0.0, connection=13.52, completion=3.3136094674556213, energy=7.668005481482568, transformer=0.
已连接电池 batt_ev_133, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
时间步 56 执行前: 排队电池 batt_ev_133 已接入
已连接电池 batt_ev_145, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 62kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 120.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=21.818181818181817失败。
功率需求: 30.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 36.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=18.18181818181818失败。
功率需求: 25.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=21.818181818181817，设置charger_power=-0.0失败。
功率需求: 30.00 kW, 充电桩功率: 21.82 kW, 最终充电功率: 21.82 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 21.818181818181817, -4.43037077746918
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.18 更新为 0.35。
SOC从 0.85 更新为 0.94。
SOC从 0.65 更新为 0.84。
SOC从 0.67 更新为 0.89。
SOC从 0.88 更新为 0.96。
SOC从 0.44 更新为 0.62。
SOC从 0.60 更新为 0.76。
SOC从 0.68 更新为 0.85。
SOC从 0.52 更新为 0.71。
SOC从 0.99 更新为 1.00。
已断开电池: batt_ev_118
时间步 57 执行前: 电池 batt_ev_118 已充满 (SOC: 93.8%)，离开
已断开电池: batt_ev_153
时间步 57: 电池 batt_ev_153 已离开，当前SOC: 62.4%，能量满足率: 62.9%
已断开电池: batt_ev_175
时间步 57 执行前: 电池 batt_ev_175 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_029
时间步 57 执行前: 电池 batt_ev_029 已充满 (SOC: 84.1%)，离开
奖励各项的值：powerloss=-0.1842581725549337, voltage=-0.24641098437760522, ctrl=-0.0, connection=13.84, completion=3.4104046242774566, energy=7.700507503846391, transformer=0.
已连接电池 batt_ev_044, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_044 已接入
已连接电池 batt_ev_154, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_154 已接入
已连接电池 batt_ev_179, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_179 已接入
已连接电池 batt_ev_246, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 74kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=14.545454545454545失败。
功率需求: 15.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=3.6363636363636362失败。
功率需求: 25.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=43.63636363636363失败。
功率需求: 40.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=29.09090909090909失败。
功率需求: 15.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=50.90909090909091失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=47.27272727272727。
功率需求: 80.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 47.27272727272727, -9.599136684516559
SOC从 0.35 更新为 0.51。
SOC从 0.18 更新为 0.42。
SOC从 0.32 更新为 0.47。
SOC从 0.89 更新为 0.98。
SOC从 0.96 更新为 1.00。
SOC从 0.18 更新为 0.52。
SOC从 0.76 更新为 0.88。
SOC从 0.85 更新为 0.92。
SOC从 0.71 更新为 0.84。
SOC从 0.48 更新为 0.64。
已断开电池: batt_ev_199
时间步 58 执行前: 电池 batt_ev_199 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_169
时间步 58: 电池 batt_ev_169 已离开，当前SOC: 87.9%，能量满足率: 85.6%
已断开电池: batt_ev_059
时间步 58: 电池 batt_ev_059 已离开，当前SOC: 92.2%，能量满足率: 92.7%
已断开电池: batt_ev_195
时间步 58 执行前: 电池 batt_ev_195 已充满 (SOC: 98.4%)，离开
已断开电池: batt_ev_133
时间步 58: 电池 batt_ev_133 已离开，当前SOC: 51.3%，能量满足率: 41.6%
奖励各项的值：powerloss=-0.19830858885937022, voltage=-0.2565097244519743, ctrl=-0.0, connection=14.24, completion=3.4269662921348316, energy=7.720074077913466, transformer=0.
已连接电池 batt_ev_184, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
时间步 58 执行前: 排队电池 batt_ev_184 已接入
已连接电池 batt_ev_066, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
时间步 58 执行前: 排队电池 batt_ev_066 已接入
已连接电池 batt_ev_233, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
已连接电池 batt_ev_219, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_249, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 120.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=50.90909090909091。
功率需求: 120.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 120.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=25.454545454545453失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 60.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.28 更新为 0.41。
SOC从 0.42 更新为 0.62。
SOC从 0.47 更新为 0.63。
SOC从 0.08 更新为 0.25。
SOC从 0.22 更新为 0.52。
SOC从 0.52 更新为 0.75。
SOC从 0.18 更新为 0.39。
SOC从 0.08 更新为 0.23。
SOC从 0.84 更新为 0.97。
SOC从 0.64 更新为 0.80。
已断开电池: batt_ev_145
时间步 59: 电池 batt_ev_145 已离开，当前SOC: 97.2%，能量满足率: 98.2%
已断开电池: batt_ev_044
时间步 59: 电池 batt_ev_044 已离开，当前SOC: 62.2%，能量满足率: 55.3%
已断开电池: batt_ev_179
时间步 59: 电池 batt_ev_179 已离开，当前SOC: 74.6%，能量满足率: 70.8%
奖励各项的值：powerloss=-0.21288244284450764, voltage=-0.27704285046375565, ctrl=-0.0, connection=14.48, completion=3.3701657458563536, energy=7.715976352192372, transformer=0.
已连接电池 batt_ev_032, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_032 已接入
已连接电池 batt_ev_060, 初始SOC: 56.99999999999999%, 最大功率: 100kW, 电池容量: 90kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_060 已接入
已连接电池 batt_ev_103, 初始SOC: 72.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_103 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 120.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 120.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=32.72727272727273失败。
功率需求: 40.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 40.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_060 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_103 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.41 更新为 0.54。
SOC从 0.48 更新为 0.65。
SOC从 0.63 更新为 0.78。
SOC从 0.25 更新为 0.41。
SOC从 0.52 更新为 0.72。
SOC从 0.57 更新为 0.72。
SOC从 0.39 更新为 0.57。
SOC从 0.23 更新为 0.37。
SOC从 0.72 更新为 0.83。
SOC从 0.80 更新为 0.93。
已断开电池: batt_ev_154
时间步 60: 电池 batt_ev_154 已离开，当前SOC: 77.9%，能量满足率: 69.6%
已断开电池: batt_ev_246
时间步 60: 电池 batt_ev_246 已离开，当前SOC: 93.5%，能量满足率: 90.9%
已断开电池: batt_ev_184
时间步 60: 电池 batt_ev_184 已离开，当前SOC: 54.5%，能量满足率: 37.8%
已断开电池: batt_ev_233
时间步 60: 电池 batt_ev_233 已离开，当前SOC: 72.3%，能量满足率: 66.2%
已断开电池: batt_ev_103
时间步 60: 电池 batt_ev_103 已离开，当前SOC: 83.1%，能量满足率: 55.6%
奖励各项的值：powerloss=-0.2175576682648311, voltage=-0.28676765536500337, ctrl=-0.0, connection=14.88, completion=3.279569892473118, energy=7.680660277789221, transformer=0.
已连接电池 batt_ev_205, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 114kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_205 已接入
已连接电池 batt_ev_072, 初始SOC: 12.0%, 最大功率: 100kW, 电池容量: 79kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_072 已接入
已连接电池 batt_ev_217, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_217 已接入
已连接电池 batt_ev_124, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 70kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_124 已接入
已连接电池 batt_ev_189, 初始SOC: 88.0%, 最大功率: 80kW, 电池容量: 78kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_189 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 100.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 96.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 40.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=25.454545454545453。
功率需求: 20.00 kW, 充电桩功率: 25.45 kW, 最终充电功率: 20.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_060 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_217 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 20.0, -4.061173212680082
SOC从 0.48 更新为 0.60。
SOC从 0.65 更新为 0.79。
SOC从 0.12 更新为 0.30。
SOC从 0.41 更新为 0.58。
SOC从 0.38 更新为 0.59。
SOC从 0.72 更新为 0.83。
SOC从 0.57 更新为 0.71。
SOC从 0.37 更新为 0.52。
SOC从 0.38 更新为 0.57。
SOC从 0.88 更新为 0.94。
已断开电池: batt_ev_066
时间步 61: 电池 batt_ev_066 已离开，当前SOC: 58.2%，能量满足率: 55.8%
已断开电池: batt_ev_060
时间步 61: 电池 batt_ev_060 已离开，当前SOC: 83.3%，能量满足率: 64.1%
已断开电池: batt_ev_217
时间步 61: 电池 batt_ev_217 已离开，当前SOC: 59.1%，能量满足率: 35.1%
奖励各项的值：powerloss=-0.2181837148700351, voltage=-0.29299485999126906, ctrl=-0.0, connection=15.120000000000001, completion=3.2275132275132274, energy=7.640748259243354, transformer=0.
已连接电池 batt_ev_073, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 106kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_073 已接入
已连接电池 batt_ev_020, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 99kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_020 已接入
已连接电池 batt_ev_208, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 61kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_208 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=47.27272727272727失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=50.90909090909091。
功率需求: 96.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
初次设置charger_power=54.54545454545455。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 72.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=25.454545454545453，设置charger_power=10.909090909090908失败。
功率需求: 20.00 kW, 充电桩功率: 25.45 kW, 最终充电功率: 20.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.60 更新为 0.72。
SOC从 0.79 更新为 0.89。
SOC从 0.30 更新为 0.49。
SOC从 0.48 更新为 0.60。
SOC从 0.32 更新为 0.46。
SOC从 0.38 更新为 0.60。
SOC从 0.71 更新为 0.81。
SOC从 0.52 更新为 0.66。
SOC从 0.57 更新为 0.77。
SOC从 0.94 更新为 1.00。
已断开电池: batt_ev_219
时间步 62: 电池 batt_ev_219 已离开，当前SOC: 80.5%，能量满足率: 97.7%
已断开电池: batt_ev_032
时间步 62: 电池 batt_ev_032 已离开，当前SOC: 89.0%，能量满足率: 82.0%
已断开电池: batt_ev_189
时间步 62 执行前: 电池 batt_ev_189 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.21580694209400986, voltage=-0.29424110373572177, ctrl=-0.0, connection=15.36, completion=3.229166666666667, energy=7.667060051119817, transformer=0.
已连接电池 batt_ev_091, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_091 已接入
时间步 62: 电池 batt_ev_176 已错过离开时间，无法接入
已连接电池 batt_ev_102, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_102 已接入
已连接电池 batt_ev_236, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 92kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_236 已接入
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 72.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 72.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=36.36363636363636失败。
功率需求: 40.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=47.27272727272727。
功率需求: 80.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 50.90909090909091, -10.337531814094755
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_236 充电的有无功功率为 47.27272727272727, -9.599136684516559
SOC从 0.72 更新为 0.82。
SOC从 0.22 更新为 0.42。
SOC从 0.49 更新为 0.67。
SOC从 0.60 更新为 0.72。
SOC从 0.46 更新为 0.60。
SOC从 0.60 更新为 0.83。
SOC从 0.48 更新为 0.70。
SOC从 0.66 更新为 0.81。
SOC从 0.77 更新为 0.91。
SOC从 0.38 更新为 0.51。
已断开电池: batt_ev_249
时间步 63: 电池 batt_ev_249 已离开，当前SOC: 80.8%，能量满足率: 80.8%
已断开电池: batt_ev_205
时间步 63 执行前: 电池 batt_ev_205 已充满 (SOC: 82.5%)，离开
已断开电池: batt_ev_072
时间步 63: 电池 batt_ev_072 已离开，当前SOC: 67.3%，能量满足率: 64.2%
已断开电池: batt_ev_124
时间步 63: 电池 batt_ev_124 已离开，当前SOC: 91.3%，能量满足率: 98.6%
已断开电池: batt_ev_236
时间步 63: 电池 batt_ev_236 已离开，当前SOC: 50.8%，能量满足率: 23.8%
奖励各项的值：powerloss=-0.21657102097836645, voltage=-0.30522694250966875, ctrl=-0.0, connection=15.76, completion=3.197969543147208, energy=7.659011729138595, transformer=0.
已连接电池 batt_ev_074, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_074 已接入
时间步 63: 电池 batt_ev_130 已错过离开时间，无法接入
已连接电池 batt_ev_061, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 78kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_061 已接入
已连接电池 batt_ev_012, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 98kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_012 已接入
时间步 63: 电池 batt_ev_108 已错过离开时间，无法接入
已连接电池 batt_ev_228, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_228 已接入
已连接电池 batt_ev_218, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 100.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=21.818181818181817失败。
功率需求: 40.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=58.18181818181818。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=47.27272727272727。
功率需求: 64.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_074 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_012 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 47.27272727272727, -9.599136684516559
SOC从 0.48 更新为 0.70。
SOC从 0.42 更新为 0.60。
SOC从 0.28 更新为 0.47。
SOC从 0.72 更新为 0.83。
SOC从 0.60 更新为 0.73。
SOC从 0.83 更新为 0.99。
SOC从 0.70 更新为 0.86。
SOC从 0.48 更新为 0.63。
SOC从 0.22 更新为 0.48。
SOC从 0.38 更新为 0.55。
已断开电池: batt_ev_073
时间步 64: 电池 batt_ev_073 已离开，当前SOC: 83.3%，能量满足率: 70.7%
已断开电池: batt_ev_020
时间步 64: 电池 batt_ev_020 已离开，当前SOC: 73.3%，能量满足率: 68.9%
已断开电池: batt_ev_208
时间步 64 执行前: 电池 batt_ev_208 已充满 (SOC: 99.1%)，离开
已断开电池: batt_ev_091
时间步 64: 电池 batt_ev_091 已离开，当前SOC: 60.3%，能量满足率: 50.4%
奖励各项的值：powerloss=-0.2153531937010934, voltage=-0.321586042324542, ctrl=-0.0, connection=16.080000000000002, completion=3.1840796019900495, energy=7.650833202116637, transformer=0.
已连接电池 batt_ev_243, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 64 执行前: 排队电池 batt_ev_243 已接入
已连接电池 batt_ev_122, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=50.90909090909091。
功率需求: 60.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=29.09090909090909失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 72.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 48.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_074 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_012 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_122 充电的有无功功率为 50.90909090909091, -10.337531814094755
SOC从 0.70 更新为 0.81。
SOC从 0.12 更新为 0.37。
SOC从 0.47 更新为 0.65。
SOC从 0.28 更新为 0.59。
SOC从 0.86 更新为 0.93。
SOC从 0.63 更新为 0.78。
SOC从 0.48 更新为 0.70。
SOC从 0.55 更新为 0.72。
已断开电池: batt_ev_102
时间步 65: 电池 batt_ev_102 已离开，当前SOC: 93.0%，能量满足率: 90.0%
已断开电池: batt_ev_074
时间步 65 执行前: 电池 batt_ev_074 已充满 (SOC: 81.3%)，离开
已断开电池: batt_ev_012
时间步 65 执行前: 电池 batt_ev_012 已充满 (SOC: 77.7%)，离开
已断开电池: batt_ev_122
时间步 65: 电池 batt_ev_122 已离开，当前SOC: 59.0%，能量满足率: 44.4%
奖励各项的值：powerloss=-0.20802261187149107, voltage=-0.2933018748512928, ctrl=-0.0, connection=16.4, completion=3.2195121951219514, energy=7.66464884729332, transformer=0.
已连接电池 batt_ev_139, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 84kWh，并创BMS。
智能体的动作为: [25  1  1  0  2  1  1  1  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=47.27272727272727失败。
功率需求: 32.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.37 更新为 0.59。
SOC从 0.65 更新为 0.84。
SOC从 0.12 更新为 0.28。
SOC从 0.70 更新为 0.82。
SOC从 0.72 更新为 0.83。
奖励各项的值：powerloss=-0.2089258112106587, voltage=-0.1980860506550619, ctrl=-0.0, connection=16.4, completion=3.2195121951219514, energy=7.66464884729332, transformer=0.
已连接电池 batt_ev_004, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_019, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
智能体的动作为: [25  0  1  0  2  1  1  0  0  1  3]
初次设置charger_power=58.18181818181818。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=29.09090909090909失败。
功率需求: 40.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=54.54545454545455。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=36.36363636363636失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=47.27272727272727，设置charger_power=32.72727272727273失败。
功率需求: 32.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.52 更新为 0.73。
SOC从 0.59 更新为 0.76。
SOC从 0.84 更新为 0.97。
SOC从 0.28 更新为 0.44。
SOC从 0.08 更新为 0.23。
SOC从 0.82 更新为 0.93。
SOC从 0.83 更新为 0.95。
已断开电池: batt_ev_228
时间步 67: 电池 batt_ev_228 已离开，当前SOC: 93.0%，能量满足率: 93.4%
已断开电池: batt_ev_218
时间步 67 执行前: 电池 batt_ev_218 已充满 (SOC: 94.6%)，离开
已断开电池: batt_ev_243
时间步 67: 电池 batt_ev_243 已离开，当前SOC: 76.1%，能量满足率: 80.2%
奖励各项的值：powerloss=-0.2081281782827576, voltage=-0.12040860001770515, ctrl=-0.0, connection=16.64, completion=3.2211538461538463, energy=7.685654423550266, transformer=0.
智能体的动作为: [25  0  1  0  2  1  1  0  0  1  3]
已有历史设置self.charger_power=58.18181818181818，设置charger_power=43.63636363636363失败。
功率需求: 24.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=3.6363636363636362失败。
功率需求: 25.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 100.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.73 更新为 0.87。
SOC从 0.97 更新为 1.00。
SOC从 0.44 更新为 0.61。
SOC从 0.23 更新为 0.38。
已断开电池: batt_ev_061
时间步 68 执行前: 电池 batt_ev_061 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.19650783834087898, voltage=-0.09833713218860618, ctrl=-0.0, connection=16.72, completion=3.253588516746411, energy=7.696727847361031, transformer=0.
智能体的动作为: [25  0  1  1  2  1  1  0  0  1  3]
已有历史设置self.charger_power=58.18181818181818，设置charger_power=21.818181818181817失败。
功率需求: 15.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.87 更新为 0.96。
SOC从 0.61 更新为 0.75。
SOC从 0.38 更新为 0.53。
已断开电池: batt_ev_139
时间步 69: 电池 batt_ev_139 已离开，当前SOC: 75.0%，能量满足率: 73.3%
奖励各项的值：powerloss=-0.19466262560867376, voltage=-0.0496756955976152, ctrl=-0.0, connection=16.8, completion=3.238095238095238, energy=7.69496048330383, transformer=0.
已连接电池 batt_ev_177, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [25  3  1  1  2  1  1  0  0  1  3]
已有历史设置self.charger_power=58.18181818181818，设置charger_power=7.2727272727272725失败。
功率需求: 15.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=50.90909090909091。
功率需求: 64.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 50.91 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 50.90909090909091, -10.337531814094755
SOC从 0.96 更新为 1.00。
SOC从 0.38 更新为 0.60。
SOC从 0.53 更新为 0.68。
已断开电池: batt_ev_019
时间步 70 执行前: 电池 batt_ev_019 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.18373131498342712, voltage=-0.04204488842512566, ctrl=-0.0, connection=16.88, completion=3.2701421800947865, energy=7.705884841202863, transformer=0.
已连接电池 batt_ev_202, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_160, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [25  3  1  1  2  1  1  0  0  1  3]
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 48.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=58.18181818181818。
功率需求: 80.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
初次设置charger_power=58.18181818181818。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.60 更新为 0.80。
SOC从 0.68 更新为 0.83。
SOC从 0.48 更新为 0.67。
SOC从 0.18 更新为 0.53。
奖励各项的值：powerloss=-0.17249228342451467, voltage=-0.08139206355105788, ctrl=-0.0, connection=16.88, completion=3.2701421800947865, energy=7.705884841202863, transformer=0.
智能体的动作为: [25  0  1  0  2  1  1  0  0  1  3]
已有历史设置self.charger_power=50.90909090909091，设置charger_power=32.72727272727273失败。
功率需求: 32.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=32.72727272727273失败。
功率需求: 40.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=54.54545454545455失败。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.80 更新为 0.93。
SOC从 0.83 更新为 0.94。
SOC从 0.67 更新为 0.86。
SOC从 0.53 更新为 0.75。
已断开电池: batt_ev_004
时间步 72 执行前: 电池 batt_ev_004 已充满 (SOC: 93.9%)，离开
已断开电池: batt_ev_202
时间步 72 执行前: 电池 batt_ev_202 已充满 (SOC: 86.3%)，离开
奖励各项的值：powerloss=-0.1529207166465716, voltage=-0.133423629385514, ctrl=-0.0, connection=17.04, completion=3.333333333333333, energy=7.72742582860941, transformer=0.
已连接电池 batt_ev_099, 初始SOC: 68.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
已连接电池 batt_ev_100, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [25  0  1  1  2  1  1  0  0  1  3]
初次设置charger_power=54.54545454545455。
功率需求: 36.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=50.90909090909091，设置charger_power=10.909090909090908失败。
功率需求: 20.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=36.36363636363636失败。
功率需求: 24.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 80.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.68 更新为 0.81。
SOC从 0.93 更新为 1.00。
SOC从 0.75 更新为 0.90。
SOC从 0.18 更新为 0.42。
已断开电池: batt_ev_177
时间步 73 执行前: 电池 batt_ev_177 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_160
时间步 73: 电池 batt_ev_160 已离开，当前SOC: 90.1%，能量满足率: 90.1%
奖励各项的值：powerloss=-0.12570144451325072, voltage=-0.18098804794555834, ctrl=-0.0, connection=17.2, completion=3.3488372093023253, energy=7.7439574317919435, transformer=0.
智能体的动作为: [25  0  1  1  2  1  1  0  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=47.27272727272727失败。
功率需求: 24.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.81 更新为 0.90。
SOC从 0.42 更新为 0.65。
已断开电池: batt_ev_100
时间步 74: 电池 batt_ev_100 已离开，当前SOC: 65.0%，能量满足率: 63.6%
奖励各项的值：powerloss=-0.11661798154611754, voltage=-0.21401123431529, ctrl=-0.0, connection=17.28, completion=3.333333333333333, energy=7.737531754716969, transformer=0.
智能体的动作为: [30  3  1  1  2  1  1  0  0  1  0]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=21.818181818181817失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.90 更新为 0.96。
奖励各项的值：powerloss=-0.10927096603309434, voltage=-0.2416045323124738, ctrl=-0.0, connection=17.28, completion=3.333333333333333, energy=7.737531754716969, transformer=0.
智能体的动作为: [21  3 15  1  6  8  8  9 14  9  0]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=3.6363636363636362失败。
功率需求: 15.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_099
时间步 76 执行前: 电池 batt_ev_099 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.10902622492234568, voltage=-0.27046890337388607, ctrl=-0.0, connection=17.36, completion=3.3640552995391704, energy=7.747957875662973, transformer=0.
已连接电池 batt_ev_120, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [21  3 15  1  6  8  8  9 14  9  0]
初次设置charger_power=58.18181818181818。
功率需求: 120.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.18 更新为 0.36。
奖励各项的值：powerloss=-0.1117538339541631, voltage=-0.25099525070283013, ctrl=-0.0, connection=17.36, completion=3.3640552995391704, energy=7.747957875662973, transformer=0.
智能体的动作为: [30  3  2  1  2  8  0  3 14  9  0]
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.36 更新为 0.53。
奖励各项的值：powerloss=-0.11752196708316937, voltage=-0.24055710107596662, ctrl=-0.0, connection=17.36, completion=3.3640552995391704, energy=7.747957875662973, transformer=0.
已连接电池 batt_ev_035, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 77kWh，并创BMS。
智能体的动作为: [30  3  2  1  2  8  0  3 14  9  0]
初次设置charger_power=54.54545454545455。
功率需求: 64.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 72.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.48 更新为 0.66。
SOC从 0.53 更新为 0.71。
已断开电池: batt_ev_120
时间步 79: 电池 batt_ev_120 已离开，当前SOC: 71.2%，能量满足率: 66.5%
奖励各项的值：powerloss=-0.13776009294489447, voltage=-0.3580868297566209, ctrl=-0.0, connection=17.44, completion=3.3486238532110093, energy=7.742939552447244, transformer=0.
已连接电池 batt_ev_151, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
智能体的动作为: [25  3  1  1  2  1  0  0  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.54545454545455。
功率需求: 120.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.66 更新为 0.81。
SOC从 0.28 更新为 0.44。
奖励各项的值：powerloss=-0.15325390581157924, voltage=-0.39059128237587837, ctrl=-0.0, connection=17.44, completion=3.3486238532110093, energy=7.742939552447244, transformer=0.
智能体的动作为: [30  3  1  1  2  1  0  0  0  1  3]
已有历史设置self.charger_power=54.54545454545455，设置charger_power=40.0失败。
功率需求: 32.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=54.54545454545455，设置charger_power=54.54545454545455失败。
功率需求: 96.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 54.54545454545454, -11.07592694367295
SOC从 0.81 更新为 0.92。
SOC从 0.44 更新为 0.60。
已断开电池: batt_ev_035
时间步 81: 电池 batt_ev_035 已离开，当前SOC: 91.7%，能量满足率: 87.4%
已断开电池: batt_ev_151
时间步 81: 电池 batt_ev_151 已离开，当前SOC: 59.7%，能量满足率: 45.3%
奖励各项的值：powerloss=-0.16463565941425773, voltage=-0.34147690593447466, ctrl=-0.0, connection=17.6, completion=3.3181818181818183, energy=7.7328638465134345, transformer=0.
智能体的动作为: [30  3  1  1  2  1  0  0  0  1  0]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.16965050417630817, voltage=-0.298948762679101, ctrl=-0.0, connection=17.6, completion=3.3181818181818183, energy=7.7328638465134345, transformer=0.
智能体的动作为: [21  3 15  1  6  8  8  9 14  9  0]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.17849156007201275, voltage=-0.3390324503699582, ctrl=-0.0, connection=17.6, completion=3.3181818181818183, energy=7.7328638465134345, transformer=0.
已连接电池 batt_ev_056, 初始SOC: 62.0%, 最大功率: 80kW, 电池容量: 64kWh，并创BMS。
已连接电池 batt_ev_226, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [21  3 15  1  6  8  8  9 14  9  0]
初次设置charger_power=47.27272727272727。
功率需求: 48.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 47.27 kW。
初次设置charger_power=29.09090909090909。
功率需求: 60.00 kW, 充电桩功率: 29.09 kW, 最终充电功率: 29.09 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 47.27272727272727, -9.599136684516559
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 29.090909090909086, -5.907161036625574
SOC从 0.62 更新为 0.80。
SOC从 0.18 更新为 0.34。
奖励各项的值：powerloss=-0.18676338484791996, voltage=-0.34328806475505624, ctrl=-0.0, connection=17.6, completion=3.3181818181818183, energy=7.7328638465134345, transformer=0.
已连接电池 batt_ev_048, 初始SOC: 42.0%, 最大功率: 120kW, 电池容量: 93kWh，并创BMS。
智能体的动作为: [30  3  2  1  2  1  1  0  0  1  0]
已有历史设置self.charger_power=47.27272727272727，设置charger_power=36.36363636363636失败。
功率需求: 32.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=29.09090909090909，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 29.09 kW, 最终充电功率: 29.09 kW。
初次设置charger_power=58.18181818181818。
功率需求: 96.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 29.090909090909086, -5.907161036625574
已在 set_all_batteries_before_solve 中设置 batt_ev_048 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.80 更新为 0.93。
SOC从 0.34 更新为 0.50。
SOC从 0.42 更新为 0.58。
已断开电池: batt_ev_048
时间步 85: 电池 batt_ev_048 已离开，当前SOC: 57.6%，能量满足率: 27.9%
奖励各项的值：powerloss=-0.19443931331848696, voltage=-0.41595676147863303, ctrl=-0.0, connection=17.68, completion=3.3031674208144794, energy=7.710515045406331, transformer=0.
已连接电池 batt_ev_234, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_227, 初始SOC: 8.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
智能体的动作为: [25  3  1  1  2  1  1  0  0  1  3]
已有历史设置self.charger_power=47.27272727272727，设置charger_power=10.909090909090908失败。
功率需求: 20.00 kW, 充电桩功率: 47.27 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=50.90909090909091。
功率需求: 36.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=29.09090909090909，设置charger_power=54.54545454545455失败。
功率需求: 48.00 kW, 充电桩功率: 29.09 kW, 最终充电功率: 29.09 kW。
初次设置charger_power=58.18181818181818。
功率需求: 60.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 29.090909090909086, -5.907161036625574
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 58.18181818181817, -11.814322073251148
SOC从 0.93 更新为 1.00。
SOC从 0.57 更新为 0.71。
SOC从 0.50 更新为 0.65。
SOC从 0.08 更新为 0.39。
已断开电池: batt_ev_056
时间步 86 执行前: 电池 batt_ev_056 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_226
时间步 86: 电池 batt_ev_226 已离开，当前SOC: 65.4%，能量满足率: 74.1%
奖励各项的值：powerloss=-0.1963454210144882, voltage=-0.3926311412673811, ctrl=-0.0, connection=17.84, completion=3.3183856502242155, energy=7.719426516046086, transformer=0.
智能体的动作为: [25  0  1  1  2  1  1  0  0  1  3]
已有历史设置self.charger_power=50.90909090909091，设置charger_power=50.90909090909091失败。
功率需求: 24.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=58.18181818181818失败。
功率需求: 48.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.71 更新为 0.81。
SOC从 0.39 更新为 0.64。
奖励各项的值：powerloss=-0.19030351934638784, voltage=-0.34514459388951035, ctrl=-0.0, connection=17.84, completion=3.3183856502242155, energy=7.719426516046086, transformer=0.
智能体的动作为: [30  3  2  1  2  1  0  3 14  1  0]
已有历史设置self.charger_power=50.90909090909091，设置charger_power=43.63636363636363失败。
功率需求: 24.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=58.18181818181818，设置charger_power=7.2727272727272725失败。
功率需求: 36.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.81 更新为 0.90。
SOC从 0.64 更新为 0.84。
已断开电池: batt_ev_227
时间步 88: 电池 batt_ev_227 已离开，当前SOC: 83.6%，能量满足率: 84.0%
奖励各项的值：powerloss=-0.18656138700165817, voltage=-0.34587250214126675, ctrl=-0.0, connection=17.92, completion=3.3035714285714284, energy=7.72248378748851, transformer=0.
智能体的动作为: [21  3  2  1  2  8  0  3 14  9  0]
已有历史设置self.charger_power=50.90909090909091，设置charger_power=21.818181818181817失败。
功率需求: 15.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.90 更新为 0.96。
奖励各项的值：powerloss=-0.18587390451209712, voltage=-0.2816891952503586, ctrl=-0.0, connection=17.92, completion=3.3035714285714284, energy=7.72248378748851, transformer=0.
智能体的动作为: [21  3 15  1  6  8  8  9 14  9  0]
已有历史设置self.charger_power=50.90909090909091，设置charger_power=7.2727272727272725失败。
功率需求: 15.00 kW, 充电桩功率: 50.91 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_234
时间步 90 执行前: 电池 batt_ev_234 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.19973830610233295, voltage=-0.20601251890041583, ctrl=-0.0, connection=18.0, completion=3.333333333333333, energy=7.732606081766339, transformer=0.
智能体的动作为: [21  3 15  1  6  8  8  9 14  9  0]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.19617676491812283, voltage=-0.07846179495861305, ctrl=-0.0, connection=18.0, completion=3.333333333333333, energy=7.732606081766339, transformer=0.
智能体的动作为: [21  3 15  1  6  8  8  9 14  9  0]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.19009302252945393, voltage=-0.05499017312744492, ctrl=-0.0, connection=18.0, completion=3.333333333333333, energy=7.732606081766339, transformer=0.
已连接电池 batt_ev_238, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [21  3 15  1  6  8  8  9 14  9  0]
初次设置charger_power=25.454545454545453。
功率需求: 48.00 kW, 充电桩功率: 25.45 kW, 最终充电功率: 25.45 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 25.454545454545453, -5.168765907047377
SOC从 0.48 更新为 0.64。
奖励各项的值：powerloss=-0.19226239306797055, voltage=-0.019323487833671216, ctrl=-0.0, connection=18.0, completion=3.333333333333333, energy=7.732606081766339, transformer=0.
智能体的动作为: [21  3 15  1  6  8  8  9 14  9  0]
已有历史设置self.charger_power=25.454545454545453，设置charger_power=25.454545454545453失败。
功率需求: 36.00 kW, 充电桩功率: 25.45 kW, 最终充电功率: 25.45 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 25.454545454545453, -5.168765907047377
SOC从 0.64 更新为 0.79。
奖励各项的值：powerloss=-0.17970302440930086, voltage=-0.015720468497260054, ctrl=-0.0, connection=18.0, completion=3.333333333333333, energy=7.732606081766339, transformer=0.
智能体的动作为: [21  3 15  1  6  8  8  9 14  9  0]
已有历史设置self.charger_power=25.454545454545453，设置charger_power=25.454545454545453失败。
功率需求: 24.00 kW, 充电桩功率: 25.45 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.79 更新为 0.94。
已断开电池: batt_ev_238
时间步 95 执行前: 电池 batt_ev_238 已充满 (SOC: 93.7%)，离开
奖励各项的值：powerloss=-0.1627314437983647, voltage=-0.08495398012169142, ctrl=-0.0, connection=18.080000000000002, completion=3.36283185840708, energy=7.7426387982186995, transformer=0.
已连接电池 batt_ev_025, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
已连接电池 batt_ev_013, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 89kWh，并创BMS。
已连接电池 batt_ev_117, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 111kWh，并创BMS。
已连接电池 batt_ev_166, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 114kWh，并创BMS。
智能体的动作为: [21  3 15  1  6  8  8  9 14  9  0]
初次设置charger_power=3.6363636363636362。
功率需求: 60.00 kW, 充电桩功率: 3.64 kW, 最终充电功率: 3.64 kW。
初次设置charger_power=54.54545454545455。
功率需求: 72.00 kW, 充电桩功率: 54.55 kW, 最终充电功率: 54.55 kW。
初次设置charger_power=29.09090909090909。
功率需求: 120.00 kW, 充电桩功率: 29.09 kW, 最终充电功率: 29.09 kW。
初次设置charger_power=58.18181818181818。
功率需求: 120.00 kW, 充电桩功率: 58.18 kW, 最终充电功率: 58.18 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_025 充电的有无功功率为 3.636363636363636, -0.7383951295781968
已在 set_all_batteries_before_solve 中设置 batt_ev_013 充电的有无功功率为 58.18181818181817, -11.814322073251148
已在 set_all_batteries_before_solve 中设置 batt_ev_117 充电的有无功功率为 54.54545454545454, -11.07592694367295
已在 set_all_batteries_before_solve 中设置 batt_ev_166 充电的有无功功率为 29.090909090909086, -5.907161036625574
SOC从 0.12 更新为 0.14。
SOC从 0.52 更新为 0.64。
SOC从 0.28 更新为 0.34。
SOC从 0.18 更新为 0.34。
已断开电池: batt_ev_025
时间步 96: 电池 batt_ev_025 已离开，当前SOC: 13.9%，能量满足率: 2.2%
已断开电池: batt_ev_013
时间步 96: 电池 batt_ev_013 已离开，当前SOC: 34.3%，能量满足率: 20.4%
已断开电池: batt_ev_117
时间步 96: 电池 batt_ev_117 已离开，当前SOC: 64.3%，能量满足率: 26.7%
已断开电池: batt_ev_166
时间步 96: 电池 batt_ev_166 已离开，当前SOC: 34.4%，能量满足率: 9.1%
奖励各项的值：powerloss=-0.1502362427491059, voltage=-0.15406064544314813, ctrl=-0.9765, connection=18.400000000000002, completion=3.304347826086956, energy=7.6333836919792954, transformer=0.
调度记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250513_224309_13Bus_1000000\test_results_20250514_073953\schedule.csv
储能放电功率记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250513_224309_13Bus_1000000\test_results_20250514_073953\storage_schedule.csv
储能能量记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250513_224309_13Bus_1000000\test_results_20250514_073953\storage_energy.csv
已生成GIF动画，包含96步
测试完成 - 总奖励: 2081.0546
测试结果保存在: D:\LENOVO\Documents\Python\ML\powergym\results_20250513_224309_13Bus_1000000\test_results_20250514_073953
运行时间: 32238.10秒

进程已结束，退出代码为 0

```