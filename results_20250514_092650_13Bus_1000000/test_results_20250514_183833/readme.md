

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
已从D:\LENOVO\Documents\Python\ML\powergym\results_20250514_092650_13Bus_1000000\model\ppo_model加载模型
BatteryStationManager已重置
智能体的动作为: [30  4  8  5  2  6  0  4  1  0  7]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -87.5, -28.759859203150533
奖励各项的值：powerloss=-0.11528455066215637, voltage=-0.19392386168940234, ctrl=-0.0, connection=0.0, completion=0.0, energy=0.0, transformer=0.
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
智能体的动作为: [30  4  8  5  2  6  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 90.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 40.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 67.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -68.75, -22.59703223104685
已在 set_all_batteries_before_solve 中设置 batt_ev_030 充电的有无功功率为 90.0, -18.27527945706037
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 37.5, -7.614699773775154
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 67.5, -13.706459592795278
SOC从 0.18 更新为 0.43。
SOC从 0.32 更新为 0.46。
SOC从 0.18 更新为 0.33。
SOC从 0.12 更新为 0.33。
SOC从 0.22 更新为 0.40。
SOC从 0.28 更新为 0.55。
SOC从 0.12 更新为 0.50。
SOC从 0.38 更新为 0.68。
SOC从 0.22 更新为 0.55。
SOC从 0.12 更新为 0.35。
已断开电池: batt_ev_030
时间步 2 执行前: 电池 batt_ev_030 已充满 (SOC: 43.0%)，离开
超出专变安全限值
奖励各项的值：powerloss=-0.1545185473812124, voltage=-0.2504700478586619, ctrl=-0.0, connection=0.08, completion=10.0, energy=10.0, transformer=-1.6643965541900856.
已连接电池 batt_ev_224, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
时间步 2 执行前: 排队电池 batt_ev_224 已接入
智能体的动作为: [25  4  6  5  2  1  0  0  1  5  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 67.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 67.5, -13.706459592795278
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 45.0, -9.137639728530186
SOC从 0.28 更新为 0.53。
SOC从 0.46 更新为 0.65。
SOC从 0.33 更新为 0.48。
SOC从 0.33 更新为 0.54。
SOC从 0.40 更新为 0.68。
SOC从 0.55 更新为 0.82。
SOC从 0.50 更新为 0.89。
SOC从 0.68 更新为 0.98。
SOC从 0.55 更新为 0.78。
SOC从 0.35 更新为 0.59。
已断开电池: batt_ev_064
时间步 3 执行前: 电池 batt_ev_064 已充满 (SOC: 54.3%)，离开
已断开电池: batt_ev_239
时间步 3 执行前: 电池 batt_ev_239 已充满 (SOC: 82.3%)，离开
已断开电池: batt_ev_039
时间步 3: 电池 batt_ev_039 已离开，当前SOC: 88.9%，能量满足率: 89.4%
已断开电池: batt_ev_242
时间步 3 执行前: 电池 batt_ev_242 已充满 (SOC: 98.5%)，离开
已断开电池: batt_ev_045
时间步 3: 电池 batt_ev_045 已离开，当前SOC: 58.9%，能量满足率: 54.5%
超出专变安全限值
奖励各项的值：powerloss=-0.15362542725527994, voltage=-0.2643130885163636, ctrl=-0.0, connection=0.48, completion=6.666666666666666, energy=9.0658542039356, transformer=-2.9722582624974736.
时间步 3: 电池 batt_ev_092 已错过离开时间，无法接入
已连接电池 batt_ev_081, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 50kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_081 已接入
已连接电池 batt_ev_076, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_076 已接入
已连接电池 batt_ev_235, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_235 已接入
时间步 3: 电池 batt_ev_104 已错过离开时间，无法接入
已连接电池 batt_ev_018, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_018 已接入
已连接电池 batt_ev_062, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_062 已接入
智能体的动作为: [25  4  6  5  2  1  0  0  1  5  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 67.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 37.5, -7.614699773775154
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_235 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_062 充电的有无功功率为 67.5, -13.706459592795278
SOC从 0.53 更新为 0.78。
SOC从 0.65 更新为 0.83。
SOC从 0.48 更新为 0.63。
SOC从 0.12 更新为 0.47。
SOC从 0.68 更新为 0.96。
SOC从 0.28 更新为 0.53。
SOC从 0.62 更新为 0.94。
SOC从 0.32 更新为 0.55。
SOC从 0.78 更新为 0.99。
SOC从 0.57 更新为 0.79。
已断开电池: batt_ev_126
时间步 4: 电池 batt_ev_126 已离开，当前SOC: 63.5%，能量满足率: 56.9%
已断开电池: batt_ev_042
时间步 4 执行前: 电池 batt_ev_042 已充满 (SOC: 99.1%)，离开
已断开电池: batt_ev_235
时间步 4 执行前: 电池 batt_ev_235 已充满 (SOC: 93.9%)，离开
奖励各项的值：powerloss=-0.14467275528591222, voltage=-0.30455080089802467, ctrl=-0.0, connection=0.72, completion=6.666666666666666, energy=8.897865220924388, transformer=0.
时间步 4: 电池 batt_ev_200 已错过离开时间，无法接入
时间步 4: 电池 batt_ev_163 已错过离开时间，无法接入
已连接电池 batt_ev_014, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_014 已接入
已连接电池 batt_ev_180, 初始SOC: 8.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_180 已接入
已连接电池 batt_ev_036, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_036 已接入
智能体的动作为: [25  4  6  5  2  1  0  0  1  5  7]
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 55.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 7.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 82.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 7.5, -1.522939954755031
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 37.5, -7.614699773775154
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_062 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_014 充电的有无功功率为 55.0, -11.168226334870226
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 82.5, -16.75233950230534
SOC从 0.78 更新为 0.99。
SOC从 0.83 更新为 0.99。
SOC从 0.28 更新为 0.45。
SOC从 0.47 更新为 0.82。
SOC从 0.96 更新为 0.99。
SOC从 0.53 更新为 0.78。
SOC从 0.08 更新为 0.37。
SOC从 0.55 更新为 0.78。
SOC从 0.57 更新为 0.84。
SOC从 0.79 更新为 0.98。
已断开电池: batt_ev_149
时间步 5 执行前: 电池 batt_ev_149 已充满 (SOC: 99.0%)，离开
已断开电池: batt_ev_123
时间步 5 执行前: 电池 batt_ev_123 已充满 (SOC: 99.2%)，离开
已断开电池: batt_ev_224
时间步 5 执行前: 电池 batt_ev_224 已充满 (SOC: 98.8%)，离开
已断开电池: batt_ev_076
时间步 5: 电池 batt_ev_076 已离开，当前SOC: 78.0%，能量满足率: 71.4%
已断开电池: batt_ev_062
时间步 5 执行前: 电池 batt_ev_062 已充满 (SOC: 98.4%)，离开
奖励各项的值：powerloss=-0.14574237786010558, voltage=-0.3202325968366293, ctrl=-0.0, connection=1.12, completion=7.142857142857143, energy=9.087403152226901, transformer=0.
已连接电池 batt_ev_231, 初始SOC: 8.0%, 最大功率: 80kW, 电池容量: 62kWh，并创BMS。
时间步 5 执行前: 排队电池 batt_ev_231 已接入
已连接电池 batt_ev_067, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 5 执行前: 排队电池 batt_ev_067 已接入
已连接电池 batt_ev_248, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
时间步 5 执行前: 排队电池 batt_ev_248 已接入
已连接电池 batt_ev_240, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
时间步 5 执行前: 排队电池 batt_ev_240 已接入
已连接电池 batt_ev_119, 初始SOC: 72.0%, 最大功率: 100kW, 电池容量: 88kWh，并创BMS。
时间步 5 执行前: 排队电池 batt_ev_119 已接入
智能体的动作为: [25  4  6  5  2  1  0  0  1  5  7]
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 55.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 35.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 35.0, -7.107053122190145
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_014 充电的有无功功率为 55.0, -11.168226334870226
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_231 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 37.5, -7.614699773775154
已在 set_all_batteries_before_solve 中设置 batt_ev_248 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_119 充电的有无功功率为 56.25, -11.422049660662733
SOC从 0.08 更新为 0.32。
SOC从 0.32 更新为 0.48。
SOC从 0.45 更新为 0.63。
SOC从 0.82 更新为 0.99。
SOC从 0.22 更新为 0.45。
SOC从 0.48 更新为 0.91。
SOC从 0.37 更新为 0.67。
SOC从 0.78 更新为 1.00。
SOC从 0.84 更新为 0.98。
SOC从 0.72 更新为 0.88。
已断开电池: batt_ev_081
时间步 6 执行前: 电池 batt_ev_081 已充满 (SOC: 99.5%)，离开
已断开电池: batt_ev_018
时间步 6 执行前: 电池 batt_ev_018 已充满 (SOC: 99.6%)，离开
已断开电池: batt_ev_014
时间步 6: 电池 batt_ev_014 已离开，当前SOC: 62.8%，能量满足率: 58.0%
已断开电池: batt_ev_036
时间步 6 执行前: 电池 batt_ev_036 已充满 (SOC: 98.4%)，离开
已断开电池: batt_ev_231
时间步 6: 电池 batt_ev_231 已离开，当前SOC: 32.2%，能量满足率: 26.9%
已断开电池: batt_ev_248
时间步 6: 电池 batt_ev_248 已离开，当前SOC: 45.0%，能量满足率: 30.3%
已断开电池: batt_ev_119
时间步 6: 电池 batt_ev_119 已离开，当前SOC: 88.0%，能量满足率: 61.5%
奖励各项的值：powerloss=-0.1559541266314824, voltage=-0.34809688946035644, ctrl=-0.0, connection=1.68, completion=6.190476190476191, energy=8.328161700869106, transformer=0.
已连接电池 batt_ev_158, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_158 已接入
已连接电池 batt_ev_157, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_157 已接入
已连接电池 batt_ev_096, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_096 已接入
已连接电池 batt_ev_187, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_187 已接入
已连接电池 batt_ev_106, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 92kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_106 已接入
已连接电池 batt_ev_055, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_055 已接入
已连接电池 batt_ev_216, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_216 已接入
智能体的动作为: [25  4  6  5  2  1  0  0  1  5  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 22.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 37.5, -7.614699773775154
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 22.5, -4.568819864265093
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_157 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_187 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_106 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_216 充电的有无功功率为 33.75, -6.853229796397639
SOC从 0.28 更新为 0.52。
SOC从 0.48 更新为 0.63。
SOC从 0.12 更新为 0.31。
SOC从 0.18 更新为 0.43。
SOC从 0.57 更新为 0.80。
SOC从 0.91 更新为 0.99。
SOC从 0.67 更新为 0.96。
SOC从 0.32 更新为 0.63。
SOC从 0.28 更新为 0.46。
SOC从 0.42 更新为 0.58。
已断开电池: batt_ev_240
时间步 7 执行前: 电池 batt_ev_240 已充满 (SOC: 98.9%)，离开
已断开电池: batt_ev_157
时间步 7: 电池 batt_ev_157 已离开，当前SOC: 30.7%，能量满足率: 21.8%
已断开电池: batt_ev_187
时间步 7: 电池 batt_ev_187 已离开，当前SOC: 80.4%，能量满足率: 57.2%
奖励各项的值：powerloss=-0.16744467656974388, voltage=-0.3852196501099403, ctrl=-0.0, connection=1.92, completion=5.833333333333334, energy=8.03277278706817, transformer=0.
已连接电池 batt_ev_247, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 87kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_247 已接入
时间步 7: 电池 batt_ev_244 已错过离开时间，无法接入
已连接电池 batt_ev_090, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_090 已接入
已连接电池 batt_ev_128, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 80kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_128 已接入
智能体的动作为: [25  4  6  5  2  1  0  0  1  5  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 82.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 7.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 7.5, -1.522939954755031
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 37.5, -7.614699773775154
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_106 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_216 充电的有无功功率为 33.75, -6.853229796397639
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 82.5, -16.75233950230534
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_128 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.52 更新为 0.76。
SOC从 0.63 更新为 0.79。
SOC从 0.18 更新为 0.42。
SOC从 0.43 更新为 0.68。
SOC从 0.48 更新为 0.76。
SOC从 0.42 更新为 0.67。
SOC从 0.96 更新为 1.00。
SOC从 0.63 更新为 0.93。
SOC从 0.46 更新为 0.64。
SOC从 0.58 更新为 0.74。
已断开电池: batt_ev_180
时间步 8 执行前: 电池 batt_ev_180 已充满 (SOC: 99.9%)，离开
已断开电池: batt_ev_067
时间步 8: 电池 batt_ev_067 已离开，当前SOC: 78.9%，能量满足率: 71.0%
已断开电池: batt_ev_158
时间步 8 执行前: 电池 batt_ev_158 已充满 (SOC: 75.9%)，离开
已断开电池: batt_ev_106
时间步 8: 电池 batt_ev_106 已离开，当前SOC: 93.1%，能量满足率: 92.6%
已断开电池: batt_ev_216
时间步 8: 电池 batt_ev_216 已离开，当前SOC: 73.8%，能量满足率: 56.9%
超出专变安全限值
奖励各项的值：powerloss=-0.18883175648045006, voltage=-0.38757153073692097, ctrl=-0.0, connection=2.32, completion=5.517241379310345, energy=8.097743115958039, transformer=-2.269296079879962.
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
智能体的动作为: [25  4  6  5  2  1  0  0  1  5  7]
功率需求已禁用，直接使用桩侧设置功率: 90.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 62.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 82.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 90.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 82.5, -16.75233950230534
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 90.0, -18.27527945706037
已在 set_all_batteries_before_solve 中设置 batt_ev_128 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 90.0, -18.27527945706037
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 62.5, -12.691166289625256
已在 set_all_batteries_before_solve 中设置 batt_ev_173 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_132 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 56.25, -11.422049660662733
SOC从 0.72 更新为 0.98。
SOC从 0.22 更新为 0.38。
SOC从 0.42 更新为 0.65。
SOC从 0.68 更新为 0.94。
SOC从 0.76 更新为 0.99。
SOC从 0.67 更新为 0.92。
SOC从 0.57 更新为 0.95。
SOC从 0.18 更新为 0.45。
SOC从 0.64 更新为 0.82。
SOC从 0.08 更新为 0.26。
已断开电池: batt_ev_096
时间步 9 执行前: 电池 batt_ev_096 已充满 (SOC: 93.7%)，离开
已断开电池: batt_ev_055
时间步 9: 电池 batt_ev_055 已离开，当前SOC: 82.3%，能量满足率: 77.5%
已断开电池: batt_ev_247
时间步 9: 电池 batt_ev_247 已离开，当前SOC: 65.4%，能量满足率: 59.3%
已断开电池: batt_ev_090
时间步 9 执行前: 电池 batt_ev_090 已充满 (SOC: 98.6%)，离开
已断开电池: batt_ev_128
时间步 9: 电池 batt_ev_128 已离开，当前SOC: 92.0%，能量满足率: 89.3%
已断开电池: batt_ev_220
时间步 9 执行前: 电池 batt_ev_220 已充满 (SOC: 98.5%)，离开
已断开电池: batt_ev_173
时间步 9: 电池 batt_ev_173 已离开，当前SOC: 95.5%，能量满足率: 93.8%
已断开电池: batt_ev_132
时间步 9: 电池 batt_ev_132 已离开，当前SOC: 44.5%，能量满足率: 33.2%
超出专变安全限值
奖励各项的值：powerloss=-0.21338719023991415, voltage=-0.47774625621953115, ctrl=-0.0, connection=2.96, completion=5.135135135135135, energy=8.11189722002622, transformer=-7.691132065605615.
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
已连接电池 batt_ev_000, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 80kWh，并创BMS。
已连接电池 batt_ev_008, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 60kWh，并创BMS。
智能体的动作为: [25  4  6  5  2  1  0  0  1  5  7]
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 62.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 55.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 55.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 62.5, -12.691166289625256
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_191 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 55.0, -11.168226334870226
已在 set_all_batteries_before_solve 中设置 batt_ev_161 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_008 充电的有无功功率为 55.0, -11.168226334870226
SOC从 0.18 更新为 0.40。
SOC从 0.38 更新为 0.55。
SOC从 0.22 更新为 0.43。
SOC从 0.22 更新为 0.46。
SOC从 0.82 更新为 0.98。
SOC从 0.28 更新为 0.57。
SOC从 0.38 更新为 0.67。
SOC从 0.18 更新为 0.41。
SOC从 0.68 更新为 0.91。
SOC从 0.26 更新为 0.44。
已断开电池: batt_ev_150
时间步 10: 电池 batt_ev_150 已离开，当前SOC: 44.1%，能量满足率: 40.1%
已断开电池: batt_ev_191
时间步 10: 电池 batt_ev_191 已离开，当前SOC: 39.6%，能量满足率: 26.9%
已断开电池: batt_ev_161
时间步 10: 电池 batt_ev_161 已离开，当前SOC: 46.3%，能量满足率: 32.0%
已断开电池: batt_ev_008
时间步 10 执行前: 电池 batt_ev_008 已充满 (SOC: 90.9%)，离开
超出专变安全限值
奖励各项的值：powerloss=-0.22297426397591624, voltage=-0.4588657834177279, ctrl=-0.0, connection=3.2800000000000002, completion=4.878048780487805, energy=7.80580390436864, transformer=-5.395267997976635.
已连接电池 batt_ev_162, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_162 已接入
已连接电池 batt_ev_170, 初始SOC: 42.0%, 最大功率: 120kW, 电池容量: 99kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_170 已接入
已连接电池 batt_ev_085, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_085 已接入
已连接电池 batt_ev_222, 初始SOC: 8.0%, 最大功率: 80kW, 电池容量: 56kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 55.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 105.00 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 55.0, -11.168226334870226
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 105.0, -21.32115936657043
已在 set_all_batteries_before_solve 中设置 batt_ev_085 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_222 充电的有无功功率为 45.0, -9.137639728530186
SOC从 0.28 更新为 0.45。
SOC从 0.55 更新为 0.68。
SOC从 0.43 更新为 0.63。
SOC从 0.42 更新为 0.69。
SOC从 0.98 更新为 0.98。
SOC从 0.57 更新为 0.86。
SOC从 0.67 更新为 0.97。
SOC从 0.41 更新为 0.65。
SOC从 0.62 更新为 0.99。
SOC从 0.08 更新为 0.28。
已断开电池: batt_ev_016
时间步 11: 电池 batt_ev_016 已离开，当前SOC: 68.0%，能量满足率: 60.6%
已断开电池: batt_ev_193
时间步 11: 电池 batt_ev_193 已离开，当前SOC: 63.0%，能量满足率: 54.0%
已断开电池: batt_ev_186
时间步 11: 电池 batt_ev_186 已离开，当前SOC: 98.1%，能量满足率: 89.3%
已断开电池: batt_ev_085
时间步 11 执行前: 电池 batt_ev_085 已充满 (SOC: 98.6%)，离开
已断开电池: batt_ev_222
时间步 11: 电池 batt_ev_222 已离开，当前SOC: 28.1%，能量满足率: 22.3%
超出专变安全限值
奖励各项的值：powerloss=-0.22963377147251868, voltage=-0.494158464606842, ctrl=-0.0, connection=3.68, completion=4.565217391304348, energy=7.666466837972706, transformer=-2.396999821234516.
已连接电池 batt_ev_114, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_114 已接入
已连接电池 batt_ev_009, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_009 已接入
已连接电池 batt_ev_113, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_065, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_203, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 82.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 105.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 43.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 6.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 43.75, -8.88381640273768
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 6.25, -1.2691166289625255
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 105.0, -21.32115936657043
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 82.5, -16.75233950230534
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 33.75, -6.853229796397639
SOC从 0.45 更新为 0.63。
SOC从 0.92 更新为 0.99。
SOC从 0.18 更新为 0.38。
SOC从 0.69 更新为 0.95。
SOC从 0.28 更新为 0.65。
SOC从 0.86 更新为 0.99。
SOC从 0.97 更新为 0.99。
SOC从 0.65 更新为 0.88。
SOC从 0.62 更新为 0.90。
SOC从 0.28 更新为 0.47。
已断开电池: batt_ev_194
时间步 12 执行前: 电池 batt_ev_194 已充满 (SOC: 98.9%)，离开
已断开电池: batt_ev_078
时间步 12 执行前: 电池 batt_ev_078 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_170
时间步 12: 电池 batt_ev_170 已离开，当前SOC: 95.0%，能量满足率: 94.7%
奖励各项的值：powerloss=-0.22941432193963113, voltage=-0.5111824143437427, ctrl=-0.0, connection=3.92, completion=4.6938775510204085, energy=7.7985137044171715, transformer=0.
已连接电池 batt_ev_011, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 12 执行前: 排队电池 batt_ev_011 已接入
已连接电池 batt_ev_041, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_232, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 82.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 105.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 35.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 18.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 35.0, -7.107053122190145
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 82.5, -16.75233950230534
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 105.0, -21.32115936657043
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 18.75, -3.807349886887577
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 33.75, -6.853229796397639
已在 set_all_batteries_before_solve 中设置 batt_ev_011 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.63 更新为 0.80。
SOC从 0.99 更新为 0.99。
SOC从 0.38 更新为 0.58。
SOC从 0.32 更新为 0.57。
SOC从 0.65 更新为 0.99。
SOC从 0.12 更新为 0.49。
SOC从 0.38 更新为 0.61。
SOC从 0.88 更新为 0.99。
SOC从 0.90 更新为 0.98。
SOC从 0.47 更新为 0.66。
已断开电池: batt_ev_000
时间步 13 执行前: 电池 batt_ev_000 已充满 (SOC: 99.2%)，离开
已断开电池: batt_ev_162
时间步 13: 电池 batt_ev_162 已离开，当前SOC: 79.9%，能量满足率: 74.2%
已断开电池: batt_ev_113
时间步 13 执行前: 电池 batt_ev_113 已充满 (SOC: 98.6%)，离开
已断开电池: batt_ev_065
时间步 13 执行前: 电池 batt_ev_065 已充满 (SOC: 98.5%)，离开
已断开电池: batt_ev_011
时间步 13: 电池 batt_ev_011 已离开，当前SOC: 57.0%，能量满足率: 37.9%
奖励各项的值：powerloss=-0.23153587248390212, voltage=-0.5503368711977075, ctrl=-0.0, connection=4.32, completion=4.814814814814815, energy=7.839493198553752, transformer=0.
已连接电池 batt_ev_237, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_237 已接入
已连接电池 batt_ev_052, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_052 已接入
已连接电池 batt_ev_206, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 62kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_206 已接入
已连接电池 batt_ev_172, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
已连接电池 batt_ev_229, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 82.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 82.5, -16.75233950230534
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 33.75, -6.853229796397639
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_052 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_206 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.78 更新为 0.94。
SOC从 0.99 更新为 0.99。
SOC从 0.58 更新为 0.78。
SOC从 0.38 更新为 0.60。
SOC从 0.22 更新为 0.45。
SOC从 0.49 更新为 0.86。
SOC从 0.61 更新为 0.84。
SOC从 0.38 更新为 0.73。
SOC从 0.38 更新为 0.63。
SOC从 0.66 更新为 0.86。
已断开电池: batt_ev_114
时间步 14: 电池 batt_ev_114 已离开，当前SOC: 99.4%，能量满足率: 91.9%
已断开电池: batt_ev_203
时间步 14: 电池 batt_ev_203 已离开，当前SOC: 85.5%，能量满足率: 82.2%
已断开电池: batt_ev_206
时间步 14: 电池 batt_ev_206 已离开，当前SOC: 44.7%，能量满足率: 37.8%
奖励各项的值：powerloss=-0.22892011063832732, voltage=-0.5460874784716552, ctrl=-0.0, connection=4.5600000000000005, completion=4.56140350877193, energy=7.7986694439604065, transformer=0.
已连接电池 batt_ev_164, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_164 已接入
已连接电池 batt_ev_134, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_214, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 80kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 82.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 82.5, -16.75233950230534
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 37.5, -7.614699773775154
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_052 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 56.25, -11.422049660662733
SOC从 0.94 更新为 1.00。
SOC从 0.42 更新为 0.55。
SOC从 0.78 更新为 0.98。
SOC从 0.60 更新为 0.82。
SOC从 0.32 更新为 0.67。
SOC从 0.86 更新为 1.00。
SOC从 0.84 更新为 0.99。
SOC从 0.73 更新为 0.99。
SOC从 0.63 更新为 0.88。
SOC从 0.48 更新为 0.66。
已断开电池: batt_ev_009
时间步 15 执行前: 电池 batt_ev_009 已充满 (SOC: 98.1%)，离开
已断开电池: batt_ev_041
时间步 15 执行前: 电池 batt_ev_041 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_232
时间步 15 执行前: 电池 batt_ev_232 已充满 (SOC: 98.6%)，离开
已断开电池: batt_ev_237
时间步 15 执行前: 电池 batt_ev_237 已充满 (SOC: 99.7%)，离开
已断开电池: batt_ev_052
时间步 15 执行前: 电池 batt_ev_052 已充满 (SOC: 81.8%)，离开
已断开电池: batt_ev_172
时间步 15 执行前: 电池 batt_ev_172 已充满 (SOC: 98.9%)，离开
已断开电池: batt_ev_229
时间步 15 执行前: 电池 batt_ev_229 已充满 (SOC: 88.0%)，离开
奖励各项的值：powerloss=-0.22501823633183504, voltage=-0.538799765502691, ctrl=-0.0, connection=5.12, completion=5.15625, energy=8.039439973527237, transformer=0.
已连接电池 batt_ev_143, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_143 已接入
已连接电池 batt_ev_245, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_245 已接入
已连接电池 batt_ev_098, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_098 已接入
已连接电池 batt_ev_190, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 63kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_190 已接入
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.48 更新为 0.73。
SOC从 0.55 更新为 0.68。
SOC从 0.38 更新为 0.54。
SOC从 0.42 更新为 0.67。
SOC从 0.67 更新为 0.99。
SOC从 0.18 更新为 0.58。
SOC从 0.66 更新为 0.83。
已断开电池: batt_ev_134
时间步 16 执行前: 电池 batt_ev_134 已充满 (SOC: 99.1%)，离开
奖励各项的值：powerloss=-0.22094084751686965, voltage=-0.5318106666844202, ctrl=-0.0, connection=5.2, completion=5.230769230769231, energy=8.069602435472973, transformer=0.
已连接电池 batt_ev_069, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 56kWh，并创BMS。
已连接电池 batt_ev_071, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 93.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 93.75, -19.03674943443788
SOC从 0.73 更新为 0.99。
SOC从 0.68 更新为 0.81。
SOC从 0.54 更新为 0.69。
SOC从 0.67 更新为 0.92。
SOC从 0.58 更新为 0.97。
SOC从 0.38 更新为 0.65。
SOC从 0.42 更新为 0.66。
SOC从 0.83 更新为 0.99。
已断开电池: batt_ev_214
时间步 17 执行前: 电池 batt_ev_214 已充满 (SOC: 98.8%)，离开
已断开电池: batt_ev_143
时间步 17 执行前: 电池 batt_ev_143 已充满 (SOC: 98.8%)，离开
已断开电池: batt_ev_245
时间步 17: 电池 batt_ev_245 已离开，当前SOC: 69.2%，能量满足率: 52.1%
已断开电池: batt_ev_190
时间步 17 执行前: 电池 batt_ev_190 已充满 (SOC: 97.4%)，离开
奖励各项的值：powerloss=-0.2288033815419098, voltage=-0.5097485493997356, ctrl=-0.0, connection=5.5200000000000005, completion=5.362318840579711, energy=8.112046797287157, transformer=0.
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 20.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 93.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 93.75, -19.03674943443788
SOC从 0.81 更新为 0.95。
SOC从 0.92 更新为 0.99。
SOC从 0.65 更新为 0.92。
SOC从 0.66 更新为 0.91。
已断开电池: batt_ev_098
时间步 18 执行前: 电池 batt_ev_098 已充满 (SOC: 99.1%)，离开
已断开电池: batt_ev_071
时间步 18 执行前: 电池 batt_ev_071 已充满 (SOC: 90.8%)，离开
奖励各项的值：powerloss=-0.21821157296449986, voltage=-0.3397758850121746, ctrl=-0.0, connection=5.68, completion=5.492957746478874, energy=8.165228577645266, transformer=0.
已连接电池 batt_ev_083, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_174, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_167, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 11.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 18.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 65.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 11.25, -2.2844099321325464
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 18.75, -3.807349886887577
已在 set_all_batteries_before_solve 中设置 batt_ev_083 充电的有无功功率为 65.0, -13.198812941210267
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 45.0, -9.137639728530186
SOC从 0.32 更新为 0.54。
SOC从 0.95 更新为 1.00。
SOC从 0.18 更新为 0.46。
SOC从 0.92 更新为 1.00。
SOC从 0.68 更新为 0.98。
已断开电池: batt_ev_164
时间步 19 执行前: 电池 batt_ev_164 已充满 (SOC: 99.6%)，离开
已断开电池: batt_ev_069
时间步 19 执行前: 电池 batt_ev_069 已充满 (SOC: 99.9%)，离开
已断开电池: batt_ev_083
时间步 19 执行前: 电池 batt_ev_083 已充满 (SOC: 98.1%)，离开
奖励各项的值：powerloss=-0.21259365430402816, voltage=-0.21336978034160348, ctrl=-0.0, connection=5.92, completion=5.675675675675675, energy=8.239611202875864, transformer=0.
已连接电池 batt_ev_115, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
已连接电池 batt_ev_181, 初始SOC: 56.99999999999999%, 最大功率: 80kW, 电池容量: 69kWh，并创BMS。
已连接电池 batt_ev_182, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 95kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 67.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 67.5, -13.706459592795278
SOC从 0.54 更新为 0.76。
SOC从 0.12 更新为 0.34。
SOC从 0.46 更新为 0.75。
SOC从 0.57 更新为 0.86。
SOC从 0.28 更新为 0.46。
奖励各项的值：powerloss=-0.20898255311840297, voltage=-0.15788095842131034, ctrl=-0.0, connection=5.92, completion=5.675675675675675, energy=8.239611202875864, transformer=0.
已连接电池 batt_ev_037, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_138, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
已连接电池 batt_ev_095, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
智能体的动作为: [25  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 65.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 35.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 67.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 65.0, -13.198812941210267
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 35.0, -7.107053122190145
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 67.5, -13.706459592795278
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_138 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 30.0, -6.091759819020124
SOC从 0.76 更新为 0.98。
SOC从 0.12 更新为 0.28。
SOC从 0.34 更新为 0.57。
SOC从 0.32 更新为 0.59。
SOC从 0.75 更新为 0.99。
SOC从 0.86 更新为 0.99。
SOC从 0.48 更新为 0.81。
SOC从 0.46 更新为 0.64。
已断开电池: batt_ev_174
时间步 21 执行前: 电池 batt_ev_174 已充满 (SOC: 99.4%)，离开
已断开电池: batt_ev_167
时间步 21 执行前: 电池 batt_ev_167 已充满 (SOC: 98.2%)，离开
已断开电池: batt_ev_181
时间步 21 执行前: 电池 batt_ev_181 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_138
时间步 21 执行前: 电池 batt_ev_138 已充满 (SOC: 80.7%)，离开
奖励各项的值：powerloss=-0.21311013861938996, voltage=-0.11539445872293275, ctrl=-0.0, connection=6.24, completion=5.897435897435898, energy=8.329887551446332, transformer=0.
已连接电池 batt_ev_197, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 75kWh，并创BMS。
已连接电池 batt_ev_026, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 102kWh，并创BMS。
已连接电池 batt_ev_212, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_010, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 71kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 67.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 67.5, -13.706459592795278
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_212 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 112.5, -22.844099321325466
SOC从 0.22 更新为 0.43。
SOC从 0.28 更新为 0.43。
SOC从 0.57 更新为 0.79。
SOC从 0.59 更新为 0.86。
SOC从 0.48 更新为 0.88。
SOC从 0.52 更新为 0.79。
SOC从 0.32 更新为 0.61。
SOC从 0.64 更新为 0.81。
已断开电池: batt_ev_182
时间步 22: 电池 batt_ev_182 已离开，当前SOC: 81.3%，能量满足率: 76.1%
已断开电池: batt_ev_010
时间步 22 执行前: 电池 batt_ev_010 已充满 (SOC: 87.6%)，离开
奖励各项的值：powerloss=-0.21149212167460285, voltage=-0.10434882035749382, ctrl=-0.0, connection=6.4, completion=5.875, energy=8.341809535592503, transformer=0.
已连接电池 batt_ev_241, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 68kWh，并创BMS。
已连接电池 batt_ev_084, 初始SOC: 78.0%, 最大功率: 100kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_038, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
已连接电池 batt_ev_040, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 35.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 37.5, -7.614699773775154
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 35.0, -7.107053122190145
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_212 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_084 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 33.75, -6.853229796397639
SOC从 0.43 更新为 0.64。
SOC从 0.43 更新为 0.59。
SOC从 0.79 更新为 1.00。
SOC从 0.86 更新为 0.99。
SOC从 0.42 更新为 0.74。
SOC从 0.48 更新为 0.70。
SOC从 0.79 更新为 0.99。
SOC从 0.78 更新为 0.98。
SOC从 0.61 更新为 0.91。
SOC从 0.78 更新为 0.93。
已断开电池: batt_ev_115
时间步 23 执行前: 电池 batt_ev_115 已充满 (SOC: 99.6%)，离开
已断开电池: batt_ev_037
时间步 23 执行前: 电池 batt_ev_037 已充满 (SOC: 99.3%)，离开
已断开电池: batt_ev_197
时间步 23 执行前: 电池 batt_ev_197 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_212
时间步 23: 电池 batt_ev_212 已离开，当前SOC: 63.7%，能量满足率: 54.8%
已断开电池: batt_ev_084
时间步 23 执行前: 电池 batt_ev_084 已充满 (SOC: 98.2%)，离开
奖励各项的值：powerloss=-0.19246418824207842, voltage=-0.11800050136165918, ctrl=-0.0, connection=6.8, completion=6.0, energy=8.386202576326484, transformer=0.
已连接电池 batt_ev_046, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_046 已接入
已连接电池 batt_ev_050, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_050 已接入
已连接电池 batt_ev_125, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
已连接电池 batt_ev_137, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 84kWh，并创BMS。
已连接电池 batt_ev_221, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 75kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 55.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 55.0, -11.168226334870226
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_046 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_050 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_125 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 112.5, -22.844099321325466
SOC从 0.42 更新为 0.65。
SOC从 0.59 更新为 0.74。
SOC从 0.28 更新为 0.49。
SOC从 0.28 更新为 0.48。
SOC从 0.74 更新为 0.98。
SOC从 0.70 更新为 0.92。
SOC从 0.52 更新为 0.76。
SOC从 0.28 更新为 0.66。
SOC从 0.91 更新为 0.98。
SOC从 0.93 更新为 0.99。
已断开电池: batt_ev_026
时间步 24 执行前: 电池 batt_ev_026 已充满 (SOC: 98.2%)，离开
已断开电池: batt_ev_241
时间步 24 执行前: 电池 batt_ev_241 已充满 (SOC: 92.1%)，离开
已断开电池: batt_ev_038
时间步 24 执行前: 电池 batt_ev_038 已充满 (SOC: 98.0%)，离开
已断开电池: batt_ev_040
时间步 24 执行前: 电池 batt_ev_040 已充满 (SOC: 99.4%)，离开
奖励各项的值：powerloss=-0.1746651916697416, voltage=-0.19105386234240074, ctrl=-0.0, connection=7.12, completion=6.179775280898876, energy=8.45873279761518, transformer=0.
已连接电池 batt_ev_109, 初始SOC: 88.0%, 最大功率: 100kW, 电池容量: 70kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_109 已接入
已连接电池 batt_ev_034, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 68kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_034 已接入
已连接电池 batt_ev_141, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 75kWh，并创BMS。
已连接电池 batt_ev_101, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 68kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 31.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 97.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_046 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_050 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_125 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 97.5, -19.798219411815403
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 31.25, -6.345583144812628
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_141 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 45.0, -9.137639728530186
SOC从 0.65 更新为 0.88。
SOC从 0.74 更新为 0.90。
SOC从 0.49 更新为 0.71。
SOC从 0.48 更新为 0.67。
SOC从 0.88 更新为 0.99。
SOC从 0.22 更新为 0.51。
SOC从 0.76 更新为 1.00。
SOC从 0.66 更新为 0.98。
SOC从 0.28 更新为 0.68。
SOC从 0.22 更新为 0.39。
已断开电池: batt_ev_095
时间步 25: 电池 batt_ev_095 已离开，当前SOC: 90.1%，能量满足率: 90.8%
已断开电池: batt_ev_046
时间步 25: 电池 batt_ev_046 已离开，当前SOC: 87.9%，能量满足率: 82.0%
已断开电池: batt_ev_050
时间步 25: 电池 batt_ev_050 已离开，当前SOC: 71.0%，能量满足率: 71.6%
已断开电池: batt_ev_125
时间步 25: 电池 batt_ev_125 已离开，当前SOC: 67.2%，能量满足率: 61.2%
已断开电池: batt_ev_137
时间步 25 执行前: 电池 batt_ev_137 已充满 (SOC: 99.6%)，离开
已断开电池: batt_ev_221
时间步 25 执行前: 电池 batt_ev_221 已充满 (SOC: 98.0%)，离开
超出专变安全限值
奖励各项的值：powerloss=-0.15848259231811535, voltage=-0.24984778049286227, ctrl=-0.0, connection=7.6000000000000005, completion=6.0, energy=8.456789675310993, transformer=-1.761199952975295.
已连接电池 batt_ev_075, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_075 已接入
已连接电池 batt_ev_093, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_093 已接入
已连接电池 batt_ev_047, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 56kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_047 已接入
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 90.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_141 充电的有无功功率为 90.0, -18.27527945706037
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_075 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 41.25, -8.37616975115267
SOC从 0.42 更新为 0.63。
SOC从 0.38 更新为 0.54。
SOC从 0.38 更新为 0.56。
SOC从 0.99 更新为 0.99。
SOC从 0.51 更新为 0.81。
SOC从 0.68 更新为 0.98。
SOC从 0.39 更新为 0.55。
已断开电池: batt_ev_141
时间步 26 执行前: 电池 batt_ev_141 已充满 (SOC: 98.0%)，离开
已断开电池: batt_ev_075
时间步 26 执行前: 电池 batt_ev_075 已充满 (SOC: 62.6%)，离开
奖励各项的值：powerloss=-0.1347931603361807, voltage=-0.2595757934458276, ctrl=-0.0, connection=7.76, completion=6.082474226804123, energy=8.48860844489221, transformer=0.
已连接电池 batt_ev_031, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_057, 初始SOC: 8.0%, 最大功率: 80kW, 电池容量: 73kWh，并创BMS。
已连接电池 batt_ev_111, 初始SOC: 68.0%, 最大功率: 100kW, 电池容量: 83kWh，并创BMS。
已连接电池 batt_ev_006, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
已连接电池 batt_ev_225, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 94kWh，并创BMS。
智能体的动作为: [25  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 93.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_031 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 93.75, -19.03674943443788
已在 set_all_batteries_before_solve 中设置 batt_ev_006 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_225 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.57 更新为 0.76。
SOC从 0.54 更新为 0.71。
SOC从 0.56 更新为 0.75。
SOC从 0.42 更新为 0.74。
SOC从 0.99 更新为 0.99。
SOC从 0.81 更新为 0.99。
SOC从 0.08 更新为 0.35。
SOC从 0.68 更新为 0.96。
SOC从 0.52 更新为 0.84。
SOC从 0.55 更新为 0.72。
已断开电池: batt_ev_034
时间步 27 执行前: 电池 batt_ev_034 已充满 (SOC: 99.2%)，离开
已断开电池: batt_ev_031
时间步 27 执行前: 电池 batt_ev_031 已充满 (SOC: 74.4%)，离开
超出专变安全限值
奖励各项的值：powerloss=-0.1471068876740921, voltage=-0.30018734412167847, ctrl=-0.0, connection=7.92, completion=6.161616161616161, energy=8.519141607621659, transformer=-0.357877703082022.
已连接电池 batt_ev_054, 初始SOC: 82.0%, 最大功率: 120kW, 电池容量: 85kWh，并创BMS。
已连接电池 batt_ev_129, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 94kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 6.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 6.25, -1.2691166289625255
已在 set_all_batteries_before_solve 中设置 batt_ev_006 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_225 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.76 更新为 0.95。
SOC从 0.71 更新为 0.87。
SOC从 0.75 更新为 0.93。
SOC从 0.82 更新为 1.00。
SOC从 0.99 更新为 0.99。
SOC从 0.28 更新为 0.55。
SOC从 0.35 更新为 0.63。
SOC从 0.96 更新为 0.98。
SOC从 0.84 更新为 1.00。
SOC从 0.72 更新为 0.88。
已断开电池: batt_ev_109
时间步 28: 电池 batt_ev_109 已离开，当前SOC: 99.2%，能量满足率: 93.0%
已断开电池: batt_ev_047
时间步 28: 电池 batt_ev_047 已离开，当前SOC: 93.2%，能量满足率: 92.1%
已断开电池: batt_ev_111
时间步 28 执行前: 电池 batt_ev_111 已充满 (SOC: 98.1%)，离开
已断开电池: batt_ev_006
时间步 28 执行前: 电池 batt_ev_006 已充满 (SOC: 94.5%)，离开
已断开电池: batt_ev_225
时间步 28 执行前: 电池 batt_ev_225 已充满 (SOC: 99.9%)，离开
奖励各项的值：powerloss=-0.13778300102910163, voltage=-0.2823072874013244, ctrl=-0.0, connection=8.32, completion=6.153846153846154, energy=8.57594226293289, transformer=0.
已连接电池 batt_ev_088, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 50kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_088 已接入
已连接电池 batt_ev_007, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 84kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_007 已接入
已连接电池 batt_ev_142, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_142 已接入
已连接电池 batt_ev_147, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_147 已接入
已连接电池 batt_ev_079, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 78kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 37.5, -7.614699773775154
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_007 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_147 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.38 更新为 0.60。
SOC从 0.87 更新为 1.00。
SOC从 0.32 更新为 0.52。
SOC从 1.00 更新为 1.00。
SOC从 0.32 更新为 0.60。
SOC从 0.55 更新为 0.81。
SOC从 0.63 更新为 0.90。
SOC从 0.52 更新为 0.75。
SOC从 0.08 更新为 0.40。
SOC从 0.88 更新为 0.99。
已断开电池: batt_ev_101
时间步 29 执行前: 电池 batt_ev_101 已充满 (SOC: 99.2%)，离开
已断开电池: batt_ev_093
时间步 29 执行前: 电池 batt_ev_093 已充满 (SOC: 99.7%)，离开
已断开电池: batt_ev_057
时间步 29 执行前: 电池 batt_ev_057 已充满 (SOC: 90.2%)，离开
已断开电池: batt_ev_147
时间步 29 执行前: 电池 batt_ev_147 已充满 (SOC: 75.0%)，离开
超出专变安全限值
奖励各项的值：powerloss=-0.15042655367008786, voltage=-0.2896304218129231, ctrl=-0.0, connection=8.64, completion=6.296296296296297, energy=8.628685142083524, transformer=-2.1426836044283677.
时间步 29: 电池 batt_ev_156 已错过离开时间，无法接入
已连接电池 batt_ev_053, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_053 已接入
已连接电池 batt_ev_211, 初始SOC: 62.0%, 最大功率: 120kW, 电池容量: 106kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_211 已接入
已连接电池 batt_ev_017, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_087, 初始SOC: 62.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_007 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 56.25, -11.422049660662733
SOC从 0.60 更新为 0.83。
SOC从 0.32 更新为 0.45。
SOC从 0.52 更新为 0.73。
SOC从 1.00 更新为 1.00。
SOC从 0.60 更新为 0.88。
SOC从 0.81 更新为 0.99。
SOC从 0.62 更新为 0.90。
SOC从 0.28 更新为 0.49。
SOC从 0.40 更新为 0.72。
SOC从 0.62 更新为 0.77。
已断开电池: batt_ev_129
时间步 30 执行前: 电池 batt_ev_129 已充满 (SOC: 99.5%)，离开
已断开电池: batt_ev_007
时间步 30: 电池 batt_ev_007 已离开，当前SOC: 72.9%，能量满足率: 62.0%
已断开电池: batt_ev_211
时间步 30 执行前: 电池 batt_ev_211 已充满 (SOC: 90.3%)，离开
超出专变安全限值
奖励各项的值：powerloss=-0.1632131285446896, voltage=-0.30760721706486915, ctrl=-0.0, connection=8.88, completion=6.306306306306306, energy=8.631525171588462, transformer=-4.565712145386215.
时间步 30: 电池 batt_ev_021 已错过离开时间，无法接入
已连接电池 batt_ev_209, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_209 已接入
已连接电池 batt_ev_178, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 93kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_178 已接入
已连接电池 batt_ev_110, 初始SOC: 22.0%, 最大功率: 100kW, 电池容量: 65kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_110 已接入
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 81.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 33.75, -6.853229796397639
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 81.25, -16.49851617651283
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_178 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_110 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.83 更新为 1.00。
SOC从 0.45 更新为 0.58。
SOC从 0.38 更新为 0.56。
SOC从 1.00 更新为 1.00。
SOC从 0.88 更新为 0.99。
SOC从 0.42 更新为 0.69。
SOC从 0.22 更新为 0.60。
SOC从 0.49 更新为 0.71。
SOC从 0.72 更新为 0.98。
SOC从 0.77 更新为 0.93。
已断开电池: batt_ev_054
时间步 31: 电池 batt_ev_054 已离开，当前SOC: 99.6%，能量满足率: 98.0%
已断开电池: batt_ev_088
时间步 31 执行前: 电池 batt_ev_088 已充满 (SOC: 99.9%)，离开
已断开电池: batt_ev_142
时间步 31 执行前: 电池 batt_ev_142 已充满 (SOC: 99.5%)，离开
已断开电池: batt_ev_079
时间步 31 执行前: 电池 batt_ev_079 已充满 (SOC: 98.1%)，离开
已断开电池: batt_ev_087
时间步 31 执行前: 电池 batt_ev_087 已充满 (SOC: 92.9%)，离开
奖励各项的值：powerloss=-0.1711989469957929, voltage=-0.25875049316612886, ctrl=-0.0, connection=9.28, completion=6.379310344827587, energy=8.688820824266783, transformer=0.
已连接电池 batt_ev_112, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 71kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_112 已接入
已连接电池 batt_ev_223, 初始SOC: 22.0%, 最大功率: 100kW, 电池容量: 81kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_223 已接入
已连接电池 batt_ev_207, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_207 已接入
已连接电池 batt_ev_198, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 88kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_198 已接入
已连接电池 batt_ev_152, 初始SOC: 68.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_152 已接入
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 87.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_178 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_110 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_223 充电的有无功功率为 87.5, -17.76763280547536
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_198 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 33.75, -6.853229796397639
SOC从 0.22 更新为 0.43。
SOC从 0.58 更新为 0.71。
SOC从 0.56 更新为 0.74。
SOC从 0.22 更新为 0.49。
SOC从 0.28 更新为 0.57。
SOC从 0.69 更新为 0.96。
SOC从 0.60 更新为 0.99。
SOC从 0.71 更新为 0.92。
SOC从 0.08 更新为 0.36。
SOC从 0.68 更新为 0.85。
已断开电池: batt_ev_053
时间步 32: 电池 batt_ev_053 已离开，当前SOC: 71.1%，能量满足率: 59.2%
已断开电池: batt_ev_178
时间步 32: 电池 batt_ev_178 已离开，当前SOC: 95.8%，能量满足率: 96.0%
已断开电池: batt_ev_110
时间步 32 执行前: 电池 batt_ev_110 已充满 (SOC: 98.9%)，离开
超出专变安全限值
奖励各项的值：powerloss=-0.19795957999679673, voltage=-0.24550277750063687, ctrl=-0.0, connection=9.52, completion=6.302521008403361, energy=8.684221770254887, transformer=-4.94881512538974.
时间步 32: 电池 batt_ev_192 已错过离开时间，无法接入
已连接电池 batt_ev_171, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
时间步 32 执行前: 排队电池 batt_ev_171 已接入
已连接电池 batt_ev_022, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 68kWh，并创BMS。
时间步 32 执行前: 排队电池 batt_ev_022 已接入
已连接电池 batt_ev_028, 初始SOC: 82.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 32 执行前: 排队电池 batt_ev_028 已接入
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 87.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 18.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 18.75, -3.807349886887577
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_223 充电的有无功功率为 87.5, -17.76763280547536
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_198 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 37.5, -7.614699773775154
SOC从 0.43 更新为 0.64。
SOC从 0.12 更新为 0.29。
SOC从 0.74 更新为 0.91。
SOC从 0.49 更新为 0.76。
SOC从 0.57 更新为 0.87。
SOC从 0.32 更新为 0.54。
SOC从 0.82 更新为 0.98。
SOC从 0.92 更新为 0.99。
SOC从 0.36 更新为 0.65。
SOC从 0.85 更新为 0.99。
已断开电池: batt_ev_017
时间步 33 执行前: 电池 batt_ev_017 已充满 (SOC: 99.0%)，离开
已断开电池: batt_ev_209
时间步 33: 电池 batt_ev_209 已离开，当前SOC: 91.3%，能量满足率: 88.9%
已断开电池: batt_ev_112
时间步 33: 电池 batt_ev_112 已离开，当前SOC: 64.3%，能量满足率: 70.4%
已断开电池: batt_ev_223
时间步 33 执行前: 电池 batt_ev_223 已充满 (SOC: 76.0%)，离开
已断开电池: batt_ev_198
时间步 33: 电池 batt_ev_198 已离开，当前SOC: 64.8%，能量满足率: 67.6%
已断开电池: batt_ev_152
时间步 33 执行前: 电池 batt_ev_152 已充满 (SOC: 99.3%)，离开
奖励各项的值：powerloss=-0.20456858463864744, voltage=-0.3123682708202735, ctrl=-0.0, connection=10.0, completion=6.24, energy=8.688933155840083, transformer=0.
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
智能体的动作为: [25  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 87.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 22.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 22.5, -4.568819864265093
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_155 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_094 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 87.5, -17.76763280547536
已在 set_all_batteries_before_solve 中设置 batt_ev_068 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_185 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.52 更新为 0.72。
SOC从 0.29 更新为 0.47。
SOC从 0.28 更新为 0.46。
SOC从 0.38 更新为 0.71。
SOC从 0.87 更新为 0.98。
SOC从 0.54 更新为 0.76。
SOC从 0.98 更新为 0.98。
SOC从 0.18 更新为 0.41。
SOC从 0.48 更新为 0.86。
已断开电池: batt_ev_207
时间步 34 执行前: 电池 batt_ev_207 已充满 (SOC: 98.3%)，离开
已断开电池: batt_ev_171
时间步 34: 电池 batt_ev_171 已离开，当前SOC: 46.9%，能量满足率: 43.6%
已断开电池: batt_ev_022
时间步 34: 电池 batt_ev_022 已离开，当前SOC: 76.1%，能量满足率: 66.8%
已断开电池: batt_ev_028
时间步 34: 电池 batt_ev_028 已离开，当前SOC: 98.4%，能量满足率: 91.3%
已断开电池: batt_ev_068
时间步 34: 电池 batt_ev_068 已离开，当前SOC: 40.7%，能量满足率: 37.8%
已断开电池: batt_ev_185
时间步 34 执行前: 电池 batt_ev_185 已充满 (SOC: 85.5%)，离开
奖励各项的值：powerloss=-0.2144323494606777, voltage=-0.33043282610666136, ctrl=-0.0, connection=10.48, completion=6.106870229007634, energy=8.626516985294733, transformer=0.
已连接电池 batt_ev_049, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
已连接电池 batt_ev_023, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_155 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_094 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_049 充电的有无功功率为 33.75, -6.853229796397639
已在 set_all_batteries_before_solve 中设置 batt_ev_023 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.72 更新为 0.91。
SOC从 0.92 更新为 0.99。
SOC从 0.46 更新为 0.65。
SOC从 0.71 更新为 0.99。
SOC从 0.32 更新为 0.48。
已断开电池: batt_ev_155
时间步 35: 电池 batt_ev_155 已离开，当前SOC: 91.5%，能量满足率: 85.8%
已断开电池: batt_ev_094
时间步 35: 电池 batt_ev_094 已离开，当前SOC: 64.8%，能量满足率: 52.6%
已断开电池: batt_ev_140
时间步 35 执行前: 电池 batt_ev_140 已充满 (SOC: 98.6%)，离开
奖励各项的值：powerloss=-0.2142858088017931, voltage=-0.30196840870958974, ctrl=-0.0, connection=10.72, completion=6.044776119402985, energy=8.611307200396888, transformer=0.
已连接电池 batt_ev_121, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 48.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_049 充电的有无功功率为 48.75, -9.899109705907701
已在 set_all_batteries_before_solve 中设置 batt_ev_023 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 75.0, -15.229399547550308
SOC从 0.99 更新为 0.99。
SOC从 0.48 更新为 0.80。
SOC从 0.48 更新为 0.71。
已断开电池: batt_ev_049
时间步 36: 电池 batt_ev_049 已离开，当前SOC: 70.9%，能量满足率: 59.0%
奖励各项的值：powerloss=-0.2135755890897823, voltage=-0.3834143182711025, ctrl=-0.0, connection=10.8, completion=6.0, energy=8.59120607893703, transformer=0.
智能体的动作为: [30  4  0  5  2  2  0  4  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_023 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 45.0, -9.137639728530186
SOC从 0.99 更新为 0.99。
SOC从 0.80 更新为 0.99。
已断开电池: batt_ev_023
时间步 37: 电池 batt_ev_023 已离开，当前SOC: 98.8%，能量满足率: 85.2%
已断开电池: batt_ev_121
时间步 37 执行前: 电池 batt_ev_121 已充满 (SOC: 98.8%)，离开
奖励各项的值：powerloss=-0.21201364538843523, voltage=-0.4188097909368649, ctrl=-0.0, connection=10.96, completion=5.985401459854015, energy=8.60098940094326, transformer=0.
已连接电池 batt_ev_015, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
已连接电池 batt_ev_201, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 90.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 90.0, -18.27527945706037
SOC从 0.52 更新为 0.77。
SOC从 0.18 更新为 0.40。
奖励各项的值：powerloss=-0.21509493278876898, voltage=-0.4486426575852098, ctrl=-0.0, connection=10.96, completion=5.985401459854015, energy=8.60098940094326, transformer=0.
已连接电池 batt_ev_080, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_204, 初始SOC: 2.0%, 最大功率: 80kW, 电池容量: 81kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  4  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 90.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 90.0, -18.27527945706037
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.77 更新为 1.00。
SOC从 0.40 更新为 0.62。
SOC从 0.57 更新为 0.83。
SOC从 0.02 更新为 0.27。
已断开电池: batt_ev_015
时间步 39 执行前: 电池 batt_ev_015 已充满 (SOC: 99.6%)，离开
奖励各项的值：powerloss=-0.22096563639894656, voltage=-0.45292583824397603, ctrl=-0.0, connection=11.040000000000001, completion=6.0144927536231885, energy=8.61112715890744, transformer=0.
已连接电池 batt_ev_183, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 71kWh，并创BMS。
已连接电池 batt_ev_230, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 33.75, -6.853229796397639
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_183 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 41.25, -8.37616975115267
SOC从 0.38 更新为 0.64。
SOC从 0.52 更新为 0.68。
SOC从 0.62 更新为 0.91。
SOC从 0.83 更新为 0.99。
SOC从 0.27 更新为 0.51。
已断开电池: batt_ev_201
时间步 40 执行前: 电池 batt_ev_201 已充满 (SOC: 90.8%)，离开
已断开电池: batt_ev_080
时间步 40 执行前: 电池 batt_ev_080 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_183
时间步 40 执行前: 电池 batt_ev_183 已充满 (SOC: 64.4%)，离开
奖励各项的值：powerloss=-0.2194407613836015, voltage=-0.477567485456718, ctrl=-0.0, connection=11.28, completion=6.099290780141844, energy=8.640677644888132, transformer=0.
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 41.25, -8.37616975115267
SOC从 0.68 更新为 0.84。
SOC从 0.51 更新为 0.76。
已断开电池: batt_ev_204
时间步 41: 电池 batt_ev_204 已离开，当前SOC: 76.1%，能量满足率: 77.2%
已断开电池: batt_ev_230
时间步 41: 电池 batt_ev_230 已离开，当前SOC: 83.7%，能量满足率: 69.0%
奖励各项的值：powerloss=-0.20675788479390136, voltage=-0.37954066483051996, ctrl=-0.0, connection=11.44, completion=6.013986013986013, energy=8.622013415259977, transformer=0.
智能体的动作为: [30 12  2  5  2  2  0  4  1  0  3]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.20394208881777662, voltage=-0.2279147893327238, ctrl=-0.0, connection=11.44, completion=6.013986013986013, energy=8.622013415259977, transformer=0.
已连接电池 batt_ev_148, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_215, 初始SOC: 62.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_210, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [30 12 14 12  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 7.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 105.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 97.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 105.0, -21.32115936657043
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 97.5, -19.798219411815403
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 7.5, -1.522939954755031
SOC从 0.57 更新为 0.60。
SOC从 0.28 更新为 0.57。
SOC从 0.62 更新为 0.94。
已断开电池: batt_ev_215
时间步 43 执行前: 电池 batt_ev_215 已充满 (SOC: 94.1%)，离开
奖励各项的值：powerloss=-0.20891249641913218, voltage=-0.12073427940708648, ctrl=-0.0, connection=11.52, completion=6.041666666666666, energy=8.631582766542895, transformer=0.
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 105.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 105.0, -21.32115936657043
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 30.0, -6.091759819020124
SOC从 0.60 更新为 0.74。
SOC从 0.57 更新为 0.86。
已断开电池: batt_ev_210
时间步 44: 电池 batt_ev_210 已离开，当前SOC: 74.0%，能量满足率: 41.6%
奖励各项的值：powerloss=-0.1975835016969505, voltage=-0.11113683862488344, ctrl=-0.0, connection=11.6, completion=6.0, energy=8.6007112346565, transformer=0.
已连接电池 batt_ev_146, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
已连接电池 batt_ev_027, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 107kWh，并创BMS。
智能体的动作为: [30  4  0  5  2  2  0  4  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.86 更新为 0.98。
SOC从 0.42 更新为 0.64。
SOC从 0.32 更新为 0.60。
已断开电池: batt_ev_148
时间步 45 执行前: 电池 batt_ev_148 已充满 (SOC: 98.1%)，离开
奖励各项的值：powerloss=-0.1990891369545217, voltage=-0.06190433699022835, ctrl=-0.0, connection=11.68, completion=6.027397260273972, energy=8.61029540428214, transformer=0.
已连接电池 batt_ev_135, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_127, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 88kWh，并创BMS。
已连接电池 batt_ev_165, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 105kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 112.5, -22.844099321325466
SOC从 0.32 更新为 0.60。
SOC从 0.64 更新为 0.88。
SOC从 0.60 更新为 0.88。
SOC从 0.18 更新为 0.46。
SOC从 0.18 更新为 0.45。
已断开电池: batt_ev_027
时间步 46: 电池 batt_ev_027 已离开，当前SOC: 88.1%，能量满足率: 93.5%
奖励各项的值：powerloss=-0.2014012384584328, voltage=-0.07396444110775002, ctrl=-0.0, connection=11.76, completion=5.986394557823129, energy=8.615298798759971, transformer=0.
已连接电池 batt_ev_003, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_001, 初始SOC: 38.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
已连接电池 batt_ev_086, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 35.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 35.0, -7.107053122190145
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 33.75, -6.853229796397639
SOC从 0.60 更新为 0.88。
SOC从 0.42 更新为 0.64。
SOC从 0.88 更新为 0.99。
SOC从 0.46 更新为 0.75。
SOC从 0.45 更新为 0.72。
SOC从 0.38 更新为 0.81。
SOC从 0.12 更新为 0.26。
已断开电池: batt_ev_146
时间步 47 执行前: 电池 batt_ev_146 已充满 (SOC: 99.0%)，离开
已断开电池: batt_ev_135
时间步 47: 电池 batt_ev_135 已离开，当前SOC: 87.6%，能量满足率: 84.2%
奖励各项的值：powerloss=-0.18796865913678698, voltage=-0.13986948885005068, ctrl=-0.0, connection=11.92, completion=5.973154362416108, energy=8.623264643189422, transformer=0.
智能体的动作为: [25  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 87.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 87.5, -17.76763280547536
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 33.75, -6.853229796397639
SOC从 0.64 更新为 0.87。
SOC从 0.75 更新为 1.00。
SOC从 0.72 更新为 0.98。
SOC从 0.81 更新为 1.00。
SOC从 0.26 更新为 0.40。
已断开电池: batt_ev_127
时间步 48 执行前: 电池 batt_ev_127 已充满 (SOC: 99.7%)，离开
已断开电池: batt_ev_165
时间步 48 执行前: 电池 batt_ev_165 已充满 (SOC: 98.4%)，离开
已断开电池: batt_ev_001
时间步 48 执行前: 电池 batt_ev_001 已充满 (SOC: 99.6%)，离开
奖励各项的值：powerloss=-0.15833197050277814, voltage=-0.1793808030842281, ctrl=-0.0, connection=12.16, completion=6.052631578947368, energy=8.650437051547527, transformer=0.
已连接电池 batt_ev_043, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_051, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
已连接电池 batt_ev_144, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 40.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 87.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 37.5, -7.614699773775154
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 33.75, -6.853229796397639
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 87.5, -17.76763280547536
已在 set_all_batteries_before_solve 中设置 batt_ev_144 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.42 更新为 0.57。
SOC从 0.87 更新为 0.99。
SOC从 0.48 更新为 0.71。
SOC从 0.22 更新为 0.61。
SOC从 0.40 更新为 0.54。
已断开电池: batt_ev_003
时间步 49 执行前: 电池 batt_ev_003 已充满 (SOC: 98.8%)，离开
已断开电池: batt_ev_144
时间步 49 执行前: 电池 batt_ev_144 已充满 (SOC: 61.2%)，离开
奖励各项的值：powerloss=-0.1295713389911013, voltage=-0.22388492028732054, ctrl=-0.0, connection=12.32, completion=6.103896103896104, energy=8.667963843085872, transformer=0.
已连接电池 batt_ev_188, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
已连接电池 batt_ev_107, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 60kWh，并创BMS。
已连接电池 batt_ev_131, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: 90.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 40.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 87.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 48.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 48.75, -9.899109705907701
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 87.5, -17.76763280547536
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 90.0, -18.27527945706037
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.18 更新为 0.44。
SOC从 0.57 更新为 0.72。
SOC从 0.71 更新为 0.94。
SOC从 0.28 更新为 0.59。
SOC从 0.22 更新为 0.55。
SOC从 0.54 更新为 0.75。
已断开电池: batt_ev_086
时间步 50: 电池 batt_ev_086 已离开，当前SOC: 74.5%，能量满足率: 78.1%
已断开电池: batt_ev_051
时间步 50 执行前: 电池 batt_ev_051 已充满 (SOC: 93.6%)，离开
奖励各项的值：powerloss=-0.13213818871342176, voltage=-0.26111553528624043, ctrl=-0.0, connection=12.48, completion=6.089743589743589, energy=8.671032148516394, transformer=0.
已连接电池 batt_ev_136, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
已连接电池 batt_ev_116, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 52kWh，并创BMS。
已连接电池 batt_ev_196, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 90.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 40.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 90.0, -18.27527945706037
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 41.25, -8.37616975115267
SOC从 0.44 更新为 0.70。
SOC从 0.72 更新为 0.87。
SOC从 0.18 更新为 0.41。
SOC从 0.59 更新为 0.90。
SOC从 0.55 更新为 0.87。
SOC从 0.42 更新为 0.65。
SOC从 0.42 更新为 0.80。
已断开电池: batt_ev_131
时间步 51: 电池 batt_ev_131 已离开，当前SOC: 87.2%，能量满足率: 85.8%
奖励各项的值：powerloss=-0.1330065182067874, voltage=-0.29654308283787234, ctrl=-0.0, connection=12.56, completion=6.050955414012739, energy=8.6704601966019, transformer=0.
已连接电池 batt_ev_005, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_063, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
已连接电池 batt_ev_033, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
已连接电池 batt_ev_077, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 90.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 20.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 40.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 67.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 90.0, -18.27527945706037
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 67.5, -13.706459592795278
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.70 更新为 0.96。
SOC从 0.87 更新为 0.99。
SOC从 0.41 更新为 0.65。
SOC从 0.52 更新为 0.85。
SOC从 0.90 更新为 0.99。
SOC从 0.38 更新为 0.66。
SOC从 0.18 更新为 0.43。
SOC从 0.65 更新为 0.88。
SOC从 0.80 更新为 1.00。
SOC从 0.32 更新为 0.49。
已断开电池: batt_ev_043
时间步 52 执行前: 电池 batt_ev_043 已充满 (SOC: 98.8%)，离开
已断开电池: batt_ev_107
时间步 52 执行前: 电池 batt_ev_107 已充满 (SOC: 98.8%)，离开
已断开电池: batt_ev_116
时间步 52 执行前: 电池 batt_ev_116 已充满 (SOC: 99.7%)，离开
奖励各项的值：powerloss=-0.13778713760933448, voltage=-0.2924531965750554, ctrl=-0.0, connection=12.8, completion=6.125, energy=8.695389067915613, transformer=0.
已连接电池 batt_ev_082, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
时间步 52 执行前: 排队电池 batt_ev_082 已接入
已连接电池 batt_ev_159, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 53kWh，并创BMS。
时间步 52 执行前: 排队电池 batt_ev_159 已接入
时间步 52: 电池 batt_ev_097 已错过离开时间，无法接入
已连接电池 batt_ev_105, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 52 执行前: 排队电池 batt_ev_105 已接入
智能体的动作为: [25  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 7.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 40.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 22.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 65.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 40.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 67.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 7.5, -1.522939954755031
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 22.5, -4.568819864265093
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 67.5, -13.706459592795278
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 65.0, -13.198812941210267
已在 set_all_batteries_before_solve 中设置 batt_ev_105 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.96 更新为 0.99。
SOC从 0.38 更新为 0.58。
SOC从 0.65 更新为 0.88。
SOC从 0.85 更新为 0.99。
SOC从 0.68 更新为 0.99。
SOC从 0.66 更新为 0.94。
SOC从 0.43 更新为 0.69。
SOC从 0.88 更新为 1.00。
SOC从 0.42 更新为 0.71。
SOC从 0.49 更新为 0.67。
已断开电池: batt_ev_188
时间步 53 执行前: 电池 batt_ev_188 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_136
时间步 53 执行前: 电池 batt_ev_136 已充满 (SOC: 99.9%)，离开
已断开电池: batt_ev_063
时间步 53 执行前: 电池 batt_ev_063 已充满 (SOC: 98.9%)，离开
已断开电池: batt_ev_077
时间步 53: 电池 batt_ev_077 已离开，当前SOC: 68.6%，能量满足率: 63.3%
已断开电池: batt_ev_159
时间步 53 执行前: 电池 batt_ev_159 已充满 (SOC: 98.7%)，离开
奖励各项的值：powerloss=-0.13353228589750443, voltage=-0.2662050566456742, ctrl=-0.0, connection=13.200000000000001, completion=6.181818181818182, energy=8.712674938124538, transformer=0.
已连接电池 batt_ev_058, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_058 已接入
已连接电池 batt_ev_118, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 90kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_118 已接入
已连接电池 batt_ev_199, 初始SOC: 52.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_153, 初始SOC: 2.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_169, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 85kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 40.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 18.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 105.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 93.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 11.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 93.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 67.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 18.75, -3.807349886887577
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 11.25, -2.2844099321325464
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 67.5, -13.706459592795278
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_105 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_058 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 105.0, -21.32115936657043
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 93.75, -19.03674943443788
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 93.75, -19.03674943443788
SOC从 0.28 更新为 0.44。
SOC从 0.58 更新为 0.77。
SOC从 0.88 更新为 0.99。
SOC从 0.57 更新为 0.86。
SOC从 0.52 更新为 0.83。
SOC从 0.94 更新为 0.99。
SOC从 0.02 更新为 0.25。
SOC从 0.28 更新为 0.56。
SOC从 0.71 更新为 1.00。
SOC从 0.67 更新为 0.84。
已断开电池: batt_ev_196
时间步 54 执行前: 电池 batt_ev_196 已充满 (SOC: 99.0%)，离开
已断开电池: batt_ev_005
时间步 54 执行前: 电池 batt_ev_005 已充满 (SOC: 98.8%)，离开
已断开电池: batt_ev_033
时间步 54: 电池 batt_ev_033 已离开，当前SOC: 84.2%，能量满足率: 79.1%
已断开电池: batt_ev_105
时间步 54 执行前: 电池 batt_ev_105 已充满 (SOC: 99.7%)，离开
超出专变安全限值
奖励各项的值：powerloss=-0.14910189982470562, voltage=-0.2774960410367333, ctrl=-0.0, connection=13.52, completion=6.213017751479289, energy=8.73075898747349, transformer=-0.35675424313286613.
已连接电池 batt_ev_059, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
已连接电池 batt_ev_175, 初始SOC: 88.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
智能体的动作为: [25  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 40.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 93.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_058 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 93.75, -19.03674943443788
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 45.0, -9.137639728530186
SOC从 0.44 更新为 0.61。
SOC从 0.77 更新为 0.97。
SOC从 0.18 更新为 0.37。
SOC从 0.86 更新为 0.99。
SOC从 0.83 更新为 0.99。
SOC从 0.88 更新为 1.00。
SOC从 0.25 更新为 0.48。
SOC从 0.56 更新为 0.83。
已断开电池: batt_ev_082
时间步 55: 电池 batt_ev_082 已离开，当前SOC: 96.8%，能量满足率: 98.0%
已断开电池: batt_ev_058
时间步 55 执行前: 电池 batt_ev_058 已充满 (SOC: 60.6%)，离开
已断开电池: batt_ev_118
时间步 55 执行前: 电池 batt_ev_118 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_199
时间步 55 执行前: 电池 batt_ev_199 已充满 (SOC: 99.3%)，离开
奖励各项的值：powerloss=-0.1520630050909711, voltage=-0.25741942095619974, ctrl=-0.0, connection=13.84, completion=6.242774566473988, energy=8.75897219914247, transformer=0.
已连接电池 batt_ev_029, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_195, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
已连接电池 batt_ev_213, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_133, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 33.75, -6.853229796397639
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.28 更新为 0.45。
SOC从 0.18 更新为 0.36。
SOC从 0.37 更新为 0.57。
SOC从 1.00 更新为 1.00。
SOC从 0.48 更新为 0.71。
SOC从 0.83 更新为 1.00。
SOC从 0.42 更新为 0.74。
SOC从 0.38 更新为 0.59。
已断开电池: batt_ev_169
时间步 56 执行前: 电池 batt_ev_169 已充满 (SOC: 99.7%)，离开
已断开电池: batt_ev_029
时间步 56 执行前: 电池 batt_ev_029 已充满 (SOC: 73.7%)，离开
奖励各项的值：powerloss=-0.16703897480423888, voltage=-0.22799247325135719, ctrl=-0.0, connection=14.0, completion=6.285714285714286, energy=8.773155374009413, transformer=0.
已连接电池 batt_ev_145, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_044, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
已连接电池 batt_ev_154, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
已连接电池 batt_ev_179, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 93.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 33.75, -6.853229796397639
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 93.75, -19.03674943443788
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.45 更新为 0.62。
SOC从 0.36 更新为 0.55。
SOC从 0.57 更新为 0.76。
SOC从 0.52 更新为 0.80。
SOC从 0.18 更新为 0.42。
SOC从 1.00 更新为 1.00。
SOC从 0.71 更新为 0.94。
SOC从 0.32 更新为 0.57。
SOC从 0.18 更新为 0.55。
SOC从 0.59 更新为 0.79。
已断开电池: batt_ev_153
时间步 57: 电池 batt_ev_153 已离开，当前SOC: 94.3%，能量满足率: 96.2%
已断开电池: batt_ev_213
时间步 57 执行前: 电池 batt_ev_213 已充满 (SOC: 62.1%)，离开
奖励各项的值：powerloss=-0.1919581303139986, voltage=-0.2499125898534893, ctrl=-0.0, connection=14.16, completion=6.271186440677966, energy=8.784845056875886, transformer=0.
已连接电池 batt_ev_246, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 74kWh，并创BMS。
已连接电池 batt_ev_184, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 93.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 33.75, -6.853229796397639
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 93.75, -19.03674943443788
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.48 更新为 0.73。
SOC从 0.55 更新为 0.73。
SOC从 0.76 更新为 0.96。
SOC从 0.80 更新为 0.98。
SOC从 0.42 更新为 0.66。
SOC从 1.00 更新为 1.00。
SOC从 0.28 更新为 0.57。
SOC从 0.57 更新为 0.81。
SOC从 0.55 更新为 0.93。
SOC从 0.79 更新为 1.00。
已断开电池: batt_ev_059
时间步 58: 电池 batt_ev_059 已离开，当前SOC: 95.8%，能量满足率: 97.3%
已断开电池: batt_ev_175
时间步 58: 电池 batt_ev_175 已离开，当前SOC: 99.6%，能量满足率: 96.6%
已断开电池: batt_ev_195
时间步 58 执行前: 电池 batt_ev_195 已充满 (SOC: 99.8%)，离开
已断开电池: batt_ev_133
时间步 58: 电池 batt_ev_133 已离开，当前SOC: 72.9%，能量满足率: 68.6%
已断开电池: batt_ev_145
时间步 58 执行前: 电池 batt_ev_145 已充满 (SOC: 98.4%)，离开
奖励各项的值：powerloss=-0.21058859204805783, voltage=-0.2615594869313598, ctrl=-0.0, connection=14.56, completion=6.208791208791209, energy=8.797630190728245, transformer=0.
已连接电池 batt_ev_066, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
时间步 58 执行前: 排队电池 batt_ev_066 已接入
已连接电池 batt_ev_233, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
已连接电池 batt_ev_219, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_249, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
已连接电池 batt_ev_032, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [25  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 7.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 7.5, -1.522939954755031
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 45.0, -9.137639728530186
SOC从 0.73 更新为 0.99。
SOC从 0.08 更新为 0.28。
SOC从 0.22 更新为 0.45。
SOC从 0.18 更新为 0.38。
SOC从 0.66 更新为 0.91。
SOC从 0.08 更新为 0.38。
SOC从 0.57 更新为 0.86。
SOC从 0.81 更新为 0.99。
SOC从 0.93 更新为 0.98。
SOC从 0.48 更新为 0.62。
已断开电池: batt_ev_044
时间步 59: 电池 batt_ev_044 已离开，当前SOC: 90.7%，能量满足率: 90.9%
已断开电池: batt_ev_154
时间步 59 执行前: 电池 batt_ev_154 已充满 (SOC: 99.4%)，离开
已断开电池: batt_ev_179
时间步 59: 电池 batt_ev_179 已离开，当前SOC: 97.7%，能量满足率: 99.6%
已断开电池: batt_ev_246
时间步 59 执行前: 电池 batt_ev_246 已充满 (SOC: 98.7%)，离开
超出专变安全限值
奖励各项的值：powerloss=-0.22299887575994748, voltage=-0.280446464735149, ctrl=-0.0, connection=14.88, completion=6.182795698924731, energy=8.818379499752258, transformer=-2.9710569965773743.
已连接电池 batt_ev_060, 初始SOC: 56.99999999999999%, 最大功率: 100kW, 电池容量: 90kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_060 已接入
已连接电池 batt_ev_103, 初始SOC: 72.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_103 已接入
已连接电池 batt_ev_205, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 114kWh，并创BMS。
已连接电池 batt_ev_072, 初始SOC: 12.0%, 最大功率: 100kW, 电池容量: 79kWh，并创BMS。
智能体的动作为: [25  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_060 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_103 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.57 更新为 0.78。
SOC从 0.28 更新为 0.47。
SOC从 0.45 更新为 0.68。
SOC从 0.38 更新为 0.58。
SOC从 0.72 更新为 0.98。
SOC从 0.38 更新为 0.68。
SOC从 0.86 更新为 0.99。
SOC从 0.48 更新为 0.73。
SOC从 0.12 更新为 0.44。
SOC从 0.62 更新为 0.75。
已断开电池: batt_ev_184
时间步 60 执行前: 电池 batt_ev_184 已充满 (SOC: 99.0%)，离开
已断开电池: batt_ev_233
时间步 60: 电池 batt_ev_233 已离开，当前SOC: 67.8%，能量满足率: 60.3%
已断开电池: batt_ev_103
时间步 60 执行前: 电池 batt_ev_103 已充满 (SOC: 98.0%)，离开
超出专变安全限值
奖励各项的值：powerloss=-0.2333215047568131, voltage=-0.2915703957757443, ctrl=-0.0, connection=15.120000000000001, completion=6.190476190476191, energy=8.816126067301598, transformer=-6.478813160365485.
已连接电池 batt_ev_217, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_217 已接入
已连接电池 batt_ev_124, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 70kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_124 已接入
已连接电池 batt_ev_189, 初始SOC: 88.0%, 最大功率: 80kW, 电池容量: 78kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_189 已接入
智能体的动作为: [25  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 93.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 35.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 100.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_060 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_217 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 93.75, -19.03674943443788
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 35.0, -7.107053122190145
SOC从 0.78 更新为 0.99。
SOC从 0.47 更新为 0.67。
SOC从 0.38 更新为 0.56。
SOC从 0.58 更新为 0.79。
SOC从 0.38 更新为 0.71。
SOC从 0.68 更新为 0.98。
SOC从 0.88 更新为 0.99。
SOC从 0.73 更新为 0.97。
SOC从 0.44 更新为 0.75。
SOC从 0.75 更新为 0.89。
已断开电池: batt_ev_066
时间步 61: 电池 batt_ev_066 已离开，当前SOC: 67.2%，能量满足率: 65.8%
已断开电池: batt_ev_249
时间步 61 执行前: 电池 batt_ev_249 已充满 (SOC: 98.0%)，离开
已断开电池: batt_ev_060
时间步 61 执行前: 电池 batt_ev_060 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_205
时间步 61 执行前: 电池 batt_ev_205 已充满 (SOC: 97.3%)，离开
已断开电池: batt_ev_217
时间步 61: 电池 batt_ev_217 已离开，当前SOC: 56.1%，能量满足率: 30.1%
超出专变安全限值
奖励各项的值：powerloss=-0.2359259518169868, voltage=-0.2984194534608009, ctrl=-0.0, connection=15.52, completion=6.185567010309279, energy=8.792996876141565, transformer=-7.499783866489856.
已连接电池 batt_ev_073, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 106kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_073 已接入
已连接电池 batt_ev_020, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 99kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_020 已接入
已连接电池 batt_ev_208, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 61kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_208 已接入
已连接电池 batt_ev_091, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_091 已接入
已连接电池 batt_ev_176, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [25  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 90.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 35.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 35.0, -7.107053122190145
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 90.0, -18.27527945706037
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_176 充电的有无功功率为 56.25, -11.422049660662733
SOC从 0.48 更新为 0.69。
SOC从 0.32 更新为 0.47。
SOC从 0.38 更新为 0.66。
SOC从 0.79 更新为 0.99。
SOC从 0.71 更新为 0.98。
SOC从 0.22 更新为 0.44。
SOC从 0.99 更新为 0.99。
SOC从 0.38 更新为 0.64。
SOC从 0.75 更新为 0.99。
SOC从 0.89 更新为 1.00。
已断开电池: batt_ev_219
时间步 62 执行前: 电池 batt_ev_219 已充满 (SOC: 98.8%)，离开
已断开电池: batt_ev_032
时间步 62 执行前: 电池 batt_ev_032 已充满 (SOC: 99.8%)，离开
已断开电池: batt_ev_072
时间步 62 执行前: 电池 batt_ev_072 已充满 (SOC: 99.0%)，离开
已断开电池: batt_ev_124
时间步 62 执行前: 电池 batt_ev_124 已充满 (SOC: 98.3%)，离开
已断开电池: batt_ev_176
时间步 62: 电池 batt_ev_176 已离开，当前SOC: 64.0%，能量满足率: 43.4%
奖励各项的值：powerloss=-0.22299009909998405, voltage=-0.2969923512511463, ctrl=-0.0, connection=15.92, completion=6.231155778894473, energy=8.794878895197504, transformer=0.
已连接电池 batt_ev_102, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_102 已接入
已连接电池 batt_ev_236, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 92kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_236 已接入
已连接电池 batt_ev_074, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_074 已接入
已连接电池 batt_ev_130, 初始SOC: 82.0%, 最大功率: 80kW, 电池容量: 52kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_130 已接入
已连接电池 batt_ev_061, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 78kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_061 已接入
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 90.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 93.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: -0.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 35.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 -0.0, 0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 90.0, -18.27527945706037
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_236 充电的有无功功率为 93.75, -19.03674943443788
已在 set_all_batteries_before_solve 中设置 batt_ev_074 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_130 充电的有无功功率为 35.0, -7.107053122190145
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 56.25, -11.422049660662733
SOC从 0.69 更新为 0.90。
SOC从 0.47 更新为 0.62。
SOC从 0.66 更新为 0.94。
SOC从 0.48 更新为 0.72。
SOC从 0.38 更新为 0.63。
SOC从 0.44 更新为 0.67。
SOC从 0.99 更新为 0.99。
SOC从 0.48 更新为 0.74。
SOC从 0.82 更新为 0.99。
SOC从 0.28 更新为 0.46。
已断开电池: batt_ev_189
时间步 63: 电池 batt_ev_189 已离开，当前SOC: 99.2%，能量满足率: 93.5%
已断开电池: batt_ev_236
时间步 63: 电池 batt_ev_236 已离开，当前SOC: 63.5%，能量满足率: 47.2%
已断开电池: batt_ev_074
时间步 63 执行前: 电池 batt_ev_074 已充满 (SOC: 74.0%)，离开
已断开电池: batt_ev_130
时间步 63: 电池 batt_ev_130 已离开，当前SOC: 98.8%，能量满足率: 93.5%
奖励各项的值：powerloss=-0.22035436349965756, voltage=-0.306527398257177, ctrl=-0.0, connection=16.240000000000002, completion=6.157635467980295, energy=8.786185604917298, transformer=0.
已连接电池 batt_ev_012, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 98kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_012 已接入
时间步 63: 电池 batt_ev_108 已错过离开时间，无法接入
已连接电池 batt_ev_228, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_228 已接入
已连接电池 batt_ev_218, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
已连接电池 batt_ev_243, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 12.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 112.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 37.5, -7.614699773775154
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 12.5, -2.538233257925051
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 52.5, -10.660579683285215
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_012 充电的有无功功率为 112.5, -22.844099321325466
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.90 更新为 0.99。
SOC从 0.62 更新为 0.77。
SOC从 0.94 更新为 0.99。
SOC从 0.72 更新为 0.96。
SOC从 0.48 更新为 0.77。
SOC从 0.67 更新为 0.89。
SOC从 0.22 更新为 0.50。
SOC从 0.38 更新为 0.65。
SOC从 0.12 更新为 0.40。
SOC从 0.46 更新为 0.64。
已断开电池: batt_ev_073
时间步 64 执行前: 电池 batt_ev_073 已充满 (SOC: 99.3%)，离开
已断开电池: batt_ev_020
时间步 64: 电池 batt_ev_020 已离开，当前SOC: 77.5%，能量满足率: 75.8%
已断开电池: batt_ev_208
时间步 64 执行前: 电池 batt_ev_208 已充满 (SOC: 99.5%)，离开
已断开电池: batt_ev_091
时间步 64: 电池 batt_ev_091 已离开，当前SOC: 89.2%，能量满足率: 88.4%
已断开电池: batt_ev_012
时间步 64 执行前: 电池 batt_ev_012 已充满 (SOC: 76.7%)，离开
奖励各项的值：powerloss=-0.22146837952021323, voltage=-0.3236744241212519, ctrl=-0.0, connection=16.64, completion=6.153846153846154, energy=8.798119362314425, transformer=0.
已连接电池 batt_ev_122, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  7]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 7.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 7.5, -1.522939954755031
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_122 充电的有无功功率为 45.0, -9.137639728530186
SOC从 0.28 更新为 0.55。
SOC从 0.96 更新为 0.99。
SOC从 0.50 更新为 0.79。
SOC从 0.65 更新为 0.92。
SOC从 0.40 更新为 0.68。
SOC从 0.64 更新为 0.82。
已断开电池: batt_ev_102
时间步 65 执行前: 电池 batt_ev_102 已充满 (SOC: 99.2%)，离开
已断开电池: batt_ev_122
时间步 65: 电池 batt_ev_122 已离开，当前SOC: 55.4%，能量满足率: 39.2%
奖励各项的值：powerloss=-0.20493248169208295, voltage=-0.2914998724434148, ctrl=-0.0, connection=16.8, completion=6.142857142857143, energy=8.78061279994561, transformer=0.
已连接电池 batt_ev_139, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 84kWh，并创BMS。
智能体的动作为: [30  4  8  5  2  1  0  0  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: 40.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 20.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 60.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 50.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 50.0, -10.152933031700204
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 40.0, -8.122346425360163
SOC从 0.12 更新为 0.24。
SOC从 0.79 更新为 1.00。
SOC从 0.92 更新为 0.99。
SOC从 0.68 更新为 0.95。
SOC从 0.82 更新为 0.98。
已断开电池: batt_ev_061
时间步 66 执行前: 电池 batt_ev_061 已充满 (SOC: 98.1%)，离开
已断开电池: batt_ev_228
时间步 66 执行前: 电池 batt_ev_228 已充满 (SOC: 99.8%)，离开
已断开电池: batt_ev_218
时间步 66 执行前: 电池 batt_ev_218 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_243
时间步 66 执行前: 电池 batt_ev_243 已充满 (SOC: 95.3%)，离开
奖励各项的值：powerloss=-0.20882876633539144, voltage=-0.19800726506061128, ctrl=-0.0, connection=17.12, completion=6.214953271028038, energy=8.803405084058776, transformer=0.
已连接电池 batt_ev_004, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_019, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
智能体的动作为: [30  4  0  5  2 14  0  4  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 7.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 7.5, -1.522939954755031
SOC从 0.24 更新为 0.48。
SOC从 0.08 更新为 0.27。
SOC从 0.52 更新为 0.56。
奖励各项的值：powerloss=-0.2014348486992406, voltage=-0.11626891715779797, ctrl=-0.0, connection=17.12, completion=6.214953271028038, energy=8.803405084058776, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: 10.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 10.0, -2.030586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 52.5, -10.660579683285215
SOC从 0.48 更新为 0.51。
SOC从 0.27 更新为 0.46。
SOC从 0.56 更新为 0.87。
奖励各项的值：powerloss=-0.19508142331495837, voltage=-0.09728014110945704, ctrl=-0.0, connection=17.12, completion=6.214953271028038, energy=8.803405084058776, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 10.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 22.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 10.0, -2.030586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 22.5, -4.568819864265093
SOC从 0.51 更新为 0.54。
SOC从 0.46 更新为 0.65。
SOC从 0.87 更新为 1.00。
已断开电池: batt_ev_139
时间步 69: 电池 batt_ev_139 已离开，当前SOC: 53.7%，能量满足率: 48.4%
已断开电池: batt_ev_019
时间步 69 执行前: 电池 batt_ev_019 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.19382715056470587, voltage=-0.0490341672106509, ctrl=-0.0, connection=17.28, completion=6.203703703703703, energy=8.790618746430036, transformer=0.
已连接电池 batt_ev_177, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 68.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 68.75, -13.960282918587783
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.65 更新为 0.84。
SOC从 0.38 更新为 0.72。
奖励各项的值：powerloss=-0.1852316750250889, voltage=-0.04314118015502855, ctrl=-0.0, connection=17.28, completion=6.203703703703703, energy=8.790618746430036, transformer=0.
已连接电池 batt_ev_202, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_160, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 25.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 56.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 65.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 56.25, -11.422049660662733
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 65.0, -13.198812941210267
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 52.5, -10.660579683285215
SOC从 0.48 更新为 0.56。
SOC从 0.84 更新为 0.99。
SOC从 0.18 更新为 0.50。
SOC从 0.72 更新为 0.99。
已断开电池: batt_ev_004
时间步 71 执行前: 电池 batt_ev_004 已充满 (SOC: 99.0%)，离开
已断开电池: batt_ev_177
时间步 71 执行前: 电池 batt_ev_177 已充满 (SOC: 99.4%)，离开
奖励各项的值：powerloss=-0.17132972435892097, voltage=-0.08064472539038636, ctrl=-0.0, connection=17.44, completion=6.238532110091743, energy=8.801713987288478, transformer=0.
智能体的动作为: [30  4  2  5  2  2  0  4  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: 75.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 75.0, -15.229399547550308
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 52.5, -10.660579683285215
SOC从 0.56 更新为 0.81。
SOC从 0.50 更新为 0.82。
奖励各项的值：powerloss=-0.15072213353620262, voltage=-0.13179742409906048, ctrl=-0.0, connection=17.44, completion=6.238532110091743, energy=8.801713987288478, transformer=0.
已连接电池 batt_ev_099, 初始SOC: 68.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
已连接电池 batt_ev_100, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 25.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 26.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 26.25, -5.330289841642608
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 45.0, -9.137639728530186
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 45.0, -9.137639728530186
SOC从 0.81 更新为 0.89。
SOC从 0.82 更新为 0.98。
SOC从 0.68 更新为 0.85。
SOC从 0.18 更新为 0.37。
已断开电池: batt_ev_202
时间步 73 执行前: 电池 batt_ev_202 已充满 (SOC: 89.1%)，离开
已断开电池: batt_ev_160
时间步 73 执行前: 电池 batt_ev_160 已充满 (SOC: 98.0%)，离开
奖励各项的值：powerloss=-0.1261047563872571, voltage=-0.18129445760113327, ctrl=-0.0, connection=17.6, completion=6.272727272727273, energy=8.812607496494945, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 37.5, -7.614699773775154
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 45.0, -9.137639728530186
SOC从 0.85 更新为 0.99。
SOC从 0.37 更新为 0.57。
已断开电池: batt_ev_099
时间步 74 执行前: 电池 batt_ev_099 已充满 (SOC: 98.8%)，离开
已断开电池: batt_ev_100
时间步 74: 电池 batt_ev_100 已离开，当前SOC: 56.8%，能量满足率: 52.4%
奖励各项的值：powerloss=-0.1168469584147824, voltage=-0.21423133589635102, ctrl=-0.0, connection=17.76, completion=6.261261261261262, energy=8.80187369597154, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.1084645862318677, voltage=-0.24070316338142606, ctrl=-0.0, connection=17.76, completion=6.261261261261262, energy=8.80187369597154, transformer=0.
智能体的动作为: [30 12 14 12  2  2  0  4  7  0  3]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.10822517520506605, voltage=-0.269556600210461, ctrl=-0.0, connection=17.76, completion=6.261261261261262, energy=8.80187369597154, transformer=0.
已连接电池 batt_ev_120, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [30 12 14 12  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.18 更新为 0.55。
奖励各项的值：powerloss=-0.1153392515057774, voltage=-0.2544079507143726, ctrl=-0.0, connection=17.76, completion=6.261261261261262, energy=8.80187369597154, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.55 更新为 0.91。
奖励各项的值：powerloss=-0.12105784231376453, voltage=-0.24398457923433536, ctrl=-0.0, connection=17.76, completion=6.261261261261262, energy=8.80187369597154, transformer=0.
已连接电池 batt_ev_035, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 77kWh，并创BMS。
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 22.50 kW。
功率需求已禁用，直接使用桩侧设置功率: 65.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 22.5, -4.568819864265093
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 65.0, -13.198812941210267
SOC从 0.91 更新为 0.98。
SOC从 0.48 更新为 0.69。
已断开电池: batt_ev_120
时间步 79 执行前: 电池 batt_ev_120 已充满 (SOC: 98.0%)，离开
奖励各项的值：powerloss=-0.1363927499301065, voltage=-0.3567395847205712, ctrl=-0.0, connection=17.84, completion=6.278026905829597, energy=8.807246459666736, transformer=0.
已连接电池 batt_ev_151, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 65.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 65.0, -13.198812941210267
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.28 更新为 0.32。
SOC从 0.69 更新为 0.90。
奖励各项的值：powerloss=-0.15208616840953393, voltage=-0.3894109193031614, ctrl=-0.0, connection=17.84, completion=6.278026905829597, energy=8.807246459666736, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 30.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.32 更新为 0.37。
SOC从 0.90 更新为 1.00。
已断开电池: batt_ev_035
时间步 81 执行前: 电池 batt_ev_035 已充满 (SOC: 99.9%)，离开
已断开电池: batt_ev_151
时间步 81: 电池 batt_ev_151 已离开，当前SOC: 36.7%，能量满足率: 12.5%
奖励各项的值：powerloss=-0.16253029813980233, voltage=-0.3393596075308203, ctrl=-0.0, connection=18.0, completion=6.2666666666666675, energy=8.778941367474497, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.16964960589341926, voltage=-0.29893775106469844, ctrl=-0.0, connection=18.0, completion=6.2666666666666675, energy=8.778941367474497, transformer=0.
智能体的动作为: [30 12 14 12  2  2  0  4  7  0  3]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.17849155899479302, voltage=-0.3390324392664601, ctrl=-0.0, connection=18.0, completion=6.2666666666666675, energy=8.778941367474497, transformer=0.
已连接电池 batt_ev_056, 初始SOC: 62.0%, 最大功率: 80kW, 电池容量: 64kWh，并创BMS。
已连接电池 batt_ev_226, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [30 12 14 12  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 70.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 70.0, -14.21410624438029
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.18 更新为 0.26。
SOC从 0.62 更新为 0.89。
奖励各项的值：powerloss=-0.18719676442745634, voltage=-0.3436939197547373, ctrl=-0.0, connection=18.0, completion=6.2666666666666675, energy=8.778941367474497, transformer=0.
已连接电池 batt_ev_048, 初始SOC: 42.0%, 最大功率: 120kW, 电池容量: 93kWh，并创BMS。
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 25.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_048 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.26 更新为 0.49。
SOC从 0.89 更新为 0.99。
SOC从 0.42 更新为 0.74。
已断开电池: batt_ev_056
时间步 85 执行前: 电池 batt_ev_056 已充满 (SOC: 99.1%)，离开
已断开电池: batt_ev_048
时间步 85: 电池 batt_ev_048 已离开，当前SOC: 74.3%，能量满足率: 57.6%
奖励各项的值：powerloss=-0.19795790987462134, voltage=-0.41884276264329223, ctrl=-0.0, connection=18.16, completion=6.255506607929515, energy=8.771022803283508, transformer=0.
已连接电池 batt_ev_234, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_227, 初始SOC: 8.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
智能体的动作为: [30 12  2  5  2  2  0  4  1  0  3]
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 41.25 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 41.25, -8.37616975115267
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 52.5, -10.660579683285215
SOC从 0.57 更新为 0.63。
SOC从 0.49 更新为 0.71。
SOC从 0.08 更新为 0.36。
已断开电池: batt_ev_226
时间步 86: 电池 batt_ev_226 已离开，当前SOC: 71.0%，能量满足率: 82.8%
奖励各项的值：powerloss=-0.1945642122375213, voltage=-0.3911482487696394, ctrl=-0.0, connection=18.240000000000002, completion=6.228070175438597, energy=8.768859778974676, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 52.5, -10.660579683285215
SOC从 0.63 更新为 0.69。
SOC从 0.36 更新为 0.64。
奖励各项的值：powerloss=-0.19007804416288135, voltage=-0.3449230766605016, ctrl=-0.0, connection=18.240000000000002, completion=6.228070175438597, energy=8.768859778974676, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 52.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 52.5, -10.660579683285215
SOC从 0.69 更新为 0.75。
SOC从 0.64 更新为 0.92。
已断开电池: batt_ev_227
时间步 88: 电池 batt_ev_227 已离开，当前SOC: 91.8%，能量满足率: 93.1%
奖励各项的值：powerloss=-0.1869343663623593, voltage=-0.3462258045238964, ctrl=-0.0, connection=18.32, completion=6.200873362445415, energy=8.77123181809526, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.75 更新为 0.81。
奖励各项的值：powerloss=-0.18587593495712984, voltage=-0.2817081376547681, ctrl=-0.0, connection=18.32, completion=6.200873362445415, energy=8.77123181809526, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.81 更新为 0.87。
已断开电池: batt_ev_234
时间步 90: 电池 batt_ev_234 已离开，当前SOC: 86.8%，能量满足率: 72.6%
奖励各项的值：powerloss=-0.1997383090551201, voltage=-0.2060125420948311, ctrl=-0.0, connection=18.400000000000002, completion=6.173913043478261, energy=8.76465690219676, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.19617676489350927, voltage=-0.07846179497760897, ctrl=-0.0, connection=18.400000000000002, completion=6.173913043478261, energy=8.76465690219676, transformer=0.
智能体的动作为: [30 12 14 12  2  2  0  4  7  0  3]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.1900930225293191, voltage=-0.05499017312745602, ctrl=-0.0, connection=18.400000000000002, completion=6.173913043478261, energy=8.76465690219676, transformer=0.
已连接电池 batt_ev_238, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [30 12 14 12  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 45.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 45.0, -9.137639728530186
SOC从 0.48 更新为 0.75。
奖励各项的值：powerloss=-0.19322634123297436, voltage=-0.01950579580764389, ctrl=-0.0, connection=18.400000000000002, completion=6.173913043478261, energy=8.76465690219676, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 37.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 37.5, -7.614699773775154
SOC从 0.75 更新为 0.98。
已断开电池: batt_ev_238
时间步 94 执行前: 电池 batt_ev_238 已充满 (SOC: 98.3%)，离开
奖励各项的值：powerloss=-0.18029974802688062, voltage=-0.01583818100834966, ctrl=-0.0, connection=18.48, completion=6.190476190476191, energy=8.770004707814955, transformer=0.
智能体的动作为: [30 12 14  5  2  2  0  4  7  0  3]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.1615460253066968, voltage=-0.08384895442516083, ctrl=-0.0, connection=18.48, completion=6.190476190476191, energy=8.770004707814955, transformer=0.
已连接电池 batt_ev_025, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
已连接电池 batt_ev_013, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 89kWh，并创BMS。
已连接电池 batt_ev_117, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 111kWh，并创BMS。
已连接电池 batt_ev_166, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 114kWh，并创BMS。
智能体的动作为: [30 12 14 12  2  2  0  4  7  0  3]
功率需求已禁用，直接使用桩侧设置功率: 15.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 33.75 kW。
功率需求已禁用，直接使用桩侧设置功率: 120.00 kW。
功率需求已禁用，直接使用桩侧设置功率: 97.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_025 充电的有无功功率为 33.75, -6.853229796397639
已在 set_all_batteries_before_solve 中设置 batt_ev_013 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_117 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_166 充电的有无功功率为 97.5, -19.798219411815403
SOC从 0.52 更新为 0.55。
SOC从 0.12 更新为 0.29。
SOC从 0.18 更新为 0.52。
SOC从 0.28 更新为 0.49。
已断开电池: batt_ev_025
时间步 96: 电池 batt_ev_025 已离开，当前SOC: 29.2%，能量满足率: 20.0%
已断开电池: batt_ev_013
时间步 96: 电池 batt_ev_013 已离开，当前SOC: 51.7%，能量满足率: 42.1%
已断开电池: batt_ev_117
时间步 96: 电池 batt_ev_117 已离开，当前SOC: 55.4%，能量满足率: 7.3%
已断开电池: batt_ev_166
时间步 96: 电池 batt_ev_166 已离开，当前SOC: 49.4%，能量满足率: 30.6%
奖励各项的值：powerloss=-0.15737671643239778, voltage=-0.1588342349189853, ctrl=-0.9767500000000001, connection=18.8, completion=6.085106382978723, energy=8.663306324378205, transformer=0.
调度记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250514_092650_13Bus_1000000\test_results_20250514_183833\schedule.csv
储能放电功率记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250514_092650_13Bus_1000000\test_results_20250514_183833\storage_schedule.csv
储能能量记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250514_092650_13Bus_1000000\test_results_20250514_183833\storage_energy.csv
已生成GIF动画，包含96步
测试完成 - 总奖励: 2436.6509
测试结果保存在: D:\LENOVO\Documents\Python\ML\powergym\results_20250514_092650_13Bus_1000000\test_results_20250514_183833
运行时间: 33142.56秒

进程已结束，退出代码为 0

```