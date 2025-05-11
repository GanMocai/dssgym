

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
已从D:\LENOVO\Documents\Python\ML\powergym\results_20250510_194947_13Bus_cbat_1000000\model\ppo_model加载模型
BatteryStationManager已重置
智能体的动作为: [ 1.         -1.         -1.         -0.59071165 -1.         -0.8864835
 -0.7944239  -0.26903114 -0.02946956 -0.         -0.6318084 ]
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
智能体的动作为: [ 1.        -1.        -1.        -0.6248546 -1.        -0.9023905
 -0.8251976 -0.3120035 -0.0639666 -0.        -0.6582312]
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=74.98255491256714。
功率需求: 60.00 kW, 充电桩功率: 74.98 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=108.28685760498047。
功率需求: 60.00 kW, 充电桩功率: 108.29 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=99.02370929718018。
功率需求: 100.00 kW, 充电桩功率: 99.02 kW, 最终充电功率: 99.02 kW。
初次设置charger_power=37.44041919708252。
功率需求: 80.00 kW, 充电桩功率: 37.44 kW, 最终充电功率: 37.44 kW。
初次设置charger_power=7.675992250442505。
功率需求: 96.00 kW, 充电桩功率: 7.68 kW, 最终充电功率: 7.68 kW。
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=78.9877438545227。
功率需求: 120.00 kW, 充电桩功率: 78.99 kW, 最终充电功率: 78.99 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -60.0, -19.721046310731793
已在 set_all_batteries_before_solve 中设置 batt_ev_030 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 99.02370929718018, -20.107621780896388
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 37.44041919708252, -7.60260137573523
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 7.675992250442505, -1.55867670541185
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 78.9877438545227, -16.03914547360117
SOC从 0.18 更新为 0.51。
SOC从 0.32 更新为 0.55。
SOC从 0.18 更新为 0.40。
SOC从 0.12 更新为 0.36。
SOC从 0.22 更新为 0.51。
SOC从 0.28 更新为 0.55。
SOC从 0.12 更新为 0.30。
SOC从 0.38 更新为 0.40。
SOC从 0.22 更新为 0.22。
SOC从 0.12 更新为 0.39。
已断开电池: batt_ev_030
时间步 2 执行前: 电池 batt_ev_030 已充满 (SOC: 51.3%)，离开
奖励各项的值：powerloss=-0.14809312931709026, voltage=-0.24206590838830477, ctrl=-0.0, connection=0.08, completion=30.0, energy=10.0, transformer=0.
已连接电池 batt_ev_224, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
时间步 2 执行前: 排队电池 batt_ev_224 已接入
智能体的动作为: [ 1.         -0.50031835 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=60.03820180892944。
功率需求: 60.00 kW, 充电桩功率: 60.04 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=74.98255491256714，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 74.98 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=108.28685760498047，设置charger_power=99.12失败。
功率需求: 36.00 kW, 充电桩功率: 108.29 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=99.02370929718018，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 99.02 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=37.44041919708252，设置charger_power=120.0失败。
功率需求: 64.00 kW, 充电桩功率: 37.44 kW, 最终充电功率: 37.44 kW。
self.charger_power=7.675992250442505 改为 120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
self.charger_power=0.0 改为 120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=78.9877438545227，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 78.99 kW, 最终充电功率: 78.99 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 37.44041919708252, -7.60260137573523
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 78.9877438545227, -16.03914547360117
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.28 更新为 0.61。
SOC从 0.55 更新为 0.73。
SOC从 0.40 更新为 0.58。
SOC从 0.36 更新为 0.56。
SOC从 0.51 更新为 0.69。
SOC从 0.55 更新为 0.71。
SOC从 0.30 更新为 0.48。
SOC从 0.40 更新为 0.66。
SOC从 0.22 更新为 0.55。
SOC从 0.39 更新为 0.67。
已断开电池: batt_ev_064
时间步 3 执行前: 电池 batt_ev_064 已充满 (SOC: 55.5%)，离开
已断开电池: batt_ev_039
时间步 3: 电池 batt_ev_039 已离开，当前SOC: 48.0%，能量满足率: 41.9%
已断开电池: batt_ev_045
时间步 3: 电池 batt_ev_045 已离开，当前SOC: 66.9%，能量满足率: 63.8%
奖励各项的值：powerloss=-0.14803957637684206, voltage=-0.26214033699840433, ctrl=-0.0, connection=0.32, completion=15.0, energy=7.6413113695090455, transformer=0.
时间步 3: 电池 batt_ev_092 已错过离开时间，无法接入
已连接电池 batt_ev_081, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 50kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_081 已接入
已连接电池 batt_ev_076, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_076 已接入
已连接电池 batt_ev_235, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_235 已接入
智能体的动作为: [ 1.         -0.50031835 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=60.03820180892944，设置charger_power=60.03820180892944失败。
功率需求: 36.00 kW, 充电桩功率: 60.04 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=75.68失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=74.98255491256714，设置charger_power=115.03999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 74.98 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=108.28685760498047，设置charger_power=63.120000000000005失败。
功率需求: 36.00 kW, 充电桩功率: 108.29 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=99.02370929718018，设置charger_power=105.92000000000002失败。
功率需求: 40.00 kW, 充电桩功率: 99.02 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=80.4失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=71.44。
功率需求: 36.00 kW, 充电桩功率: 71.44 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_235 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.61 更新为 0.81。
SOC从 0.73 更新为 0.84。
SOC从 0.58 更新为 0.71。
SOC从 0.12 更新为 0.52。
SOC从 0.69 更新为 0.87。
SOC从 0.71 更新为 0.82。
SOC从 0.28 更新为 0.53。
SOC从 0.66 更新为 0.85。
SOC从 0.55 更新为 0.75。
SOC从 0.62 更新为 0.81。
已断开电池: batt_ev_126
时间步 4: 电池 batt_ev_126 已离开，当前SOC: 70.9%，能量满足率: 66.2%
已断开电池: batt_ev_239
时间步 4 执行前: 电池 batt_ev_239 已充满 (SOC: 82.1%)，离开
已断开电池: batt_ev_242
时间步 4 执行前: 电池 batt_ev_242 已充满 (SOC: 85.2%)，离开
奖励各项的值：powerloss=-0.13883699649686218, voltage=-0.3017237281476559, ctrl=-0.0, connection=0.56, completion=17.142857142857142, energy=8.168984648122816, transformer=0.
时间步 4: 电池 batt_ev_104 已错过离开时间，无法接入
已连接电池 batt_ev_018, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_018 已接入
已连接电池 batt_ev_062, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_062 已接入
时间步 4: 电池 batt_ev_200 已错过离开时间，无法接入
时间步 4: 电池 batt_ev_163 已错过离开时间，无法接入
已连接电池 batt_ev_014, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_014 已接入
智能体的动作为: [ 1.         -0.50031835 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=60.03820180892944，设置charger_power=33.599999999999994失败。
功率需求: 24.00 kW, 充电桩功率: 60.04 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=43.68000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=96.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=108.28685760498047，设置charger_power=27.120000000000005失败。
功率需求: 15.00 kW, 充电桩功率: 108.29 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=112.8失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=44.400000000000006失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=71.44，设置charger_power=35.44失败。
功率需求: 24.00 kW, 充电桩功率: 71.44 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_235 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_062 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_014 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.81 更新为 0.95。
SOC从 0.84 更新为 0.96。
SOC从 0.32 更新为 0.52。
SOC从 0.52 更新为 0.76。
SOC从 0.87 更新为 0.94。
SOC从 0.57 更新为 0.80。
SOC从 0.53 更新为 0.68。
SOC从 0.28 更新为 0.53。
SOC从 0.75 更新为 0.89。
SOC从 0.81 更新为 0.94。
已断开电池: batt_ev_123
时间步 5: 电池 batt_ev_123 已离开，当前SOC: 94.1%，能量满足率: 94.8%
已断开电池: batt_ev_042
时间步 5: 电池 batt_ev_042 已离开，当前SOC: 88.7%，能量满足率: 87.7%
已断开电池: batt_ev_076
时间步 5: 电池 batt_ev_076 已离开，当前SOC: 68.0%，能量满足率: 57.1%
已断开电池: batt_ev_235
时间步 5 执行前: 电池 batt_ev_235 已充满 (SOC: 93.9%)，离开
已断开电池: batt_ev_062
时间步 5: 电池 batt_ev_062 已离开，当前SOC: 80.4%，能量满足率: 57.0%
奖励各项的值：powerloss=-0.1363368306631981, voltage=-0.315478963580651, ctrl=-0.0, connection=0.96, completion=12.5, energy=8.071012306835556, transformer=0.
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
智能体的动作为: [ 1.        -0.5003183 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=60.03820180892944，设置charger_power=9.599999999999994失败。
功率需求: 15.00 kW, 充电桩功率: 60.04 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=11.680000000000007失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=117.92失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.0失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_014 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_231 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_248 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.95 更新为 1.00。
SOC从 0.96 更新为 1.00。
SOC从 0.52 更新为 0.66。
SOC从 0.76 更新为 0.92。
SOC从 0.08 更新为 0.37。
SOC从 0.57 更新为 0.80。
SOC从 0.08 更新为 0.40。
SOC从 0.53 更新为 0.69。
SOC从 0.32 更新为 0.52。
SOC从 0.22 更新为 0.47。
已断开电池: batt_ev_149
时间步 6 执行前: 电池 batt_ev_149 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_224
时间步 6 执行前: 电池 batt_ev_224 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_014
时间步 6: 电池 batt_ev_014 已离开，当前SOC: 68.5%，能量满足率: 67.5%
已断开电池: batt_ev_231
时间步 6: 电池 batt_ev_231 已离开，当前SOC: 40.3%，能量满足率: 35.8%
已断开电池: batt_ev_248
时间步 6: 电池 batt_ev_248 已离开，当前SOC: 46.6%，能量满足率: 32.4%
奖励各项的值：powerloss=-0.14827804577936066, voltage=-0.3445404044449951, ctrl=-0.0, connection=1.36, completion=12.352941176470587, energy=7.671939988890417, transformer=0.
已连接电池 batt_ev_240, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_240 已接入
时间步 6: 电池 batt_ev_119 已错过离开时间，无法接入
已连接电池 batt_ev_158, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_158 已接入
已连接电池 batt_ev_157, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_157 已接入
已连接电池 batt_ev_096, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_096 已接入
已连接电池 batt_ev_187, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_187 已接入
智能体的动作为: [ 1.         -0.50031835 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=60.03820180892944。
功率需求: 96.00 kW, 充电桩功率: 60.04 kW, 最终充电功率: 60.04 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=81.91999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=16.0失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=60.44失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=115.2失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=103.20000000000002。
功率需求: 36.00 kW, 充电桩功率: 103.20 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 60.03820180892944, -12.191276846195255
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_157 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_187 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.48 更新为 0.69。
SOC从 0.28 更新为 0.60。
SOC从 0.66 更新为 0.81。
SOC从 0.92 更新为 1.00。
SOC从 0.37 更新为 0.61。
SOC从 0.80 更新为 0.96。
SOC从 0.12 更新为 0.39。
SOC从 0.18 更新为 0.47。
SOC从 0.52 更新为 0.67。
SOC从 0.57 更新为 0.72。
已断开电池: batt_ev_081
时间步 7 执行前: 电池 batt_ev_081 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_018
时间步 7: 电池 batt_ev_018 已离开，当前SOC: 81.2%，能量满足率: 74.5%
已断开电池: batt_ev_036
时间步 7: 电池 batt_ev_036 已离开，当前SOC: 96.0%，能量满足率: 95.0%
已断开电池: batt_ev_157
时间步 7: 电池 batt_ev_157 已离开，当前SOC: 39.3%，能量满足率: 31.7%
已断开电池: batt_ev_187
时间步 7: 电池 batt_ev_187 已离开，当前SOC: 72.0%，能量满足率: 36.6%
奖励各项的值：powerloss=-0.16291447905596143, voltage=-0.3830242534684314, ctrl=-0.0, connection=1.76, completion=10.90909090909091, energy=7.463955500542387, transformer=0.
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
智能体的动作为: [ 1.         -0.50031835 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=60.03820180892944，设置charger_power=60.03820180892944失败。
功率需求: 72.00 kW, 充电桩功率: 60.04 kW, 最终充电功率: 60.04 kW。
已有历史设置self.charger_power=120.0，设置charger_power=75.36失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=79.68失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=110.56失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=79.19999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 60.03820180892944, -12.191276846195255
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_106 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_216 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 96.0, -19.493631420864393
SOC从 0.69 更新为 0.91。
SOC从 0.60 更新为 0.79。
SOC从 0.32 更新为 0.58。
SOC从 0.28 更新为 0.54。
SOC从 0.61 更新为 0.79。
SOC从 0.42 更新为 0.65。
SOC从 0.18 更新为 0.52。
SOC从 0.47 更新为 0.70。
SOC从 0.67 更新为 0.82。
SOC从 0.48 更新为 0.72。
已断开电池: batt_ev_180
时间步 8: 电池 batt_ev_180 已离开，当前SOC: 78.6%，能量满足率: 78.4%
已断开电池: batt_ev_067
时间步 8: 电池 batt_ev_067 已离开，当前SOC: 82.0%，能量满足率: 75.8%
已断开电池: batt_ev_240
时间步 8: 电池 batt_ev_240 已离开，当前SOC: 90.9%，能量满足率: 85.8%
已断开电池: batt_ev_158
时间步 8 执行前: 电池 batt_ev_158 已充满 (SOC: 79.1%)，离开
已断开电池: batt_ev_106
时间步 8: 电池 batt_ev_106 已离开，当前SOC: 58.1%，能量满足率: 39.5%
已断开电池: batt_ev_216
时间步 8: 电池 batt_ev_216 已离开，当前SOC: 64.6%，能量满足率: 40.4%
不太安全
奖励各项的值：powerloss=-0.19190318762726982, voltage=-0.38858183894389775, ctrl=-0.0, connection=2.24, completion=9.642857142857144, energy=7.364241234083268, transformer=-4.490422587198111.
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
智能体的动作为: [ 1.         -0.50031835 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=60.03820180892944。
功率需求: 64.00 kW, 充电桩功率: 60.04 kW, 最终充电功率: 60.04 kW。
初次设置charger_power=95.20000000000002。
功率需求: 48.00 kW, 充电桩功率: 95.20 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=111.80000000000001。
功率需求: 60.00 kW, 充电桩功率: 111.80 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=62.56失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=112.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_128 充电的有无功功率为 60.03820180892944, -12.191276846195255
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_173 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_132 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.42 更新为 0.61。
SOC从 0.72 更新为 0.86。
SOC从 0.22 更新为 0.48。
SOC从 0.54 更新为 0.70。
SOC从 0.57 更新为 0.80。
SOC从 0.18 更新为 0.46。
SOC从 0.52 更新为 0.73。
SOC从 0.70 更新为 0.87。
SOC从 0.08 更新为 0.40。
SOC从 0.72 更新为 0.84。
已断开电池: batt_ev_055
时间步 9: 电池 batt_ev_055 已离开，当前SOC: 70.1%，能量满足率: 60.2%
已断开电池: batt_ev_247
时间步 9: 电池 batt_ev_247 已离开，当前SOC: 73.2%，能量满足率: 69.0%
已断开电池: batt_ev_090
时间步 9: 电池 batt_ev_090 已离开，当前SOC: 84.0%，能量满足率: 72.0%
已断开电池: batt_ev_128
时间步 9: 电池 batt_ev_128 已离开，当前SOC: 60.8%，能量满足率: 33.5%
已断开电池: batt_ev_173
时间步 9: 电池 batt_ev_173 已离开，当前SOC: 80.1%，能量满足率: 56.3%
已断开电池: batt_ev_132
时间步 9: 电池 batt_ev_132 已离开，当前SOC: 46.3%，能量满足率: 35.4%
不太安全
奖励各项的值：powerloss=-0.20677881385836497, voltage=-0.47588438485840046, ctrl=-0.0, connection=2.72, completion=7.9411764705882355, energy=7.024324822756536, transformer=-2.8589488131073724.
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
智能体的动作为: [ 1.         -0.50031835 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=60.03820180892944。
功率需求: 100.00 kW, 充电桩功率: 60.04 kW, 最终充电功率: 60.04 kW。
已有历史设置self.charger_power=95.20000000000002，设置charger_power=47.19999999999999失败。
功率需求: 30.00 kW, 充电桩功率: 95.20 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=50.400000000000006。
功率需求: 48.00 kW, 充电桩功率: 50.40 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=26.560000000000002失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_191 充电的有无功功率为 60.03820180892944, -12.191276846195255
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_161 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.18 更新为 0.35。
SOC从 0.86 更新为 0.95。
SOC从 0.48 更新为 0.69。
SOC从 0.22 更新为 0.52。
SOC从 0.22 更新为 0.50。
SOC从 0.82 更新为 0.99。
SOC从 0.28 更新为 0.57。
SOC从 0.87 更新为 0.94。
SOC从 0.40 更新为 0.66。
SOC从 0.38 更新为 0.62。
已断开电池: batt_ev_096
时间步 10 执行前: 电池 batt_ev_096 已充满 (SOC: 94.4%)，离开
已断开电池: batt_ev_220
时间步 10 执行前: 电池 batt_ev_220 已充满 (SOC: 94.9%)，离开
已断开电池: batt_ev_150
时间步 10: 电池 batt_ev_150 已离开，当前SOC: 65.7%，能量满足率: 64.1%
已断开电池: batt_ev_191
时间步 10: 电池 batt_ev_191 已离开，当前SOC: 35.3%，能量满足率: 21.6%
已断开电池: batt_ev_161
时间步 10: 电池 batt_ev_161 已离开，当前SOC: 49.8%，能量满足率: 36.5%
不太安全
奖励各项的值：powerloss=-0.22019042899090072, voltage=-0.45811751572637727, ctrl=-0.0, connection=3.12, completion=8.461538461538462, energy=6.949971290759356, transformer=-3.3181345254706858.
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
智能体的动作为: [ 1.         -0.50031835 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=60.03820180892944。
功率需求: 80.00 kW, 充电桩功率: 60.04 kW, 最终充电功率: 60.04 kW。
初次设置charger_power=76.79999999999998。
功率需求: 48.00 kW, 充电桩功率: 76.80 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=116.39999999999998失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=50.400000000000006，设置charger_power=2.3999999999999773失败。
功率需求: 30.00 kW, 充电桩功率: 50.40 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=62.32000000000001。
功率需求: 36.00 kW, 充电桩功率: 62.32 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 60.03820180892944, -12.191276846195255
已在 set_all_batteries_before_solve 中设置 batt_ev_008 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_085 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.18 更新为 0.37。
SOC从 0.68 更新为 0.88。
SOC从 0.69 更新为 0.85。
SOC从 0.52 更新为 0.70。
SOC从 0.28 更新为 0.51。
SOC从 0.99 更新为 1.00。
SOC从 0.57 更新为 0.75。
SOC从 0.42 更新为 0.66。
SOC从 0.62 更新为 0.84。
SOC从 0.62 更新为 0.79。
已断开电池: batt_ev_016
时间步 11: 电池 batt_ev_016 已离开，当前SOC: 85.2%，能量满足率: 83.1%
已断开电池: batt_ev_193
时间步 11: 电池 batt_ev_193 已离开，当前SOC: 69.8%，能量满足率: 62.8%
已断开电池: batt_ev_186
时间步 11 执行前: 电池 batt_ev_186 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_008
时间步 11 执行前: 电池 batt_ev_008 已充满 (SOC: 88.0%)，离开
已断开电池: batt_ev_085
时间步 11 执行前: 电池 batt_ev_085 已充满 (SOC: 84.0%)，离开
奖励各项的值：powerloss=-0.2245958606340166, voltage=-0.49258966285138817, ctrl=-0.0, connection=3.52, completion=9.545454545454545, energy=7.173715847331835, transformer=0.
时间步 11: 电池 batt_ev_222 已错过离开时间，无法接入
已连接电池 batt_ev_114, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_114 已接入
已连接电池 batt_ev_009, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_009 已接入
已连接电池 batt_ev_113, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_065, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_203, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [ 1.         -0.50032073 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=60.03820180892944，设置charger_power=60.038487911224365失败。
功率需求: 64.00 kW, 充电桩功率: 60.04 kW, 最终充电功率: 60.04 kW。
初次设置charger_power=16.319999999999993。
功率需求: 15.00 kW, 充电桩功率: 16.32 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=82.08000000000001。
功率需求: 36.00 kW, 充电桩功率: 82.08 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=87.68失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=70.80000000000001失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 60.03820180892944, -12.191276846195255
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.37 更新为 0.56。
SOC从 0.92 更新为 0.99。
SOC从 0.18 更新为 0.47。
SOC从 0.28 更新为 0.67。
SOC从 0.51 更新为 0.65。
SOC从 0.62 更新为 0.79。
SOC从 0.75 更新为 0.86。
SOC从 0.66 更新为 0.84。
SOC从 0.28 更新为 0.62。
SOC从 0.79 更新为 0.91。
已断开电池: batt_ev_194
时间步 12: 电池 batt_ev_194 已离开，当前SOC: 86.1%，能量满足率: 83.1%
已断开电池: batt_ev_170
时间步 12: 电池 batt_ev_170 已离开，当前SOC: 84.4%，能量满足率: 75.8%
不太安全
奖励各项的值：powerloss=-0.23073035356291993, voltage=-0.5115621104574686, ctrl=-0.0, connection=3.68, completion=9.130434782608695, energy=7.207063102149781, transformer=-0.5627620116653589.
已连接电池 batt_ev_011, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 12 执行前: 排队电池 batt_ev_011 已接入
已连接电池 batt_ev_041, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [ 1.         -0.50031906 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=60.03820180892944，设置charger_power=60.03828763961792失败。
功率需求: 48.00 kW, 充电桩功率: 60.04 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=16.319999999999993，设置charger_power=1.3199999999999932失败。
功率需求: 15.00 kW, 充电桩功率: 16.32 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=101.75999999999999失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=91.19999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=82.08000000000001，设置charger_power=46.08000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 82.08 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=66.72失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=30.80000000000001失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_011 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.56 更新为 0.71。
SOC从 0.99 更新为 1.00。
SOC从 0.47 更新为 0.70。
SOC从 0.67 更新为 0.90。
SOC从 0.65 更新为 0.79。
SOC从 0.79 更新为 0.90。
SOC从 0.32 更新为 0.55。
SOC从 0.12 更新为 0.49。
SOC从 0.62 更新为 0.83。
SOC从 0.91 更新为 0.98。
已断开电池: batt_ev_078
时间步 13 执行前: 电池 batt_ev_078 已充满 (SOC: 98.3%)，离开
已断开电池: batt_ev_000
时间步 13: 电池 batt_ev_000 已离开，当前SOC: 70.5%，能量满足率: 65.7%
已断开电池: batt_ev_162
时间步 13: 电池 batt_ev_162 已离开，当前SOC: 78.8%，能量满足率: 72.5%
已断开电池: batt_ev_114
时间步 13 执行前: 电池 batt_ev_114 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_011
时间步 13: 电池 batt_ev_011 已离开，当前SOC: 54.9%，能量满足率: 34.6%
奖励各项的值：powerloss=-0.22941150213375044, voltage=-0.5495451201355284, ctrl=-0.0, connection=4.08, completion=9.411764705882353, energy=7.231499576761581, transformer=0.
已连接电池 batt_ev_232, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_232 已接入
已连接电池 batt_ev_237, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_237 已接入
已连接电池 batt_ev_052, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_052 已接入
已连接电池 batt_ev_206, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 62kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_206 已接入
已连接电池 batt_ev_172, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
智能体的动作为: [ 1.        -0.5173061 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=62.076730728149414。
功率需求: 48.00 kW, 充电桩功率: 62.08 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=60.72。
功率需求: 24.00 kW, 充电桩功率: 60.72 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=29.75999999999999失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=82.08000000000001，设置charger_power=22.080000000000013失败。
功率需求: 15.00 kW, 充电桩功率: 82.08 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=110.08失败。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=30.72失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=99.2。
功率需求: 48.00 kW, 充电桩功率: 99.20 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_052 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_206 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.38 更新为 0.56。
SOC从 0.78 更新为 0.87。
SOC从 0.70 更新为 0.82。
SOC从 0.90 更新为 1.00。
SOC从 0.38 更新为 0.58。
SOC从 0.90 更新为 0.97。
SOC从 0.22 更新为 0.46。
SOC从 0.49 更新为 0.79。
SOC从 0.83 更新为 0.96。
SOC从 0.38 更新为 0.68。
已断开电池: batt_ev_113
时间步 14 执行前: 电池 batt_ev_113 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_065
时间步 14: 电池 batt_ev_065 已离开，当前SOC: 96.7%，能量满足率: 96.5%
已断开电池: batt_ev_203
时间步 14: 电池 batt_ev_203 已离开，当前SOC: 96.2%，能量满足率: 97.4%
已断开电池: batt_ev_206
时间步 14: 电池 batt_ev_206 已离开，当前SOC: 46.2%，能量满足率: 40.3%
奖励各项的值：powerloss=-0.2217300722424331, voltage=-0.5430009370495958, ctrl=-0.0, connection=4.4, completion=9.272727272727273, energy=7.313164689963848, transformer=0.
已连接电池 batt_ev_229, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_229 已接入
已连接电池 batt_ev_164, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_164 已接入
已连接电池 batt_ev_134, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_214, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 80kWh，并创BMS。
智能体的动作为: [ 1.         -0.60464966 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=62.076730728149414，设置charger_power=72.55795955657959失败。
功率需求: 36.00 kW, 充电桩功率: 62.08 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=60.72，设置charger_power=36.72失败。
功率需求: 15.00 kW, 充电桩功率: 60.72 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=73.83999999999997失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=100.80000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=46.08000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=99.2，设置charger_power=51.2失败。
功率需求: 36.00 kW, 充电桩功率: 99.20 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_052 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.56 更新为 0.70。
SOC从 0.87 更新为 0.92。
SOC从 0.82 更新为 0.94。
SOC从 0.38 更新为 0.58。
SOC从 0.58 更新为 0.73。
SOC从 0.42 更新为 0.63。
SOC从 0.32 更新为 0.62。
SOC从 0.79 更新为 0.93。
SOC从 0.48 更新为 0.73。
SOC从 0.68 更新为 0.91。
已断开电池: batt_ev_009
时间步 15: 电池 batt_ev_009 已离开，当前SOC: 93.7%，能量满足率: 94.7%
已断开电池: batt_ev_232
时间步 15: 电池 batt_ev_232 已离开，当前SOC: 70.3%，能量满足率: 53.8%
已断开电池: batt_ev_052
时间步 15 执行前: 电池 batt_ev_052 已充满 (SOC: 73.0%)，离开
奖励各项的值：powerloss=-0.22274533582728478, voltage=-0.537724640917292, ctrl=-0.0, connection=4.64, completion=9.310344827586206, energy=7.363356771553495, transformer=0.
已连接电池 batt_ev_143, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_143 已接入
已连接电池 batt_ev_245, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_245 已接入
已连接电池 batt_ev_098, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_098 已接入
智能体的动作为: [ 1.         -0.60461867 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=72.5542402267456。
功率需求: 64.00 kW, 充电桩功率: 72.55 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=60.72，设置charger_power=21.72失败。
功率需求: 15.00 kW, 充电桩功率: 60.72 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=100.80000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=84.24000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=82.88失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=14.080000000000013失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=86.4失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=99.2，设置charger_power=15.199999999999989失败。
功率需求: 15.00 kW, 充电桩功率: 99.20 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.48 更新为 0.75。
SOC从 0.92 更新为 0.98。
SOC从 0.38 更新为 0.56。
SOC从 0.58 更新为 0.73。
SOC从 0.42 更新为 0.65。
SOC从 0.63 更新为 0.79。
SOC从 0.62 更新为 0.84。
SOC从 0.93 更新为 1.00。
SOC从 0.73 更新为 0.86。
SOC从 0.91 更新为 1.00。
已断开电池: batt_ev_041
时间步 16 执行前: 电池 batt_ev_041 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_237
时间步 16: 电池 batt_ev_237 已离开，当前SOC: 97.6%，能量满足率: 97.8%
已断开电池: batt_ev_172
时间步 16 执行前: 电池 batt_ev_172 已充满 (SOC: 99.9%)，离开
奖励各项的值：powerloss=-0.21845449959810345, voltage=-0.5305781886568517, ctrl=-0.0, connection=4.88, completion=9.83606557377049, energy=7.48946395812713, transformer=0.
已连接电池 batt_ev_190, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 63kWh，并创BMS。
时间步 16 执行前: 排队电池 batt_ev_190 已接入
已连接电池 batt_ev_069, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 56kWh，并创BMS。
已连接电池 batt_ev_071, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
智能体的动作为: [ 1.        -0.6149538 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=72.5542402267456，设置charger_power=58.72失败。
功率需求: 32.00 kW, 充电桩功率: 72.55 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=115.68失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=64.80000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=98.4失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.24000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=34.879999999999995失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=46.39999999999998失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.75 更新为 0.89。
SOC从 0.18 更新为 0.58。
SOC从 0.56 更新为 0.70。
SOC从 0.73 更新为 0.83。
SOC从 0.65 更新为 0.82。
SOC从 0.79 更新为 0.89。
SOC从 0.84 更新为 0.99。
SOC从 0.38 更新为 0.59。
SOC从 0.86 更新为 0.93。
SOC从 0.42 更新为 0.63。
已断开电池: batt_ev_134
时间步 17 执行前: 电池 batt_ev_134 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_214
时间步 17: 电池 batt_ev_214 已离开，当前SOC: 93.3%，能量满足率: 90.6%
已断开电池: batt_ev_245
时间步 17: 电池 batt_ev_245 已离开，当前SOC: 69.8%，能量满足率: 53.0%
奖励各项的值：powerloss=-0.22533028620177697, voltage=-0.5083361820513788, ctrl=-0.0, connection=5.12, completion=9.84375, energy=7.51910674607477, transformer=0.
智能体的动作为: [ 1.        -0.6047345 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=72.5542402267456，设置charger_power=26.72失败。
功率需求: 20.00 kW, 充电桩功率: 72.55 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=106.63999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=40.80000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=50.400000000000006失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=24.24000000000001失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=90.88失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.89 更新为 0.97。
SOC从 0.58 更新为 0.81。
SOC从 0.83 更新为 0.93。
SOC从 0.82 更新为 0.93。
SOC从 0.89 更新为 0.96。
SOC从 0.59 更新为 0.76。
SOC从 0.63 更新为 0.78。
已断开电池: batt_ev_229
时间步 18 执行前: 电池 batt_ev_229 已充满 (SOC: 93.0%)，离开
已断开电池: batt_ev_143
时间步 18: 电池 batt_ev_143 已离开，当前SOC: 97.2%，能量满足率: 98.3%
已断开电池: batt_ev_098
时间步 18: 电池 batt_ev_098 已离开，当前SOC: 93.4%，能量满足率: 91.8%
已断开电池: batt_ev_071
时间步 18 执行前: 电池 batt_ev_071 已充满 (SOC: 78.5%)，离开
奖励各项的值：powerloss=-0.22057575750854308, voltage=-0.3412579562854079, ctrl=-0.0, connection=5.44, completion=10.147058823529413, energy=7.650544319011018, transformer=0.
已连接电池 batt_ev_083, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_174, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_167, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
已有历史设置self.charger_power=120.0，设置charger_power=46.639999999999986失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=69.11999999999998。
功率需求: 48.00 kW, 充电桩功率: 69.12 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=9.240000000000009失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=54.879999999999995失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
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
奖励各项的值：powerloss=-0.21482539391959862, voltage=-0.21466135235848727, ctrl=-0.0, connection=5.68, completion=10.985915492957746, energy=7.749817094264074, transformer=0.
已连接电池 batt_ev_115, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
已连接电池 batt_ev_181, 初始SOC: 56.99999999999999%, 最大功率: 80kW, 电池容量: 69kWh，并创BMS。
已连接电池 batt_ev_182, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 95kWh，并创BMS。
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=118.68。
功率需求: 48.00 kW, 充电桩功率: 118.68 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=30.879999999999995失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=90.72失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.12 更新为 0.45。
SOC从 0.57 更新为 0.74。
SOC从 0.28 更新为 0.60。
SOC从 0.48 更新为 0.73。
SOC从 0.86 更新为 0.93。
SOC从 0.56 更新为 0.73。
奖励各项的值：powerloss=-0.21101247143160237, voltage=-0.15890266116691532, ctrl=-0.0, connection=5.68, completion=10.985915492957746, energy=7.749817094264074, transformer=0.
已连接电池 batt_ev_037, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_138, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
已连接电池 batt_ev_095, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
智能体的动作为: [ 1.        -0.9567403 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=120.0，设置charger_power=101.92失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=89.44。
功率需求: 48.00 kW, 充电桩功率: 89.44 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=118.68，设置charger_power=70.68失败。
功率需求: 32.00 kW, 充电桩功率: 118.68 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=72.47999999999999失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=15.879999999999995失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=54.72失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
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
SOC从 0.74 更新为 0.86。
SOC从 0.60 更新为 0.79。
SOC从 0.73 更新为 0.85。
SOC从 0.93 更新为 1.00。
SOC从 0.73 更新为 0.85。
SOC从 0.32 更新为 0.57。
已断开电池: batt_ev_069
时间步 21 执行前: 电池 batt_ev_069 已充满 (SOC: 99.6%)，离开
已断开电池: batt_ev_138
时间步 21 执行前: 电池 batt_ev_138 已充满 (SOC: 75.9%)，离开
奖励各项的值：powerloss=-0.21219053025475168, voltage=-0.11501300343192744, ctrl=-0.0, connection=5.84, completion=11.506849315068493, energy=7.811465940996564, transformer=0.
已连接电池 batt_ev_197, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 75kWh，并创BMS。
已连接电池 batt_ev_026, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 102kWh，并创BMS。
已连接电池 batt_ev_212, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [ 1.        -0.8888414 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=120.0，设置charger_power=53.91999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=108.96失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=118.68，设置charger_power=38.68000000000001失败。
功率需求: 20.00 kW, 充电桩功率: 118.68 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=81.60000000000002失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=40.47999999999999失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=30.72失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=112.80000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_212 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.71 更新为 0.84。
SOC从 0.32 更新为 0.56。
SOC从 0.43 更新为 0.68。
SOC从 0.86 更新为 0.93。
SOC从 0.79 更新为 0.91。
SOC从 0.52 更新为 0.68。
SOC从 0.85 更新为 0.97。
SOC从 0.22 更新为 0.50。
SOC从 0.85 更新为 0.97。
SOC从 0.57 更新为 0.75。
已断开电池: batt_ev_174
时间步 22: 电池 batt_ev_174 已离开，当前SOC: 96.8%，能量满足率: 98.5%
已断开电池: batt_ev_167
时间步 22: 电池 batt_ev_167 已离开，当前SOC: 96.7%，能量满足率: 98.0%
已断开电池: batt_ev_115
时间步 22 执行前: 电池 batt_ev_115 已充满 (SOC: 83.7%)，离开
已断开电池: batt_ev_181
时间步 22 执行前: 电池 batt_ev_181 已充满 (SOC: 93.2%)，离开
已断开电池: batt_ev_182
时间步 22: 电池 batt_ev_182 已离开，当前SOC: 91.2%，能量满足率: 90.2%
奖励各项的值：powerloss=-0.2037772364971311, voltage=-0.10166206113458864, ctrl=-0.0, connection=6.24, completion=11.538461538461538, energy=7.934768929497935, transformer=0.
已连接电池 batt_ev_010, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 71kWh，并创BMS。
时间步 22 执行前: 排队电池 batt_ev_010 已接入
已连接电池 batt_ev_241, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 68kWh，并创BMS。
已连接电池 batt_ev_084, 初始SOC: 78.0%, 最大功率: 100kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_038, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
已连接电池 batt_ev_040, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
智能体的动作为: [ 1.         -0.81043464 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=97.25215673446655。
功率需求: 96.00 kW, 充电桩功率: 97.25 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=60.96000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=54.56。
功率需求: 40.00 kW, 充电桩功率: 54.56 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=96.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=108.48失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=50.16。
功率需求: 24.00 kW, 充电桩功率: 50.16 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=64.80000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_212 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_084 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.48 更新为 0.82。
SOC从 0.56 更新为 0.73。
SOC从 0.68 更新为 0.87。
SOC从 0.48 更新为 0.66。
SOC从 0.78 更新为 0.94。
SOC从 0.68 更新为 0.84。
SOC从 0.42 更新为 0.70。
SOC从 0.50 更新为 0.72。
SOC从 0.78 更新为 0.89。
SOC从 0.75 更新为 0.87。
已断开电池: batt_ev_212
时间步 23: 电池 batt_ev_212 已离开，当前SOC: 72.0%，能量满足率: 65.8%
奖励各项的值：powerloss=-0.18987540291233118, voltage=-0.11707938729940581, ctrl=-0.0, connection=6.32, completion=11.39240506329114, energy=7.917606631256455, transformer=0.
已连接电池 batt_ev_046, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_046 已接入
智能体的动作为: [ 1.        -0.6060522 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=97.25215673446655，设置charger_power=51.68000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 97.25 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=109.44失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=24.960000000000008失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=93.44失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=54.56，设置charger_power=14.560000000000002失败。
功率需求: 25.00 kW, 充电桩功率: 54.56 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.0失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=70.56失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=113.68。
功率需求: 48.00 kW, 充电桩功率: 113.68 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=50.16，设置charger_power=26.159999999999997失败。
功率需求: 15.00 kW, 充电桩功率: 50.16 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=32.80000000000001失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_084 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_046 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.82 更新为 0.99。
SOC从 0.73 更新为 0.85。
SOC从 0.87 更新为 0.95。
SOC从 0.66 更新为 0.79。
SOC从 0.94 更新为 1.00。
SOC从 0.84 更新为 0.95。
SOC从 0.70 更新为 0.90。
SOC从 0.42 更新为 0.66。
SOC从 0.89 更新为 0.95。
SOC从 0.87 更新为 0.95。
已断开电池: batt_ev_037
时间步 24: 电池 batt_ev_037 已离开，当前SOC: 95.1%，能量满足率: 95.6%
已断开电池: batt_ev_197
时间步 24: 电池 batt_ev_197 已离开，当前SOC: 94.7%，能量满足率: 92.8%
已断开电池: batt_ev_010
时间步 24 执行前: 电池 batt_ev_010 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_084
时间步 24 执行前: 电池 batt_ev_084 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_038
时间步 24: 电池 batt_ev_038 已离开，当前SOC: 90.3%，能量满足率: 86.2%
奖励各项的值：powerloss=-0.16228770331342024, voltage=-0.18544717673188105, ctrl=-0.0, connection=6.72, completion=11.428571428571427, energy=8.011239111909315, transformer=0.
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
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=61.44失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=9.960000000000008失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=57.44失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=113.68，设置charger_power=65.68失败。
功率需求: 36.00 kW, 充电桩功率: 113.68 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=50.16，设置charger_power=11.159999999999997失败。
功率需求: 15.00 kW, 充电桩功率: 50.16 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=33.599999999999994。
功率需求: 25.00 kW, 充电桩功率: 33.60 kW, 最终充电功率: 25.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_046 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_050 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_125 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 25.0, -5.076466515850102
SOC从 0.28 更新为 0.59。
SOC从 0.85 更新为 0.97。
SOC从 0.95 更新为 1.00。
SOC从 0.79 更新为 0.88。
SOC从 0.28 更新为 0.50。
SOC从 0.52 更新为 0.66。
SOC从 0.28 更新为 0.68。
SOC从 0.66 更新为 0.85。
SOC从 0.95 更新为 1.00。
SOC从 0.88 更新为 0.97。
已断开电池: batt_ev_095
时间步 25 执行前: 电池 batt_ev_095 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_026
时间步 25: 电池 batt_ev_026 已离开，当前SOC: 96.7%，能量满足率: 98.0%
已断开电池: batt_ev_241
时间步 25: 电池 batt_ev_241 已离开，当前SOC: 87.7%，能量满足率: 90.2%
已断开电池: batt_ev_040
时间步 25 执行前: 电池 batt_ev_040 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_046
时间步 25: 电池 batt_ev_046 已离开，当前SOC: 84.9%，能量满足率: 76.5%
已断开电池: batt_ev_050
时间步 25: 电池 batt_ev_050 已离开，当前SOC: 59.2%，能量满足率: 52.1%
已断开电池: batt_ev_125
时间步 25: 电池 batt_ev_125 已离开，当前SOC: 50.4%，能量满足率: 35.0%
奖励各项的值：powerloss=-0.14597229072385673, voltage=-0.24431050263385767, ctrl=-0.0, connection=7.28, completion=11.208791208791208, energy=8.001446154135321, transformer=0.
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
智能体的动作为: [ 1.        -0.9364281 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=112.3713755607605。
功率需求: 80.00 kW, 充电桩功率: 112.37 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_141 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_075 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.22 更新为 0.51。
SOC从 0.28 更新为 0.68。
SOC从 0.22 更新为 0.51。
SOC从 0.42 更新为 0.64。
SOC从 0.38 更新为 0.64。
SOC从 0.66 更新为 0.81。
SOC从 0.68 更新为 0.92。
SOC从 0.38 更新为 0.59。
SOC从 0.97 更新为 1.00。
已断开电池: batt_ev_109
时间步 26 执行前: 电池 batt_ev_109 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_075
时间步 26 执行前: 电池 batt_ev_075 已充满 (SOC: 64.0%)，离开
不太安全
奖励各项的值：powerloss=-0.15313230313221693, voltage=-0.2683655318488465, ctrl=-0.0, connection=7.44, completion=11.612903225806452, energy=8.04442580673456, transformer=-2.2961187983184232.
已连接电池 batt_ev_031, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_057, 初始SOC: 8.0%, 最大功率: 80kW, 电池容量: 73kWh，并创BMS。
已连接电池 batt_ev_111, 初始SOC: 68.0%, 最大功率: 100kW, 电池容量: 83kWh，并创BMS。
智能体的动作为: [ 1.        -0.6046344 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=112.3713755607605，设置charger_power=72.55612850189209失败。
功率需求: 48.00 kW, 充电桩功率: 112.37 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=96.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=108.47999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=65.27999999999997失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=24.0失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=90.88失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=106.23999999999998。
功率需求: 60.00 kW, 充电桩功率: 106.24 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_141 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_031 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.51 更新为 0.69。
SOC从 0.68 更新为 0.92。
SOC从 0.51 更新为 0.69。
SOC从 0.08 更新为 0.35。
SOC从 0.64 更新为 0.84。
SOC从 0.81 更新为 0.90。
SOC从 0.92 更新为 1.00。
SOC从 0.59 更新为 0.76。
SOC从 0.42 更新为 0.72。
SOC从 0.68 更新为 0.86。
已断开电池: batt_ev_221
时间步 27 执行前: 电池 batt_ev_221 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_141
时间步 27: 电池 batt_ev_141 已离开，当前SOC: 92.0%，能量满足率: 91.4%
已断开电池: batt_ev_031
时间步 27 执行前: 电池 batt_ev_031 已充满 (SOC: 71.6%)，离开
奖励各项的值：powerloss=-0.14226507653279807, voltage=-0.29817798696087694, ctrl=-0.0, connection=7.68, completion=11.875, energy=8.096608928845534, transformer=0.
已连接电池 batt_ev_006, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_006 已接入
已连接电池 batt_ev_225, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 94kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_225 已接入
已连接电池 batt_ev_054, 初始SOC: 82.0%, 最大功率: 120kW, 电池容量: 85kWh，并创BMS。
智能体的动作为: [ 1.         -0.87602746 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=112.3713755607605，设置charger_power=84.16失败。
功率需求: 48.00 kW, 充电桩功率: 112.37 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=103.20000000000002。
功率需求: 36.00 kW, 充电桩功率: 103.20 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=84.16失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.47999999999999失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=33.27999999999997失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=54.879999999999995失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=61.19999999999999。
功率需求: 48.00 kW, 充电桩功率: 61.20 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=106.23999999999998，设置charger_power=46.24000000000001失败。
功率需求: 25.00 kW, 充电桩功率: 106.24 kW, 最终充电功率: 25.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_006 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_225 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.69 更新为 0.87。
SOC从 0.57 更新为 0.72。
SOC从 0.69 更新为 0.87。
SOC从 0.35 更新为 0.57。
SOC从 0.84 更新为 0.97。
SOC从 0.90 更新为 0.96。
SOC从 0.52 更新为 0.71。
SOC从 0.76 更新为 0.86。
SOC从 0.82 更新为 0.96。
SOC从 0.86 更新为 0.94。
已断开电池: batt_ev_137
时间步 28: 电池 batt_ev_137 已离开，当前SOC: 96.0%，能量满足率: 95.8%
已断开电池: batt_ev_047
时间步 28: 电池 batt_ev_047 已离开，当前SOC: 86.2%，能量满足率: 80.4%
已断开电池: batt_ev_006
时间步 28: 电池 batt_ev_006 已离开，当前SOC: 72.0%，能量满足率: 71.4%
奖励各项的值：powerloss=-0.133287339913423, voltage=-0.27988724920259056, ctrl=-0.0, connection=7.92, completion=11.515151515151514, energy=8.101298969251724, transformer=0.
已连接电池 batt_ev_129, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 94kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_129 已接入
已连接电池 batt_ev_088, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 50kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_088 已接入
已连接电池 batt_ev_007, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 84kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_007 已接入
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
已有历史设置self.charger_power=112.3713755607605，设置charger_power=36.16失败。
功率需求: 20.00 kW, 充电桩功率: 112.37 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=36.16失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=8.480000000000018失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=108.48000000000002失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=61.19999999999999，设置charger_power=13.199999999999989失败。
功率需求: 30.00 kW, 充电桩功率: 61.20 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=106.23999999999998，设置charger_power=21.24000000000001失败。
功率需求: 25.00 kW, 充电桩功率: 106.24 kW, 最终充电功率: 25.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_225 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_007 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.87 更新为 0.94。
SOC从 0.28 更新为 0.55。
SOC从 0.87 更新为 0.94。
SOC从 0.57 更新为 0.74。
SOC从 0.97 更新为 1.00。
SOC从 0.38 更新为 0.62。
SOC从 0.71 更新为 0.84。
SOC从 0.32 更新为 0.56。
SOC从 0.96 更新为 1.00。
SOC从 0.94 更新为 1.00。
已断开电池: batt_ev_034
时间步 29: 电池 batt_ev_034 已离开，当前SOC: 94.1%，能量满足率: 94.8%
已断开电池: batt_ev_101
时间步 29: 电池 batt_ev_101 已离开，当前SOC: 94.1%，能量满足率: 94.8%
已断开电池: batt_ev_093
时间步 29 执行前: 电池 batt_ev_093 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_057
时间步 29: 电池 batt_ev_057 已离开，当前SOC: 73.8%，能量满足率: 88.9%
已断开电池: batt_ev_111
时间步 29 执行前: 电池 batt_ev_111 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_225
时间步 29: 电池 batt_ev_225 已离开，当前SOC: 83.9%，能量满足率: 69.4%
已断开电池: batt_ev_054
时间步 29 执行前: 电池 batt_ev_054 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.1367279194754694, voltage=-0.2832393985552373, ctrl=-0.0, connection=8.48, completion=11.60377358490566, energy=8.177500608786366, transformer=0.
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
已连接电池 batt_ev_017, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_087, 初始SOC: 62.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=117.11999999999999。
功率需求: 36.00 kW, 充电桩功率: 117.12 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=76.0失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_007 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_147 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.32 更新为 0.56。
SOC从 0.55 更新为 0.71。
SOC从 0.52 更新为 0.67。
SOC从 0.08 更新为 0.40。
SOC从 0.32 更新为 0.53。
SOC从 0.62 更新为 0.80。
SOC从 0.62 更新为 0.79。
SOC从 0.56 更新为 0.74。
SOC从 0.28 更新为 0.51。
SOC从 0.62 更新为 0.78。
已断开电池: batt_ev_007
时间步 30: 电池 batt_ev_007 已离开，当前SOC: 73.7%，能量满足率: 63.1%
已断开电池: batt_ev_147
时间步 30: 电池 batt_ev_147 已离开，当前SOC: 66.8%，能量满足率: 70.3%
不太安全
奖励各项的值：powerloss=-0.1618950755760586, voltage=-0.30713594497185914, ctrl=-0.0, connection=8.64, completion=11.38888888888889, energy=8.149573675635258, transformer=-3.6727728757630644.
时间步 30: 电池 batt_ev_021 已错过离开时间，无法接入
已连接电池 batt_ev_209, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_209 已接入
已连接电池 batt_ev_178, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 93kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_178 已接入
智能体的动作为: [ 1.        -0.6074875 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=120.0，设置charger_power=72.89849996566772失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=110.72000000000003失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=40.0失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=89.12失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=78.32失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_178 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.56 更新为 0.74。
SOC从 0.71 更新为 0.81。
SOC从 0.38 更新为 0.59。
SOC从 0.40 更新为 0.66。
SOC从 0.53 更新为 0.68。
SOC从 0.80 更新为 0.92。
SOC从 0.79 更新为 0.90。
SOC从 0.42 更新为 0.64。
SOC从 0.51 更新为 0.64。
SOC从 0.78 更新为 0.89。
已断开电池: batt_ev_142
时间步 31: 电池 batt_ev_142 已离开，当前SOC: 74.0%，能量满足率: 70.0%
已断开电池: batt_ev_211
时间步 31 执行前: 电池 batt_ev_211 已充满 (SOC: 90.3%)，离开
奖励各项的值：powerloss=-0.16869353822740413, voltage=-0.25774722864233324, ctrl=-0.0, connection=8.8, completion=11.454545454545455, energy=8.15594506335098, transformer=0.
已连接电池 batt_ev_110, 初始SOC: 22.0%, 最大功率: 100kW, 电池容量: 65kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_110 已接入
已连接电池 batt_ev_112, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 71kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_112 已接入
智能体的动作为: [ 1.         -0.96382284 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=115.65874099731445。
功率需求: 100.00 kW, 充电桩功率: 115.66 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=70.72000000000003失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=95.84失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=107.03999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=16.0失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=94.08000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=38.31999999999999失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_178 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_110 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.22 更新为 0.60。
SOC从 0.81 更新为 0.92。
SOC从 0.59 更新为 0.74。
SOC从 0.66 更新为 0.85。
SOC从 0.68 更新为 0.84。
SOC从 0.92 更新为 0.99。
SOC从 0.22 更新为 0.50。
SOC从 0.64 更新为 0.80。
SOC从 0.64 更新为 0.78。
SOC从 0.89 更新为 0.96。
已断开电池: batt_ev_129
时间步 32 执行前: 电池 batt_ev_129 已充满 (SOC: 91.8%)，离开
已断开电池: batt_ev_088
时间步 32 执行前: 电池 batt_ev_088 已充满 (SOC: 99.5%)，离开
已断开电池: batt_ev_079
时间步 32: 电池 batt_ev_079 已离开，当前SOC: 84.9%，能量满足率: 85.5%
已断开电池: batt_ev_053
时间步 32: 电池 batt_ev_053 已离开，当前SOC: 84.1%，能量满足率: 78.9%
已断开电池: batt_ev_087
时间步 32 执行前: 电池 batt_ev_087 已充满 (SOC: 96.3%)，离开
已断开电池: batt_ev_178
时间步 32: 电池 batt_ev_178 已离开，当前SOC: 79.6%，能量满足率: 67.2%
已断开电池: batt_ev_110
时间步 32: 电池 batt_ev_110 已离开，当前SOC: 60.5%，能量满足率: 64.1%
奖励各项的值：powerloss=-0.18596464503751106, voltage=-0.2412919813320169, ctrl=-0.0, connection=9.36, completion=11.538461538461538, energy=8.177120223716356, transformer=0.
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
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=59.84失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=65.28。
功率需求: 36.00 kW, 充电桩功率: 65.28 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=58.08000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=41.04000000000002。
功率需求: 24.00 kW, 充电桩功率: 41.04 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_223 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_198 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.22 更新为 0.53。
SOC从 0.28 更新为 0.59。
SOC从 0.74 更新为 0.85。
SOC从 0.08 更新为 0.36。
SOC从 0.68 更新为 0.86。
SOC从 0.12 更新为 0.47。
SOC从 0.50 更新为 0.67。
SOC从 0.32 更新为 0.50。
SOC从 0.78 更新为 0.87。
SOC从 0.82 更新为 0.93。
已断开电池: batt_ev_017
时间步 33: 电池 batt_ev_017 已离开，当前SOC: 87.1%，能量满足率: 84.4%
已断开电池: batt_ev_209
时间步 33: 电池 batt_ev_209 已离开，当前SOC: 84.6%，能量满足率: 77.6%
已断开电池: batt_ev_112
时间步 33: 电池 batt_ev_112 已离开，当前SOC: 67.1%，能量满足率: 75.1%
已断开电池: batt_ev_223
时间步 33: 电池 batt_ev_223 已离开，当前SOC: 52.9%，能量满足率: 61.7%
已断开电池: batt_ev_198
时间步 33: 电池 batt_ev_198 已离开，当前SOC: 36.4%，能量满足率: 33.8%
奖励各项的值：powerloss=-0.20476654806264344, voltage=-0.31248712033748793, ctrl=-0.0, connection=9.76, completion=11.065573770491804, energy=8.114670955192103, transformer=0.
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
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=78.24失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=65.28，设置charger_power=29.28失败。
功率需求: 15.00 kW, 充电桩功率: 65.28 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=91.36失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=83.2。
功率需求: 48.00 kW, 充电桩功率: 83.20 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=41.04000000000002，设置charger_power=17.039999999999992失败。
功率需求: 15.00 kW, 充电桩功率: 41.04 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_155 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_094 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_068 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_185 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.52 更新为 0.68。
SOC从 0.59 更新为 0.78。
SOC从 0.28 更新为 0.55。
SOC从 0.38 更新为 0.68。
SOC从 0.86 更新为 0.93。
SOC从 0.47 更新为 0.75。
SOC从 0.18 更新为 0.42。
SOC从 0.50 更新为 0.67。
SOC从 0.48 更新为 0.78。
SOC从 0.93 更新为 0.99。
已断开电池: batt_ev_207
时间步 34: 电池 batt_ev_207 已离开，当前SOC: 78.0%，能量满足率: 71.4%
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
奖励各项的值：powerloss=-0.2169249227167392, voltage=-0.3315785633529078, ctrl=-0.0, connection=10.24, completion=10.78125, energy=8.077065050856314, transformer=0.
已连接电池 batt_ev_049, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
已连接电池 batt_ev_023, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
已有历史设置self.charger_power=120.0，设置charger_power=97.91999999999999失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=101.28失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=86.16失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=17.599999999999994。
功率需求: 15.00 kW, 充电桩功率: 17.60 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=83.2，设置charger_power=35.2失败。
功率需求: 24.00 kW, 充电桩功率: 83.20 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_155 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_094 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_185 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_049 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_023 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.68 更新为 0.84。
SOC从 0.32 更新为 0.55。
SOC从 0.55 更新为 0.71。
SOC从 0.68 更新为 0.90。
SOC从 0.92 更新为 0.99。
SOC从 0.78 更新为 0.93。
已断开电池: batt_ev_155
时间步 35: 电池 batt_ev_155 已离开，当前SOC: 83.6%，能量满足率: 68.6%
已断开电池: batt_ev_094
时间步 35: 电池 batt_ev_094 已离开，当前SOC: 70.9%，能量满足率: 61.2%
已断开电池: batt_ev_185
时间步 35 执行前: 电池 batt_ev_185 已充满 (SOC: 93.0%)，离开
奖励各项的值：powerloss=-0.21461058320275508, voltage=-0.3021821149640713, ctrl=-0.0, connection=10.48, completion=10.763358778625953, energy=8.067570717920248, transformer=0.
已连接电池 batt_ev_121, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [ 1.         -0.95268863 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -0.7620749 ]
已有历史设置self.charger_power=120.0，设置charger_power=96.16失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=26.159999999999997失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=17.599999999999994，设置charger_power=2.5999999999999943失败。
功率需求: 15.00 kW, 充电桩功率: 17.60 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_049 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_023 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.55 更新为 0.72。
SOC从 0.90 更新为 1.00。
SOC从 0.99 更新为 1.00。
SOC从 0.48 更新为 0.75。
已断开电池: batt_ev_140
时间步 36 执行前: 电池 batt_ev_140 已充满 (SOC: 99.6%)，离开
已断开电池: batt_ev_049
时间步 36: 电池 batt_ev_049 已离开，当前SOC: 71.6%，能量满足率: 60.0%
已断开电池: batt_ev_023
时间步 36 执行前: 电池 batt_ev_023 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.21437118020320384, voltage=-0.38410769766718866, ctrl=-0.0, connection=10.72, completion=10.970149253731343, energy=8.081008914770782, transformer=0.
智能体的动作为: [ 0.24555576 -0.979301   -1.         -1.         -0.9561635  -1.
 -0.7962081  -1.         -1.         -1.         -0.27765343]
已有历史设置self.charger_power=120.0，设置charger_power=58.72失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 32.0, -6.497877140288132
SOC从 0.75 更新为 0.89。
奖励各项的值：powerloss=-0.21143153572240841, voltage=-0.41796231937924144, ctrl=-0.0, connection=10.72, completion=10.970149253731343, energy=8.081008914770782, transformer=0.
已连接电池 batt_ev_015, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
已连接电池 batt_ev_201, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [-1.         -0.6453291  -0.84871536 -0.99299514 -0.         -0.58736336
 -0.37695846 -0.5814447  -1.         -1.         -0.        ]
已有历史设置self.charger_power=120.0，设置charger_power=26.72失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=69.77336168289185。
功率需求: 36.00 kW, 充电桩功率: 69.77 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.89 更新为 0.97。
SOC从 0.52 更新为 0.67。
SOC从 0.18 更新为 0.47。
已断开电池: batt_ev_121
时间步 38: 电池 batt_ev_121 已离开，当前SOC: 97.2%，能量满足率: 98.3%
奖励各项的值：powerloss=-0.2237562070006199, voltage=-0.38662153385616405, ctrl=-0.0, connection=10.8, completion=10.88888888888889, energy=8.093968170769342, transformer=0.
已连接电池 batt_ev_080, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_204, 初始SOC: 2.0%, 最大功率: 80kW, 电池容量: 81kWh，并创BMS。
智能体的动作为: [ 1.        -1.        -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -0.6438434]
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=69.77336168289185，设置charger_power=81.12失败。
功率需求: 36.00 kW, 充电桩功率: 69.77 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=77.26120948791504。
功率需求: 36.00 kW, 充电桩功率: 77.26 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.02 更新为 0.27。
SOC从 0.67 更新为 0.82。
SOC从 0.47 更新为 0.70。
SOC从 0.57 更新为 0.74。
奖励各项的值：powerloss=-0.21186792609118932, voltage=-0.514894169613791, ctrl=-0.0, connection=10.8, completion=10.88888888888889, energy=8.093968170769342, transformer=0.
已连接电池 batt_ev_183, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 71kWh，并创BMS。
已连接电池 batt_ev_230, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [ 1.         -0.94057167 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -0.7923392 ]
已有历史设置self.charger_power=120.0，设置charger_power=112.8685998916626失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=69.77336168289185，设置charger_power=45.120000000000005失败。
功率需求: 24.00 kW, 充电桩功率: 69.77 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=77.26120948791504，设置charger_power=56.879999999999995失败。
功率需求: 24.00 kW, 充电桩功率: 77.26 kW, 最终充电功率: 24.00 kW。
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
SOC从 0.52 更新为 0.66。
SOC从 0.74 更新为 0.85。
已断开电池: batt_ev_183
时间步 40 执行前: 电池 batt_ev_183 已充满 (SOC: 66.2%)，离开
奖励各项的值：powerloss=-0.2162000015325209, voltage=-0.47540295544610256, ctrl=-0.0, connection=10.88, completion=11.029411764705884, energy=8.107983110690157, transformer=0.
智能体的动作为: [ 1.         -0.86155796 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -0.9614033 ]
已有历史设置self.charger_power=120.0，设置charger_power=103.38695526123047失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=69.77336168289185，设置charger_power=21.120000000000005失败。
功率需求: 15.00 kW, 充电桩功率: 69.77 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=73.83999999999997失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=88.80000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=77.26120948791504，设置charger_power=32.879999999999995失败。
功率需求: 24.00 kW, 充电桩功率: 77.26 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.51 更新为 0.66。
SOC从 0.91 更新为 0.97。
SOC从 0.82 更新为 0.94。
SOC从 0.66 更新为 0.80。
SOC从 0.85 更新为 0.96。
已断开电池: batt_ev_201
时间步 41 执行前: 电池 batt_ev_201 已充满 (SOC: 93.7%)，离开
已断开电池: batt_ev_080
时间步 41 执行前: 电池 batt_ev_080 已充满 (SOC: 95.9%)，离开
已断开电池: batt_ev_204
时间步 41: 电池 batt_ev_204 已离开，当前SOC: 66.2%，能量满足率: 66.9%
已断开电池: batt_ev_230
时间步 41: 电池 batt_ev_230 已离开，当前SOC: 79.7%，能量满足率: 60.2%
奖励各项的值：powerloss=-0.20925334126604664, voltage=-0.3816497057485324, ctrl=-0.0, connection=11.200000000000001, completion=11.142857142857142, energy=8.109950091013195, transformer=0.
智能体的动作为: [ 1.         -1.         -1.         -1.         -1.         -1.
 -0.97519755 -1.         -1.         -1.         -0.6286766 ]
已有历史设置self.charger_power=69.77336168289185，设置charger_power=6.1200000000000045失败。
功率需求: 15.00 kW, 充电桩功率: 69.77 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.97 更新为 1.00。
已断开电池: batt_ev_015
时间步 42 执行前: 电池 batt_ev_015 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.2046090915674499, voltage=-0.22859067966375823, ctrl=-0.0, connection=11.28, completion=11.27659574468085, energy=8.123354700296789, transformer=0.
已连接电池 batt_ev_148, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_215, 初始SOC: 62.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_210, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [-1.         -0.5407891  -0.7425737  -0.8505698  -0.12446368 -0.4488042
 -0.         -0.4580576  -0.09553682 -0.41360766 -0.        ]
初次设置charger_power=89.10884141921997。
功率需求: 120.00 kW, 充电桩功率: 89.11 kW, 最终充电功率: 89.11 kW。
初次设置charger_power=14.935641288757324。
功率需求: 72.00 kW, 充电桩功率: 14.94 kW, 最终充电功率: 14.94 kW。
初次设置charger_power=53.85650396347046。
功率需求: 36.00 kW, 充电桩功率: 53.86 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 89.10884141921997, -18.094321989234675
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 14.935641288757324, -3.0328113158049925
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.28 更新为 0.52。
SOC从 0.62 更新为 0.67。
SOC从 0.57 更新为 0.73。
奖励各项的值：powerloss=-0.21269520204319697, voltage=-0.06280429761849948, ctrl=-0.0, connection=11.28, completion=11.27659574468085, energy=8.123354700296789, transformer=0.
智能体的动作为: [ 0.03486812 -1.         -1.         -1.         -0.8515912  -1.
 -0.779893   -1.         -1.         -1.         -0.18130524]
已有历史设置self.charger_power=89.10884141921997，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 89.11 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=14.935641288757324，设置charger_power=100.6失败。
功率需求: 72.00 kW, 充电桩功率: 14.94 kW, 最终充电功率: 14.94 kW。
已有历史设置self.charger_power=53.85650396347046，设置charger_power=58.599999999999994失败。
功率需求: 24.00 kW, 充电桩功率: 53.86 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -3.486812114715576, -1.1460597198521092
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 14.935641288757324, -3.0328113158049925
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.52 更新为 0.72。
SOC从 0.67 更新为 0.72。
SOC从 0.73 更新为 0.84。
已断开电池: batt_ev_210
时间步 44: 电池 batt_ev_210 已离开，当前SOC: 84.3%，能量满足率: 66.5%
奖励各项的值：powerloss=-0.19614808686784785, voltage=-0.11210939772245743, ctrl=-0.0, connection=11.36, completion=11.19718309859155, energy=8.112992235510651, transformer=0.
已连接电池 batt_ev_146, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
已连接电池 batt_ev_027, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 107kWh，并创BMS。
智能体的动作为: [-0.55701315 -1.         -1.         -1.         -0.67230266 -0.84913325
 -0.7406083  -1.         -1.         -1.         -0.        ]
已有历史设置self.charger_power=89.10884141921997，设置charger_power=100.95999999999998失败。
功率需求: 48.00 kW, 充电桩功率: 89.11 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=14.935641288757324，设置charger_power=80.67631959915161失败。
功率需求: 48.00 kW, 充电桩功率: 14.94 kW, 最终充电功率: 14.94 kW。
初次设置charger_power=88.87299299240112。
功率需求: 64.00 kW, 充电桩功率: 88.87 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 55.70131540298462, 18.308137010515633
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 14.935641288757324, -3.0328113158049925
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 96.0, -19.493631420864393
SOC从 0.72 更新为 0.85。
SOC从 0.32 更新为 0.54。
SOC从 0.72 更新为 0.77。
SOC从 0.42 更新为 0.62。
奖励各项的值：powerloss=-0.2025461105178722, voltage=-0.030839466142991157, ctrl=-0.0, connection=11.36, completion=11.19718309859155, energy=8.112992235510651, transformer=0.
已连接电池 batt_ev_135, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_127, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 88kWh，并创BMS。
已连接电池 batt_ev_165, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 105kWh，并创BMS。
智能体的动作为: [ 1.         -0.95920986 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -0.745683  ]
初次设置charger_power=115.10518312454224。
功率需求: 64.00 kW, 充电桩功率: 115.11 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=89.10884141921997，设置charger_power=52.95999999999998失败。
功率需求: 30.00 kW, 充电桩功率: 89.11 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=14.935641288757324，设置charger_power=70.75999999999999失败。
功率需求: 48.00 kW, 充电桩功率: 14.94 kW, 最终充电功率: 14.94 kW。
已有历史设置self.charger_power=88.87299299240112，设置charger_power=119.28失败。
功率需求: 48.00 kW, 充电桩功率: 88.87 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 14.935641288757324, -3.0328113158049925
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.32 更新为 0.62。
SOC从 0.85 更新为 0.94。
SOC从 0.54 更新为 0.71。
SOC从 0.77 更新为 0.82。
SOC从 0.62 更新为 0.77。
SOC从 0.18 更新为 0.46。
SOC从 0.18 更新为 0.47。
已断开电池: batt_ev_148
时间步 46 执行前: 电池 batt_ev_148 已充满 (SOC: 93.7%)，离开
已断开电池: batt_ev_215
时间步 46: 电池 batt_ev_215 已离开，当前SOC: 81.6%，能量满足率: 65.4%
已断开电池: batt_ev_027
时间步 46: 电池 batt_ev_027 已离开，当前SOC: 71.3%，能量满足率: 65.4%
奖励各项的值：powerloss=-0.192728385433657, voltage=-0.12915242011798833, ctrl=-0.0, connection=11.6, completion=11.172413793103448, energy=8.104350435630357, transformer=0.
已连接电池 batt_ev_003, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_001, 初始SOC: 38.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
已连接电池 batt_ev_086, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
智能体的动作为: [ 1.         -0.93895423 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=115.10518312454224，设置charger_power=82.88失败。
功率需求: 48.00 kW, 充电桩功率: 115.11 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=88.87299299240112，设置charger_power=71.28失败。
功率需求: 32.00 kW, 充电桩功率: 88.87 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -52.24, -17.170457654543814
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.62 更新为 0.84。
SOC从 0.12 更新为 0.37。
SOC从 0.77 更新为 0.88。
SOC从 0.38 更新为 0.72。
SOC从 0.46 更新为 0.69。
SOC从 0.47 更新为 0.69。
SOC从 0.42 更新为 0.68。
已断开电池: batt_ev_146
时间步 47: 电池 batt_ev_146 已离开，当前SOC: 87.6%，能量满足率: 81.4%
已断开电池: batt_ev_135
时间步 47: 电池 batt_ev_135 已离开，当前SOC: 83.9%，能量满足率: 78.6%
奖励各项的值：powerloss=-0.18153905757701477, voltage=-0.16782006390364979, ctrl=-0.0, connection=11.76, completion=11.020408163265307, energy=8.102888343837694, transformer=0.
智能体的动作为: [ 1.         -0.94992363 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=77.6失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=108.63999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=98.63999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.37 更新为 0.57。
SOC从 0.72 更新为 0.89。
SOC从 0.69 更新为 0.86。
SOC从 0.69 更新为 0.87。
SOC从 0.68 更新为 0.87。
已断开电池: batt_ev_165
时间步 48: 电池 batt_ev_165 已离开，当前SOC: 86.6%，能量满足率: 85.7%
奖励各项的值：powerloss=-0.15425032951800924, voltage=-0.17683751372511658, ctrl=-0.0, connection=11.84, completion=10.945945945945946, energy=8.106054156186284, transformer=0.
已连接电池 batt_ev_043, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_051, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
已连接电池 batt_ev_144, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [ 1.         -0.88150924 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -0.9221328 ]
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=103.19999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=29.599999999999994失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=38.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_144 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.42 更新为 0.66。
SOC从 0.48 更新为 0.69。
SOC从 0.22 更新为 0.61。
SOC从 0.57 更新为 0.72。
SOC从 0.89 更新为 1.00。
SOC从 0.86 更新为 0.93。
SOC从 0.87 更新为 0.96。
已断开电池: batt_ev_003
时间步 49: 电池 batt_ev_003 已离开，当前SOC: 95.6%，能量满足率: 95.7%
已断开电池: batt_ev_001
时间步 49 执行前: 电池 batt_ev_001 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_144
时间步 49 执行前: 电池 batt_ev_144 已充满 (SOC: 61.2%)，离开
奖励各项的值：powerloss=-0.13348805536972547, voltage=-0.2264665613439787, ctrl=-0.0, connection=12.08, completion=11.125827814569536, energy=8.140810209577365, transformer=0.
已连接电池 batt_ev_188, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
已连接电池 batt_ev_107, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 60kWh，并创BMS。
已连接电池 batt_ev_131, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [ 1.         -0.85863364 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -0.96866226]
初次设置charger_power=103.03603649139404。
功率需求: 120.00 kW, 充电桩功率: 103.04 kW, 最终充电功率: 103.04 kW。
已有历史设置self.charger_power=120.0，设置charger_power=89.12失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=119.68失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=67.19999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=23.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 103.03603649139404, -20.922359566978844
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.18 更新为 0.48。
SOC从 0.66 更新为 0.84。
SOC从 0.69 更新为 0.84。
SOC从 0.72 更新为 0.82。
SOC从 0.28 更新为 0.61。
SOC从 0.93 更新为 1.00。
SOC从 0.22 更新为 0.55。
已断开电池: batt_ev_127
时间步 50 执行前: 电池 batt_ev_127 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_086
时间步 50: 电池 batt_ev_086 已离开，当前SOC: 82.0%，能量满足率: 87.5%
已断开电池: batt_ev_051
时间步 50 执行前: 电池 batt_ev_051 已充满 (SOC: 84.5%)，离开
奖励各项的值：powerloss=-0.13205535861263956, voltage=-0.26106679258958376, ctrl=-0.0, connection=12.32, completion=11.2987012987013, energy=8.168911309390793, transformer=0.
已连接电池 batt_ev_136, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
已连接电池 batt_ev_116, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 52kWh，并创BMS。
已连接电池 batt_ev_196, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [ 1.        -0.8883828 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=103.03603649139404，设置charger_power=106.60593509674072失败。
功率需求: 96.00 kW, 充电桩功率: 103.04 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=41.120000000000005失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=92.80000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=83.52失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.48 更新为 0.76。
SOC从 0.84 更新为 0.97。
SOC从 0.42 更新为 0.62。
SOC从 0.61 更新为 0.81。
SOC从 0.42 更新为 0.73。
SOC从 0.55 更新为 0.74。
SOC从 0.18 更新为 0.52。
已断开电池: batt_ev_131
时间步 51: 电池 batt_ev_131 已离开，当前SOC: 74.2%，能量满足率: 68.6%
奖励各项的值：powerloss=-0.12876451452466842, voltage=-0.29392186468500503, ctrl=-0.0, connection=12.4, completion=11.225806451612904, energy=8.160498904545383, transformer=0.
已连接电池 batt_ev_005, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_063, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
已连接电池 batt_ev_033, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
已连接电池 batt_ev_077, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
智能体的动作为: [ 1.         -0.88391393 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=103.03603649139404，设置charger_power=83.04000000000002失败。
功率需求: 48.00 kW, 充电桩功率: 103.04 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=9.120000000000005失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=76.8。
功率需求: 36.00 kW, 充电桩功率: 76.80 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=44.80000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=56.639999999999986失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=84.32失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.76 更新为 0.90。
SOC从 0.97 更新为 1.00。
SOC从 0.38 更新为 0.60。
SOC从 0.62 更新为 0.76。
SOC从 0.52 更新为 0.74。
SOC从 0.81 更新为 0.95。
SOC从 0.73 更新为 0.88。
SOC从 0.32 更新为 0.57。
SOC从 0.18 更新为 0.43。
SOC从 0.52 更新为 0.73。
已断开电池: batt_ev_043
时间步 52 执行前: 电池 batt_ev_043 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.13201555171921428, voltage=-0.28929325480715473, ctrl=-0.0, connection=12.48, completion=11.346153846153847, energy=8.172290578234195, transformer=0.
已连接电池 batt_ev_082, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
时间步 52 执行前: 排队电池 batt_ev_082 已接入
智能体的动作为: [ 1.        -0.9364598 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=103.03603649139404，设置charger_power=35.04000000000002失败。
功率需求: 30.00 kW, 充电桩功率: 103.04 kW, 最终充电功率: 30.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=85.91999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=78.24000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=76.8，设置charger_power=40.8失败。
功率需求: 24.00 kW, 充电桩功率: 76.80 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=12.800000000000011失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=24.639999999999986失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.31999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.90 更新为 0.99。
SOC从 0.38 更新为 0.69。
SOC从 0.60 更新为 0.77。
SOC从 0.76 更新为 0.86。
SOC从 0.74 更新为 0.89。
SOC从 0.95 更新为 1.00。
SOC从 0.88 更新为 0.98。
SOC从 0.57 更新为 0.75。
SOC从 0.43 更新为 0.64。
SOC从 0.73 更新为 0.86。
已断开电池: batt_ev_188
时间步 53 执行前: 电池 batt_ev_188 已充满 (SOC: 98.5%)，离开
已断开电池: batt_ev_107
时间步 53 执行前: 电池 batt_ev_107 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_116
时间步 53: 电池 batt_ev_116 已离开，当前SOC: 97.8%，能量满足率: 99.6%
已断开电池: batt_ev_077
时间步 53: 电池 batt_ev_077 已离开，当前SOC: 63.6%，能量满足率: 57.0%
奖励各项的值：powerloss=-0.12673550149707, voltage=-0.2620268865377451, ctrl=-0.0, connection=12.8, completion=11.4375, energy=8.19082702465607, transformer=0.
已连接电池 batt_ev_159, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 53kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_159 已接入
时间步 53: 电池 batt_ev_097 已错过离开时间，无法接入
已连接电池 batt_ev_105, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_105 已接入
已连接电池 batt_ev_058, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_058 已接入
已连接电池 batt_ev_118, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 90kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_118 已接入
智能体的动作为: [ 1.         -0.86025125 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -0.97157145]
初次设置charger_power=67.84。
功率需求: 48.00 kW, 充电桩功率: 67.84 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=62.47999999999999失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=49.91999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=46.24000000000001失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=76.8，设置charger_power=16.80000000000001失败。
功率需求: 15.00 kW, 充电桩功率: 76.80 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=95.83999999999997失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=24.319999999999993失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_105 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_058 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 72.0, -14.620223565648296
SOC从 0.68 更新为 0.91。
SOC从 0.69 更新为 0.93。
SOC从 0.77 更新为 0.88。
SOC从 0.86 更新为 0.92。
SOC从 0.89 更新为 0.99。
SOC从 0.42 更新为 0.65。
SOC从 0.28 更新为 0.50。
SOC从 0.75 更新为 0.88。
SOC从 0.57 更新为 0.77。
SOC从 0.86 更新为 0.95。
已断开电池: batt_ev_136
时间步 54: 电池 batt_ev_136 已离开，当前SOC: 92.0%，能量满足率: 89.3%
已断开电池: batt_ev_196
时间步 54 执行前: 电池 batt_ev_196 已充满 (SOC: 94.7%)，离开
已断开电池: batt_ev_063
时间步 54 执行前: 电池 batt_ev_063 已充满 (SOC: 98.9%)，离开
已断开电池: batt_ev_033
时间步 54: 电池 batt_ev_033 已离开，当前SOC: 87.7%，能量满足率: 84.3%
已断开电池: batt_ev_105
时间步 54: 电池 batt_ev_105 已离开，当前SOC: 65.1%，能量满足率: 41.2%
已断开电池: batt_ev_058
时间步 54 执行前: 电池 batt_ev_058 已充满 (SOC: 49.7%)，离开
奖励各项的值：powerloss=-0.13526882711196575, voltage=-0.2698872424053822, ctrl=-0.0, connection=13.280000000000001, completion=11.566265060240964, energy=8.204919509634873, transformer=0.
已连接电池 batt_ev_199, 初始SOC: 52.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_199 已接入
已连接电池 batt_ev_153, 初始SOC: 2.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_153 已接入
已连接电池 batt_ev_169, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 85kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_169 已接入
已连接电池 batt_ev_059, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
已连接电池 batt_ev_175, 初始SOC: 88.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
智能体的动作为: [ 1.         -0.85878485 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -0.96920604]
已有历史设置self.charger_power=67.84，设置charger_power=19.840000000000003失败。
功率需求: 20.00 kW, 充电桩功率: 67.84 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=14.47999999999999失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=25.919999999999987失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=46.56。
功率需求: 30.00 kW, 充电桩功率: 46.56 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=82.80000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 30.0, -6.091759819020124
SOC从 0.91 更新为 1.00。
SOC从 0.93 更新为 1.00。
SOC从 0.88 更新为 0.95。
SOC从 0.52 更新为 0.72。
SOC从 0.02 更新为 0.25。
SOC从 0.28 更新为 0.57。
SOC从 0.18 更新为 0.46。
SOC从 0.88 更新为 0.96。
SOC从 0.77 更新为 0.90。
已断开电池: batt_ev_005
时间步 55: 电池 batt_ev_005 已离开，当前SOC: 94.9%，能量满足率: 94.9%
已断开电池: batt_ev_082
时间步 55 执行前: 电池 batt_ev_082 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_159
时间步 55 执行前: 电池 batt_ev_159 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.1515987450628164, voltage=-0.25714192963897986, ctrl=-0.0, connection=13.52, completion=11.715976331360947, energy=8.233771475385383, transformer=0.
已连接电池 batt_ev_029, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_195, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
已连接电池 batt_ev_213, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_133, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [ 1.         -0.8602071  -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -0.97150457]
初次设置charger_power=101.68。
功率需求: 48.00 kW, 充电桩功率: 101.68 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=85.91999999999999失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=113.84失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=46.56，设置charger_power=16.560000000000002失败。
功率需求: 30.00 kW, 充电桩功率: 46.56 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=34.80000000000001失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
初次设置charger_power=116.58054828643799。
功率需求: 64.00 kW, 充电桩功率: 116.58 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.38 更新为 0.67。
SOC从 0.28 更新为 0.51。
SOC从 0.18 更新为 0.55。
SOC从 0.72 更新为 0.85。
SOC从 0.25 更新为 0.48。
SOC从 0.57 更新为 0.75。
SOC从 0.46 更新为 0.69。
SOC从 0.96 更新为 1.00。
SOC从 0.90 更新为 0.99。
SOC从 0.42 更新为 0.67。
已断开电池: batt_ev_118
时间步 56 执行前: 电池 batt_ev_118 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_175
时间步 56 执行前: 电池 batt_ev_175 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_213
时间步 56 执行前: 电池 batt_ev_213 已充满 (SOC: 50.7%)，离开
奖励各项的值：powerloss=-0.1792012870245021, voltage=-0.23395853162654356, ctrl=-0.0, connection=13.76, completion=12.034883720930232, energy=8.264577786861219, transformer=0.
已连接电池 batt_ev_145, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_044, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
已连接电池 batt_ev_154, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
智能体的动作为: [ 1.         -0.94456553 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=101.68，设置charger_power=53.68000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 101.68 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=119.03999999999999。
功率需求: 48.00 kW, 充电桩功率: 119.04 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=45.920000000000016失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=84.80000000000001失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=65.84失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=116.58054828643799，设置charger_power=82.16失败。
功率需求: 48.00 kW, 充电桩功率: 116.58 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.67 更新为 0.89。
SOC从 0.52 更新为 0.71。
SOC从 0.55 更新为 0.77。
SOC从 0.85 更新为 0.98。
SOC从 0.48 更新为 0.67。
SOC从 0.75 更新为 0.87。
SOC从 0.69 更新为 0.86。
SOC从 0.18 更新为 0.44。
SOC从 0.32 更新为 0.53。
SOC从 0.67 更新为 0.86。
已断开电池: batt_ev_199
时间步 57 执行前: 电池 batt_ev_199 已充满 (SOC: 98.1%)，离开
已断开电池: batt_ev_153
时间步 57: 电池 batt_ev_153 已离开，当前SOC: 66.6%，能量满足率: 67.3%
已断开电池: batt_ev_029
时间步 57 执行前: 电池 batt_ev_029 已充满 (SOC: 86.4%)，离开
奖励各项的值：powerloss=-0.1911613804774817, voltage=-0.24962264388312283, ctrl=-0.0, connection=14.0, completion=12.17142857142857, energy=8.27564656326228, transformer=0.
已连接电池 batt_ev_179, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_179 已接入
已连接电池 batt_ev_246, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 74kWh，并创BMS。
已连接电池 batt_ev_184, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [ 1.         -0.93286216 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=101.68，设置charger_power=17.680000000000007失败。
功率需求: 15.00 kW, 充电桩功率: 101.68 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=119.03999999999999，设置charger_power=71.03999999999999失败。
功率需求: 32.00 kW, 充电桩功率: 119.04 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=76.96000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=44.80000000000001失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=29.840000000000003失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.89 更新为 0.98。
SOC从 0.71 更新为 0.84。
SOC从 0.77 更新为 0.91。
SOC从 0.18 更新为 0.55。
SOC从 0.48 更新为 0.75。
SOC从 0.87 更新为 0.94。
SOC从 0.86 更新为 0.93。
SOC从 0.44 更新为 0.65。
SOC从 0.53 更新为 0.69。
SOC从 0.28 更新为 0.57。
已断开电池: batt_ev_169
时间步 58: 电池 batt_ev_169 已离开，当前SOC: 94.2%，能量满足率: 94.5%
已断开电池: batt_ev_059
时间步 58: 电池 batt_ev_059 已离开，当前SOC: 93.0%，能量满足率: 93.8%
已断开电池: batt_ev_195
时间步 58 执行前: 电池 batt_ev_195 已充满 (SOC: 98.4%)，离开
已断开电池: batt_ev_133
时间步 58: 电池 batt_ev_133 已离开，当前SOC: 91.2%，能量满足率: 91.5%
奖励各项的值：powerloss=-0.20513905265640356, voltage=-0.2595676548707848, ctrl=-0.0, connection=14.32, completion=12.067039106145252, energy=8.302867438809601, transformer=0.
已连接电池 batt_ev_066, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
时间步 58 执行前: 排队电池 batt_ev_066 已接入
已连接电池 batt_ev_233, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
已连接电池 batt_ev_219, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_249, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
智能体的动作为: [ 1.        -0.9298734 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=111.58480882644653。
功率需求: 120.00 kW, 充电桩功率: 111.58 kW, 最终充电功率: 111.58 kW。
已有历史设置self.charger_power=119.03999999999999，设置charger_power=39.03999999999999失败。
功率需求: 32.00 kW, 充电桩功率: 119.04 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=71.2失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=73.91999999999999失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=82.24000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=118.39999999999998失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 111.58480882644653, -22.65826182739963
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.08 更新为 0.45。
SOC从 0.84 更新为 0.97。
SOC从 0.22 更新为 0.55。
SOC从 0.55 更新为 0.78。
SOC从 0.75 更新为 0.89。
SOC从 0.18 更新为 0.41。
SOC从 0.08 更新为 0.38。
SOC从 0.65 更新为 0.80。
SOC从 0.69 更新为 0.85。
SOC从 0.57 更新为 0.75。
已断开电池: batt_ev_145
时间步 59: 电池 batt_ev_145 已离开，当前SOC: 97.2%，能量满足率: 98.2%
已断开电池: batt_ev_044
时间步 59: 电池 batt_ev_044 已离开，当前SOC: 80.1%，能量满足率: 77.6%
已断开电池: batt_ev_179
时间步 59: 电池 batt_ev_179 已离开，当前SOC: 78.0%，能量满足率: 75.0%
不太安全
奖励各项的值：powerloss=-0.22172388354409353, voltage=-0.2800610360807254, ctrl=-0.0, connection=14.56, completion=11.868131868131867, energy=8.30378881343863, transformer=-2.018673063474273.
已连接电池 batt_ev_032, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_032 已接入
已连接电池 batt_ev_060, 初始SOC: 56.99999999999999%, 最大功率: 100kW, 电池容量: 90kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_060 已接入
已连接电池 batt_ev_103, 初始SOC: 72.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_103 已接入
智能体的动作为: [ 1.       -0.995117 -1.       -1.       -1.       -1.       -1.
 -1.       -1.       -1.       -1.      ]
已有历史设置self.charger_power=111.58480882644653，设置charger_power=119.41404104232788失败。
功率需求: 96.00 kW, 充电桩功率: 111.58 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=80.4失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=33.920000000000016失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=60.48000000000002。
功率需求: 24.00 kW, 充电桩功率: 60.48 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=58.39999999999998失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=104.63999999999999失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_060 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_103 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.45 更新为 0.76。
SOC从 0.48 更新为 0.68。
SOC从 0.55 更新为 0.75。
SOC从 0.57 更新为 0.74。
SOC从 0.89 更新为 0.97。
SOC从 0.41 更新为 0.60。
SOC从 0.38 更新为 0.62。
SOC从 0.72 更新为 0.83。
SOC从 0.85 更新为 0.95。
SOC从 0.75 更新为 0.86。
已断开电池: batt_ev_154
时间步 60: 电池 batt_ev_154 已离开，当前SOC: 95.2%，能量满足率: 95.7%
已断开电池: batt_ev_246
时间步 60: 电池 batt_ev_246 已离开，当前SOC: 97.0%，能量满足率: 98.0%
已断开电池: batt_ev_184
时间步 60: 电池 batt_ev_184 已离开，当前SOC: 86.3%，能量满足率: 83.2%
已断开电池: batt_ev_233
时间步 60: 电池 batt_ev_233 已离开，当前SOC: 75.3%，能量满足率: 70.2%
已断开电池: batt_ev_103
时间步 60: 电池 batt_ev_103 已离开，当前SOC: 83.1%，能量满足率: 55.6%
奖励各项的值：powerloss=-0.221309507613973, voltage=-0.2882097233207981, ctrl=-0.0, connection=14.96, completion=11.550802139037433, energy=8.297064781073955, transformer=0.
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
智能体的动作为: [ 1.         -0.93212616 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=111.58480882644653，设置charger_power=72.08000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 111.58 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=106.56失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=94.80000000000001失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=105.19999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=37.44。
功率需求: 20.00 kW, 充电桩功率: 37.44 kW, 最终充电功率: 20.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_060 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_217 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 20.0, -4.061173212680082
SOC从 0.76 更新为 0.92。
SOC从 0.68 更新为 0.82。
SOC从 0.48 更新为 0.69。
SOC从 0.74 更新为 0.85。
SOC从 0.12 更新为 0.44。
SOC从 0.60 更新为 0.73。
SOC从 0.62 更新为 0.80。
SOC从 0.38 更新为 0.59。
SOC从 0.38 更新为 0.67。
SOC从 0.88 更新为 0.94。
已断开电池: batt_ev_066
时间步 61: 电池 batt_ev_066 已离开，当前SOC: 92.1%，能量满足率: 93.4%
已断开电池: batt_ev_060
时间步 61: 电池 batt_ev_060 已离开，当前SOC: 84.8%，能量满足率: 67.8%
已断开电池: batt_ev_217
时间步 61: 电池 batt_ev_217 已离开，当前SOC: 59.1%，能量满足率: 35.1%
奖励各项的值：powerloss=-0.2259215666187594, voltage=-0.2957878524946689, ctrl=-0.0, connection=15.200000000000001, completion=11.368421052631579, energy=8.269352942128892, transformer=0.
已连接电池 batt_ev_073, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 106kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_073 已接入
已连接电池 batt_ev_020, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 99kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_020 已接入
已连接电池 batt_ev_208, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 61kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_208 已接入
智能体的动作为: [ 1.        -0.9356249 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=112.27498769760132。
功率需求: 96.00 kW, 充电桩功率: 112.27 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=58.56失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=69.19999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=80.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=93.6失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=37.44，设置charger_power=17.439999999999998失败。
功率需求: 20.00 kW, 充电桩功率: 37.44 kW, 最终充电功率: 20.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.48 更新为 0.71。
SOC从 0.82 更新为 0.92。
SOC从 0.69 更新为 0.85。
SOC从 0.32 更新为 0.56。
SOC从 0.44 更新为 0.69。
SOC从 0.73 更新为 0.83。
SOC从 0.80 更新为 0.92。
SOC从 0.38 更新为 0.71。
SOC从 0.67 更新为 0.88。
SOC从 0.94 更新为 1.00。
已断开电池: batt_ev_219
时间步 62 执行前: 电池 batt_ev_219 已充满 (SOC: 82.6%)，离开
已断开电池: batt_ev_032
时间步 62: 电池 batt_ev_032 已离开，当前SOC: 91.9%，能量满足率: 87.8%
已断开电池: batt_ev_205
时间步 62 执行前: 电池 batt_ev_205 已充满 (SOC: 84.8%)，离开
已断开电池: batt_ev_189
时间步 62 执行前: 电池 batt_ev_189 已充满 (SOC: 100.0%)，离开
不太安全
奖励各项的值：powerloss=-0.22534453555580886, voltage=-0.2976685552372138, ctrl=-0.0, connection=15.52, completion=11.597938144329897, energy=8.2987502412854, transformer=-1.0205741008066072.
已连接电池 batt_ev_091, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_091 已接入
时间步 62: 电池 batt_ev_176 已错过离开时间，无法接入
已连接电池 batt_ev_102, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_102 已接入
已连接电池 batt_ev_236, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 92kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_236 已接入
已连接电池 batt_ev_074, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_074 已接入
智能体的动作为: [ 1.         -0.93928033 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=112.27498769760132，设置charger_power=112.71363973617554失败。
功率需求: 48.00 kW, 充电桩功率: 112.27 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=114.4。
功率需求: 48.00 kW, 充电桩功率: 114.40 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=98.08000000000001失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=32.0失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=71.28失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=33.599999999999994失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=112.32000000000001。
功率需求: 48.00 kW, 充电桩功率: 112.32 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_236 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_074 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.71 更新为 0.82。
SOC从 0.22 更新为 0.44。
SOC从 0.48 更新为 0.70。
SOC从 0.56 更新为 0.74。
SOC从 0.69 更新为 0.88。
SOC从 0.38 更新为 0.60。
SOC从 0.92 更新为 0.99。
SOC从 0.71 更新为 0.87。
SOC从 0.88 更新为 0.97。
SOC从 0.48 更新为 0.70。
已断开电池: batt_ev_249
时间步 63 执行前: 电池 batt_ev_249 已充满 (SOC: 99.5%)，离开
已断开电池: batt_ev_072
时间步 63: 电池 batt_ev_072 已离开，当前SOC: 87.9%，能量满足率: 88.3%
已断开电池: batt_ev_124
时间步 63 执行前: 电池 batt_ev_124 已充满 (SOC: 96.9%)，离开
已断开电池: batt_ev_236
时间步 63: 电池 batt_ev_236 已离开，当前SOC: 59.7%，能量满足率: 40.3%
奖励各项的值：powerloss=-0.21635235396314823, voltage=-0.3050898935315671, ctrl=-0.0, connection=15.84, completion=11.666666666666666, energy=8.297043603329227, transformer=0.
时间步 63: 电池 batt_ev_130 已错过离开时间，无法接入
已连接电池 batt_ev_061, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 78kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_061 已接入
已连接电池 batt_ev_012, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 98kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_012 已接入
时间步 63: 电池 batt_ev_108 已错过离开时间，无法接入
已连接电池 batt_ev_228, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_228 已接入
已连接电池 batt_ev_218, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
智能体的动作为: [ 1.        -0.8714166 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -0.9887901]
已有历史设置self.charger_power=112.27498769760132，设置charger_power=76.48000000000002失败。
功率需求: 48.00 kW, 充电桩功率: 112.27 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=114.4，设置charger_power=66.4失败。
功率需求: 36.00 kW, 充电桩功率: 114.40 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=101.27999999999997失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=31.28失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=112.32000000000001，设置charger_power=64.32失败。
功率需求: 24.00 kW, 充电桩功率: 112.32 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_074 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_012 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.82 更新为 0.93。
SOC从 0.44 更新为 0.62。
SOC从 0.70 更新为 0.86。
SOC从 0.74 更新为 0.87。
SOC从 0.28 更新为 0.60。
SOC从 0.48 更新为 0.72。
SOC从 0.22 更新为 0.50。
SOC从 0.87 更新为 0.97。
SOC从 0.38 更新为 0.61。
SOC从 0.70 更新为 0.81。
已断开电池: batt_ev_073
时间步 64: 电池 batt_ev_073 已离开，当前SOC: 93.3%，能量满足率: 90.6%
已断开电池: batt_ev_020
时间步 64: 电池 batt_ev_020 已离开，当前SOC: 86.5%，能量满足率: 90.9%
已断开电池: batt_ev_091
时间步 64: 电池 batt_ev_091 已离开，当前SOC: 62.3%，能量满足率: 53.0%
已断开电池: batt_ev_074
时间步 64 执行前: 电池 batt_ev_074 已充满 (SOC: 81.3%)，离开
已断开电池: batt_ev_012
时间步 64 执行前: 电池 batt_ev_012 已充满 (SOC: 72.5%)，离开
奖励各项的值：powerloss=-0.2189921232787637, voltage=-0.3227683804225223, ctrl=-0.0, connection=16.240000000000002, completion=11.67487684729064, energy=8.306722076434186, transformer=0.
已连接电池 batt_ev_243, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 64 执行前: 排队电池 batt_ev_243 已接入
已连接电池 batt_ev_122, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [ 1.        -0.9083538 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=109.00245666503906。
功率需求: 60.00 kW, 充电桩功率: 109.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=118.08。
功率需求: 60.00 kW, 充电桩功率: 118.08 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=114.4，设置charger_power=30.400000000000006失败。
功率需求: 15.00 kW, 充电桩功率: 114.40 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=105.36失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=6.280000000000001失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=109.6失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_122 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.12 更新为 0.40。
SOC从 0.28 更新为 0.65。
SOC从 0.86 更新为 0.93。
SOC从 0.60 更新为 0.79。
SOC从 0.50 更新为 0.67。
SOC从 0.97 更新为 1.00。
SOC从 0.61 更新为 0.78。
已断开电池: batt_ev_208
时间步 65 执行前: 电池 batt_ev_208 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_102
时间步 65: 电池 batt_ev_102 已离开，当前SOC: 93.0%，能量满足率: 90.0%
已断开电池: batt_ev_122
时间步 65: 电池 batt_ev_122 已离开，当前SOC: 64.6%，能量满足率: 52.3%
奖励各项的值：powerloss=-0.20494550593946034, voltage=-0.29149439898543017, ctrl=-0.0, connection=16.48, completion=11.650485436893204, energy=8.303354671613478, transformer=0.
已连接电池 batt_ev_139, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 84kWh，并创BMS。
智能体的动作为: [ 1.         -0.9584537  -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -0.74024165]
已有历史设置self.charger_power=109.00245666503906，设置charger_power=115.01444578170776失败。
功率需求: 48.00 kW, 充电桩功率: 109.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=64.63999999999999失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=69.36000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=61.599999999999994失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.40 更新为 0.62。
SOC从 0.12 更新为 0.36。
SOC从 0.79 更新为 0.92。
SOC从 0.67 更新为 0.84。
SOC从 0.78 更新为 0.89。
奖励各项的值：powerloss=-0.20999094179827604, voltage=-0.19871939168640385, ctrl=-0.0, connection=16.48, completion=11.650485436893204, energy=8.303354671613478, transformer=0.
已连接电池 batt_ev_004, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_019, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
智能体的动作为: [ 0.40865564 -0.9126442  -1.         -1.         -1.         -1.
 -0.8063195  -1.         -1.         -1.         -0.3518524 ]
已有历史设置self.charger_power=109.00245666503906，设置charger_power=82.08000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 109.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=24.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=96.75833702087402。
功率需求: 100.00 kW, 充电桩功率: 96.76 kW, 最终充电功率: 96.76 kW。
已有历史设置self.charger_power=120.0，设置charger_power=33.360000000000014失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=29.599999999999994失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=42.22228646278381。
功率需求: 36.00 kW, 充电桩功率: 42.22 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 96.75833702087402, -19.647618320632255
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.62 更新为 0.79。
SOC从 0.36 更新为 0.55。
SOC从 0.92 更新为 1.00。
SOC从 0.08 更新为 0.35。
SOC从 0.84 更新为 0.96。
SOC从 0.89 更新为 0.97。
SOC从 0.52 更新为 0.73。
已断开电池: batt_ev_061
时间步 67 执行前: 电池 batt_ev_061 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_228
时间步 67: 电池 batt_ev_228 已离开，当前SOC: 95.6%，能量满足率: 96.8%
已断开电池: batt_ev_218
时间步 67 执行前: 电池 batt_ev_218 已充满 (SOC: 96.6%)，离开
已断开电池: batt_ev_243
时间步 67: 电池 batt_ev_243 已离开，当前SOC: 78.7%，能量满足率: 83.3%
奖励各项的值：powerloss=-0.20955797487569006, voltage=-0.12118164056676095, ctrl=-0.0, connection=16.8, completion=11.714285714285714, energy=8.326222000546226, transformer=0.
智能体的动作为: [ 1.         -0.95643646 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -0.6916352 ]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=96.75833702087402，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 96.76 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=42.22228646278381，设置charger_power=46.56失败。
功率需求: 24.00 kW, 充电桩功率: 42.22 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.55 更新为 0.69。
SOC从 0.35 更新为 0.57。
SOC从 0.73 更新为 0.87。
奖励各项的值：powerloss=-0.19618320244078752, voltage=-0.09811497579428119, ctrl=-0.0, connection=16.8, completion=11.714285714285714, energy=8.326222000546226, transformer=0.
智能体的动作为: [-0.84483707 -1.         -1.         -1.         -0.4822474  -0.68813145
 -0.742569   -0.97676116 -1.         -1.         -0.        ]
已有历史设置self.charger_power=120.0，设置charger_power=57.86968946456909失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=96.75833702087402，设置charger_power=89.10828351974487失败。
功率需求: 60.00 kW, 充电桩功率: 96.76 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=42.22228646278381，设置charger_power=0.0失败。
功率需求: 15.00 kW, 充电桩功率: 42.22 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 84.48370695114136, 27.768451621429204
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.69 更新为 0.83。
SOC从 0.57 更新为 0.73。
SOC从 0.87 更新为 0.96。
已断开电池: batt_ev_139
时间步 69: 电池 batt_ev_139 已离开，当前SOC: 83.4%，能量满足率: 83.1%
奖励各项的值：powerloss=-0.20114864261004314, voltage=-0.016894497395618657, ctrl=-0.0, connection=16.88, completion=11.65876777251185, energy=8.326124492678858, transformer=0.
已连接电池 batt_ev_177, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [-1.         -1.         -1.         -1.         -0.32658824 -0.6981054
 -0.607916   -0.9322187  -1.         -1.         -0.        ]
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=96.75833702087402，设置charger_power=72.94991970062256失败。
功率需求: 40.00 kW, 充电桩功率: 96.76 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=42.22228646278381，设置charger_power=0.0失败。
功率需求: 15.00 kW, 充电桩功率: 42.22 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.38 更新为 0.65。
SOC从 0.73 更新为 0.84。
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_019
时间步 70 执行前: 电池 batt_ev_019 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.19091152649251222, voltage=-0.013155398003596996, ctrl=-0.0, connection=16.96, completion=11.745283018867925, energy=8.334020131864333, transformer=0.
已连接电池 batt_ev_202, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_160, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [-1.         -0.93024683 -1.         -1.         -0.20415714 -0.6923837
 -0.45819852 -0.9042389  -1.         -1.         -0.        ]
已有历史设置self.charger_power=120.0，设置charger_power=82.32失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=96.75833702087402，设置charger_power=54.98382210731506失败。
功率需求: 40.00 kW, 充电桩功率: 96.76 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.65 更新为 0.85。
SOC从 0.48 更新为 0.74。
SOC从 0.84 更新为 0.95。
SOC从 0.18 更新为 0.55。
已断开电池: batt_ev_004
时间步 71 执行前: 电池 batt_ev_004 已充满 (SOC: 95.0%)，离开
奖励各项的值：powerloss=-0.1804385078679836, voltage=-0.026976881100184702, ctrl=-0.0, connection=17.04, completion=11.830985915492956, energy=8.34184163359267, transformer=0.
智能体的动作为: [ 0.3850441  -0.91889334 -1.         -1.         -1.         -1.
 -0.80321825 -1.         -1.         -1.         -0.3420384 ]
已有历史设置self.charger_power=120.0，设置charger_power=34.31999999999999失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=78.08000000000001失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=74.48失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -38.50440979003906, -12.655787477279247
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.85 更新为 0.94。
SOC从 0.74 更新为 0.87。
SOC从 0.55 更新为 0.77。
已断开电池: batt_ev_202
时间步 72 执行前: 电池 batt_ev_202 已充满 (SOC: 87.5%)，离开
奖励各项的值：powerloss=-0.1464567893882826, voltage=-0.1512173208463441, ctrl=-0.0, connection=17.12, completion=11.91588785046729, energy=8.349590037174012, transformer=0.
已连接电池 batt_ev_099, 初始SOC: 68.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
已连接电池 batt_ev_100, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [-1.         -0.8141652  -1.         -1.         -0.14500919 -0.6179503
 -0.50906664 -0.85152566 -1.         -1.         -0.        ]
初次设置charger_power=85.75999999999999。
功率需求: 36.00 kW, 充电桩功率: 85.76 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=14.319999999999993失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=74.15403842926025。
功率需求: 80.00 kW, 充电桩功率: 74.15 kW, 最终充电功率: 74.15 kW。
已有历史设置self.charger_power=120.0，设置charger_power=38.480000000000004失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 74.15403842926025, -15.057619724048058
SOC从 0.68 更新为 0.81。
SOC从 0.94 更新为 1.00。
SOC从 0.18 更新为 0.50。
SOC从 0.77 更新为 0.91。
已断开电池: batt_ev_177
时间步 73 执行前: 电池 batt_ev_177 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_160
时间步 73: 电池 batt_ev_160 已离开，当前SOC: 91.2%，能量满足率: 91.5%
奖励各项的值：powerloss=-0.13356529402509004, voltage=-0.12796961745347835, ctrl=-0.0, connection=17.28, completion=11.944444444444445, energy=8.360919488049321, transformer=0.
智能体的动作为: [-0.8485794  -1.         -1.         -1.         -0.48638183 -0.6897108
 -0.74033004 -0.9869393  -1.         -1.         -0.        ]
已有历史设置self.charger_power=85.75999999999999，设置charger_power=49.75999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 85.76 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=74.15403842926025，设置charger_power=82.76529550552368失败。
功率需求: 64.00 kW, 充电桩功率: 74.15 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 84.85794067382812, 27.891456297698262
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.81 更新为 0.90。
SOC从 0.50 更新为 0.78。
已断开电池: batt_ev_100
时间步 74: 电池 batt_ev_100 已离开，当前SOC: 77.6%，能量满足率: 80.5%
奖励各项的值：powerloss=-0.12246902715381594, voltage=-0.16899088793650652, ctrl=-0.0, connection=17.36, completion=11.889400921658986, energy=8.359475298191533, transformer=0.
智能体的动作为: [-1.         -0.73495567 -1.         -1.         -0.11543808 -0.542725
 -0.5676558  -0.80629975 -1.         -1.         -0.        ]
已有历史设置self.charger_power=85.75999999999999，设置charger_power=25.75999999999999失败。
功率需求: 15.00 kW, 充电桩功率: 85.76 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.90 更新为 0.96。
奖励各项的值：powerloss=-0.11509764457683458, voltage=-0.18332639249615923, ctrl=-0.0, connection=17.36, completion=11.889400921658986, energy=8.359475298191533, transformer=0.
智能体的动作为: [-1.         -0.5391644  -0.5795078  -0.7461554  -0.03576994 -0.4127019
 -0.         -0.36120626 -0.04818706 -0.43579    -0.        ]
已有历史设置self.charger_power=85.75999999999999，设置charger_power=10.759999999999991失败。
功率需求: 15.00 kW, 充电桩功率: 85.76 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_099
时间步 76 执行前: 电池 batt_ev_099 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.11479283712665642, voltage=-0.20927037299517615, ctrl=-0.0, connection=17.44, completion=11.972477064220183, energy=8.36700064086038, transformer=0.
已连接电池 batt_ev_120, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [-1.         -0.54007226 -0.57795584 -0.7447179  -0.03569832 -0.41280022
 -0.         -0.36072704 -0.0460883  -0.43649223 -0.        ]
初次设置charger_power=43.28724503517151。
功率需求: 120.00 kW, 充电桩功率: 43.29 kW, 最终充电功率: 43.29 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 43.28724503517151, -8.78984999937787
SOC从 0.18 更新为 0.31。
奖励各项的值：powerloss=-0.11683152705545191, voltage=-0.18979328623563552, ctrl=-0.0, connection=17.44, completion=11.972477064220183, energy=8.36700064086038, transformer=0.
智能体的动作为: [-1.         -0.34389436 -0.6999298  -1.         -0.         -0.60033673
 -0.24685542 -0.52327836 -1.         -1.         -0.        ]
已有历史设置self.charger_power=43.28724503517151，设置charger_power=62.793402671813965失败。
功率需求: 96.00 kW, 充电桩功率: 43.29 kW, 最终充电功率: 43.29 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 69.20000000000005, 22.744940078377347
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 43.28724503517151, -8.78984999937787
SOC从 0.31 更新为 0.44。
奖励各项的值：powerloss=-0.12081386102410178, voltage=-0.19862014056780897, ctrl=-0.0, connection=17.44, completion=11.972477064220183, energy=8.36700064086038, transformer=0.
已连接电池 batt_ev_035, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 77kWh，并创BMS。
智能体的动作为: [-1.         -0.34346104 -0.69914985 -1.         -0.         -0.5987022
 -0.24859327 -0.52451926 -1.         -1.         -0.        ]
已有历史设置self.charger_power=43.28724503517151，设置charger_power=62.94231176376343失败。
功率需求: 96.00 kW, 充电桩功率: 43.29 kW, 最终充电功率: 43.29 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 43.28724503517151, -8.78984999937787
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.44 更新为 0.58。
SOC从 0.48 更新为 0.69。
已断开电池: batt_ev_120
时间步 79: 电池 batt_ev_120 已离开，当前SOC: 57.6%，能量满足率: 49.5%
奖励各项的值：powerloss=-0.13746432387619056, voltage=-0.35781622832255167, ctrl=-0.0, connection=17.52, completion=11.917808219178081, energy=8.351389545384796, transformer=0.
已连接电池 batt_ev_151, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
智能体的动作为: [-1.         -0.88096255 -1.         -1.         -0.17090556 -0.67725044
 -0.4504963  -0.8847182  -1.         -1.         -0.        ]
初次设置charger_power=20.50866723060608。
功率需求: 120.00 kW, 充电桩功率: 20.51 kW, 最终充电功率: 20.51 kW。
已有历史设置self.charger_power=120.0，设置charger_power=96.16失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 20.50866723060608, -4.164462499235361
SOC从 0.28 更新为 0.34。
SOC从 0.69 更新为 0.84。
奖励各项的值：powerloss=-0.1515010174115331, voltage=-0.38880532622017183, ctrl=-0.0, connection=17.52, completion=11.917808219178081, energy=8.351389545384796, transformer=0.
智能体的动作为: [-1.         -0.81352615 -1.         -1.         -0.01449379 -0.5647866
 -0.51401764 -0.72323954 -1.         -1.         -0.        ]
已有历史设置self.charger_power=20.50866723060608，设置charger_power=1.7392542958259583失败。
功率需求: 96.00 kW, 充电桩功率: 20.51 kW, 最终充电功率: 20.51 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.160000000000025失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 20.50866723060608, -4.164462499235361
SOC从 0.34 更新为 0.40。
SOC从 0.84 更新为 0.95。
已断开电池: batt_ev_035
时间步 81: 电池 batt_ev_035 已离开，当前SOC: 94.8%，能量满足率: 93.5%
已断开电池: batt_ev_151
时间步 81: 电池 batt_ev_151 已离开，当前SOC: 39.9%，能量满足率: 17.0%
奖励各项的值：powerloss=-0.16290439464488282, voltage=-0.339745592835754, ctrl=-0.0, connection=17.68, completion=11.80995475113122, energy=8.325833840392745, transformer=0.
智能体的动作为: [-1.         -0.5190603  -0.77179235 -0.99916196 -0.         -0.578996
 -0.30854633 -0.5821921  -1.         -1.         -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.1696497671576165, voltage=-0.2989397313062936, ctrl=-0.0, connection=17.68, completion=11.80995475113122, energy=8.325833840392745, transformer=0.
智能体的动作为: [-1.         -0.97525406 -0.7735806  -0.65186185 -0.67068315 -0.35525936
 -0.         -0.62124044 -0.         -0.394858   -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.17849155917047588, voltage=-0.3390324412654322, ctrl=-0.0, connection=17.68, completion=11.80995475113122, energy=8.325833840392745, transformer=0.
已连接电池 batt_ev_056, 初始SOC: 62.0%, 最大功率: 80kW, 电池容量: 64kWh，并创BMS。
已连接电池 batt_ev_226, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [-1.         -0.97471577 -0.7736231  -0.6520783  -0.67056084 -0.3550608
 -0.         -0.62148994 -0.         -0.39493093 -0.        ]
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 0.0, -0.0
SOC从 0.18 更新为 0.18。
SOC从 0.62 更新为 0.62。
奖励各项的值：powerloss=-0.18307968839032146, voltage=-0.33953521011096166, ctrl=-0.0, connection=17.68, completion=11.80995475113122, energy=8.325833840392745, transformer=0.
已连接电池 batt_ev_048, 初始SOC: 42.0%, 最大功率: 120kW, 电池容量: 93kWh，并创BMS。
智能体的动作为: [-1.         -0.97854793 -0.7730639  -0.64946705 -0.6786082  -0.35479963
 -0.         -0.6257542  -0.         -0.39345238 -0.        ]
初次设置charger_power=77.93604612350464。
功率需求: 96.00 kW, 充电桩功率: 77.94 kW, 最终充电功率: 77.94 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_048 充电的有无功功率为 77.93604612350464, -15.825589140948821
SOC从 0.42 更新为 0.63。
SOC从 0.18 更新为 0.18。
SOC从 0.62 更新为 0.62。
已断开电池: batt_ev_048
时间步 85: 电池 batt_ev_048 已离开，当前SOC: 62.9%，能量满足率: 37.4%
奖励各项的值：powerloss=-0.19235887234630328, voltage=-0.41403345517674994, ctrl=-0.0, connection=17.76, completion=11.756756756756756, energy=8.305178730235845, transformer=0.
已连接电池 batt_ev_234, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_227, 初始SOC: 8.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
智能体的动作为: [-1.         -0.7446739  -1.         -1.         -0.08579711 -0.5422632
 -0.5543048  -0.7891168  -1.         -1.         -0.        ]
初次设置charger_power=108.36000000000001。
功率需求: 36.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 36.00 kW。
self.charger_power=0.0 改为 66.51657342910767。
功率需求: 60.00 kW, 充电桩功率: 66.52 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.57 更新为 0.71。
SOC从 0.18 更新为 0.51。
SOC从 0.08 更新为 0.40。
SOC从 0.62 更新为 0.62。
已断开电池: batt_ev_056
时间步 86: 电池 batt_ev_056 已离开，当前SOC: 62.0%，能量满足率: 0.0%
已断开电池: batt_ev_226
时间步 86: 电池 batt_ev_226 已离开，当前SOC: 50.6%，能量满足率: 51.0%
奖励各项的值：powerloss=-0.19701384315609485, voltage=-0.3931558975751348, ctrl=-0.0, connection=17.92, completion=11.651785714285715, energy=8.253771369678615, transformer=0.
智能体的动作为: [-0.87181544 -1.         -1.         -1.         -0.47386327 -0.67534316
 -0.73979425 -0.96509767 -1.         -1.         -0.        ]
已有历史设置self.charger_power=108.36000000000001，设置charger_power=72.36000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=112.96失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.71 更新为 0.81。
SOC从 0.40 更新为 0.65。
奖励各项的值：powerloss=-0.19030394586225022, voltage=-0.34514924528035396, ctrl=-0.0, connection=17.92, completion=11.651785714285715, energy=8.253771369678615, transformer=0.
智能体的动作为: [-1.         -0.808776   -1.         -0.99477065 -0.03768358 -0.55620307
 -0.54531926 -0.7138828  -1.         -1.         -0.        ]
已有历史设置self.charger_power=108.36000000000001，设置charger_power=48.360000000000014失败。
功率需求: 24.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=64.96失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.81 更新为 0.90。
SOC从 0.65 更新为 0.85。
已断开电池: batt_ev_227
时间步 88: 电池 batt_ev_227 已离开，当前SOC: 84.6%，能量满足率: 85.1%
奖励各项的值：powerloss=-0.1865613875547735, voltage=-0.345872506772944, ctrl=-0.0, connection=18.0, completion=11.6, energy=8.254913000470587, transformer=0.
智能体的动作为: [-1.         -0.7889634  -0.9062908  -0.968601   -0.         -0.59223086
 -0.44897377 -0.53964984 -1.         -1.         -0.        ]
已有历史设置self.charger_power=108.36000000000001，设置charger_power=24.360000000000014失败。
功率需求: 15.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.90 更新为 0.96。
奖励各项的值：powerloss=-0.1858739045104507, voltage=-0.28168919527113534, ctrl=-0.0, connection=18.0, completion=11.6, energy=8.254913000470587, transformer=0.
智能体的动作为: [-1.         -0.53276485 -0.57048017 -0.7445089  -0.01725698 -0.40819395
 -0.         -0.34868613 -0.06728792 -0.43812686 -0.        ]
已有历史设置self.charger_power=108.36000000000001，设置charger_power=9.360000000000014失败。
功率需求: 15.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_234
时间步 90 执行前: 电池 batt_ev_234 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.19973830610215962, voltage=-0.2060125189003581, ctrl=-0.0, connection=18.080000000000002, completion=11.68141592920354, energy=8.26263462436231, transformer=0.
智能体的动作为: [-1.         -0.5340021  -0.5723909  -0.7448498  -0.02068715 -0.40907347
 -0.         -0.35099104 -0.06306081 -0.43779457 -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.19617676491812283, voltage=-0.07846179495861305, ctrl=-0.0, connection=18.080000000000002, completion=11.68141592920354, energy=8.26263462436231, transformer=0.
智能体的动作为: [-1.         -0.9771135  -0.7734262  -0.6512956  -0.6709214  -0.35613298
 -0.         -0.6205674  -0.         -0.39441803 -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.19009302252945393, voltage=-0.05499017312744492, ctrl=-0.0, connection=18.080000000000002, completion=11.68141592920354, energy=8.26263462436231, transformer=0.
已连接电池 batt_ev_238, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [-1.         -0.97635037 -0.7723579  -0.65102124 -0.67103297 -0.35659063
 -0.         -0.621218   -0.         -0.3938421  -0.        ]
初次设置charger_power=42.79087543487549。
功率需求: 48.00 kW, 充电桩功率: 42.79 kW, 最终充电功率: 42.79 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 42.79087543487549, -8.689057853162325
SOC从 0.48 更新为 0.74。
奖励各项的值：powerloss=-0.19311655583933576, voltage=-0.019485389639131157, ctrl=-0.0, connection=18.080000000000002, completion=11.68141592920354, energy=8.26263462436231, transformer=0.
智能体的动作为: [-1.         -0.34866995 -0.7049163  -1.         -0.         -0.6092282
 -0.2365015  -0.5169426  -1.         -1.         -0.        ]
已有历史设置self.charger_power=42.79087543487549，设置charger_power=42.480000000000004失败。
功率需求: 24.00 kW, 充电桩功率: 42.79 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.74 更新为 0.89。
已断开电池: batt_ev_238
时间步 94 执行前: 电池 batt_ev_238 已充满 (SOC: 88.7%)，离开
奖励各项的值：powerloss=-0.17963175426696537, voltage=-0.015706961896508886, ctrl=-0.0, connection=18.16, completion=11.762114537444933, energy=8.270288216325472, transformer=0.
智能体的动作为: [-1.         -0.5280023  -0.74551237 -0.8496235  -0.11290479 -0.4504822
 -0.         -0.4698912  -0.13122053 -0.43590385 -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.16154578303860406, voltage=-0.08384762073746499, ctrl=-0.0, connection=18.16, completion=11.762114537444933, energy=8.270288216325472, transformer=0.
已连接电池 batt_ev_025, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
已连接电池 batt_ev_013, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 89kWh，并创BMS。
已连接电池 batt_ev_117, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 111kWh，并创BMS。
已连接电池 batt_ev_166, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 114kWh，并创BMS。
智能体的动作为: [-1.        -0.9779625 -0.7696652 -0.6488447 -0.6740747 -0.3584079
 -0.        -0.6230385 -0.        -0.3917378 -0.       ]
初次设置charger_power=117.35549926757812。
功率需求: 60.00 kW, 充电桩功率: 117.36 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=80.8889651298523。
功率需求: 72.00 kW, 充电桩功率: 80.89 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=74.7646164894104。
功率需求: 120.00 kW, 充电桩功率: 74.76 kW, 最终充电功率: 74.76 kW。
初次设置charger_power=47.0085346698761。
功率需求: 120.00 kW, 充电桩功率: 47.01 kW, 最终充电功率: 47.01 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_025 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_013 充电的有无功功率为 74.7646164894104, -15.181602887154654
已在 set_all_batteries_before_solve 中设置 batt_ev_117 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_166 充电的有无功功率为 47.0085346698761, -9.545490088432187
SOC从 0.12 更新为 0.43。
SOC从 0.52 更新为 0.68。
SOC从 0.18 更新为 0.39。
SOC从 0.28 更新为 0.38。
已断开电池: batt_ev_025
时间步 96: 电池 batt_ev_025 已离开，当前SOC: 42.6%，能量满足率: 35.6%
已断开电池: batt_ev_013
时间步 96: 电池 batt_ev_013 已离开，当前SOC: 39.0%，能量满足率: 26.2%
已断开电池: batt_ev_117
时间步 96: 电池 batt_ev_117 已离开，当前SOC: 68.2%，能量满足率: 35.3%
已断开电池: batt_ev_166
时间步 96: 电池 batt_ev_166 已离开，当前SOC: 38.3%，能量满足率: 14.7%
奖励各项的值：powerloss=-0.156612677028647, voltage=-0.15836978198789486, ctrl=-4.0, connection=18.48, completion=11.558441558441558, energy=8.175487809258154, transformer=0.
调度记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250510_194947_13Bus_cbat_1000000\test_results_20250511_001130\schedule.csv
储能放电功率记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250510_194947_13Bus_cbat_1000000\test_results_20250511_001130\storage_schedule.csv
储能能量记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250510_194947_13Bus_cbat_1000000\test_results_20250511_001130\storage_energy.csv
已生成GIF动画，包含96步
测试完成 - 总奖励: 2912.5209
测试结果保存在: D:\LENOVO\Documents\Python\ML\powergym\results_20250510_194947_13Bus_cbat_1000000\test_results_20250511_001130
运行时间: 15749.43秒

进程已结束，退出代码为 0

```