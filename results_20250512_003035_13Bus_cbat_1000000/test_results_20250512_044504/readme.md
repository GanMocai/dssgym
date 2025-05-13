

## 测试信息

### 原始控制台输出


```text
环境初始化中，充电站链接母线为 680
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
已从D:\LENOVO\Documents\Python\ML\powergym\results_20250512_003035_13Bus_cbat_1000000\model\ppo_model加载模型
BatteryStationManager已重置
智能体的动作为: [ 1. -1. -1. -0. -0. -1. -1. -0. -1. -1. -1.]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
奖励各项的值：powerloss=-0.1146193283763593, voltage=-0.20049466529023174, ctrl=-0.0, connection=0.0, completion=0.0, energy=0.0, transformer=0.
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
智能体的动作为: [ 1. -1. -1. -0. -0. -1. -1. -0. -1. -1. -1.]
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=0.0。
功率需求: 80.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -60.0, -19.721046310731793
已在 set_all_batteries_before_solve 中设置 batt_ev_030 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.18 更新为 0.51。
SOC从 0.32 更新为 0.55。
SOC从 0.18 更新为 0.18。
SOC从 0.12 更新为 0.12。
SOC从 0.22 更新为 0.51。
SOC从 0.28 更新为 0.55。
SOC从 0.12 更新为 0.12。
SOC从 0.38 更新为 0.64。
SOC从 0.22 更新为 0.55。
SOC从 0.12 更新为 0.54。
已断开电池: batt_ev_030
时间步 2 执行前: 电池 batt_ev_030 已充满 (SOC: 51.3%)，离开
奖励各项的值：powerloss=-0.15053753347937435, voltage=-0.24309530723187978, ctrl=-0.0, connection=0.008, completion=1.0, energy=1.0, transformer=0.
已连接电池 batt_ev_224, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
时间步 2 执行前: 排队电池 batt_ev_224 已接入
智能体的动作为: [ 1.         -0.         -1.         -0.22042614 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
self.charger_power=0.0 改为 26.45113706588745。
功率需求: 60.00 kW, 充电桩功率: 26.45 kW, 最终充电功率: 26.45 kW。
self.charger_power=0.0 改为 120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=99.12失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
self.charger_power=0.0 改为 120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=80.4失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 26.45113706588745, -5.371132464845567
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 0.0, -0.0
SOC从 0.28 更新为 0.28。
SOC从 0.55 更新为 0.73。
SOC从 0.18 更新为 0.28。
SOC从 0.12 更新为 0.36。
SOC从 0.51 更新为 0.69。
SOC从 0.55 更新为 0.71。
SOC从 0.12 更新为 0.50。
SOC从 0.64 更新为 0.83。
SOC从 0.55 更新为 0.75。
SOC从 0.54 更新为 0.79。
已断开电池: batt_ev_039
时间步 3: 电池 batt_ev_039 已离开，当前SOC: 50.5%，能量满足率: 44.7%
已断开电池: batt_ev_242
时间步 3 执行前: 电池 batt_ev_242 已充满 (SOC: 83.2%)，离开
已断开电池: batt_ev_045
时间步 3: 电池 batt_ev_045 已离开，当前SOC: 78.7%，能量满足率: 77.5%
奖励各项的值：powerloss=-0.14199031758307265, voltage=-0.2595048198527272, ctrl=-0.0, connection=0.032, completion=0.5, energy=0.8056052474657126, transformer=0.
时间步 3: 电池 batt_ev_092 已错过离开时间，无法接入
已连接电池 batt_ev_081, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 50kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_081 已接入
已连接电池 batt_ev_076, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_076 已接入
已连接电池 batt_ev_235, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_235 已接入
智能体的动作为: [ 1.        -0.        -1.        -0.2204261 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
self.charger_power=0.0 改为 0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=75.68失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=26.45113706588745，设置charger_power=26.45113170146942失败。
功率需求: 60.00 kW, 充电桩功率: 26.45 kW, 最终充电功率: 26.45 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=63.120000000000005失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=104.95999999999998失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=44.400000000000006失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=71.44。
功率需求: 36.00 kW, 充电桩功率: 71.44 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 26.45113706588745, -5.371132464845567
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_235 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.28 更新为 0.28。
SOC从 0.73 更新为 0.84。
SOC从 0.28 更新为 0.37。
SOC从 0.36 更新为 0.56。
SOC从 0.69 更新为 0.87。
SOC从 0.71 更新为 0.82。
SOC从 0.12 更新为 0.52。
SOC从 0.28 更新为 0.53。
SOC从 0.75 更新为 0.89。
SOC从 0.62 更新为 0.81。
已断开电池: batt_ev_126
时间步 4: 电池 batt_ev_126 已离开，当前SOC: 37.4%，能量满足率: 24.3%
已断开电池: batt_ev_064
时间步 4 执行前: 电池 batt_ev_064 已充满 (SOC: 55.5%)，离开
已断开电池: batt_ev_239
时间步 4 执行前: 电池 batt_ev_239 已充满 (SOC: 82.3%)，离开
奖励各项的值：powerloss=-0.13304777055795758, voltage=-0.29849871696257635, ctrl=-0.0, connection=0.056, completion=0.5714285714285714, energy=0.7807765279636004, transformer=0.
时间步 4: 电池 batt_ev_104 已错过离开时间，无法接入
已连接电池 batt_ev_018, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_018 已接入
已连接电池 batt_ev_062, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_062 已接入
时间步 4: 电池 batt_ev_200 已错过离开时间，无法接入
时间步 4: 电池 batt_ev_163 已错过离开时间，无法接入
已连接电池 batt_ev_014, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_014 已接入
智能体的动作为: [ 1.        -0.        -1.        -0.2204258 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
self.charger_power=0.0 改为 0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=43.68000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=26.451095938682556。
功率需求: 48.00 kW, 充电桩功率: 26.45 kW, 最终充电功率: 26.45 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=27.120000000000005失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=96.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=112.8失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=20.400000000000006失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=71.44，设置charger_power=35.44失败。
功率需求: 24.00 kW, 充电桩功率: 71.44 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_235 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 26.451095938682556, -5.371124113610425
已在 set_all_batteries_before_solve 中设置 batt_ev_062 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_014 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.28 更新为 0.28。
SOC从 0.84 更新为 0.96。
SOC从 0.32 更新为 0.43。
SOC从 0.57 更新为 0.80。
SOC从 0.87 更新为 0.94。
SOC从 0.28 更新为 0.53。
SOC从 0.52 更新为 0.76。
SOC从 0.53 更新为 0.68。
SOC从 0.89 更新为 0.97。
SOC从 0.81 更新为 0.94。
已断开电池: batt_ev_123
时间步 5: 电池 batt_ev_123 已离开，当前SOC: 94.1%，能量满足率: 94.8%
已断开电池: batt_ev_042
时间步 5: 电池 batt_ev_042 已离开，当前SOC: 97.0%，能量满足率: 98.7%
已断开电池: batt_ev_076
时间步 5: 电池 batt_ev_076 已离开，当前SOC: 68.0%，能量满足率: 57.1%
已断开电池: batt_ev_235
时间步 5 执行前: 电池 batt_ev_235 已充满 (SOC: 93.9%)，离开
已断开电池: batt_ev_062
时间步 5: 电池 batt_ev_062 已离开，当前SOC: 80.4%，能量满足率: 57.0%
奖励各项的值：powerloss=-0.13256286045479185, voltage=-0.3131151401330401, ctrl=-0.0, connection=0.096, completion=0.4166666666666667, energy=0.795167527755743, transformer=0.
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
智能体的动作为: [ 1.        -0.        -1.        -0.2205335 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
self.charger_power=0.0 改为 0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=11.680000000000007失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=26.451095938682556，设置charger_power=26.464020609855652失败。
功率需求: 48.00 kW, 充电桩功率: 26.45 kW, 最终充电功率: 26.45 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.0失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 26.451095938682556, -5.371124113610425
已在 set_all_batteries_before_solve 中设置 batt_ev_014 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_231 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_248 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.28 更新为 0.28。
SOC从 0.96 更新为 1.00。
SOC从 0.43 更新为 0.54。
SOC从 0.08 更新为 0.37。
SOC从 0.57 更新为 0.80。
SOC从 0.53 更新为 0.69。
SOC从 0.76 更新为 0.92。
SOC从 0.08 更新为 0.40。
SOC从 0.32 更新为 0.52。
SOC从 0.22 更新为 0.47。
已断开电池: batt_ev_149
时间步 6 执行前: 电池 batt_ev_149 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_014
时间步 6: 电池 batt_ev_014 已离开，当前SOC: 68.5%，能量满足率: 67.5%
已断开电池: batt_ev_231
时间步 6: 电池 batt_ev_231 已离开，当前SOC: 40.3%，能量满足率: 35.8%
已断开电池: batt_ev_248
时间步 6: 电池 batt_ev_248 已离开，当前SOC: 46.6%，能量满足率: 32.4%
奖励各项的值：powerloss=-0.14655099613151323, voltage=-0.3436380997064403, ctrl=-0.0, connection=0.128, completion=0.375, energy=0.7436933466237473, transformer=0.
已连接电池 batt_ev_240, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_240 已接入
时间步 6: 电池 batt_ev_119 已错过离开时间，无法接入
已连接电池 batt_ev_158, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_158 已接入
已连接电池 batt_ev_157, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_157 已接入
已连接电池 batt_ev_096, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_096 已接入
智能体的动作为: [ 1.         -0.         -1.         -0.22053228 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
self.charger_power=0.0 改为 0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=26.451095938682556，设置charger_power=26.463873982429504失败。
功率需求: 36.00 kW, 充电桩功率: 26.45 kW, 最终充电功率: 26.45 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=60.44失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=16.0失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=115.2失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 26.451095938682556, -5.371124113610425
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_157 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.28 更新为 0.28。
SOC从 0.48 更新为 0.82。
SOC从 0.54 更新为 0.65。
SOC从 0.37 更新为 0.61。
SOC从 0.80 更新为 0.96。
SOC从 0.28 更新为 0.60。
SOC从 0.92 更新为 1.00。
SOC从 0.12 更新为 0.39。
SOC从 0.52 更新为 0.67。
SOC从 0.18 更新为 0.47。
已断开电池: batt_ev_224
时间步 7: 电池 batt_ev_224 已离开，当前SOC: 28.0%，能量满足率: -0.0%
已断开电池: batt_ev_081
时间步 7 执行前: 电池 batt_ev_081 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_018
时间步 7: 电池 batt_ev_018 已离开，当前SOC: 64.5%，能量满足率: 49.3%
已断开电池: batt_ev_036
时间步 7: 电池 batt_ev_036 已离开，当前SOC: 96.0%，能量满足率: 95.0%
已断开电池: batt_ev_157
时间步 7: 电池 batt_ev_157 已离开，当前SOC: 39.3%，能量满足率: 31.7%
奖励各项的值：powerloss=-0.1622661188998291, voltage=-0.3826859350843459, ctrl=-0.0, connection=0.168, completion=0.3333333333333333, energy=0.6980493314206142, transformer=0.
时间步 7: 电池 batt_ev_187 已错过离开时间，无法接入
已连接电池 batt_ev_106, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 92kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_106 已接入
已连接电池 batt_ev_055, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_055 已接入
已连接电池 batt_ev_216, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_216 已接入
已连接电池 batt_ev_247, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 87kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_247 已接入
时间步 7: 电池 batt_ev_244 已错过离开时间，无法接入
已连接电池 batt_ev_090, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_090 已接入
智能体的动作为: [ 1.         -0.         -1.         -0.24063882 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 96.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=49.599999999999994失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=28.87665867805481。
功率需求: 100.00 kW, 充电桩功率: 28.88 kW, 最终充电功率: 28.88 kW。
已有历史设置self.charger_power=120.0，设置charger_power=79.68失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=75.36失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=79.19999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=110.56失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_106 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 28.87665867805481, -5.863655634751101
已在 set_all_batteries_before_solve 中设置 batt_ev_216 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 96.0, -19.493631420864393
SOC从 0.32 更新为 0.32。
SOC从 0.82 更新为 0.99。
SOC从 0.28 更新为 0.36。
SOC从 0.61 更新为 0.79。
SOC从 0.42 更新为 0.65。
SOC从 0.60 更新为 0.79。
SOC从 0.18 更新为 0.52。
SOC从 0.48 更新为 0.72。
SOC从 0.67 更新为 0.82。
SOC从 0.47 更新为 0.70。
已断开电池: batt_ev_180
时间步 8: 电池 batt_ev_180 已离开，当前SOC: 78.6%，能量满足率: 78.4%
已断开电池: batt_ev_067
时间步 8: 电池 batt_ev_067 已离开，当前SOC: 82.0%，能量满足率: 75.8%
已断开电池: batt_ev_240
时间步 8 执行前: 电池 batt_ev_240 已充满 (SOC: 99.4%)，离开
已断开电池: batt_ev_158
时间步 8 执行前: 电池 batt_ev_158 已充满 (SOC: 79.1%)，离开
已断开电池: batt_ev_106
时间步 8: 电池 batt_ev_106 已离开，当前SOC: 32.0%，能量满足率: 0.0%
已断开电池: batt_ev_216
时间步 8: 电池 batt_ev_216 已离开，当前SOC: 64.6%，能量满足率: 40.4%
奖励各项的值：powerloss=-0.1795622466021548, voltage=-0.3837608377851409, ctrl=-0.0, connection=0.216, completion=0.3333333333333333, energy=0.6890828930134246, transformer=0.
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
智能体的动作为: [ 1.         -0.         -1.         -0.22975929 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 64.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=95.20000000000002。
功率需求: 48.00 kW, 充电桩功率: 95.20 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=28.87665867805481，设置charger_power=27.571114897727966失败。
功率需求: 80.00 kW, 充电桩功率: 28.88 kW, 最终充电功率: 28.88 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=111.80000000000001。
功率需求: 60.00 kW, 充电桩功率: 111.80 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=112.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=62.56失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 28.87665867805481, -5.863655634751101
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_128 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_173 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_132 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.42 更新为 0.42。
SOC从 0.72 更新为 0.86。
SOC从 0.36 更新为 0.43。
SOC从 0.22 更新为 0.48。
SOC从 0.57 更新为 0.80。
SOC从 0.18 更新为 0.46。
SOC从 0.52 更新为 0.73。
SOC从 0.72 更新为 0.84。
SOC从 0.08 更新为 0.40。
SOC从 0.70 更新为 0.87。
已断开电池: batt_ev_055
时间步 9: 电池 batt_ev_055 已离开，当前SOC: 43.2%，能量满足率: 21.7%
已断开电池: batt_ev_247
时间步 9: 电池 batt_ev_247 已离开，当前SOC: 73.2%，能量满足率: 69.0%
已断开电池: batt_ev_090
时间步 9: 电池 batt_ev_090 已离开，当前SOC: 84.0%，能量满足率: 72.0%
已断开电池: batt_ev_128
时间步 9: 电池 batt_ev_128 已离开，当前SOC: 42.0%，能量满足率: 0.0%
已断开电池: batt_ev_173
时间步 9: 电池 batt_ev_173 已离开，当前SOC: 80.1%，能量满足率: 56.3%
已断开电池: batt_ev_132
时间步 9: 电池 batt_ev_132 已离开，当前SOC: 46.3%，能量满足率: 35.4%
奖励各项的值：powerloss=-0.20062329046508653, voltage=-0.4736524639198203, ctrl=-0.0, connection=0.264, completion=0.2727272727272727, energy=0.6408685305511743, transformer=0.
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
智能体的动作为: [ 1.         -0.         -1.         -0.16031268 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 100.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=95.20000000000002，设置charger_power=47.19999999999999失败。
功率需求: 30.00 kW, 充电桩功率: 95.20 kW, 最终充电功率: 30.00 kW。
初次设置charger_power=19.23752188682556。
功率需求: 80.00 kW, 充电桩功率: 19.24 kW, 最终充电功率: 19.24 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=50.400000000000006。
功率需求: 48.00 kW, 充电桩功率: 50.40 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=26.560000000000002失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_191 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 19.23752188682556, -3.906345428256138
已在 set_all_batteries_before_solve 中设置 batt_ev_161 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.18 更新为 0.18。
SOC从 0.86 更新为 0.95。
SOC从 0.22 更新为 0.29。
SOC从 0.48 更新为 0.69。
SOC从 0.22 更新为 0.50。
SOC从 0.82 更新为 0.99。
SOC从 0.28 更新为 0.57。
SOC从 0.38 更新为 0.62。
SOC从 0.40 更新为 0.66。
SOC从 0.87 更新为 0.94。
已断开电池: batt_ev_096
时间步 10 执行前: 电池 batt_ev_096 已充满 (SOC: 94.4%)，离开
已断开电池: batt_ev_220
时间步 10 执行前: 电池 batt_ev_220 已充满 (SOC: 94.9%)，离开
已断开电池: batt_ev_150
时间步 10: 电池 batt_ev_150 已离开，当前SOC: 65.7%，能量满足率: 64.1%
已断开电池: batt_ev_191
时间步 10: 电池 batt_ev_191 已离开，当前SOC: 18.0%，能量满足率: 0.0%
已断开电池: batt_ev_161
时间步 10: 电池 batt_ev_161 已离开，当前SOC: 49.8%，能量满足率: 36.5%
奖励各项的值：powerloss=-0.21217401549969406, voltage=-0.45539859313438624, ctrl=-0.0, connection=0.304, completion=0.2894736842105263, energy=0.6356627427694154, transformer=0.
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
智能体的动作为: [ 1.        -0.        -1.        -0.3056047 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=0.0。
功率需求: 80.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=76.79999999999998。
功率需求: 48.00 kW, 充电桩功率: 76.80 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=19.23752188682556，设置charger_power=36.672563552856445失败。
功率需求: 80.00 kW, 充电桩功率: 19.24 kW, 最终充电功率: 19.24 kW。
已有历史设置self.charger_power=120.0，设置charger_power=116.39999999999998失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=50.400000000000006，设置charger_power=2.3999999999999773失败。
功率需求: 30.00 kW, 充电桩功率: 50.40 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=62.32000000000001。
功率需求: 36.00 kW, 充电桩功率: 62.32 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 19.23752188682556, -3.906345428256138
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_008 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_085 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.18 更新为 0.18。
SOC从 0.68 更新为 0.88。
SOC从 0.29 更新为 0.36。
SOC从 0.69 更新为 0.85。
SOC从 0.28 更新为 0.51。
SOC从 0.99 更新为 1.00。
SOC从 0.57 更新为 0.75。
SOC从 0.62 更新为 0.79。
SOC从 0.42 更新为 0.66。
SOC从 0.62 更新为 0.84。
已断开电池: batt_ev_016
时间步 11: 电池 batt_ev_016 已离开，当前SOC: 85.2%，能量满足率: 83.1%
已断开电池: batt_ev_193
时间步 11: 电池 batt_ev_193 已离开，当前SOC: 36.4%，能量满足率: 18.9%
已断开电池: batt_ev_186
时间步 11 执行前: 电池 batt_ev_186 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_008
时间步 11 执行前: 电池 batt_ev_008 已充满 (SOC: 88.0%)，离开
已断开电池: batt_ev_085
时间步 11 执行前: 电池 batt_ev_085 已充满 (SOC: 84.0%)，离开
奖励各项的值：powerloss=-0.21897931471368984, voltage=-0.49037345379421726, ctrl=-0.0, connection=0.34400000000000003, completion=0.32558139534883723, energy=0.6552356501867007, transformer=0.
时间步 11: 电池 batt_ev_222 已错过离开时间，无法接入
已连接电池 batt_ev_114, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_114 已接入
已连接电池 batt_ev_009, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_009 已接入
已连接电池 batt_ev_113, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_065, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_203, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [ 0.32900715 -0.         -1.         -0.6885119  -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
self.charger_power=0.0 改为 0.0。
功率需求: 80.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=16.319999999999993。
功率需求: 15.00 kW, 充电桩功率: 16.32 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=82.62142896652222。
功率需求: 120.00 kW, 充电桩功率: 82.62 kW, 最终充电功率: 82.62 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=82.08000000000001。
功率需求: 36.00 kW, 充电桩功率: 82.08 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=87.68失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=70.80000000000001失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 82.62142896652222, -16.776996705609513
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.18 更新为 0.18。
SOC从 0.92 更新为 0.99。
SOC从 0.18 更新为 0.38。
SOC从 0.28 更新为 0.67。
SOC从 0.51 更新为 0.65。
SOC从 0.62 更新为 0.79。
SOC从 0.75 更新为 0.86。
SOC从 0.79 更新为 0.91。
SOC从 0.66 更新为 0.84。
SOC从 0.28 更新为 0.62。
已断开电池: batt_ev_194
时间步 12: 电池 batt_ev_194 已离开，当前SOC: 86.1%，能量满足率: 83.1%
已断开电池: batt_ev_170
时间步 12: 电池 batt_ev_170 已离开，当前SOC: 84.4%，能量满足率: 75.8%
奖励各项的值：powerloss=-0.22449100415771156, voltage=-0.509365973000897, ctrl=-0.0, connection=0.36, completion=0.3111111111111111, energy=0.6614060777701565, transformer=0.
已连接电池 batt_ev_011, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 12 执行前: 排队电池 batt_ev_011 已接入
已连接电池 batt_ev_041, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [ 0.3581891 -0.        -1.        -0.6829045 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
self.charger_power=0.0 改为 0.0。
功率需求: 80.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=16.319999999999993，设置charger_power=1.3199999999999932失败。
功率需求: 15.00 kW, 充电桩功率: 16.32 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=82.62142896652222，设置charger_power=81.94853782653809失败。
功率需求: 96.00 kW, 充电桩功率: 82.62 kW, 最终充电功率: 82.62 kW。
已有历史设置self.charger_power=120.0，设置charger_power=101.75999999999999失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=91.19999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=82.08000000000001，设置charger_power=46.08000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 82.08 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=30.80000000000001失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=66.72失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 82.62142896652222, -16.776996705609513
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_011 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.18 更新为 0.18。
SOC从 0.99 更新为 1.00。
SOC从 0.38 更新为 0.58。
SOC从 0.67 更新为 0.90。
SOC从 0.65 更新为 0.79。
SOC从 0.79 更新为 0.90。
SOC从 0.32 更新为 0.55。
SOC从 0.91 更新为 0.98。
SOC从 0.12 更新为 0.49。
SOC从 0.62 更新为 0.83。
已断开电池: batt_ev_078
时间步 13 执行前: 电池 batt_ev_078 已充满 (SOC: 98.3%)，离开
已断开电池: batt_ev_000
时间步 13: 电池 batt_ev_000 已离开，当前SOC: 18.0%，能量满足率: 0.0%
已断开电池: batt_ev_162
时间步 13: 电池 batt_ev_162 已离开，当前SOC: 78.8%，能量满足率: 72.5%
已断开电池: batt_ev_114
时间步 13 执行前: 电池 batt_ev_114 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_011
时间步 13: 电池 batt_ev_011 已离开，当前SOC: 54.9%，能量满足率: 34.6%
奖励各项的值：powerloss=-0.22565483946646042, voltage=-0.5479077789617226, ctrl=-0.0, connection=0.4, completion=0.32, energy=0.6566973714250424, transformer=0.
已连接电池 batt_ev_232, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_232 已接入
已连接电池 batt_ev_237, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_237 已接入
已连接电池 batt_ev_052, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_052 已接入
已连接电池 batt_ev_206, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 62kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_206 已接入
已连接电池 batt_ev_172, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
智能体的动作为: [ 0.21177936 -0.         -1.         -0.7099162  -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=60.72。
功率需求: 24.00 kW, 充电桩功率: 60.72 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=82.62142896652222，设置charger_power=85.18994092941284失败。
功率需求: 72.00 kW, 充电桩功率: 82.62 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=29.75999999999999失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=82.08000000000001，设置charger_power=22.080000000000013失败。
功率需求: 15.00 kW, 充电桩功率: 82.08 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=99.2。
功率需求: 48.00 kW, 充电桩功率: 99.20 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=110.08失败。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=30.72失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_052 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_206 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.38 更新为 0.38。
SOC从 0.78 更新为 0.87。
SOC从 0.58 更新为 0.76。
SOC从 0.90 更新为 1.00。
SOC从 0.38 更新为 0.58。
SOC从 0.90 更新为 0.97。
SOC从 0.22 更新为 0.46。
SOC从 0.38 更新为 0.68。
SOC从 0.49 更新为 0.79。
SOC从 0.83 更新为 0.96。
已断开电池: batt_ev_113
时间步 14 执行前: 电池 batt_ev_113 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_065
时间步 14: 电池 batt_ev_065 已离开，当前SOC: 96.7%，能量满足率: 96.5%
已断开电池: batt_ev_203
时间步 14: 电池 batt_ev_203 已离开，当前SOC: 96.2%，能量满足率: 97.4%
已断开电池: batt_ev_206
时间步 14: 电池 batt_ev_206 已离开，当前SOC: 46.2%，能量满足率: 40.3%
奖励各项的值：powerloss=-0.22030754360333543, voltage=-0.5422600976838998, ctrl=-0.0, connection=0.432, completion=0.3148148148148148, energy=0.6699375282327632, transformer=0.
已连接电池 batt_ev_229, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_229 已接入
已连接电池 batt_ev_164, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_164 已接入
已连接电池 batt_ev_134, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_214, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 80kWh，并创BMS。
智能体的动作为: [-1.         -0.32844636 -1.         -0.93171513 -0.7831229  -1.
 -1.         -1.         -1.         -1.         -1.        ]
self.charger_power=0.0 改为 39.41356301307678。
功率需求: 48.00 kW, 充电桩功率: 39.41 kW, 最终充电功率: 39.41 kW。
已有历史设置self.charger_power=60.72，设置charger_power=36.72失败。
功率需求: 15.00 kW, 充电桩功率: 60.72 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=82.62142896652222，设置charger_power=100.56失败。
功率需求: 48.00 kW, 充电桩功率: 82.62 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=93.97474765777588。
功率需求: 48.00 kW, 充电桩功率: 93.97 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=100.80000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=99.2，设置charger_power=51.2失败。
功率需求: 36.00 kW, 充电桩功率: 99.20 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=46.08000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 39.41356301307678, -8.003265316249294
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_052 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.38 更新为 0.53。
SOC从 0.87 更新为 0.92。
SOC从 0.76 更新为 0.87。
SOC从 0.38 更新为 0.58。
SOC从 0.58 更新为 0.73。
SOC从 0.42 更新为 0.63。
SOC从 0.32 更新为 0.62。
SOC从 0.68 更新为 0.91。
SOC从 0.79 更新为 0.93。
SOC从 0.48 更新为 0.73。
已断开电池: batt_ev_009
时间步 15: 电池 batt_ev_009 已离开，当前SOC: 87.2%，能量满足率: 86.6%
已断开电池: batt_ev_232
时间步 15: 电池 batt_ev_232 已离开，当前SOC: 53.2%，能量满足率: 25.3%
已断开电池: batt_ev_052
时间步 15 执行前: 电池 batt_ev_052 已充满 (SOC: 73.0%)，离开
奖励各项的值：powerloss=-0.23086473459240617, voltage=-0.4733095801282716, ctrl=-0.0, connection=0.456, completion=0.3157894736842105, energy=0.6718372738195761, transformer=0.
已连接电池 batt_ev_143, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_143 已接入
已连接电池 batt_ev_245, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_245 已接入
已连接电池 batt_ev_098, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_098 已接入
智能体的动作为: [-0.75835806 -0.10745862 -1.         -0.87841135 -0.9369783  -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=12.895034551620483。
功率需求: 64.00 kW, 充电桩功率: 12.90 kW, 最终充电功率: 12.90 kW。
已有历史设置self.charger_power=60.72，设置charger_power=21.72失败。
功率需求: 15.00 kW, 充电桩功率: 60.72 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=105.40936231613159。
功率需求: 48.00 kW, 充电桩功率: 105.41 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=93.97474765777588，设置charger_power=100.80000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 93.97 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=84.24000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=82.88失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=99.2，设置charger_power=15.199999999999989失败。
功率需求: 15.00 kW, 充电桩功率: 99.20 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=14.080000000000013失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=86.4失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 75.83580613136292, 24.926024078804772
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 12.895034551620483, -2.618448444881261
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.48 更新为 0.53。
SOC从 0.92 更新为 0.98。
SOC从 0.38 更新为 0.56。
SOC从 0.58 更新为 0.73。
SOC从 0.42 更新为 0.65。
SOC从 0.63 更新为 0.79。
SOC从 0.62 更新为 0.84。
SOC从 0.91 更新为 1.00。
SOC从 0.93 更新为 1.00。
SOC从 0.73 更新为 0.86。
已断开电池: batt_ev_041
时间步 16 执行前: 电池 batt_ev_041 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_237
时间步 16: 电池 batt_ev_237 已离开，当前SOC: 97.6%，能量满足率: 97.8%
已断开电池: batt_ev_172
时间步 16 执行前: 电池 batt_ev_172 已充满 (SOC: 99.9%)，离开
奖励各项的值：powerloss=-0.22128865313962498, voltage=-0.4805650403749673, ctrl=-0.0, connection=0.48, completion=0.3333333333333333, energy=0.6878830912880177, transformer=0.
已连接电池 batt_ev_190, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 63kWh，并创BMS。
时间步 16 执行前: 排队电池 batt_ev_190 已接入
已连接电池 batt_ev_069, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 56kWh，并创BMS。
已连接电池 batt_ev_071, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
智能体的动作为: [-1.         -0.9203657  -0.99373454 -0.97350043 -0.5405632  -1.
 -1.         -1.         -1.         -1.         -0.97441524]
已有历史设置self.charger_power=12.895034551620483，设置charger_power=109.84失败。
功率需求: 48.00 kW, 充电桩功率: 12.90 kW, 最终充电功率: 12.90 kW。
初次设置charger_power=119.24814462661743。
功率需求: 100.00 kW, 充电桩功率: 119.25 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=105.40936231613159，设置charger_power=115.68失败。
功率需求: 36.00 kW, 充电桩功率: 105.41 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=93.97474765777588，设置charger_power=64.80000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 93.97 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=98.4失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.24000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=34.879999999999995失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=46.39999999999998失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 12.895034551620483, -2.618448444881261
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.53 更新为 0.59。
SOC从 0.18 更新为 0.58。
SOC从 0.56 更新为 0.70。
SOC从 0.73 更新为 0.83。
SOC从 0.65 更新为 0.82。
SOC从 0.79 更新为 0.89。
SOC从 0.84 更新为 0.99。
SOC从 0.38 更新为 0.59。
SOC从 0.42 更新为 0.63。
SOC从 0.86 更新为 0.93。
已断开电池: batt_ev_134
时间步 17 执行前: 电池 batt_ev_134 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_214
时间步 17: 电池 batt_ev_214 已离开，当前SOC: 93.3%，能量满足率: 90.6%
已断开电池: batt_ev_245
时间步 17: 电池 batt_ev_245 已离开，当前SOC: 69.8%，能量满足率: 53.0%
奖励各项的值：powerloss=-0.23212086662666848, voltage=-0.4432387715538644, ctrl=-0.0, connection=0.504, completion=0.3333333333333333, energy=0.6938021985330808, transformer=0.
智能体的动作为: [-1.         -0.3420688  -1.         -0.921144   -0.76487184 -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=12.895034551620483，设置charger_power=41.04825496673584失败。
功率需求: 48.00 kW, 充电桩功率: 12.90 kW, 最终充电功率: 12.90 kW。
已有历史设置self.charger_power=119.24814462661743，设置charger_power=106.63999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 119.25 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=93.97474765777588，设置charger_power=40.80000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 93.97 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=50.400000000000006失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=24.24000000000001失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=90.88失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 12.895034551620483, -2.618448444881261
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.59 更新为 0.64。
SOC从 0.58 更新为 0.81。
SOC从 0.83 更新为 0.93。
SOC从 0.82 更新为 0.93。
SOC从 0.89 更新为 0.96。
SOC从 0.59 更新为 0.76。
SOC从 0.63 更新为 0.78。
已断开电池: batt_ev_229
时间步 18 执行前: 电池 batt_ev_229 已充满 (SOC: 93.0%)，离开
已断开电池: batt_ev_143
时间步 18: 电池 batt_ev_143 已离开，当前SOC: 64.4%，能量满足率: 32.7%
已断开电池: batt_ev_098
时间步 18: 电池 batt_ev_098 已离开，当前SOC: 93.4%，能量满足率: 91.8%
已断开电池: batt_ev_071
时间步 18 执行前: 电池 batt_ev_071 已充满 (SOC: 78.5%)，离开
奖励各项的值：powerloss=-0.22796609821893432, voltage=-0.28281048779778883, ctrl=-0.0, connection=0.536, completion=0.34328358208955223, energy=0.700826320621515, transformer=0.
已连接电池 batt_ev_083, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_174, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_167, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.81585133 -0.9593141  -0.4237475  -1.
 -1.         -1.         -1.         -1.         -0.9244719 ]
已有历史设置self.charger_power=119.24814462661743，设置charger_power=46.639999999999986失败。
功率需求: 40.00 kW, 充电桩功率: 119.25 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=69.11999999999998。
功率需求: 48.00 kW, 充电桩功率: 69.12 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=9.240000000000009失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=54.879999999999995失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=110.93662977218628。
功率需求: 48.00 kW, 充电桩功率: 110.94 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_083 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.81 更新为 0.97。
SOC从 0.68 更新为 0.90。
SOC从 0.96 更新为 1.00。
SOC从 0.18 更新为 0.48。
SOC从 0.76 更新为 0.86。
SOC从 0.32 更新为 0.56。
已断开电池: batt_ev_164
时间步 19 执行前: 电池 batt_ev_164 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_190
时间步 19 执行前: 电池 batt_ev_190 已充满 (SOC: 97.4%)，离开
已断开电池: batt_ev_083
时间步 19 执行前: 电池 batt_ev_083 已充满 (SOC: 90.2%)，离开
奖励各项的值：powerloss=-0.22262704825860377, voltage=-0.15879037311163247, ctrl=-0.0, connection=0.56, completion=0.37142857142857144, energy=0.7136480497377358, transformer=0.
已连接电池 batt_ev_115, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
已连接电池 batt_ev_181, 初始SOC: 56.99999999999999%, 最大功率: 80kW, 电池容量: 69kWh，并创BMS。
已连接电池 batt_ev_182, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 95kWh，并创BMS。
智能体的动作为: [-1.        -1.        -0.7601679 -0.8519338 -0.3654381 -1.
 -1.        -1.        -1.        -1.        -0.9363443]
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=43.852572441101074。
功率需求: 48.00 kW, 充电桩功率: 43.85 kW, 最终充电功率: 43.85 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=30.879999999999995失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=110.93662977218628，设置charger_power=90.72失败。
功率需求: 36.00 kW, 充电桩功率: 110.94 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 43.852572441101074, -8.904644625245624
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.12 更新为 0.45。
SOC从 0.57 更新为 0.73。
SOC从 0.28 更新为 0.60。
SOC从 0.48 更新为 0.73。
SOC从 0.86 更新为 0.93。
SOC从 0.56 更新为 0.73。
奖励各项的值：powerloss=-0.21865116762343667, voltage=-0.1026981020366935, ctrl=-0.0, connection=0.56, completion=0.37142857142857144, energy=0.7136480497377358, transformer=0.
已连接电池 batt_ev_037, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_138, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
已连接电池 batt_ev_095, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.81452245 -0.956258   -0.42724168 -1.
 -1.         -1.         -1.         -1.         -0.92654836]
已有历史设置self.charger_power=120.0，设置charger_power=101.92失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=89.44。
功率需求: 48.00 kW, 充电桩功率: 89.44 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=114.75095987319946。
功率需求: 60.00 kW, 充电桩功率: 114.75 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=43.852572441101074，设置charger_power=51.269001960754395失败。
功率需求: 32.00 kW, 充电桩功率: 43.85 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=72.47999999999999失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=15.879999999999995失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=110.93662977218628，设置charger_power=54.72失败。
功率需求: 24.00 kW, 充电桩功率: 110.94 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_138 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.45 更新为 0.71。
SOC从 0.48 更新为 0.76。
SOC从 0.12 更新为 0.43。
SOC从 0.73 更新为 0.84。
SOC从 0.60 更新为 0.79。
SOC从 0.73 更新为 0.85。
SOC从 0.93 更新为 1.00。
SOC从 0.32 更新为 0.57。
SOC从 0.73 更新为 0.85。
已断开电池: batt_ev_069
时间步 21 执行前: 电池 batt_ev_069 已充满 (SOC: 99.6%)，离开
已断开电池: batt_ev_138
时间步 21 执行前: 电池 batt_ev_138 已充满 (SOC: 75.9%)，离开
奖励各项的值：powerloss=-0.2201594918393543, voltage=-0.0585813934487156, ctrl=-0.0, connection=0.5760000000000001, completion=0.3888888888888889, energy=0.7216022705783542, transformer=0.
已连接电池 batt_ev_197, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 75kWh，并创BMS。
已连接电池 batt_ev_026, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 102kWh，并创BMS。
已连接电池 batt_ev_212, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.75758344 -0.74176526 -0.34036303 -1.
 -1.         -1.         -1.         -1.         -0.96294713]
已有历史设置self.charger_power=120.0，设置charger_power=53.91999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=90.91001272201538。
功率需求: 96.00 kW, 充电桩功率: 90.91 kW, 最终充电功率: 90.91 kW。
已有历史设置self.charger_power=114.75095987319946，设置charger_power=89.01183128356934失败。
功率需求: 48.00 kW, 充电桩功率: 114.75 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=43.852572441101074，设置charger_power=40.843563079833984失败。
功率需求: 32.00 kW, 充电桩功率: 43.85 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=81.60000000000002失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=40.47999999999999失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=112.80000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=110.93662977218628，设置charger_power=30.72失败。
功率需求: 24.00 kW, 充电桩功率: 110.94 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 90.91001272201538, -18.460065421552716
已在 set_all_batteries_before_solve 中设置 batt_ev_212 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.71 更新为 0.84。
SOC从 0.32 更新为 0.54。
SOC从 0.43 更新为 0.68。
SOC从 0.84 更新为 0.96。
SOC从 0.79 更新为 0.91。
SOC从 0.52 更新为 0.68。
SOC从 0.85 更新为 0.97。
SOC从 0.22 更新为 0.50。
SOC从 0.57 更新为 0.75。
SOC从 0.85 更新为 0.97。
已断开电池: batt_ev_174
时间步 22: 电池 batt_ev_174 已离开，当前SOC: 96.8%，能量满足率: 98.5%
已断开电池: batt_ev_167
时间步 22: 电池 batt_ev_167 已离开，当前SOC: 96.7%，能量满足率: 98.0%
已断开电池: batt_ev_115
时间步 22 执行前: 电池 batt_ev_115 已充满 (SOC: 83.7%)，离开
已断开电池: batt_ev_181
时间步 22 执行前: 电池 batt_ev_181 已充满 (SOC: 96.1%)，离开
已断开电池: batt_ev_182
时间步 22: 电池 batt_ev_182 已离开，当前SOC: 91.2%，能量满足率: 90.2%
奖励各项的值：powerloss=-0.2122042398318179, voltage=-0.04535926201385321, ctrl=-0.0, connection=0.616, completion=0.38961038961038963, energy=0.7379592176941621, transformer=0.
已连接电池 batt_ev_010, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 71kWh，并创BMS。
时间步 22 执行前: 排队电池 batt_ev_010 已接入
已连接电池 batt_ev_241, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 68kWh，并创BMS。
已连接电池 batt_ev_084, 初始SOC: 78.0%, 最大功率: 100kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_038, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
已连接电池 batt_ev_040, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
智能体的动作为: [-1.         -0.75015485 -0.7121012  -0.25696212 -0.20287177 -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=90.01858234405518。
功率需求: 96.00 kW, 充电桩功率: 90.02 kW, 最终充电功率: 90.02 kW。
已有历史设置self.charger_power=90.91001272201538，设置charger_power=85.45214653015137失败。
功率需求: 72.00 kW, 充电桩功率: 90.91 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=114.75095987319946，设置charger_power=30.83545446395874失败。
功率需求: 36.00 kW, 充电桩功率: 114.75 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=24.34461236000061。
功率需求: 48.00 kW, 充电桩功率: 24.34 kW, 最终充电功率: 24.34 kW。
初次设置charger_power=54.56。
功率需求: 40.00 kW, 充电桩功率: 54.56 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=96.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=108.48失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=64.80000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=50.16。
功率需求: 24.00 kW, 充电桩功率: 50.16 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 24.159999999999968, 7.9410079811213246
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_212 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 90.01858234405518, -18.27905276295565
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 24.34461236000061, -4.943384379475747
已在 set_all_batteries_before_solve 中设置 batt_ev_084 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.48 更新为 0.80。
SOC从 0.54 更新为 0.72。
SOC从 0.68 更新为 0.87。
SOC从 0.48 更新为 0.57。
SOC从 0.78 更新为 0.94。
SOC从 0.68 更新为 0.84。
SOC从 0.42 更新为 0.70。
SOC从 0.50 更新为 0.72。
SOC从 0.75 更新为 0.87。
SOC从 0.78 更新为 0.89。
已断开电池: batt_ev_212
时间步 23: 电池 batt_ev_212 已离开，当前SOC: 72.0%，能量满足率: 65.8%
奖励各项的值：powerloss=-0.18975900126631412, voltage=-0.10270394949517092, ctrl=-0.0, connection=0.624, completion=0.38461538461538464, energy=0.7369327499909305, transformer=0.
已连接电池 batt_ev_046, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_046 已接入
智能体的动作为: [-1.         -0.40260276 -0.8340999  -0.13396569 -0.2576274  -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=90.01858234405518，设置charger_power=48.312331438064575失败。
功率需求: 48.00 kW, 充电桩功率: 90.02 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=90.91001272201538，设置charger_power=100.09198665618896失败。
功率需求: 48.00 kW, 充电桩功率: 90.91 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=114.75095987319946，设置charger_power=16.07588231563568失败。
功率需求: 15.00 kW, 充电桩功率: 114.75 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=24.34461236000061，设置charger_power=30.915287733078003失败。
功率需求: 36.00 kW, 充电桩功率: 24.34 kW, 最终充电功率: 24.34 kW。
已有历史设置self.charger_power=54.56，设置charger_power=14.560000000000002失败。
功率需求: 25.00 kW, 充电桩功率: 54.56 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.0失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=70.56失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=113.68。
功率需求: 48.00 kW, 充电桩功率: 113.68 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=32.80000000000001失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=50.16，设置charger_power=26.159999999999997失败。
功率需求: 15.00 kW, 充电桩功率: 50.16 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 24.34461236000061, -4.943384379475747
已在 set_all_batteries_before_solve 中设置 batt_ev_084 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_046 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.80 更新为 0.97。
SOC从 0.72 更新为 0.84。
SOC从 0.87 更新为 0.95。
SOC从 0.57 更新为 0.66。
SOC从 0.94 更新为 1.00。
SOC从 0.84 更新为 0.95。
SOC从 0.70 更新为 0.90。
SOC从 0.42 更新为 0.66。
SOC从 0.87 更新为 0.95。
SOC从 0.89 更新为 0.95。
已断开电池: batt_ev_037
时间步 24: 电池 batt_ev_037 已离开，当前SOC: 95.1%，能量满足率: 95.6%
已断开电池: batt_ev_197
时间步 24: 电池 batt_ev_197 已离开，当前SOC: 94.7%，能量满足率: 92.8%
已断开电池: batt_ev_010
时间步 24 执行前: 电池 batt_ev_010 已充满 (SOC: 96.6%)，离开
已断开电池: batt_ev_084
时间步 24 执行前: 电池 batt_ev_084 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_038
时间步 24: 电池 batt_ev_038 已离开，当前SOC: 90.3%，能量满足率: 86.2%
奖励各项的值：powerloss=-0.16155011910182884, voltage=-0.18504877172098144, ctrl=-0.0, connection=0.664, completion=0.3855421686746988, energy=0.7497116946072871, transformer=0.
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
智能体的动作为: [-1.         -1.         -0.41313833 -0.0976026  -0.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=90.91001272201538，设置charger_power=49.57659959793091失败。
功率需求: 48.00 kW, 充电桩功率: 90.91 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=114.75095987319946，设置charger_power=9.960000000000008失败。
功率需求: 15.00 kW, 充电桩功率: 114.75 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=24.34461236000061，设置charger_power=0.0失败。
功率需求: 36.00 kW, 充电桩功率: 24.34 kW, 最终充电功率: 24.34 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=113.68，设置charger_power=65.68失败。
功率需求: 36.00 kW, 充电桩功率: 113.68 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=33.599999999999994。
功率需求: 25.00 kW, 充电桩功率: 33.60 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=50.16，设置charger_power=11.159999999999997失败。
功率需求: 15.00 kW, 充电桩功率: 50.16 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 24.34461236000061, -4.943384379475747
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_046 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_050 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_125 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 25.0, -5.076466515850102
SOC从 0.28 更新为 0.59。
SOC从 0.84 更新为 0.95。
SOC从 0.95 更新为 1.00。
SOC从 0.66 更新为 0.75。
SOC从 0.28 更新为 0.50。
SOC从 0.52 更新为 0.66。
SOC从 0.28 更新为 0.68。
SOC从 0.66 更新为 0.85。
SOC从 0.88 更新为 0.97。
SOC从 0.95 更新为 1.00。
已断开电池: batt_ev_095
时间步 25 执行前: 电池 batt_ev_095 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_026
时间步 25: 电池 batt_ev_026 已离开，当前SOC: 95.5%，能量满足率: 96.2%
已断开电池: batt_ev_241
时间步 25: 电池 batt_ev_241 已离开，当前SOC: 74.9%，能量满足率: 61.1%
已断开电池: batt_ev_040
时间步 25 执行前: 电池 batt_ev_040 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_046
时间步 25: 电池 batt_ev_046 已离开，当前SOC: 84.9%，能量满足率: 76.5%
已断开电池: batt_ev_050
时间步 25: 电池 batt_ev_050 已离开，当前SOC: 59.2%，能量满足率: 52.1%
已断开电池: batt_ev_125
时间步 25: 电池 batt_ev_125 已离开，当前SOC: 50.4%，能量满足率: 35.0%
奖励各项的值：powerloss=-0.14599660361369932, voltage=-0.24432229865674282, ctrl=-0.0, connection=0.72, completion=0.37777777777777777, energy=0.7492686546480598, transformer=0.
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
智能体的动作为: [-1.         -1.         -0.4115393  -0.09345018 -0.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=49.38471436500549。
功率需求: 120.00 kW, 充电桩功率: 49.38 kW, 最终充电功率: 49.38 kW。
初次设置charger_power=11.214021742343903。
功率需求: 80.00 kW, 充电桩功率: 11.21 kW, 最终充电功率: 11.21 kW。
初次设置charger_power=0.0。
功率需求: 80.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=113.28失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=96.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=33.599999999999994，设置charger_power=8.600000000000023失败。
功率需求: 25.00 kW, 充电桩功率: 33.60 kW, 最终充电功率: 25.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_141 充电的有无功功率为 49.38471436500549, -10.02799395475088
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 11.214021742343903, -2.277104235320954
已在 set_all_batteries_before_solve 中设置 batt_ev_075 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.22 更新为 0.51。
SOC从 0.28 更新为 0.44。
SOC从 0.22 更新为 0.26。
SOC从 0.42 更新为 0.42。
SOC从 0.38 更新为 0.64。
SOC从 0.66 更新为 0.81。
SOC从 0.68 更新为 0.92。
SOC从 0.38 更新为 0.59。
SOC从 0.97 更新为 1.00。
已断开电池: batt_ev_109
时间步 26 执行前: 电池 batt_ev_109 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.13705409734656054, voltage=-0.26087380954955774, ctrl=-0.0, connection=0.728, completion=0.38461538461538464, energy=0.7520239441574218, transformer=0.
已连接电池 batt_ev_031, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_057, 初始SOC: 8.0%, 最大功率: 80kW, 电池容量: 73kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.41128486 -0.09323283 -0.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=49.38471436500549，设置charger_power=49.35418367385864失败。
功率需求: 96.00 kW, 充电桩功率: 49.38 kW, 最终充电功率: 49.38 kW。
已有历史设置self.charger_power=11.214021742343903，设置charger_power=11.187939941883087失败。
功率需求: 80.00 kW, 充电桩功率: 11.21 kW, 最终充电功率: 11.21 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 80.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=108.47999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=65.27999999999997失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=24.0失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=90.88失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_141 充电的有无功功率为 49.38471436500549, -10.02799395475088
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 11.214021742343903, -2.277104235320954
已在 set_all_batteries_before_solve 中设置 batt_ev_075 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_031 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.51 更新为 0.69。
SOC从 0.44 更新为 0.61。
SOC从 0.26 更新为 0.30。
SOC从 0.42 更新为 0.42。
SOC从 0.64 更新为 0.84。
SOC从 0.81 更新为 0.90。
SOC从 0.92 更新为 1.00。
SOC从 0.59 更新为 0.76。
SOC从 0.08 更新为 0.35。
SOC从 0.42 更新为 0.72。
已断开电池: batt_ev_221
时间步 27 执行前: 电池 batt_ev_221 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_141
时间步 27: 电池 batt_ev_141 已离开，当前SOC: 60.9%，能量满足率: 47.0%
已断开电池: batt_ev_031
时间步 27 执行前: 电池 batt_ev_031 已充满 (SOC: 71.6%)，离开
奖励各项的值：powerloss=-0.13365379221784893, voltage=-0.2936539628363821, ctrl=-0.0, connection=0.752, completion=0.39361702127659576, energy=0.7543048415829955, transformer=0.
已连接电池 batt_ev_111, 初始SOC: 68.0%, 最大功率: 100kW, 电池容量: 83kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_111 已接入
已连接电池 batt_ev_006, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_006 已接入
已连接电池 batt_ev_225, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 94kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_225 已接入
智能体的动作为: [-1.         -1.         -0.41103667 -0.0926561  -0.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=120.0，设置charger_power=84.16失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=49.324400424957275。
功率需求: 60.00 kW, 充电桩功率: 49.32 kW, 最终充电功率: 49.32 kW。
已有历史设置self.charger_power=11.214021742343903，设置charger_power=11.118731796741486失败。
功率需求: 64.00 kW, 充电桩功率: 11.21 kW, 最终充电功率: 11.21 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 80.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.47999999999999失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=33.27999999999997失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=103.20000000000002。
功率需求: 36.00 kW, 充电桩功率: 103.20 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=54.879999999999995失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 11.214021742343903, -2.277104235320954
已在 set_all_batteries_before_solve 中设置 batt_ev_075 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 49.324400424957275, -10.015746686867129
已在 set_all_batteries_before_solve 中设置 batt_ev_006 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_225 充电的有无功功率为 72.0, -14.620223565648296
SOC从 0.69 更新为 0.87。
SOC从 0.68 更新为 0.83。
SOC从 0.30 更新为 0.34。
SOC从 0.42 更新为 0.42。
SOC从 0.84 更新为 0.97。
SOC从 0.90 更新为 0.96。
SOC从 0.57 更新为 0.72。
SOC从 0.76 更新为 0.86。
SOC从 0.35 更新为 0.57。
SOC从 0.52 更新为 0.71。
已断开电池: batt_ev_137
时间步 28: 电池 batt_ev_137 已离开，当前SOC: 96.0%，能量满足率: 95.8%
已断开电池: batt_ev_047
时间步 28: 电池 batt_ev_047 已离开，当前SOC: 86.2%，能量满足率: 80.4%
已断开电池: batt_ev_006
时间步 28: 电池 batt_ev_006 已离开，当前SOC: 72.0%，能量满足率: 71.4%
奖励各项的值：powerloss=-0.12904642100528715, voltage=-0.27735810961865504, ctrl=-0.0, connection=0.776, completion=0.38144329896907214, energy=0.7564955586337786, transformer=0.
已连接电池 batt_ev_054, 初始SOC: 82.0%, 最大功率: 120kW, 电池容量: 85kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_054 已接入
已连接电池 batt_ev_129, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 94kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_129 已接入
已连接电池 batt_ev_088, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 50kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_088 已接入
智能体的动作为: [-1.         -1.         -0.41261086 -0.09653362 -0.         -1.
 -1.         -1.         -1.         -1.         -0.99698865]
已有历史设置self.charger_power=120.0，设置charger_power=36.16失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=49.324400424957275，设置charger_power=49.51330304145813失败。
功率需求: 40.00 kW, 充电桩功率: 49.32 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=11.214021742343903，设置charger_power=11.584034264087677失败。
功率需求: 64.00 kW, 充电桩功率: 11.21 kW, 最终充电功率: 11.21 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 80.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=8.480000000000018失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=61.19999999999999。
功率需求: 48.00 kW, 充电桩功率: 61.20 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=108.48000000000002失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 11.214021742343903, -2.277104235320954
已在 set_all_batteries_before_solve 中设置 batt_ev_075 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_225 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.87 更新为 0.94。
SOC从 0.83 更新为 0.95。
SOC从 0.34 更新为 0.38。
SOC从 0.42 更新为 0.42。
SOC从 0.97 更新为 1.00。
SOC从 0.82 更新为 0.96。
SOC从 0.28 更新为 0.55。
SOC从 0.38 更新为 0.62。
SOC从 0.57 更新为 0.74。
SOC从 0.71 更新为 0.84。
已断开电池: batt_ev_034
时间步 29: 电池 batt_ev_034 已离开，当前SOC: 94.1%，能量满足率: 94.8%
已断开电池: batt_ev_101
时间步 29: 电池 batt_ev_101 已离开，当前SOC: 38.5%，能量满足率: 21.7%
已断开电池: batt_ev_075
时间步 29: 电池 batt_ev_075 已离开，当前SOC: 42.0%，能量满足率: 0.0%
已断开电池: batt_ev_093
时间步 29 执行前: 电池 batt_ev_093 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_057
时间步 29: 电池 batt_ev_057 已离开，当前SOC: 73.8%，能量满足率: 88.9%
已断开电池: batt_ev_225
时间步 29: 电池 batt_ev_225 已离开，当前SOC: 83.9%，能量满足率: 69.4%
奖励各项的值：powerloss=-0.1327989709326594, voltage=-0.28098350546875484, ctrl=-0.0, connection=0.8240000000000001, completion=0.36893203883495146, energy=0.7488086572467291, transformer=0.
已连接电池 batt_ev_007, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 84kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_007 已接入
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
智能体的动作为: [-1.         -1.         -0.41225207 -0.09566655 -0.         -1.
 -1.         -1.         -1.         -1.         -0.99827325]
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=49.324400424957275，设置charger_power=16.920000000000016失败。
功率需求: 25.00 kW, 充电桩功率: 49.32 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=11.479986011981964。
功率需求: 96.00 kW, 充电桩功率: 11.48 kW, 最终充电功率: 11.48 kW。
初次设置charger_power=0.0。
功率需求: 36.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=61.19999999999999，设置charger_power=13.199999999999989失败。
功率需求: 30.00 kW, 充电桩功率: 61.20 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=76.0失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=119.79279041290283。
功率需求: 72.00 kW, 充电桩功率: 119.79 kW, 最终充电功率: 72.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_007 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 11.479986011981964, -2.3311105836901604
已在 set_all_batteries_before_solve 中设置 batt_ev_147 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 72.0, -14.620223565648296
SOC从 0.32 更新为 0.56。
SOC从 0.95 更新为 1.00。
SOC从 0.32 更新为 0.35。
SOC从 0.52 更新为 0.52。
SOC从 0.08 更新为 0.40。
SOC从 0.96 更新为 1.00。
SOC从 0.55 更新为 0.71。
SOC从 0.62 更新为 0.80。
SOC从 0.32 更新为 0.53。
SOC从 0.62 更新为 0.79。
已断开电池: batt_ev_111
时间步 30 执行前: 电池 batt_ev_111 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_054
时间步 30 执行前: 电池 batt_ev_054 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_007
时间步 30: 电池 batt_ev_007 已离开，当前SOC: 55.8%，能量满足率: 36.1%
已断开电池: batt_ev_147
时间步 30: 电池 batt_ev_147 已离开，当前SOC: 52.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.14978562651936092, voltage=-0.3020227691297417, ctrl=-0.0, connection=0.856, completion=0.37383177570093457, energy=0.7428788977304995, transformer=0.
已连接电池 batt_ev_017, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_017 已接入
已连接电池 batt_ev_087, 初始SOC: 62.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_087 已接入
时间步 30: 电池 batt_ev_021 已错过离开时间，无法接入
已连接电池 batt_ev_209, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_209 已接入
已连接电池 batt_ev_178, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 93kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_178 已接入
智能体的动作为: [-1.         -1.         -0.41097283 -0.09250586 -0.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=49.31674003601074。
功率需求: 60.00 kW, 充电桩功率: 49.32 kW, 最终充电功率: 49.32 kW。
已有历史设置self.charger_power=11.479986011981964，设置charger_power=11.100703775882721失败。
功率需求: 96.00 kW, 充电桩功率: 11.48 kW, 最终充电功率: 11.48 kW。
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=110.72000000000003失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=40.0失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=119.79279041290283，设置charger_power=89.12失败。
功率需求: 48.00 kW, 充电桩功率: 119.79 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 11.479986011981964, -2.3311105836901604
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 49.31674003601074, -10.014191178547708
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_178 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.28 更新为 0.51。
SOC从 0.62 更新为 0.76。
SOC从 0.35 更新为 0.38。
SOC从 0.38 更新为 0.38。
SOC从 0.40 更新为 0.66。
SOC从 0.42 更新为 0.64。
SOC从 0.71 更新为 0.81。
SOC从 0.80 更新为 0.92。
SOC从 0.53 更新为 0.68。
SOC从 0.79 更新为 0.90。
已断开电池: batt_ev_142
时间步 31: 电池 batt_ev_142 已离开，当前SOC: 37.7%，能量满足率: 9.6%
已断开电池: batt_ev_211
时间步 31 执行前: 电池 batt_ev_211 已充满 (SOC: 90.3%)，离开
奖励各项的值：powerloss=-0.16353290038350377, voltage=-0.2554487197718891, ctrl=-0.0, connection=0.872, completion=0.3761467889908257, energy=0.7393000800351388, transformer=0.
已连接电池 batt_ev_110, 初始SOC: 22.0%, 最大功率: 100kW, 电池容量: 65kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_110 已接入
已连接电池 batt_ev_112, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 71kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_112 已接入
智能体的动作为: [-1.        -1.        -0.4109866 -0.0925413 -0.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=49.31674003601074，设置charger_power=49.318392276763916失败。
功率需求: 40.00 kW, 充电桩功率: 49.32 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=11.104955971240997。
功率需求: 100.00 kW, 充电桩功率: 11.10 kW, 最终充电功率: 11.10 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=107.03999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=70.72000000000003失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=16.0失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_178 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_110 充电的有无功功率为 11.104955971240997, -2.2549574859197836
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.51 更新为 0.64。
SOC从 0.76 更新为 0.87。
SOC从 0.22 更新为 0.26。
SOC从 0.38 更新为 0.38。
SOC从 0.66 更新为 0.85。
SOC从 0.64 更新为 0.80。
SOC从 0.81 更新为 0.92。
SOC从 0.92 更新为 0.99。
SOC从 0.68 更新为 0.84。
SOC从 0.22 更新为 0.50。
已断开电池: batt_ev_129
时间步 32 执行前: 电池 batt_ev_129 已充满 (SOC: 91.8%)，离开
已断开电池: batt_ev_088
时间步 32 执行前: 电池 batt_ev_088 已充满 (SOC: 99.5%)，离开
已断开电池: batt_ev_079
时间步 32: 电池 batt_ev_079 已离开，当前SOC: 84.9%，能量满足率: 85.5%
已断开电池: batt_ev_053
时间步 32: 电池 batt_ev_053 已离开，当前SOC: 84.1%，能量满足率: 78.9%
已断开电池: batt_ev_087
时间步 32: 电池 batt_ev_087 已离开，当前SOC: 86.5%，能量满足率: 81.8%
已断开电池: batt_ev_178
时间步 32: 电池 batt_ev_178 已离开，当前SOC: 79.6%，能量满足率: 67.2%
已断开电池: batt_ev_110
时间步 32: 电池 batt_ev_110 已离开，当前SOC: 26.3%，能量满足率: 7.1%
奖励各项的值：powerloss=-0.17876981204140385, voltage=-0.2379978641265379, ctrl=-0.0, connection=0.928, completion=0.3706896551724138, energy=0.7395588342470333, transformer=0.
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
智能体的动作为: [-1.         -1.         -0.44248527 -0.15126018 -0.         -0.9913849
 -1.         -0.92052275 -1.         -1.         -0.9149862 ]
已有历史设置self.charger_power=120.0，设置charger_power=94.08000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=53.09823274612427。
功率需求: 100.00 kW, 充电桩功率: 53.10 kW, 最终充电功率: 53.10 kW。
初次设置charger_power=18.151221871376038。
功率需求: 60.00 kW, 充电桩功率: 18.15 kW, 最终充电功率: 18.15 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=118.96619081497192。
功率需求: 100.00 kW, 充电桩功率: 118.97 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=65.28。
功率需求: 36.00 kW, 充电桩功率: 65.28 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=110.46272993087769。
功率需求: 60.00 kW, 充电桩功率: 110.46 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=41.04000000000002。
功率需求: 24.00 kW, 充电桩功率: 41.04 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=109.79834318161011失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_223 充电的有无功功率为 53.09823274612427, -10.782056023460612
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 18.151221871376038, -3.6857628020722597
已在 set_all_batteries_before_solve 中设置 batt_ev_198 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.64 更新为 0.78。
SOC从 0.22 更新为 0.38。
SOC从 0.28 更新为 0.37。
SOC从 0.38 更新为 0.38。
SOC从 0.08 更新为 0.36。
SOC从 0.68 更新为 0.86。
SOC从 0.12 更新为 0.47。
SOC从 0.32 更新为 0.50。
SOC从 0.82 更新为 0.93。
SOC从 0.50 更新为 0.67。
已断开电池: batt_ev_017
时间步 33: 电池 batt_ev_017 已离开，当前SOC: 78.0%，能量满足率: 71.4%
已断开电池: batt_ev_209
时间步 33: 电池 batt_ev_209 已离开，当前SOC: 38.0%，能量满足率: 0.0%
已断开电池: batt_ev_112
时间步 33: 电池 batt_ev_112 已离开，当前SOC: 67.1%，能量满足率: 75.1%
已断开电池: batt_ev_223
时间步 33: 电池 batt_ev_223 已离开，当前SOC: 38.4%，能量满足率: 32.8%
已断开电池: batt_ev_198
时间步 33: 电池 batt_ev_198 已离开，当前SOC: 36.4%，能量满足率: 33.8%
奖励各项的值：powerloss=-0.19830944026253705, voltage=-0.3097507321276671, ctrl=-0.0, connection=0.968, completion=0.35537190082644626, energy=0.7266127436368005, transformer=0.
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
智能体的动作为: [-1.         -1.         -0.43891934 -0.14604498 -0.         -1.
 -1.         -0.9348306  -1.         -1.         -0.9224422 ]
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=52.67032027244568。
功率需求: 60.00 kW, 充电桩功率: 52.67 kW, 最终充电功率: 52.67 kW。
已有历史设置self.charger_power=18.151221871376038，设置charger_power=17.52539813518524失败。
功率需求: 48.00 kW, 充电桩功率: 18.15 kW, 最终充电功率: 18.15 kW。
初次设置charger_power=0.0。
功率需求: 80.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=65.28，设置charger_power=29.28失败。
功率需求: 15.00 kW, 充电桩功率: 65.28 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=110.46272993087769，设置charger_power=91.36失败。
功率需求: 48.00 kW, 充电桩功率: 110.46 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=41.04000000000002，设置charger_power=17.039999999999992失败。
功率需求: 15.00 kW, 充电桩功率: 41.04 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=83.2。
功率需求: 48.00 kW, 充电桩功率: 83.20 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 18.151221871376038, -3.6857628020722597
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_155 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_094 充电的有无功功率为 52.67032027244568, -10.695164689686854
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_068 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_185 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.52 更新为 0.68。
SOC从 0.28 更新为 0.52。
SOC从 0.37 更新为 0.47。
SOC从 0.38 更新为 0.38。
SOC从 0.18 更新为 0.42。
SOC从 0.86 更新为 0.93。
SOC从 0.47 更新为 0.75。
SOC从 0.50 更新为 0.67。
SOC从 0.93 更新为 0.99。
SOC从 0.48 更新为 0.78。
已断开电池: batt_ev_207
时间步 34: 电池 batt_ev_207 已离开，当前SOC: 46.9%，能量满足率: 27.0%
已断开电池: batt_ev_152
时间步 34 执行前: 电池 batt_ev_152 已充满 (SOC: 93.0%)，离开
已断开电池: batt_ev_171
时间步 34: 电池 batt_ev_171 已离开，当前SOC: 74.8%，能量满足率: 78.5%
已断开电池: batt_ev_022
时间步 34: 电池 batt_ev_022 已离开，当前SOC: 67.3%，能量满足率: 53.5%
已断开电池: batt_ev_028
时间步 34: 电池 batt_ev_028 已离开，当前SOC: 99.1%，能量满足率: 95.0%
已断开电池: batt_ev_068
时间步 34: 电池 batt_ev_068 已离开，当前SOC: 42.2%，能量满足率: 40.3%
奖励各项的值：powerloss=-0.2105566125181779, voltage=-0.32842376137385276, ctrl=-0.0, connection=1.016, completion=0.3464566929133858, energy=0.7233349713277354, transformer=0.
已连接电池 batt_ev_049, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
已连接电池 batt_ev_023, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.8246156  -0.16865759 -0.         -0.8144232
 -1.         -0.40388942 -0.3072973  -1.         -0.98638135]
已有历史设置self.charger_power=120.0，设置charger_power=97.91999999999999失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=52.67032027244568，设置charger_power=98.95387172698975失败。
功率需求: 36.00 kW, 充电桩功率: 52.67 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=20.23891031742096。
功率需求: 48.00 kW, 充电桩功率: 20.24 kW, 最终充电功率: 20.24 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 80.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=17.599999999999994。
功率需求: 15.00 kW, 充电桩功率: 17.60 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=83.2，设置charger_power=35.2失败。
功率需求: 24.00 kW, 充电桩功率: 83.20 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_155 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_094 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_185 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_049 充电的有无功功率为 20.23891031742096, -4.109686021747226
已在 set_all_batteries_before_solve 中设置 batt_ev_023 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.68 更新为 0.84。
SOC从 0.52 更新为 0.68。
SOC从 0.32 更新为 0.42。
SOC从 0.38 更新为 0.38。
SOC从 0.92 更新为 0.99。
SOC从 0.78 更新为 0.93。
已断开电池: batt_ev_155
时间步 35: 电池 batt_ev_155 已离开，当前SOC: 83.6%，能量满足率: 68.6%
已断开电池: batt_ev_094
时间步 35: 电池 batt_ev_094 已离开，当前SOC: 67.6%，能量满足率: 56.6%
已断开电池: batt_ev_185
时间步 35 执行前: 电池 batt_ev_185 已充满 (SOC: 93.0%)，离开
奖励各项的值：powerloss=-0.2100198862714074, voltage=-0.2990482754145751, ctrl=-0.0, connection=1.04, completion=0.34615384615384615, energy=0.7239661649149802, transformer=0.
已连接电池 batt_ev_121, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [-1.         -1.         -1.         -1.         -0.41547203 -1.
 -1.         -1.         -1.         -1.         -0.9396512 ]
已有历史设置self.charger_power=20.23891031742096，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 20.24 kW, 最终充电功率: 20.24 kW。
self.charger_power=0.0 改为 49.85664367675781。
功率需求: 80.00 kW, 充电桩功率: 49.86 kW, 最终充电功率: 49.86 kW。
已有历史设置self.charger_power=17.599999999999994，设置charger_power=2.5999999999999943失败。
功率需求: 15.00 kW, 充电桩功率: 17.60 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 49.85664367675781, -10.12382328870923
已在 set_all_batteries_before_solve 中设置 batt_ev_049 充电的有无功功率为 20.23891031742096, -4.109686021747226
已在 set_all_batteries_before_solve 中设置 batt_ev_023 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.42 更新为 0.51。
SOC从 0.38 更新为 0.57。
SOC从 0.99 更新为 1.00。
SOC从 0.48 更新为 0.75。
已断开电池: batt_ev_140
时间步 36: 电池 batt_ev_140 已离开，当前SOC: 56.6%，能量满足率: 31.0%
已断开电池: batt_ev_049
时间步 36: 电池 batt_ev_049 已离开，当前SOC: 51.1%，能量满足率: 28.9%
已断开电池: batt_ev_023
时间步 36 执行前: 电池 batt_ev_023 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.2148170117787202, voltage=-0.3844534386179199, ctrl=-0.0, connection=1.064, completion=0.3458646616541353, energy=0.7196606004797316, transformer=0.
智能体的动作为: [-1.        -1.        -1.        -1.        -0.31329   -1.
 -1.        -1.        -1.        -1.        -0.9275898]
已有历史设置self.charger_power=120.0，设置charger_power=58.72失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 32.0, -6.497877140288132
SOC从 0.75 更新为 0.89。
奖励各项的值：powerloss=-0.2114319752221644, voltage=-0.4179660714929079, ctrl=-0.0, connection=1.064, completion=0.3458646616541353, energy=0.7196606004797316, transformer=0.
已连接电池 batt_ev_015, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
已连接电池 batt_ev_201, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [-1.         -0.30545306 -1.         -0.72905    -0.95450115 -1.
 -1.         -0.6713614  -1.         -1.         -0.70627314]
已有历史设置self.charger_power=120.0，设置charger_power=26.72失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=80.56336641311646。
功率需求: 36.00 kW, 充电桩功率: 80.56 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.89 更新为 0.97。
SOC从 0.52 更新为 0.67。
SOC从 0.18 更新为 0.47。
已断开电池: batt_ev_121
时间步 38: 电池 batt_ev_121 已离开，当前SOC: 97.2%，能量满足率: 98.3%
奖励各项的值：powerloss=-0.2163838596189619, voltage=-0.450043400944935, ctrl=-0.0, connection=1.072, completion=0.34328358208955223, energy=0.7216261993377756, transformer=0.
已连接电池 batt_ev_080, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_204, 初始SOC: 2.0%, 最大功率: 80kW, 电池容量: 81kWh，并创BMS。
智能体的动作为: [-1.        -1.        -1.        -1.        -0.        -1.
 -1.        -0.9390169 -1.        -1.        -0.7056498]
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=80.56336641311646，设置charger_power=81.12失败。
功率需求: 36.00 kW, 充电桩功率: 80.56 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=92.88000000000001。
功率需求: 36.00 kW, 充电桩功率: 92.88 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.02 更新为 0.27。
SOC从 0.67 更新为 0.82。
SOC从 0.47 更新为 0.70。
SOC从 0.57 更新为 0.74。
奖励各项的值：powerloss=-0.2190917823409737, voltage=-0.45147739786214336, ctrl=-0.0, connection=1.072, completion=0.34328358208955223, energy=0.7216261993377756, transformer=0.
已连接电池 batt_ev_183, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 71kWh，并创BMS。
已连接电池 batt_ev_230, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [-1.         -1.         -1.         -1.         -0.         -1.
 -1.         -0.42327875 -1.         -1.         -0.6131522 ]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=80.56336641311646，设置charger_power=45.120000000000005失败。
功率需求: 24.00 kW, 充电桩功率: 80.56 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=92.88000000000001，设置charger_power=56.879999999999995失败。
功率需求: 24.00 kW, 充电桩功率: 92.88 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=73.57826471328735。
功率需求: 36.00 kW, 充电桩功率: 73.58 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_183 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.27 更新为 0.51。
SOC从 0.38 更新为 0.66。
SOC从 0.82 更新为 0.91。
SOC从 0.70 更新为 0.82。
SOC从 0.74 更新为 0.85。
SOC从 0.52 更新为 0.66。
已断开电池: batt_ev_183
时间步 40 执行前: 电池 batt_ev_183 已充满 (SOC: 66.2%)，离开
奖励各项的值：powerloss=-0.21621431272463543, voltage=-0.4754996615769702, ctrl=-0.0, connection=1.08, completion=0.34814814814814815, energy=0.7236882274908291, transformer=0.
智能体的动作为: [-1.         -1.         -1.         -0.8042451  -0.         -0.9383474
 -1.         -0.24598633 -0.9446263  -1.         -0.7134187 ]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=80.56336641311646，设置charger_power=21.120000000000005失败。
功率需求: 15.00 kW, 充电桩功率: 80.56 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=73.83999999999997失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=92.88000000000001，设置charger_power=32.879999999999995失败。
功率需求: 24.00 kW, 充电桩功率: 92.88 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=73.57826471328735，设置charger_power=85.6102466583252失败。
功率需求: 36.00 kW, 充电桩功率: 73.58 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.51 更新为 0.66。
SOC从 0.91 更新为 0.97。
SOC从 0.82 更新为 0.94。
SOC从 0.85 更新为 0.96。
SOC从 0.66 更新为 0.80。
已断开电池: batt_ev_201
时间步 41 执行前: 电池 batt_ev_201 已充满 (SOC: 93.7%)，离开
已断开电池: batt_ev_080
时间步 41 执行前: 电池 batt_ev_080 已充满 (SOC: 95.9%)，离开
已断开电池: batt_ev_204
时间步 41: 电池 batt_ev_204 已离开，当前SOC: 66.2%，能量满足率: 66.9%
已断开电池: batt_ev_230
时间步 41: 电池 batt_ev_230 已离开，当前SOC: 79.7%，能量满足率: 60.2%
奖励各项的值：powerloss=-0.2092533619662338, voltage=-0.38164972093270855, ctrl=-0.0, connection=1.112, completion=0.35251798561151076, energy=0.7263931056119463, transformer=0.
智能体的动作为: [-1.         -1.         -1.         -1.         -0.11313026 -1.
 -1.         -1.         -1.         -1.         -0.85642195]
已有历史设置self.charger_power=80.56336641311646，设置charger_power=6.1200000000000045失败。
功率需求: 15.00 kW, 充电桩功率: 80.56 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.97 更新为 1.00。
已断开电池: batt_ev_015
时间步 42 执行前: 电池 batt_ev_015 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.20460909158973473, voltage=-0.2285906793235548, ctrl=-0.0, connection=1.12, completion=0.35714285714285715, energy=0.728347440571861, transformer=0.
已连接电池 batt_ev_148, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_215, 初始SOC: 62.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_210, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [ 1.         -1.         -0.77373344 -0.         -0.87251806 -0.33286852
 -0.5006716  -0.         -0.         -0.47249058 -0.6607558 ]
初次设置charger_power=0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=104.70216751098633。
功率需求: 72.00 kW, 充电桩功率: 104.70 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=39.94422197341919。
功率需求: 36.00 kW, 充电桩功率: 39.94 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.28 更新为 0.28。
SOC从 0.62 更新为 0.86。
SOC从 0.57 更新为 0.73。
奖励各项的值：powerloss=-0.19668772711914959, voltage=-0.17156059896154652, ctrl=-0.0, connection=1.12, completion=0.35714285714285715, energy=0.728347440571861, transformer=0.
智能体的动作为: [-1.         -1.         -1.         -1.         -0.8747986  -1.
 -1.         -1.         -1.         -1.         -0.77730334]
self.charger_power=0.0 改为 120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=104.70216751098633，设置charger_power=43.51999999999998失败。
功率需求: 30.00 kW, 充电桩功率: 104.70 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=39.94422197341919，设置charger_power=58.599999999999994失败。
功率需求: 24.00 kW, 充电桩功率: 39.94 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.28 更新为 0.61。
SOC从 0.86 更新为 0.96。
SOC从 0.73 更新为 0.84。
已断开电池: batt_ev_215
时间步 44 执行前: 电池 batt_ev_215 已充满 (SOC: 95.6%)，离开
已断开电池: batt_ev_210
时间步 44: 电池 batt_ev_210 已离开，当前SOC: 84.3%，能量满足率: 66.5%
奖励各项的值：powerloss=-0.20694535057110897, voltage=-0.05732065331167213, ctrl=-0.0, connection=1.1360000000000001, completion=0.3591549295774648, energy=0.7298157052825849, transformer=0.
已连接电池 batt_ev_146, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
已连接电池 batt_ev_027, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 107kWh，并创BMS。
智能体的动作为: [-1.         -1.         -1.         -1.         -0.15027265 -1.
 -1.         -1.         -1.         -1.         -0.88532597]
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 96.0, -19.493631420864393
SOC从 0.32 更新为 0.54。
SOC从 0.61 更新为 0.81。
SOC从 0.42 更新为 0.62。
奖励各项的值：powerloss=-0.19892877728466357, voltage=-0.0617997179340124, ctrl=-0.0, connection=1.1360000000000001, completion=0.3591549295774648, energy=0.7298157052825849, transformer=0.
已连接电池 batt_ev_135, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_127, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 88kWh，并创BMS。
已连接电池 batt_ev_165, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 105kWh，并创BMS。
智能体的动作为: [-0.72821856 -1.         -1.         -1.         -0.         -1.
 -1.         -0.65935713 -1.         -1.         -0.5352045 ]
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=70.07999999999998失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=119.28失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.32 更新为 0.62。
SOC从 0.54 更新为 0.71。
SOC从 0.81 更新为 0.94。
SOC从 0.62 更新为 0.77。
SOC从 0.18 更新为 0.46。
SOC从 0.18 更新为 0.47。
已断开电池: batt_ev_148
时间步 46 执行前: 电池 batt_ev_148 已充满 (SOC: 93.9%)，离开
已断开电池: batt_ev_027
时间步 46: 电池 batt_ev_027 已离开，当前SOC: 71.3%，能量满足率: 65.4%
奖励各项的值：powerloss=-0.2004326988545296, voltage=-0.07353922687032055, ctrl=-0.0, connection=1.1520000000000001, completion=0.3611111111111111, energy=0.731166914983359, transformer=0.
已连接电池 batt_ev_003, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_001, 初始SOC: 38.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
已连接电池 batt_ev_086, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.5256983  -0.22631834 -0.         -0.8096742
 -1.         -0.6982325  -1.         -1.         -0.8141078 ]
已有历史设置self.charger_power=120.0，设置charger_power=82.88失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=71.28失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=83.7878966331482。
功率需求: 96.00 kW, 充电桩功率: 83.79 kW, 最终充电功率: 83.79 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=97.69293308258057。
功率需求: 80.00 kW, 充电桩功率: 97.69 kW, 最终充电功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 83.7878966331482, -17.013858067667453
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 0.0, -0.0
SOC从 0.62 更新为 0.84。
SOC从 0.12 更新为 0.12。
SOC从 0.77 更新为 0.88。
SOC从 0.38 更新为 0.68。
SOC从 0.46 更新为 0.69。
SOC从 0.47 更新为 0.69。
SOC从 0.42 更新为 0.68。
已断开电池: batt_ev_146
时间步 47: 电池 batt_ev_146 已离开，当前SOC: 87.6%，能量满足率: 81.4%
已断开电池: batt_ev_135
时间步 47: 电池 batt_ev_135 已离开，当前SOC: 83.9%，能量满足率: 78.6%
奖励各项的值：powerloss=-0.18085059772420375, voltage=-0.1366815423640455, ctrl=-0.0, connection=1.168, completion=0.3561643835616438, energy=0.7321055691464223, transformer=0.
智能体的动作为: [-1.         -1.         -0.827623   -0.1609499  -0.         -0.8067383
 -1.         -0.40521064 -0.26110816 -1.         -0.99211293]
self.charger_power=0.0 改为 0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=83.7878966331482，设置charger_power=48.625277280807495失败。
功率需求: 72.00 kW, 充电桩功率: 83.79 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=31.332979202270508失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=97.69293308258057，设置charger_power=98.63999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 97.69 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 0.0, -0.0
SOC从 0.12 更新为 0.12。
SOC从 0.68 更新为 0.94。
SOC从 0.69 更新为 0.86。
SOC从 0.69 更新为 0.87。
SOC从 0.68 更新为 0.87。
已断开电池: batt_ev_165
时间步 48: 电池 batt_ev_165 已离开，当前SOC: 86.6%，能量满足率: 85.7%
奖励各项的值：powerloss=-0.1528331767409864, voltage=-0.17588588904182023, ctrl=-0.0, connection=1.176, completion=0.35374149659863946, energy=0.7329561629423165, transformer=0.
已连接电池 batt_ev_043, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_051, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
已连接电池 batt_ev_144, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [-1.         -1.         -1.         -1.         -0.         -1.
 -1.         -0.56111884 -1.         -1.         -0.577326  ]
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=83.7878966331482，设置charger_power=17.80000000000001失败。
功率需求: 30.00 kW, 充电桩功率: 83.79 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=97.69293308258057，设置charger_power=38.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 97.69 kW, 最终充电功率: 25.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_144 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.48 更新为 0.69。
SOC从 0.22 更新为 0.61。
SOC从 0.12 更新为 0.12。
SOC从 0.42 更新为 0.66。
SOC从 0.94 更新为 1.00。
SOC从 0.86 更新为 0.93。
SOC从 0.87 更新为 0.96。
已断开电池: batt_ev_003
时间步 49: 电池 batt_ev_003 已离开，当前SOC: 95.6%，能量满足率: 95.7%
已断开电池: batt_ev_001
时间步 49 执行前: 电池 batt_ev_001 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_144
时间步 49 执行前: 电池 batt_ev_144 已充满 (SOC: 61.2%)，离开
奖励各项的值：powerloss=-0.13116833541694808, voltage=-0.22496458723484825, ctrl=-0.0, connection=1.2, completion=0.36, energy=0.7380079240372116, transformer=0.
已连接电池 batt_ev_188, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
已连接电池 batt_ev_107, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 60kWh，并创BMS。
已连接电池 batt_ev_131, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [-1.         -1.         -1.         -0.83249694 -0.         -0.9417306
 -1.         -0.25224665 -0.98466057 -1.         -0.70090955]
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=119.68失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=89.12失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=23.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.18 更新为 0.53。
SOC从 0.69 更新为 0.84。
SOC从 0.12 更新为 0.12。
SOC从 0.66 更新为 0.84。
SOC从 0.28 更新为 0.61。
SOC从 0.93 更新为 1.00。
SOC从 0.22 更新为 0.55。
已断开电池: batt_ev_127
时间步 50 执行前: 电池 batt_ev_127 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_086
时间步 50: 电池 batt_ev_086 已离开，当前SOC: 12.0%，能量满足率: 0.0%
已断开电池: batt_ev_051
时间步 50 执行前: 电池 batt_ev_051 已充满 (SOC: 84.5%)，离开
奖励各项的值：powerloss=-0.1315745680701402, voltage=-0.2607612498125955, ctrl=-0.0, connection=1.224, completion=0.3660130718954248, energy=0.7366090758534753, transformer=0.
已连接电池 batt_ev_136, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
已连接电池 batt_ev_116, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 52kWh，并创BMS。
已连接电池 batt_ev_196, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.8532903  -0.24877529 -0.         -0.8343369
 -1.         -0.33802623 -0.26703373 -1.         -0.9601794 ]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=29.853034615516663。
功率需求: 64.00 kW, 充电桩功率: 29.85 kW, 最终充电功率: 29.85 kW。
已有历史设置self.charger_power=120.0，设置charger_power=41.120000000000005失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=92.80000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=40.56314706802368。
功率需求: 64.00 kW, 充电桩功率: 40.56 kW, 最终充电功率: 40.56 kW。
已有历史设置self.charger_power=120.0，设置charger_power=83.52失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=115.22152662277222。
功率需求: 60.00 kW, 充电桩功率: 115.22 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 29.853034615516663, -6.061917224887374
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 40.56314706802368, -8.236698314733019
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.53 更新为 0.74。
SOC从 0.42 更新为 0.51。
SOC从 0.84 更新为 0.97。
SOC从 0.61 更新为 0.81。
SOC从 0.42 更新为 0.61。
SOC从 0.55 更新为 0.74。
SOC从 0.18 更新为 0.52。
已断开电池: batt_ev_131
时间步 51: 电池 batt_ev_131 已离开，当前SOC: 74.2%，能量满足率: 68.6%
奖励各项的值：powerloss=-0.12331117441303355, voltage=-0.29012172532791647, ctrl=-0.0, connection=1.232, completion=0.36363636363636365, energy=0.7362836848143959, transformer=0.
已连接电池 batt_ev_005, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_063, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
已连接电池 batt_ev_033, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
已连接电池 batt_ev_077, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
智能体的动作为: [-1.         -1.         -1.         -0.75546116 -0.         -0.9354497
 -1.         -0.23582955 -0.87861407 -1.         -0.7350898 ]
已有历史设置self.charger_power=120.0，设置charger_power=90.08000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=29.853034615516663，设置charger_power=90.65533876419067失败。
功率需求: 48.00 kW, 充电桩功率: 29.85 kW, 最终充电功率: 29.85 kW。
初次设置charger_power=0.0。
功率需求: 36.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=9.120000000000005失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=44.80000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=40.56314706802368，设置charger_power=28.299545645713806失败。
功率需求: 48.00 kW, 充电桩功率: 40.56 kW, 最终充电功率: 40.56 kW。
初次设置charger_power=105.43368816375732。
功率需求: 96.00 kW, 充电桩功率: 105.43 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=115.22152662277222，设置charger_power=84.32失败。
功率需求: 36.00 kW, 充电桩功率: 115.22 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 29.853034615516663, -6.061917224887374
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 40.56314706802368, -8.236698314733019
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.74 更新为 0.88。
SOC从 0.38 更新为 0.60。
SOC从 0.51 更新为 0.60。
SOC从 0.52 更新为 0.52。
SOC从 0.97 更新为 1.00。
SOC从 0.81 更新为 0.95。
SOC从 0.61 更新为 0.81。
SOC从 0.32 更新为 0.57。
SOC从 0.18 更新为 0.43。
SOC从 0.52 更新为 0.73。
已断开电池: batt_ev_043
时间步 52 执行前: 电池 batt_ev_043 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.12881764355009523, voltage=-0.2873198546119493, ctrl=-0.0, connection=1.24, completion=0.36774193548387096, energy=0.7379850803962386, transformer=0.
已连接电池 batt_ev_082, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
时间步 52 执行前: 排队电池 batt_ev_082 已接入
智能体的动作为: [-1.         -1.         -0.841713   -0.15812218 -0.         -0.7953605
 -1.         -0.3982304  -0.15509602 -1.         -1.        ]
已有历史设置self.charger_power=120.0，设置charger_power=42.079999999999984失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=85.91999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=29.853034615516663，设置charger_power=18.974661827087402失败。
功率需求: 48.00 kW, 充电桩功率: 29.85 kW, 最终充电功率: 29.85 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 36.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=95.44326066970825。
功率需求: 64.00 kW, 充电桩功率: 95.44 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=12.800000000000011失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=40.56314706802368，设置charger_power=39.52000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 40.56 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=105.43368816375732，设置charger_power=18.611522912979126失败。
功率需求: 72.00 kW, 充电桩功率: 105.43 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=115.22152662277222，设置charger_power=48.31999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 115.22 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 29.853034615516663, -6.061917224887374
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.88 更新为 0.96。
SOC从 0.60 更新为 0.77。
SOC从 0.60 更新为 0.69。
SOC从 0.52 更新为 0.52。
SOC从 0.38 更新为 0.69。
SOC从 0.95 更新为 1.00。
SOC从 0.81 更新为 0.96。
SOC从 0.57 更新为 0.75。
SOC从 0.43 更新为 0.64。
SOC从 0.73 更新为 0.86。
已断开电池: batt_ev_107
时间步 53 执行前: 电池 batt_ev_107 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_116
时间步 53: 电池 batt_ev_116 已离开，当前SOC: 96.4%，能量满足率: 97.1%
已断开电池: batt_ev_077
时间步 53: 电池 batt_ev_077 已离开，当前SOC: 63.6%，能量满足率: 57.0%
奖励各项的值：powerloss=-0.125775827137634, voltage=-0.26134913795821335, ctrl=-0.0, connection=1.264, completion=0.3670886075949367, energy=0.7400535541818695, transformer=0.
已连接电池 batt_ev_159, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 53kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_159 已接入
时间步 53: 电池 batt_ev_097 已错过离开时间，无法接入
已连接电池 batt_ev_105, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_105 已接入
已连接电池 batt_ev_058, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_058 已接入
智能体的动作为: [-1.         -1.         -0.88160586 -0.52738404 -0.         -0.9374679
 -1.         -0.19469322 -0.61937827 -1.         -0.8328834 ]
已有历史设置self.charger_power=120.0，设置charger_power=12.079999999999984失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=49.91999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=29.853034615516663，设置charger_power=63.28608512878418失败。
功率需求: 48.00 kW, 充电桩功率: 29.85 kW, 最终充电功率: 29.85 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 36.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=95.44326066970825，设置charger_power=62.47999999999999失败。
功率需求: 48.00 kW, 充电桩功率: 95.44 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=67.84。
功率需求: 48.00 kW, 充电桩功率: 67.84 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=23.363186717033386。
功率需求: 48.00 kW, 充电桩功率: 23.36 kW, 最终充电功率: 23.36 kW。
已有历史设置self.charger_power=105.43368816375732，设置charger_power=74.32539224624634失败。
功率需求: 48.00 kW, 充电桩功率: 105.43 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=115.22152662277222，设置charger_power=24.319999999999993失败。
功率需求: 15.00 kW, 充电桩功率: 115.22 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 29.853034615516663, -6.061917224887374
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_105 充电的有无功功率为 23.363186717033386, -4.7440974029029555
已在 set_all_batteries_before_solve 中设置 batt_ev_058 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.96 更新为 1.00。
SOC从 0.77 更新为 0.88。
SOC从 0.69 更新为 0.78。
SOC从 0.52 更新为 0.52。
SOC从 0.69 更新为 0.93。
SOC从 0.68 更新为 0.91。
SOC从 0.42 更新为 0.53。
SOC从 0.75 更新为 0.88。
SOC从 0.28 更新为 0.50。
SOC从 0.86 更新为 0.95。
已断开电池: batt_ev_188
时间步 54 执行前: 电池 batt_ev_188 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_136
时间步 54: 电池 batt_ev_136 已离开，当前SOC: 78.4%，能量满足率: 65.0%
已断开电池: batt_ev_196
时间步 54 执行前: 电池 batt_ev_196 已充满 (SOC: 94.7%)，离开
已断开电池: batt_ev_033
时间步 54: 电池 batt_ev_033 已离开，当前SOC: 87.7%，能量满足率: 84.3%
已断开电池: batt_ev_105
时间步 54: 电池 batt_ev_105 已离开，当前SOC: 53.2%，能量满足率: 20.1%
已断开电池: batt_ev_058
时间步 54 执行前: 电池 batt_ev_058 已充满 (SOC: 49.7%)，离开
奖励各项的值：powerloss=-0.1305296100044297, voltage=-0.26663486719996854, ctrl=-0.0, connection=1.312, completion=0.3719512195121951, energy=0.7415995317424003, transformer=0.
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
智能体的动作为: [-1.         -1.         -1.         -0.8424723  -0.         -0.9467344
 -1.         -0.25494742 -0.99474984 -1.         -0.6978057 ]
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=25.919999999999987失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=101.09667778015137。
功率需求: 60.00 kW, 充电桩功率: 101.10 kW, 最终充电功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 36.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=95.44326066970825，设置charger_power=14.47999999999999失败。
功率需求: 20.00 kW, 充电桩功率: 95.44 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=67.84，设置charger_power=19.840000000000003失败。
功率需求: 20.00 kW, 充电桩功率: 67.84 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=30.593690872192383。
功率需求: 60.00 kW, 充电桩功率: 30.59 kW, 最终充电功率: 30.59 kW。
初次设置charger_power=119.36998128890991。
功率需求: 100.00 kW, 充电桩功率: 119.37 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=46.56。
功率需求: 30.00 kW, 充电桩功率: 46.56 kW, 最终充电功率: 30.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 30.593690872192383, -6.212313892358143
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 30.0, -6.091759819020124
SOC从 0.57 更新为 0.77。
SOC从 0.88 更新为 0.95。
SOC从 0.52 更新为 0.72。
SOC从 0.52 更新为 0.52。
SOC从 0.93 更新为 1.00。
SOC从 0.91 更新为 1.00。
SOC从 0.02 更新为 0.14。
SOC从 0.28 更新为 0.57。
SOC从 0.18 更新为 0.46。
SOC从 0.88 更新为 0.96。
已断开电池: batt_ev_005
时间步 55: 电池 batt_ev_005 已离开，当前SOC: 94.9%，能量满足率: 94.9%
已断开电池: batt_ev_063
时间步 55: 电池 batt_ev_063 已离开，当前SOC: 52.0%，能量满足率: 0.0%
已断开电池: batt_ev_082
时间步 55 执行前: 电池 batt_ev_082 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_159
时间步 55 执行前: 电池 batt_ev_159 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.1512419363043978, voltage=-0.25693422175911085, ctrl=-0.0, connection=1.344, completion=0.375, energy=0.741496412379927, transformer=0.
已连接电池 batt_ev_029, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_195, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
已连接电池 batt_ev_213, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_133, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.8787547  -0.50771606 -0.         -0.9316276
 -1.         -0.20150208 -0.59529954 -1.         -0.8414491 ]
已有历史设置self.charger_power=120.0，设置charger_power=82.80000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=105.45056104660034。
功率需求: 64.00 kW, 充电桩功率: 105.45 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=101.09667778015137，设置charger_power=60.92592716217041失败。
功率需求: 40.00 kW, 充电桩功率: 101.10 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=111.7953085899353。
功率需求: 60.00 kW, 充电桩功率: 111.80 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=30.593690872192383，设置charger_power=24.18025016784668失败。
功率需求: 60.00 kW, 充电桩功率: 30.59 kW, 最终充电功率: 30.59 kW。
已有历史设置self.charger_power=119.36998128890991，设置charger_power=71.4359450340271失败。
功率需求: 60.00 kW, 充电桩功率: 119.37 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=113.84失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=46.56，设置charger_power=16.560000000000002失败。
功率需求: 30.00 kW, 充电桩功率: 46.56 kW, 最终充电功率: 30.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 30.593690872192383, -6.212313892358143
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.77 更新为 0.90。
SOC从 0.42 更新为 0.67。
SOC从 0.72 更新为 0.85。
SOC从 0.38 更新为 0.38。
SOC从 0.28 更新为 0.51。
SOC从 0.18 更新为 0.55。
SOC从 0.14 更新为 0.26。
SOC从 0.57 更新为 0.75。
SOC从 0.46 更新为 0.69。
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_175
时间步 56 执行前: 电池 batt_ev_175 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_213
时间步 56 执行前: 电池 batt_ev_213 已充满 (SOC: 50.7%)，离开
奖励各项的值：powerloss=-0.17516386596553526, voltage=-0.23218326446574844, ctrl=-0.0, connection=1.36, completion=0.38235294117647056, energy=0.7445376310578102, transformer=0.
已连接电池 batt_ev_145, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_044, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.7723697  -0.17128985 -0.         -0.8264683
 -1.         -0.45065385 -0.60243475 -1.         -0.9571902 ]
已有历史设置self.charger_power=120.0，设置charger_power=34.80000000000001失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=105.45056104660034，设置charger_power=82.16失败。
功率需求: 48.00 kW, 充电桩功率: 105.45 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=101.09667778015137，设置charger_power=20.554781556129456失败。
功率需求: 40.00 kW, 充电桩功率: 101.10 kW, 最终充电功率: 40.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=99.17619466781616。
功率需求: 48.00 kW, 充电桩功率: 99.18 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=30.593690872192383，设置charger_power=54.07846212387085失败。
功率需求: 60.00 kW, 充电桩功率: 30.59 kW, 最终充电功率: 30.59 kW。
已有历史设置self.charger_power=119.36998128890991，设置charger_power=72.29217052459717失败。
功率需求: 40.00 kW, 充电桩功率: 119.37 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=65.84失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=114.86282587051392。
功率需求: 60.00 kW, 充电桩功率: 114.86 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 30.593690872192383, -6.212313892358143
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.90 更新为 0.99。
SOC从 0.67 更新为 0.86。
SOC从 0.85 更新为 0.98。
SOC从 0.38 更新为 0.38。
SOC从 0.52 更新为 0.71。
SOC从 0.55 更新为 0.77。
SOC从 0.26 更新为 0.37。
SOC从 0.75 更新为 0.87。
SOC从 0.69 更新为 0.86。
SOC从 0.18 更新为 0.44。
已断开电池: batt_ev_118
时间步 57 执行前: 电池 batt_ev_118 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_199
时间步 57 执行前: 电池 batt_ev_199 已充满 (SOC: 98.1%)，离开
已断开电池: batt_ev_153
时间步 57: 电池 batt_ev_153 已离开，当前SOC: 37.3%，能量满足率: 36.8%
已断开电池: batt_ev_029
时间步 57 执行前: 电池 batt_ev_029 已充满 (SOC: 86.4%)，离开
奖励各项的值：powerloss=-0.18442896282277083, voltage=-0.2465001140085743, ctrl=-0.0, connection=1.3920000000000001, completion=0.39080459770114945, energy=0.7467769295480816, transformer=0.
已连接电池 batt_ev_154, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_154 已接入
已连接电池 batt_ev_179, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_179 已接入
已连接电池 batt_ev_246, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 74kWh，并创BMS。
已连接电池 batt_ev_184, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.8811016  -0.52749753 -0.         -0.93777245
 -1.         -0.19426654 -0.6196608  -1.         -0.8328281 ]
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=105.73219299316406。
功率需求: 60.00 kW, 充电桩功率: 105.73 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=63.29970359802246。
功率需求: 80.00 kW, 充电桩功率: 63.30 kW, 最终充电功率: 63.30 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=99.17619466781616，设置charger_power=71.03999999999999失败。
功率需求: 32.00 kW, 充电桩功率: 99.18 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=76.96000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=23.31198513507843。
功率需求: 120.00 kW, 充电桩功率: 23.31 kW, 最终充电功率: 23.31 kW。
已有历史设置self.charger_power=119.36998128890991，设置charger_power=44.80000000000001失败。
功率需求: 25.00 kW, 充电桩功率: 119.37 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=29.840000000000003失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=114.86282587051392，设置charger_power=99.93937253952026失败。
功率需求: 48.00 kW, 充电桩功率: 114.86 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 63.29970359802246, -12.85355303114389
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 23.31198513507843, -4.733700478248839
SOC从 0.32 更新为 0.53。
SOC从 0.18 更新为 0.55。
SOC从 0.48 更新为 0.69。
SOC从 0.38 更新为 0.38。
SOC从 0.71 更新为 0.84。
SOC从 0.77 更新为 0.91。
SOC从 0.28 更新为 0.34。
SOC从 0.87 更新为 0.94。
SOC从 0.86 更新为 0.93。
SOC从 0.44 更新为 0.65。
已断开电池: batt_ev_169
时间步 58: 电池 batt_ev_169 已离开，当前SOC: 94.2%，能量满足率: 94.5%
已断开电池: batt_ev_059
时间步 58: 电池 batt_ev_059 已离开，当前SOC: 93.0%，能量满足率: 93.8%
已断开电池: batt_ev_133
时间步 58: 电池 batt_ev_133 已离开，当前SOC: 91.2%，能量满足率: 91.5%
奖励各项的值：powerloss=-0.19821655327330456, voltage=-0.2564652059566952, ctrl=-0.0, connection=1.416, completion=0.384180790960452, energy=0.7499248476777863, transformer=0.
已连接电池 batt_ev_066, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
时间步 58 执行前: 排队电池 batt_ev_066 已接入
已连接电池 batt_ev_233, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
已连接电池 batt_ev_219, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.88907975 -0.5380658  -0.         -0.9375246
 -1.         -0.19552734 -0.6308403  -1.         -0.82832056]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=105.73219299316406，设置charger_power=71.2失败。
功率需求: 36.00 kW, 充电桩功率: 105.73 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=63.29970359802246，设置charger_power=64.56789493560791失败。
功率需求: 60.00 kW, 充电桩功率: 63.30 kW, 最终充电功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=99.17619466781616，设置charger_power=39.03999999999999失败。
功率需求: 32.00 kW, 充电桩功率: 99.18 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=23.31198513507843，设置charger_power=23.463281393051147失败。
功率需求: 96.00 kW, 充电桩功率: 23.31 kW, 最终充电功率: 23.31 kW。
初次设置charger_power=75.70083618164062。
功率需求: 60.00 kW, 充电桩功率: 75.70 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=114.86282587051392，设置charger_power=82.24000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 114.86 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 23.31198513507843, -4.733700478248839
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.53 更新为 0.69。
SOC从 0.55 更新为 0.78。
SOC从 0.69 更新为 0.90。
SOC从 0.38 更新为 0.38。
SOC从 0.84 更新为 0.97。
SOC从 0.08 更新为 0.47。
SOC从 0.34 更新为 0.39。
SOC从 0.22 更新为 0.55。
SOC从 0.18 更新为 0.41。
SOC从 0.65 更新为 0.80。
已断开电池: batt_ev_145
时间步 59: 电池 batt_ev_145 已离开，当前SOC: 97.2%，能量满足率: 98.2%
已断开电池: batt_ev_044
时间步 59: 电池 batt_ev_044 已离开，当前SOC: 80.1%，能量满足率: 77.6%
已断开电池: batt_ev_179
时间步 59: 电池 batt_ev_179 已离开，当前SOC: 78.0%，能量满足率: 75.0%
奖励各项的值：powerloss=-0.21243996010553157, voltage=-0.2768681137098872, ctrl=-0.0, connection=1.44, completion=0.37777777777777777, energy=0.7513573738269964, transformer=0.
已连接电池 batt_ev_249, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_249 已接入
已连接电池 batt_ev_032, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_032 已接入
已连接电池 batt_ev_060, 初始SOC: 56.99999999999999%, 最大功率: 100kW, 电池容量: 90kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_060 已接入
智能体的动作为: [-1.         -1.         -0.84223765 -0.15785879 -0.         -0.79485494
 -1.         -0.39814907 -0.15094951 -1.         -1.        ]
已有历史设置self.charger_power=120.0，设置charger_power=118.39999999999998失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=101.06851816177368。
功率需求: 120.00 kW, 充电桩功率: 101.07 kW, 最终充电功率: 101.07 kW。
已有历史设置self.charger_power=63.29970359802246，设置charger_power=18.943054676055908失败。
功率需求: 25.00 kW, 充电桩功率: 63.30 kW, 最终充电功率: 25.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=95.38259267807007。
功率需求: 64.00 kW, 充电桩功率: 95.38 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=23.31198513507843，设置charger_power=47.777888774871826失败。
功率需求: 96.00 kW, 充电桩功率: 23.31 kW, 最终充电功率: 23.31 kW。
已有历史设置self.charger_power=75.70083618164062，设置charger_power=18.113940954208374失败。
功率需求: 36.00 kW, 充电桩功率: 75.70 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 23.31198513507843, -4.733700478248839
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 101.06851816177368, -20.522837930193283
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_060 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.69 更新为 0.85。
SOC从 0.08 更新为 0.33。
SOC从 0.90 更新为 0.98。
SOC从 0.38 更新为 0.38。
SOC从 0.48 更新为 0.68。
SOC从 0.47 更新为 0.79。
SOC从 0.39 更新为 0.45。
SOC从 0.55 更新为 0.75。
SOC从 0.41 更新为 0.60。
SOC从 0.57 更新为 0.74。
已断开电池: batt_ev_195
时间步 60: 电池 batt_ev_195 已离开，当前SOC: 38.0%，能量满足率: 0.0%
已断开电池: batt_ev_154
时间步 60: 电池 batt_ev_154 已离开，当前SOC: 84.6%，能量满足率: 79.7%
已断开电池: batt_ev_246
时间步 60 执行前: 电池 batt_ev_246 已充满 (SOC: 98.1%)，离开
已断开电池: batt_ev_184
时间步 60: 电池 batt_ev_184 已离开，当前SOC: 45.0%，能量满足率: 24.3%
已断开电池: batt_ev_233
时间步 60: 电池 batt_ev_233 已离开，当前SOC: 75.3%，能量满足率: 70.2%
奖励各项的值：powerloss=-0.2197694174504541, voltage=-0.2876070492307603, ctrl=-0.0, connection=1.48, completion=0.372972972972973, energy=0.7458708626542715, transformer=0.
时间步 60: 电池 batt_ev_103 已错过离开时间，无法接入
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
智能体的动作为: [-1.         -1.         -0.84215015 -0.15749756 -0.         -0.7946883
 -1.         -0.39840454 -0.15062001 -1.         -1.        ]
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=101.06851816177368，设置charger_power=101.05801820755005失败。
功率需求: 96.00 kW, 充电桩功率: 101.07 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=18.899706602096558。
功率需求: 100.00 kW, 充电桩功率: 18.90 kW, 最终充电功率: 18.90 kW。
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=95.38259267807007，设置charger_power=95.36259412765503失败。
功率需求: 48.00 kW, 充电桩功率: 95.38 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=63.68000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=47.808544635772705。
功率需求: 80.00 kW, 充电桩功率: 47.81 kW, 最终充电功率: 47.81 kW。
初次设置charger_power=18.07440161705017。
功率需求: 20.00 kW, 充电桩功率: 18.07 kW, 最终充电功率: 18.07 kW。
已有历史设置self.charger_power=120.0，设置charger_power=105.19999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=94.80000000000001失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_060 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 18.899706602096558, -3.8377491089973716
已在 set_all_batteries_before_solve 中设置 batt_ev_217 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 47.808544635772705, -9.707939040601005
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 18.07440161705017, -3.6701637841192856
SOC从 0.48 更新为 0.69。
SOC从 0.33 更新为 0.57。
SOC从 0.12 更新为 0.18。
SOC从 0.38 更新为 0.38。
SOC从 0.68 更新为 0.82。
SOC从 0.79 更新为 0.95。
SOC从 0.38 更新为 0.55。
SOC从 0.88 更新为 0.94。
SOC从 0.60 更新为 0.73。
SOC从 0.74 更新为 0.85。
已断开电池: batt_ev_066
时间步 61: 电池 batt_ev_066 已离开，当前SOC: 94.8%，能量满足率: 96.5%
已断开电池: batt_ev_060
时间步 61: 电池 batt_ev_060 已离开，当前SOC: 84.8%，能量满足率: 67.8%
已断开电池: batt_ev_217
时间步 61: 电池 batt_ev_217 已离开，当前SOC: 38.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.21695666469487068, voltage=-0.29249657736402535, ctrl=-0.0, connection=1.504, completion=0.3670212765957447, energy=0.74270493961069, transformer=0.
已连接电池 batt_ev_073, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 106kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_073 已接入
已连接电池 batt_ev_020, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 99kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_020 已接入
已连接电池 batt_ev_208, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 61kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_208 已接入
智能体的动作为: [-1.         -1.         -0.8788964  -0.509834   -0.         -0.9323499
 -1.         -0.20062344 -0.5979413  -1.         -0.84051967]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=101.06851816177368，设置charger_power=105.46756982803345失败。
功率需求: 72.00 kW, 充电桩功率: 101.07 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=18.899706602096558，设置charger_power=61.180078983306885失败。
功率需求: 100.00 kW, 充电桩功率: 18.90 kW, 最终充电功率: 18.90 kW。
初次设置charger_power=0.0。
功率需求: 96.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=95.38259267807007，设置charger_power=58.56失败。
功率需求: 32.00 kW, 充电桩功率: 95.38 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=47.808544635772705，设置charger_power=24.074812531471252失败。
功率需求: 60.00 kW, 充电桩功率: 47.81 kW, 最终充电功率: 47.81 kW。
已有历史设置self.charger_power=18.07440161705017，设置charger_power=19.360000000000014失败。
功率需求: 20.00 kW, 充电桩功率: 18.07 kW, 最终充电功率: 18.07 kW。
已有历史设置self.charger_power=120.0，设置charger_power=69.19999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=100.86236000061035。
功率需求: 80.00 kW, 充电桩功率: 100.86 kW, 最终充电功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 18.899706602096558, -3.8377491089973716
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 47.808544635772705, -9.707939040601005
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 18.07440161705017, -3.6701637841192856
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.69 更新为 0.85。
SOC从 0.57 更新为 0.75。
SOC从 0.18 更新为 0.24。
SOC从 0.48 更新为 0.48。
SOC从 0.82 更新为 0.92。
SOC从 0.32 更新为 0.56。
SOC从 0.55 更新为 0.72。
SOC从 0.94 更新为 1.00。
SOC从 0.73 更新为 0.83。
SOC从 0.38 更新为 0.71。
已断开电池: batt_ev_219
时间步 62 执行前: 电池 batt_ev_219 已充满 (SOC: 82.6%)，离开
已断开电池: batt_ev_032
时间步 62: 电池 batt_ev_032 已离开，当前SOC: 91.9%，能量满足率: 87.8%
已断开电池: batt_ev_205
时间步 62 执行前: 电池 batt_ev_205 已充满 (SOC: 84.8%)，离开
奖励各项的值：powerloss=-0.21576377829448404, voltage=-0.29421606714460147, ctrl=-0.0, connection=1.528, completion=0.3717277486910995, energy=0.7461077352214529, transformer=0.
已连接电池 batt_ev_091, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_091 已接入
时间步 62: 电池 batt_ev_176 已错过离开时间，无法接入
已连接电池 batt_ev_102, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_102 已接入
已连接电池 batt_ev_236, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 92kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_236 已接入
智能体的动作为: [-1.         -1.         -0.87789625 -0.49938202 -0.         -0.92892736
 -1.         -0.20477253 -0.5849868  -1.         -0.8451105 ]
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=101.06851816177368，设置charger_power=98.92000000000002失败。
功率需求: 48.00 kW, 充电桩功率: 101.07 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=18.899706602096558，设置charger_power=59.92584228515625失败。
功率需求: 100.00 kW, 充电桩功率: 18.90 kW, 最终充电功率: 18.90 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 96.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=111.47128343582153。
功率需求: 48.00 kW, 充电桩功率: 111.47 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=47.808544635772705，设置charger_power=24.57270383834839失败。
功率需求: 40.00 kW, 充电桩功率: 47.81 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=18.07440161705017，设置charger_power=1.2799999999999727失败。
功率需求: 20.00 kW, 充电桩功率: 18.07 kW, 最终充电功率: 18.07 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=100.86236000061035，设置charger_power=71.28失败。
功率需求: 40.00 kW, 充电桩功率: 100.86 kW, 最终充电功率: 40.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 18.899706602096558, -3.8377491089973716
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 18.07440161705017, -3.6701637841192856
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_236 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.22 更新为 0.44。
SOC从 0.75 更新为 0.87。
SOC从 0.24 更新为 0.30。
SOC从 0.48 更新为 0.48。
SOC从 0.48 更新为 0.70。
SOC从 0.56 更新为 0.74。
SOC从 0.72 更新为 0.86。
SOC从 1.00 更新为 1.00。
SOC从 0.38 更新为 0.60。
SOC从 0.71 更新为 0.87。
已断开电池: batt_ev_249
时间步 63: 电池 batt_ev_249 已离开，当前SOC: 87.3%，能量满足率: 88.1%
已断开电池: batt_ev_072
时间步 63: 电池 batt_ev_072 已离开，当前SOC: 29.9%，能量满足率: 20.8%
已断开电池: batt_ev_124
时间步 63: 电池 batt_ev_124 已离开，当前SOC: 86.4%，能量满足率: 89.7%
已断开电池: batt_ev_189
时间步 63 执行前: 电池 batt_ev_189 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_236
时间步 63: 电池 batt_ev_236 已离开，当前SOC: 59.7%，能量满足率: 40.3%
奖励各项的值：powerloss=-0.21092229638954849, voltage=-0.3027334332008702, ctrl=-0.0, connection=1.568, completion=0.3673469387755102, energy=0.7443631443104063, transformer=0.
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
智能体的动作为: [-1.         -1.         -0.8953423  -0.54583013 -0.         -0.93714935
 -1.         -0.1967736  -0.63896954 -1.         -0.82501197]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=107.44107484817505。
功率需求: 48.00 kW, 充电桩功率: 107.44 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=65.49961566925049。
功率需求: 100.00 kW, 充电桩功率: 65.50 kW, 最终充电功率: 65.50 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 96.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=111.47128343582153，设置charger_power=66.4失败。
功率需求: 36.00 kW, 充电桩功率: 111.47 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=101.27999999999997失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=23.61283242702484。
功率需求: 96.00 kW, 充电桩功率: 23.61 kW, 最终充电功率: 23.61 kW。
初次设置charger_power=76.676344871521。
功率需求: 60.00 kW, 充电桩功率: 76.68 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=100.86236000061035，设置charger_power=31.28失败。
功率需求: 25.00 kW, 充电桩功率: 100.86 kW, 最终充电功率: 25.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_074 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 65.49961566925049, -13.300264229840032
已在 set_all_batteries_before_solve 中设置 batt_ev_012 充电的有无功功率为 23.61283242702484, -4.794790126406845
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.44 更新为 0.62。
SOC从 0.48 更新为 0.70。
SOC从 0.28 更新为 0.49。
SOC从 0.48 更新为 0.48。
SOC从 0.70 更新为 0.86。
SOC从 0.74 更新为 0.87。
SOC从 0.48 更新为 0.54。
SOC从 0.22 更新为 0.50。
SOC从 0.38 更新为 0.61。
SOC从 0.87 更新为 0.97。
已断开电池: batt_ev_073
时间步 64: 电池 batt_ev_073 已离开，当前SOC: 48.0%，能量满足率: 0.0%
已断开电池: batt_ev_020
时间步 64: 电池 batt_ev_020 已离开，当前SOC: 86.5%，能量满足率: 90.9%
已断开电池: batt_ev_091
时间步 64: 电池 batt_ev_091 已离开，当前SOC: 62.3%，能量满足率: 53.0%
奖励各项的值：powerloss=-0.21063166717860438, voltage=-0.31951657763909846, ctrl=-0.0, connection=1.592, completion=0.36180904522613067, energy=0.7403744256943539, transformer=0.
已连接电池 batt_ev_243, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 64 执行前: 排队电池 batt_ev_243 已接入
已连接电池 batt_ev_122, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.9424895  -0.6037865  -0.         -0.934705
 -1.         -0.2068105  -0.7006031  -1.         -0.80029476]
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=107.44107484817505，设置charger_power=64.32失败。
功率需求: 24.00 kW, 充电桩功率: 107.44 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=65.49961566925049，设置charger_power=72.4543833732605失败。
功率需求: 80.00 kW, 充电桩功率: 65.50 kW, 最终充电功率: 65.50 kW。
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=111.47128343582153，设置charger_power=30.400000000000006失败。
功率需求: 15.00 kW, 充电桩功率: 111.47 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=23.61283242702484，设置charger_power=24.81726050376892失败。
功率需求: 72.00 kW, 充电桩功率: 23.61 kW, 最终充电功率: 23.61 kW。
已有历史设置self.charger_power=76.676344871521，设置charger_power=84.07237529754639失败。
功率需求: 36.00 kW, 充电桩功率: 76.68 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=109.6失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=100.86236000061035，设置charger_power=6.280000000000001失败。
功率需求: 25.00 kW, 充电桩功率: 100.86 kW, 最终充电功率: 25.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_074 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 65.49961566925049, -13.300264229840032
已在 set_all_batteries_before_solve 中设置 batt_ev_012 充电的有无功功率为 23.61283242702484, -4.794790126406845
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_122 充电的有无功功率为 0.0, -0.0
SOC从 0.12 更新为 0.40。
SOC从 0.70 更新为 0.81。
SOC从 0.49 更新为 0.70。
SOC从 0.28 更新为 0.28。
SOC从 0.86 更新为 0.93。
SOC从 0.54 更新为 0.60。
SOC从 0.50 更新为 0.67。
SOC从 0.61 更新为 0.78。
SOC从 0.97 更新为 1.00。
已断开电池: batt_ev_208
时间步 65 执行前: 电池 batt_ev_208 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_102
时间步 65: 电池 batt_ev_102 已离开，当前SOC: 93.0%，能量满足率: 90.0%
已断开电池: batt_ev_074
时间步 65 执行前: 电池 batt_ev_074 已充满 (SOC: 81.3%)，离开
已断开电池: batt_ev_012
时间步 65: 电池 batt_ev_012 已离开，当前SOC: 60.0%，能量满足率: 60.2%
已断开电池: batt_ev_122
时间步 65: 电池 batt_ev_122 已离开，当前SOC: 28.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.20454534436077526, voltage=-0.2913480144224212, ctrl=-0.0, connection=1.6320000000000001, completion=0.3627450980392157, energy=0.73939486043874, transformer=0.
已连接电池 batt_ev_139, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 84kWh，并创BMS。
智能体的动作为: [-0.79285944 -1.         -1.         -1.         -0.         -1.
 -1.         -0.71647924 -1.         -1.         -0.558044  ]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=65.49961566925049，设置charger_power=93.63999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 65.50 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=76.676344871521，设置charger_power=69.36000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 76.68 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=61.599999999999994失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.40 更新为 0.62。
SOC从 0.70 更新为 0.89。
SOC从 0.12 更新为 0.36。
SOC从 0.67 更新为 0.84。
SOC从 0.78 更新为 0.89。
奖励各项的值：powerloss=-0.21111205135960937, voltage=-0.19937734834617693, ctrl=-0.0, connection=1.6320000000000001, completion=0.3627450980392157, energy=0.73939486043874, transformer=0.
已连接电池 batt_ev_004, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_019, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
智能体的动作为: [-1.         -1.         -1.         -1.         -0.14360395 -1.
 -1.         -1.         -1.         -1.         -0.88168526]
已有历史设置self.charger_power=120.0，设置charger_power=82.08000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=65.49961566925049，设置charger_power=33.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 65.50 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=17.232474088668823。
功率需求: 36.00 kW, 充电桩功率: 17.23 kW, 最终充电功率: 17.23 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=76.676344871521，设置charger_power=33.360000000000014失败。
功率需求: 24.00 kW, 充电桩功率: 76.68 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=29.599999999999994失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 17.232474088668823, -3.4992031078552714
SOC从 0.62 更新为 0.79。
SOC从 0.08 更新为 0.35。
SOC从 0.89 更新为 0.97。
SOC从 0.52 更新为 0.62。
SOC从 0.36 更新为 0.55。
SOC从 0.84 更新为 0.96。
SOC从 0.89 更新为 0.97。
已断开电池: batt_ev_228
时间步 67: 电池 batt_ev_228 已离开，当前SOC: 95.6%，能量满足率: 96.8%
已断开电池: batt_ev_218
时间步 67 执行前: 电池 batt_ev_218 已充满 (SOC: 96.6%)，离开
已断开电池: batt_ev_243
时间步 67: 电池 batt_ev_243 已离开，当前SOC: 78.7%，能量满足率: 83.3%
奖励各项的值：powerloss=-0.208656787879673, voltage=-0.12070849528184269, ctrl=-0.0, connection=1.6560000000000001, completion=0.36231884057971014, energy=0.7422130787716715, transformer=0.
智能体的动作为: [-1.         -1.         -1.         -1.         -0.         -1.
 -1.         -0.88649964 -1.         -1.         -0.6480581 ]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=65.49961566925049，设置charger_power=8.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 65.50 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=17.232474088668823，设置charger_power=0.0失败。
功率需求: 36.00 kW, 充电桩功率: 17.23 kW, 最终充电功率: 17.23 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 17.232474088668823, -3.4992031078552714
SOC从 0.35 更新为 0.57。
SOC从 0.97 更新为 1.00。
SOC从 0.62 更新为 0.72。
SOC从 0.55 更新为 0.69。
已断开电池: batt_ev_061
时间步 68 执行前: 电池 batt_ev_061 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.19716099874504012, voltage=-0.09879248285556308, ctrl=-0.0, connection=1.6640000000000001, completion=0.36538461538461536, energy=0.7434524389698847, transformer=0.
智能体的动作为: [-1.        -1.        -1.        -1.        -0.7134165 -1.
 -1.        -1.        -1.        -1.        -0.8798966]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=17.232474088668823，设置charger_power=48.08失败。
功率需求: 24.00 kW, 充电桩功率: 17.23 kW, 最终充电功率: 17.23 kW。
已有历史设置self.charger_power=120.0，设置charger_power=103.68失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 17.232474088668823, -3.4992031078552714
SOC从 0.57 更新为 0.74。
SOC从 0.72 更新为 0.82。
SOC从 0.69 更新为 0.83。
已断开电池: batt_ev_139
时间步 69: 电池 batt_ev_139 已离开，当前SOC: 83.4%，能量满足率: 83.1%
奖励各项的值：powerloss=-0.1950606266848245, voltage=-0.04997302266968706, ctrl=-0.0, connection=1.672, completion=0.36363636363636365, energy=0.743869244448752, transformer=0.
已连接电池 batt_ev_177, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [-1.         -0.         -1.         -1.         -1.         -0.9510403
 -1.         -1.         -1.         -1.         -0.19666718]
已有历史设置self.charger_power=120.0，设置charger_power=94.88失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=17.232474088668823，设置charger_power=30.840000000000003失败。
功率需求: 24.00 kW, 充电桩功率: 17.23 kW, 最终充电功率: 17.23 kW。
初次设置charger_power=114.12483930587769。
功率需求: 64.00 kW, 充电桩功率: 114.12 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 17.232474088668823, -3.4992031078552714
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.74 更新为 0.85。
SOC从 0.82 更新为 0.92。
SOC从 0.38 更新为 0.65。
已断开电池: batt_ev_019
时间步 70: 电池 batt_ev_019 已离开，当前SOC: 92.1%，能量满足率: 87.2%
奖励各项的值：powerloss=-0.1837723135998412, voltage=-0.04207673378787691, ctrl=-0.0, connection=1.68, completion=0.3619047619047619, energy=0.7444774264374862, transformer=0.
已连接电池 batt_ev_202, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_160, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [-1.         -0.         -1.         -1.         -1.         -0.95676017
 -1.         -1.         -1.         -1.         -0.21531853]
已有历史设置self.charger_power=120.0，设置charger_power=54.879999999999995失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=114.12483930587769，设置charger_power=82.32失败。
功率需求: 48.00 kW, 充电桩功率: 114.12 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=25.838223695755005。
功率需求: 60.00 kW, 充电桩功率: 25.84 kW, 最终充电功率: 25.84 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 25.838223695755005, -5.246675096821798
SOC从 0.85 更新为 0.96。
SOC从 0.65 更新为 0.85。
SOC从 0.48 更新为 0.74。
SOC从 0.18 更新为 0.34。
已断开电池: batt_ev_004
时间步 71 执行前: 电池 batt_ev_004 已充满 (SOC: 95.9%)，离开
奖励各项的值：powerloss=-0.1710482147927339, voltage=-0.08045645513860222, ctrl=-0.0, connection=1.688, completion=0.36492890995260663, energy=0.7456884338951284, transformer=0.
智能体的动作为: [-1.        -1.        -1.        -1.        -0.6105121 -1.
 -1.        -1.        -1.        -1.        -0.9400525]
已有历史设置self.charger_power=114.12483930587769，设置charger_power=34.31999999999999失败。
功率需求: 20.00 kW, 充电桩功率: 114.12 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=78.08000000000001失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=25.838223695755005，设置charger_power=108.64失败。
功率需求: 48.00 kW, 充电桩功率: 25.84 kW, 最终充电功率: 25.84 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 25.838223695755005, -5.246675096821798
SOC从 0.85 更新为 0.94。
SOC从 0.74 更新为 0.87。
SOC从 0.34 更新为 0.50。
已断开电池: batt_ev_202
时间步 72 执行前: 电池 batt_ev_202 已充满 (SOC: 87.5%)，离开
奖励各项的值：powerloss=-0.1484300257275399, voltage=-0.12999113827261377, ctrl=-0.0, connection=1.696, completion=0.36792452830188677, energy=0.7468880167541136, transformer=0.
已连接电池 batt_ev_099, 初始SOC: 68.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
已连接电池 batt_ev_100, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [-1.         -0.         -1.         -0.9930787  -1.         -0.7247612
 -0.42939577 -1.         -1.         -0.8891076  -0.16321474]
初次设置charger_power=0.0。
功率需求: 36.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=114.12483930587769，设置charger_power=14.319999999999993失败。
功率需求: 20.00 kW, 充电桩功率: 114.12 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=25.838223695755005，设置charger_power=19.585769176483154失败。
功率需求: 48.00 kW, 充电桩功率: 25.84 kW, 最终充电功率: 25.84 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 25.838223695755005, -5.246675096821798
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.68 更新为 0.68。
SOC从 0.94 更新为 1.00。
SOC从 0.18 更新为 0.52。
SOC从 0.50 更新为 0.65。
已断开电池: batt_ev_177
时间步 73 执行前: 电池 batt_ev_177 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_160
时间步 73: 电池 batt_ev_160 已离开，当前SOC: 65.3%，能量满足率: 59.1%
奖励各项的值：powerloss=-0.1251799501042775, voltage=-0.18058016326716997, ctrl=-0.0, connection=1.712, completion=0.3691588785046729, energy=0.7473416505159284, transformer=0.
智能体的动作为: [-1.         -0.         -1.         -1.         -1.         -0.94655883
 -1.         -1.         -1.         -1.         -0.17970715]
self.charger_power=0.0 改为 0.0。
功率需求: 36.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=110.24失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.68 更新为 0.68。
SOC从 0.52 更新为 0.73。
已断开电池: batt_ev_100
时间步 74: 电池 batt_ev_100 已离开，当前SOC: 73.2%，能量满足率: 74.6%
奖励各项的值：powerloss=-0.11487683163701673, voltage=-0.21228788856482828, ctrl=-0.0, connection=1.72, completion=0.3674418604651163, energy=0.7473334249756974, transformer=0.
智能体的动作为: [-1.         -0.30510908 -1.         -0.730799   -0.9551167  -1.
 -1.         -0.67158663 -1.         -1.         -0.70639056]
self.charger_power=0.0 改为 36.61309003829956。
功率需求: 36.00 kW, 充电桩功率: 36.61 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.68 更新为 0.81。
奖励各项的值：powerloss=-0.11042229498350835, voltage=-0.2428463945321413, ctrl=-0.0, connection=1.72, completion=0.3674418604651163, energy=0.7473334249756974, transformer=0.
智能体的动作为: [ 0.079404   -0.6733502  -1.         -0.5833968  -1.         -0.95110327
 -0.9915868  -0.06420552 -0.7273949  -1.         -0.74547124]
已有历史设置self.charger_power=36.61309003829956，设置charger_power=49.75999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 36.61 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -7.940399646759033, -2.609883152657554
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.81 更新为 0.90。
奖励各项的值：powerloss=-0.10908654516777683, voltage=-0.2758429204599988, ctrl=-0.0, connection=1.72, completion=0.3674418604651163, energy=0.7473334249756974, transformer=0.
已连接电池 batt_ev_120, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [ 1.         -1.         -0.43722042 -0.10320666 -0.60890615 -0.07834309
 -0.29288712 -0.         -0.         -0.26299736 -0.53480357]
已有历史设置self.charger_power=36.61309003829956，设置charger_power=25.75999999999999失败。
功率需求: 15.00 kW, 充电桩功率: 36.61 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=31.559683084487915。
功率需求: 120.00 kW, 充电桩功率: 31.56 kW, 最终充电功率: 31.56 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 31.559683084487915, -6.408466977169752
SOC从 0.90 更新为 0.96。
SOC从 0.18 更新为 0.28。
已断开电池: batt_ev_099
时间步 77: 电池 batt_ev_099 已离开，当前SOC: 96.0%，能量满足率: 93.3%
奖励各项的值：powerloss=-0.10592562763334133, voltage=-0.3107020139489647, ctrl=-0.0, connection=1.728, completion=0.36574074074074076, energy=0.7481922323642152, transformer=0.
智能体的动作为: [-1.         -0.3076482  -1.         -0.73048013 -0.9574761  -1.
 -1.         -0.669511   -1.         -1.         -0.707536  ]
已有历史设置self.charger_power=31.559683084487915，设置charger_power=120.0失败。
功率需求: 120.00 kW, 充电桩功率: 31.56 kW, 最终充电功率: 31.56 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 31.559683084487915, -6.408466977169752
SOC从 0.28 更新为 0.37。
奖励各项的值：powerloss=-0.12205073776403397, voltage=-0.1816511968648693, ctrl=-0.0, connection=1.728, completion=0.36574074074074076, energy=0.7481922323642152, transformer=0.
已连接电池 batt_ev_035, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 77kWh，并创BMS。
智能体的动作为: [ 1.         -1.         -0.585058   -0.27724934 -0.72103006 -0.21727288
 -0.41890967 -0.         -0.         -0.41581738 -0.5838753 ]
初次设置charger_power=33.269920349121094。
功率需求: 64.00 kW, 充电桩功率: 33.27 kW, 最终充电功率: 33.27 kW。
已有历史设置self.charger_power=31.559683084487915，设置charger_power=49.898085594177246失败。
功率需求: 96.00 kW, 充电桩功率: 31.56 kW, 最终充电功率: 31.56 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 31.559683084487915, -6.408466977169752
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 33.269920349121094, -6.755745465492527
SOC从 0.48 更新为 0.59。
SOC从 0.37 更新为 0.47。
已断开电池: batt_ev_120
时间步 79: 电池 batt_ev_120 已离开，当前SOC: 46.9%，能量满足率: 36.1%
奖励各项的值：powerloss=-0.12958143855225404, voltage=-0.4171907507774808, ctrl=-0.0, connection=1.736, completion=0.3640552995391705, energy=0.7464071214811161, transformer=0.
已连接电池 batt_ev_151, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
智能体的动作为: [-1.         -0.27094477 -1.         -0.77877605 -0.92623514 -1.
 -1.         -0.67558396 -1.         -1.         -0.67129344]
已有历史设置self.charger_power=33.269920349121094，设置charger_power=93.45312595367432失败。
功率需求: 48.00 kW, 充电桩功率: 33.27 kW, 最终充电功率: 33.27 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 33.269920349121094, -6.755745465492527
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.59 更新为 0.70。
SOC从 0.28 更新为 0.63。
奖励各项的值：powerloss=-0.16265795454182772, voltage=-0.3310788450769775, ctrl=-0.0, connection=1.736, completion=0.3640552995391705, energy=0.7464071214811161, transformer=0.
智能体的动作为: [-1.         -0.57893676 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -0.4372812 ]
已有历史设置self.charger_power=33.269920349121094，设置charger_power=93.6失败。
功率需求: 48.00 kW, 充电桩功率: 33.27 kW, 最终充电功率: 33.27 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 7.960000000000036, 2.616325477223763
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 33.269920349121094, -6.755745465492527
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 72.0, -14.620223565648296
SOC从 0.70 更新为 0.80。
SOC从 0.63 更新为 0.84。
已断开电池: batt_ev_035
时间步 81: 电池 batt_ev_035 已离开，当前SOC: 80.4%，能量满足率: 64.8%
已断开电池: batt_ev_151
时间步 81: 电池 batt_ev_151 已离开，当前SOC: 83.8%，能量满足率: 79.7%
奖励各项的值：powerloss=-0.16614297407565087, voltage=-0.33752166628685076, ctrl=-0.0, connection=1.752, completion=0.3607305936073059, energy=0.7461917773625795, transformer=0.
智能体的动作为: [-1.         -0.         -1.         -1.         -1.         -1.
 -0.97247386 -1.         -1.         -1.         -0.31886733]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.1696514611194325, voltage=-0.2989587207357647, ctrl=-0.0, connection=1.752, completion=0.3607305936073059, energy=0.7461917773625795, transformer=0.
智能体的动作为: [ 1.         -1.         -0.3998523  -0.         -0.0138804  -0.34667733
 -0.67093444 -0.         -0.         -0.         -0.65613395]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
奖励各项的值：powerloss=-0.17222032268649812, voltage=-0.40048187648917377, ctrl=-0.0, connection=1.752, completion=0.3607305936073059, energy=0.7461917773625795, transformer=0.
已连接电池 batt_ev_056, 初始SOC: 62.0%, 最大功率: 80kW, 电池容量: 64kWh，并创BMS。
已连接电池 batt_ev_226, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [ 1.         -1.         -0.40044868 -0.         -0.01427643 -0.3467753
 -0.67129934 -0.         -0.         -0.         -0.65754586]
初次设置charger_power=48.05384159088135。
功率需求: 60.00 kW, 充电桩功率: 48.05 kW, 最终充电功率: 48.05 kW。
初次设置charger_power=1.7131716012954712。
功率需求: 48.00 kW, 充电桩功率: 1.71 kW, 最终充电功率: 1.71 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 1.7131716012954712, -0.34787433079527047
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 48.05384159088135, -9.757748711762968
SOC从 0.18 更新为 0.44。
SOC从 0.62 更新为 0.63。
奖励各项的值：powerloss=-0.17892391234372512, voltage=-0.4036482091722604, ctrl=-0.0, connection=1.752, completion=0.3607305936073059, energy=0.7461917773625795, transformer=0.
已连接电池 batt_ev_048, 初始SOC: 42.0%, 最大功率: 120kW, 电池容量: 93kWh，并创BMS。
智能体的动作为: [-1.         -0.30457428 -1.         -0.73095757 -0.9546904  -1.
 -1.         -0.6720934  -1.         -1.         -0.7061778 ]
已有历史设置self.charger_power=48.05384159088135，设置charger_power=102.84失败。
功率需求: 48.00 kW, 充电桩功率: 48.05 kW, 最终充电功率: 48.00 kW。
self.charger_power=1.7131716012954712 改为 95.56。
功率需求: 48.00 kW, 充电桩功率: 95.56 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=80.65120697021484。
功率需求: 96.00 kW, 充电桩功率: 80.65 kW, 最终充电功率: 80.65 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_048 充电的有无功功率为 80.65120697021484, -16.37692606588768
SOC从 0.44 更新为 0.70。
SOC从 0.63 更新为 0.81。
SOC从 0.42 更新为 0.64。
已断开电池: batt_ev_048
时间步 85: 电池 batt_ev_048 已离开，当前SOC: 63.7%，能量满足率: 38.7%
奖励各项的值：powerloss=-0.2047801861028042, voltage=-0.3557664862058596, ctrl=-0.0, connection=1.76, completion=0.35909090909090907, energy=0.7445595273481747, transformer=0.
已连接电池 batt_ev_234, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_227, 初始SOC: 8.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
智能体的动作为: [-1.         -1.         -1.         -1.         -0.82500476 -1.
 -1.         -1.         -1.         -1.         -0.7513874 ]
已有历史设置self.charger_power=48.05384159088135，设置charger_power=54.84失败。
功率需求: 24.00 kW, 充电桩功率: 48.05 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=95.56，设置charger_power=47.56失败。
功率需求: 32.00 kW, 充电桩功率: 95.56 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=108.36000000000001。
功率需求: 36.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=90.16649007797241。
功率需求: 60.00 kW, 充电桩功率: 90.17 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.70 更新为 0.83。
SOC从 0.81 更新为 0.94。
SOC从 0.57 更新为 0.71。
SOC从 0.08 更新为 0.40。
已断开电池: batt_ev_056
时间步 86: 电池 batt_ev_056 已离开，当前SOC: 93.9%，能量满足率: 88.7%
已断开电池: batt_ev_226
时间步 86 执行前: 电池 batt_ev_226 已充满 (SOC: 83.2%)，离开
奖励各项的值：powerloss=-0.20411381762968367, voltage=-0.33021758148345626, ctrl=-0.0, connection=1.776, completion=0.36036036036036034, energy=0.7463505169666595, transformer=0.
智能体的动作为: [-1.         -0.         -1.         -1.         -1.         -0.9621692
 -1.         -1.         -1.         -1.         -0.15481724]
已有历史设置self.charger_power=108.36000000000001，设置charger_power=72.36000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=90.16649007797241，设置charger_power=18.578068614006042失败。
功率需求: 48.00 kW, 充电桩功率: 90.17 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.71 更新为 0.81。
SOC从 0.40 更新为 0.65。
奖励各项的值：powerloss=-0.1903140625684015, voltage=-0.34523070366640596, ctrl=-0.0, connection=1.776, completion=0.36036036036036034, energy=0.7463505169666595, transformer=0.
智能体的动作为: [-1.         -0.06973403 -1.         -1.         -0.8153725  -0.96035016
 -1.         -0.6824035  -1.         -0.83177847 -0.5198526 ]
已有历史设置self.charger_power=108.36000000000001，设置charger_power=48.360000000000014失败。
功率需求: 24.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=90.16649007797241，设置charger_power=62.382309436798096失败。
功率需求: 36.00 kW, 充电桩功率: 90.17 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.81 更新为 0.90。
SOC从 0.65 更新为 0.85。
已断开电池: batt_ev_227
时间步 88: 电池 batt_ev_227 已离开，当前SOC: 84.6%，能量满足率: 85.1%
奖励各项的值：powerloss=-0.18656139835485008, voltage=-0.3458725479343827, ctrl=-0.0, connection=1.784, completion=0.35874439461883406, energy=0.7468200833918639, transformer=0.
智能体的动作为: [-1.         -0.30416393 -1.         -0.7312289  -0.9543627  -1.
 -1.         -0.6723705  -1.         -1.         -0.7059625 ]
已有历史设置self.charger_power=108.36000000000001，设置charger_power=24.360000000000014失败。
功率需求: 15.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.90 更新为 0.96。
奖励各项的值：powerloss=-0.1858739046046504, voltage=-0.281689194811543, ctrl=-0.0, connection=1.784, completion=0.35874439461883406, energy=0.7468200833918639, transformer=0.
智能体的动作为: [ 1.         -1.         -0.43607104 -0.09820277 -0.60761356 -0.07755525
 -0.292345   -0.         -0.         -0.261484   -0.53438324]
已有历史设置self.charger_power=108.36000000000001，设置charger_power=9.306629598140717失败。
功率需求: 15.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_234
时间步 90 执行前: 电池 batt_ev_234 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.19282851801181922, voltage=-0.2602338279258243, ctrl=-0.0, connection=1.792, completion=0.36160714285714285, energy=0.7479503508767217, transformer=0.
智能体的动作为: [ 1.         -1.         -0.43607366 -0.09821593 -0.60762626 -0.07755354
 -0.292339   -0.         -0.         -0.2614883  -0.5343888 ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
奖励各项的值：powerloss=-0.1892610987315282, voltage=-0.13287519375059675, ctrl=-0.0, connection=1.792, completion=0.36160714285714285, energy=0.7479503508767217, transformer=0.
智能体的动作为: [ 1.         -1.         -0.40019587 -0.         -0.01413456 -0.34671113
 -0.6711191  -0.         -0.         -0.         -0.65692824]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
奖励各项的值：powerloss=-0.183280782368381, voltage=-0.10930895163358656, ctrl=-0.0, connection=1.792, completion=0.36160714285714285, energy=0.7479503508767217, transformer=0.
已连接电池 batt_ev_238, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [ 1.         -1.         -0.40018678 -0.         -0.01409528 -0.34673765
 -0.6711451  -0.         -0.         -0.         -0.65692806]
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 0.0, -0.0
SOC从 0.48 更新为 0.48。
奖励各项的值：powerloss=-0.18425174731022173, voltage=-0.06877354320798723, ctrl=-0.0, connection=1.792, completion=0.36160714285714285, energy=0.7479503508767217, transformer=0.
智能体的动作为: [ 1.         -1.         -0.39989662 -0.         -0.01481571 -0.3459232
 -0.67010367 -0.         -0.         -0.         -0.6556595 ]
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 0.0, -0.0
SOC从 0.48 更新为 0.48。
奖励各项的值：powerloss=-0.17187466006239038, voltage=-0.05318890113377828, ctrl=-0.0, connection=1.792, completion=0.36160714285714285, energy=0.7479503508767217, transformer=0.
智能体的动作为: [ 1.         -1.         -0.3998346  -0.         -0.01503373 -0.34569567
 -0.6698209  -0.         -0.         -0.         -0.65534806]
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 0.0, -0.0
SOC从 0.48 更新为 0.48。
奖励各项的值：powerloss=-0.1552367185668459, voltage=-0.13780635462476765, ctrl=-0.0, connection=1.792, completion=0.36160714285714285, energy=0.7479503508767217, transformer=0.
已连接电池 batt_ev_025, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
已连接电池 batt_ev_013, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 89kWh，并创BMS。
已连接电池 batt_ev_117, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 111kWh，并创BMS。
已连接电池 batt_ev_166, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 114kWh，并创BMS。
智能体的动作为: [ 1.         -1.         -0.3997355  -0.         -0.01532688 -0.34537858
 -0.66942155 -0.         -0.         -0.         -0.65488607]
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求: 72.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=80.33058643341064。
功率需求: 120.00 kW, 充电桩功率: 80.33 kW, 最终充电功率: 80.33 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_025 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_013 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_117 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_166 充电的有无功功率为 80.33058643341064, -16.311821289112466
SOC从 0.12 更新为 0.43。
SOC从 0.52 更新为 0.52。
SOC从 0.28 更新为 0.46。
SOC从 0.48 更新为 0.48。
SOC从 0.18 更新为 0.18。
已断开电池: batt_ev_238
时间步 96: 电池 batt_ev_238 已离开，当前SOC: 48.0%，能量满足率: 0.0%
已断开电池: batt_ev_025
时间步 96: 电池 batt_ev_025 已离开，当前SOC: 42.6%，能量满足率: 35.6%
已断开电池: batt_ev_013
时间步 96: 电池 batt_ev_013 已离开，当前SOC: 18.0%，能量满足率: 0.0%
已断开电池: batt_ev_117
时间步 96: 电池 batt_ev_117 已离开，当前SOC: 52.0%，能量满足率: 0.0%
已断开电池: batt_ev_166
时间步 96: 电池 batt_ev_166 已离开，当前SOC: 45.6%，能量满足率: 25.2%
奖励各项的值：powerloss=-0.14350537001471492, voltage=-0.20784677451281208, ctrl=-0.37500000000000006, connection=1.832, completion=0.3537117903930131, energy=0.7342727685811797, transformer=0.
调度记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250512_003035_13Bus_cbat_1000000\test_results_20250512_044504\schedule.csv
储能放电功率记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250512_003035_13Bus_cbat_1000000\test_results_20250512_044504\storage_schedule.csv
储能能量记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250512_003035_13Bus_cbat_1000000\test_results_20250512_044504\storage_energy.csv
已生成GIF动画，包含96步
测试完成 - 总奖励: 171.6605
测试结果保存在: D:\LENOVO\Documents\Python\ML\powergym\results_20250512_003035_13Bus_cbat_1000000\test_results_20250512_044504
运行时间: 15302.13秒

进程已结束，退出代码为 0

```