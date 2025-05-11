

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
已从D:\LENOVO\Documents\Python\ML\powergym\results_20250511_121502_13Bus_cbat_s2_1000000\model\ppo_model加载模型
BatteryStationManager已重置
智能体的动作为: [ 1.       -1.       -1.       -1.       -1.       -1.       -0.800688
 -1.       -0.       -0.       -1.      ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
奖励各项的值：powerloss=-0.26476130168372947, voltage=0.0, ctrl=-0.0, connection=0.0, completion=0.0, energy=0.0, transformer=0.
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
智能体的动作为: [ 1.        -1.        -1.        -1.        -1.        -1.
 -0.8297179 -1.        -0.        -0.        -1.       ]
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=99.5661449432373。
功率需求: 100.00 kW, 充电桩功率: 99.57 kW, 最终充电功率: 99.57 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=0.0。
功率需求: 96.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -60.0, -19.721046310731793
已在 set_all_batteries_before_solve 中设置 batt_ev_030 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 99.5661449432373, -20.217768036664886
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.18 更新为 0.51。
SOC从 0.32 更新为 0.55。
SOC从 0.18 更新为 0.40。
SOC从 0.12 更新为 0.36。
SOC从 0.22 更新为 0.51。
SOC从 0.28 更新为 0.55。
SOC从 0.12 更新为 0.50。
SOC从 0.38 更新为 0.38。
SOC从 0.22 更新为 0.22。
SOC从 0.12 更新为 0.54。
已断开电池: batt_ev_030
时间步 2 执行前: 电池 batt_ev_030 已充满 (SOC: 51.3%)，离开
不太安全
奖励各项的值：powerloss=-0.28568786650045835, voltage=0.0, ctrl=-0.0, connection=0.08, completion=10.0, energy=10.0, transformer=-1.1509584371881887.
已连接电池 batt_ev_224, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
时间步 2 执行前: 排队电池 batt_ev_224 已接入
智能体的动作为: [ 1.        -0.8276582 -1.        -0.7813467 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=99.3189811706543。
功率需求: 60.00 kW, 充电桩功率: 99.32 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=93.76160144805908失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=99.12失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=99.5661449432373，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 99.57 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=103.04失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
self.charger_power=0.0 改为 120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
self.charger_power=0.0 改为 120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.28 更新为 0.61。
SOC从 0.55 更新为 0.73。
SOC从 0.40 更新为 0.58。
SOC从 0.36 更新为 0.56。
SOC从 0.51 更新为 0.69。
SOC从 0.55 更新为 0.71。
SOC从 0.50 更新为 0.74。
SOC从 0.38 更新为 0.64。
SOC从 0.22 更新为 0.55。
SOC从 0.54 更新为 0.79。
已断开电池: batt_ev_064
时间步 3 执行前: 电池 batt_ev_064 已充满 (SOC: 55.5%)，离开
已断开电池: batt_ev_039
时间步 3: 电池 batt_ev_039 已离开，当前SOC: 73.5%，能量满足率: 71.6%
已断开电池: batt_ev_045
时间步 3: 电池 batt_ev_045 已离开，当前SOC: 78.7%，能量满足率: 77.5%
奖励各项的值：powerloss=-0.2753275329661974, voltage=-0.00962142045657588, ctrl=-0.0, connection=0.32, completion=5.0, energy=8.726893261776983, transformer=0.
时间步 3: 电池 batt_ev_092 已错过离开时间，无法接入
已连接电池 batt_ev_081, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 50kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_081 已接入
已连接电池 batt_ev_076, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_076 已接入
已连接电池 batt_ev_235, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_235 已接入
智能体的动作为: [ 1.        -0.8242353 -1.        -0.7602307 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=99.3189811706543，设置charger_power=69.6失败。
功率需求: 36.00 kW, 充电桩功率: 99.32 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=75.68失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=91.22768640518188失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=63.120000000000005失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=99.5661449432373，设置charger_power=105.39999999999998失败。
功率需求: 40.00 kW, 充电桩功率: 99.57 kW, 最终充电功率: 40.00 kW。
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
SOC从 0.64 更新为 0.83。
SOC从 0.55 更新为 0.75。
SOC从 0.62 更新为 0.81。
已断开电池: batt_ev_126
时间步 4: 电池 batt_ev_126 已离开，当前SOC: 70.9%，能量满足率: 66.2%
已断开电池: batt_ev_239
时间步 4 执行前: 电池 batt_ev_239 已充满 (SOC: 82.2%)，离开
已断开电池: batt_ev_242
时间步 4 执行前: 电池 batt_ev_242 已充满 (SOC: 83.2%)，离开
奖励各项的值：powerloss=-0.26459098519730706, voltage=-0.05419262241258549, ctrl=-0.0, connection=0.56, completion=5.7142857142857135, energy=8.789317157990208, transformer=0.
时间步 4: 电池 batt_ev_104 已错过离开时间，无法接入
已连接电池 batt_ev_018, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_018 已接入
已连接电池 batt_ev_062, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_062 已接入
时间步 4: 电池 batt_ev_200 已错过离开时间，无法接入
时间步 4: 电池 batt_ev_163 已错过离开时间，无法接入
已连接电池 batt_ev_014, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_014 已接入
智能体的动作为: [ 1.         -0.8205894  -1.         -0.72605747 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=99.3189811706543，设置charger_power=33.599999999999994失败。
功率需求: 24.00 kW, 充电桩功率: 99.32 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=43.68000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=87.12689638137817。
功率需求: 48.00 kW, 充电桩功率: 87.13 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=96.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=27.120000000000005失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
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
奖励各项的值：powerloss=-0.26700740221940084, voltage=-0.0830892490545776, ctrl=-0.0, connection=0.96, completion=4.166666666666667, energy=8.432872937591537, transformer=0.
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
智能体的动作为: [ 1.         -0.81963885 -1.         -0.68951666 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=99.3189811706543，设置charger_power=9.599999999999994失败。
功率需求: 15.00 kW, 充电桩功率: 99.32 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=11.680000000000007失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=87.12689638137817，设置charger_power=82.74199962615967失败。
功率需求: 36.00 kW, 充电桩功率: 87.13 kW, 最终充电功率: 36.00 kW。
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
奖励各项的值：powerloss=-0.2927427954976565, voltage=-0.13689092891129073, ctrl=-0.0, connection=1.36, completion=4.117647058823529, energy=7.927371022365226, transformer=0.
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
智能体的动作为: [ 1.         -0.81980014 -1.         -0.67979103 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=98.37601661682129。
功率需求: 96.00 kW, 充电桩功率: 98.38 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=87.12689638137817，设置charger_power=81.57492399215698失败。
功率需求: 36.00 kW, 充电桩功率: 87.13 kW, 最终充电功率: 36.00 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_157 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_187 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.48 更新为 0.82。
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
奖励各项的值：powerloss=-0.3391646562404222, voltage=-0.22171770766147514, ctrl=-0.0, connection=1.76, completion=3.6363636363636367, energy=7.6613340264092855, transformer=0.
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
智能体的动作为: [ 1.        -0.8198302 -1.        -0.6785191 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=98.37601661682129，设置charger_power=49.599999999999994失败。
功率需求: 48.00 kW, 充电桩功率: 98.38 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=75.36失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=81.42229557037354。
功率需求: 96.00 kW, 充电桩功率: 81.42 kW, 最终充电功率: 81.42 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_106 充电的有无功功率为 81.42229557037354, -16.533502284266056
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_216 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 96.0, -19.493631420864393
SOC从 0.82 更新为 0.99。
SOC从 0.60 更新为 0.79。
SOC从 0.32 更新为 0.54。
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
时间步 8 执行前: 电池 batt_ev_240 已充满 (SOC: 99.4%)，离开
已断开电池: batt_ev_158
时间步 8 执行前: 电池 batt_ev_158 已充满 (SOC: 79.1%)，离开
已断开电池: batt_ev_106
时间步 8: 电池 batt_ev_106 已离开，当前SOC: 54.1%，能量满足率: 33.5%
已断开电池: batt_ev_216
时间步 8: 电池 batt_ev_216 已离开，当前SOC: 64.6%，能量满足率: 40.4%
不太安全
奖励各项的值：powerloss=-0.38673930789718025, voltage=-0.9202573857474161, ctrl=-0.0, connection=2.24, completion=3.5714285714285716, energy=7.54873093841011, transformer=-3.133581893589275.
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
智能体的动作为: [ 1.         -0.8198368  -1.         -0.67825323 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=98.38041543960571。
功率需求: 64.00 kW, 充电桩功率: 98.38 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=95.20000000000002。
功率需求: 48.00 kW, 充电桩功率: 95.20 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=81.39038801193237。
功率需求: 100.00 kW, 充电桩功率: 81.39 kW, 最终充电功率: 81.39 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_128 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 81.39038801193237, -16.52702317818489
已在 set_all_batteries_before_solve 中设置 batt_ev_173 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_132 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.42 更新为 0.62。
SOC从 0.72 更新为 0.86。
SOC从 0.22 更新为 0.43。
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
时间步 9: 电池 batt_ev_128 已离开，当前SOC: 62.0%，能量满足率: 35.7%
已断开电池: batt_ev_173
时间步 9: 电池 batt_ev_173 已离开，当前SOC: 80.1%，能量满足率: 56.3%
已断开电池: batt_ev_132
时间步 9: 电池 batt_ev_132 已离开，当前SOC: 46.3%，能量满足率: 35.4%
不太安全
奖励各项的值：powerloss=-0.42845014538888004, voltage=-2.0552211773702735, ctrl=-0.0, connection=2.72, completion=2.9411764705882355, energy=7.182756995227379, transformer=-2.1116316872093592.
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
智能体的动作为: [ 1.        -0.8198375 -1.        -0.6782222 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=98.38050127029419。
功率需求: 100.00 kW, 充电桩功率: 98.38 kW, 最终充电功率: 98.38 kW。
已有历史设置self.charger_power=95.20000000000002，设置charger_power=47.19999999999999失败。
功率需求: 30.00 kW, 充电桩功率: 95.20 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=81.39038801193237，设置charger_power=81.38666152954102失败。
功率需求: 80.00 kW, 充电桩功率: 81.39 kW, 最终充电功率: 80.00 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_191 充电的有无功功率为 98.38050127029419, -19.977012820447882
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_161 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.18 更新为 0.46。
SOC从 0.86 更新为 0.95。
SOC从 0.43 更新为 0.64。
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
时间步 10: 电池 batt_ev_191 已离开，当前SOC: 46.3%，能量满足率: 35.3%
已断开电池: batt_ev_161
时间步 10: 电池 batt_ev_161 已离开，当前SOC: 49.8%，能量满足率: 36.5%
不太安全
奖励各项的值：powerloss=-0.45972824624004155, voltage=-2.870072195063641, ctrl=-0.0, connection=3.12, completion=3.076923076923077, energy=7.1233848970572495, transformer=-5.273265737184165.
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
智能体的动作为: [ 1.         -0.81983757 -1.         -0.6782198  -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=98.38050842285156。
功率需求: 80.00 kW, 充电桩功率: 98.38 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=76.79999999999998。
功率需求: 48.00 kW, 充电桩功率: 76.80 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=81.39038801193237，设置charger_power=81.3863754272461失败。
功率需求: 60.00 kW, 充电桩功率: 81.39 kW, 最终充电功率: 60.00 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_008 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_085 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.18 更新为 0.43。
SOC从 0.68 更新为 0.88。
SOC从 0.64 更新为 0.80。
SOC从 0.52 更新为 0.70。
SOC从 0.28 更新为 0.51。
SOC从 0.99 更新为 1.00。
SOC从 0.57 更新为 0.75。
SOC从 0.42 更新为 0.66。
SOC从 0.62 更新为 0.84。
SOC从 0.62 更新为 0.79。
已断开电池: batt_ev_016
时间步 11: 电池 batt_ev_016 已离开，当前SOC: 80.3%，能量满足率: 76.7%
已断开电池: batt_ev_193
时间步 11: 电池 batt_ev_193 已离开，当前SOC: 69.8%，能量满足率: 62.8%
已断开电池: batt_ev_186
时间步 11 执行前: 电池 batt_ev_186 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_008
时间步 11 执行前: 电池 batt_ev_008 已充满 (SOC: 88.0%)，离开
已断开电池: batt_ev_085
时间步 11 执行前: 电池 batt_ev_085 已充满 (SOC: 84.0%)，离开
奖励各项的值：powerloss=-0.4765998215433518, voltage=-3.52179190921598, ctrl=-0.0, connection=3.52, completion=3.4090909090909087, energy=7.31278599106566, transformer=0.
时间步 11: 电池 batt_ev_222 已错过离开时间，无法接入
已连接电池 batt_ev_114, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_114 已接入
已连接电池 batt_ev_009, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_009 已接入
已连接电池 batt_ev_113, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_065, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_203, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [ 1.         -0.81983775 -1.         -0.6782195  -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=98.38050842285156，设置charger_power=98.38052988052368失败。
功率需求: 64.00 kW, 充电桩功率: 98.38 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=16.319999999999993。
功率需求: 15.00 kW, 充电桩功率: 16.32 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=81.38633966445923。
功率需求: 120.00 kW, 充电桩功率: 81.39 kW, 最终充电功率: 81.39 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 81.38633966445923, -16.526201126169212
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.43 更新为 0.63。
SOC从 0.92 更新为 0.99。
SOC从 0.18 更新为 0.38。
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
奖励各项的值：powerloss=-0.4828866388900224, voltage=-3.6292991422957552, ctrl=-0.0, connection=3.68, completion=3.2608695652173916, energy=7.340086717895179, transformer=0.
已连接电池 batt_ev_011, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 12 执行前: 排队电池 batt_ev_011 已接入
已连接电池 batt_ev_041, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [ 1.         -0.8198379  -1.         -0.67821956 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=98.38050842285156，设置charger_power=98.3805513381958失败。
功率需求: 48.00 kW, 充电桩功率: 98.38 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=16.319999999999993，设置charger_power=1.3199999999999932失败。
功率需求: 15.00 kW, 充电桩功率: 16.32 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=81.38633966445923，设置charger_power=81.3863468170166失败。
功率需求: 96.00 kW, 充电桩功率: 81.39 kW, 最终充电功率: 81.39 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 81.38633966445923, -16.526201126169212
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_011 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.63 更新为 0.78。
SOC从 0.99 更新为 1.00。
SOC从 0.38 更新为 0.58。
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
时间步 13: 电池 batt_ev_000 已离开，当前SOC: 78.0%，能量满足率: 75.0%
已断开电池: batt_ev_162
时间步 13: 电池 batt_ev_162 已离开，当前SOC: 78.8%，能量满足率: 72.5%
已断开电池: batt_ev_114
时间步 13 执行前: 电池 batt_ev_114 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_011
时间步 13: 电池 batt_ev_011 已离开，当前SOC: 54.9%，能量满足率: 34.6%
奖励各项的值：powerloss=-0.4895715300548454, voltage=-3.9204283658018713, ctrl=-0.0, connection=4.08, completion=3.333333333333333, energy=7.36980273998292, transformer=0.
已连接电池 batt_ev_232, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_232 已接入
已连接电池 batt_ev_237, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_237 已接入
已连接电池 batt_ev_052, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_052 已接入
已连接电池 batt_ev_206, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 62kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_206 已接入
已连接电池 batt_ev_172, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
智能体的动作为: [ 1.         -0.8200213  -1.         -0.67836964 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=98.4025526046753。
功率需求: 48.00 kW, 充电桩功率: 98.40 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=60.72。
功率需求: 24.00 kW, 充电桩功率: 60.72 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=81.38633966445923，设置charger_power=81.40435695648193失败。
功率需求: 72.00 kW, 充电桩功率: 81.39 kW, 最终充电功率: 72.00 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 72.0, -14.620223565648296
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
SOC从 0.58 更新为 0.75。
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
奖励各项的值：powerloss=-0.482909826605463, voltage=-3.849699420988857, ctrl=-0.0, connection=4.4, completion=3.2727272727272725, energy=7.441409441314544, transformer=0.
已连接电池 batt_ev_229, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_229 已接入
已连接电池 batt_ev_164, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_164 已接入
已连接电池 batt_ev_134, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_214, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 80kWh，并创BMS。
智能体的动作为: [ 1.         -0.8378216  -1.         -0.69292617 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=98.4025526046753，设置charger_power=100.53859233856201失败。
功率需求: 36.00 kW, 充电桩功率: 98.40 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=60.72，设置charger_power=36.72失败。
功率需求: 15.00 kW, 充电桩功率: 60.72 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=81.38633966445923，设置charger_power=83.1511402130127失败。
功率需求: 48.00 kW, 充电桩功率: 81.39 kW, 最终充电功率: 48.00 kW。
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
SOC从 0.75 更新为 0.87。
SOC从 0.38 更新为 0.58。
SOC从 0.58 更新为 0.73。
SOC从 0.42 更新为 0.63。
SOC从 0.32 更新为 0.62。
SOC从 0.79 更新为 0.93。
SOC从 0.48 更新为 0.73。
SOC从 0.68 更新为 0.91。
已断开电池: batt_ev_009
时间步 15: 电池 batt_ev_009 已离开，当前SOC: 86.6%，能量满足率: 85.8%
已断开电池: batt_ev_232
时间步 15: 电池 batt_ev_232 已离开，当前SOC: 70.3%，能量满足率: 53.8%
已断开电池: batt_ev_052
时间步 15 执行前: 电池 batt_ev_052 已充满 (SOC: 73.0%)，离开
奖励各项的值：powerloss=-0.48129332059709373, voltage=-3.7823742759652745, ctrl=-0.0, connection=4.64, completion=3.275862068965517, energy=7.4696936507636895, transformer=0.
已连接电池 batt_ev_143, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_143 已接入
已连接电池 batt_ev_245, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_245 已接入
已连接电池 batt_ev_098, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_098 已接入
智能体的动作为: [ 1.        -0.8562044 -1.        -0.7079137 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=102.74452686309814。
功率需求: 64.00 kW, 充电桩功率: 102.74 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=60.72，设置charger_power=21.72失败。
功率需求: 15.00 kW, 充电桩功率: 60.72 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=84.94964361190796。
功率需求: 48.00 kW, 充电桩功率: 84.95 kW, 最终充电功率: 48.00 kW。
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
奖励各项的值：powerloss=-0.4771876334660519, voltage=-3.674948131069452, ctrl=-0.0, connection=4.88, completion=3.442622950819672, energy=7.590571154753216, transformer=0.
已连接电池 batt_ev_190, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 63kWh，并创BMS。
时间步 16 执行前: 排队电池 batt_ev_190 已接入
已连接电池 batt_ev_069, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 56kWh，并创BMS。
已连接电池 batt_ev_071, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
智能体的动作为: [ 1.         -0.9870525  -1.         -0.81057763 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=102.74452686309814，设置charger_power=58.72失败。
功率需求: 32.00 kW, 充电桩功率: 102.74 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=84.94964361190796，设置charger_power=97.26931571960449失败。
功率需求: 36.00 kW, 充电桩功率: 84.95 kW, 最终充电功率: 36.00 kW。
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
奖励各项的值：powerloss=-0.48580821756505765, voltage=-3.7429486899507314, ctrl=-0.0, connection=5.12, completion=3.4375, energy=7.615474542859007, transformer=0.
智能体的动作为: [ 1.        -0.9064776 -1.        -0.7485197 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=102.74452686309814，设置charger_power=26.72失败。
功率需求: 20.00 kW, 充电桩功率: 102.74 kW, 最终充电功率: 20.00 kW。
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
奖励各项的值：powerloss=-0.49144555638264276, voltage=-3.4434257896618794, ctrl=-0.0, connection=5.44, completion=3.5294117647058827, energy=7.741243421866772, transformer=0.
已连接电池 batt_ev_083, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_174, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_167, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [ 1.        -1.        -1.        -0.8208246 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
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
奖励各项的值：powerloss=-0.4796187499454384, voltage=-2.9214105883000885, ctrl=-0.0, connection=5.68, completion=3.8028169014084505, energy=7.836683840661134, transformer=0.
已连接电池 batt_ev_115, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
已连接电池 batt_ev_181, 初始SOC: 56.99999999999999%, 最大功率: 80kW, 电池容量: 69kWh，并创BMS。
已连接电池 batt_ev_182, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 95kWh，并创BMS。
智能体的动作为: [ 1.        -1.        -1.        -0.8197467 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
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
奖励各项的值：powerloss=-0.46495328347261505, voltage=-2.4194876975417134, ctrl=-0.0, connection=5.68, completion=3.8028169014084505, energy=7.836683840661134, transformer=0.
已连接电池 batt_ev_037, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_138, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
已连接电池 batt_ev_095, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
智能体的动作为: [ 1.         -0.9933034  -1.         -0.81503075 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=120.0，设置charger_power=101.92失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=89.44。
功率需求: 48.00 kW, 充电桩功率: 89.44 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=97.8036904335022。
功率需求: 60.00 kW, 充电桩功率: 97.80 kW, 最终充电功率: 60.00 kW。
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
奖励各项的值：powerloss=-0.4645316197197943, voltage=-2.8031258807401382, ctrl=-0.0, connection=5.84, completion=3.9726027397260273, energy=7.895952776533432, transformer=0.
已连接电池 batt_ev_197, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 75kWh，并创BMS。
已连接电池 batt_ev_026, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 102kWh，并创BMS。
已连接电池 batt_ev_212, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [ 1.        -0.993225  -1.        -0.8149754 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=120.0，设置charger_power=53.91999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=97.8036904335022，设置charger_power=97.79704570770264失败。
功率需求: 48.00 kW, 充电桩功率: 97.80 kW, 最终充电功率: 48.00 kW。
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
奖励各项的值：powerloss=-0.44195693930579283, voltage=-2.342314258455558, ctrl=-0.0, connection=6.24, completion=3.974358974358974, energy=8.013839942243976, transformer=0.
已连接电池 batt_ev_010, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 71kWh，并创BMS。
时间步 22 执行前: 排队电池 batt_ev_010 已接入
已连接电池 batt_ev_241, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 68kWh，并创BMS。
已连接电池 batt_ev_084, 初始SOC: 78.0%, 最大功率: 100kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_038, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
已连接电池 batt_ev_040, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
智能体的动作为: [ 1.        -0.9927752 -1.        -0.8146579 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=119.13302421569824。
功率需求: 96.00 kW, 充电桩功率: 119.13 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=97.8036904335022，设置charger_power=60.96000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 97.80 kW, 最终充电功率: 36.00 kW。
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
奖励各项的值：powerloss=-0.4020993910214899, voltage=-1.7203954171284563, ctrl=-0.0, connection=6.32, completion=3.924050632911392, energy=7.9956767451069775, transformer=0.
已连接电池 batt_ev_046, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_046 已接入
智能体的动作为: [ 1.         -0.988506   -1.         -0.81162065 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=119.13302421569824，设置charger_power=51.68000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 119.13 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=109.44失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=97.8036904335022，设置charger_power=24.960000000000008失败。
功率需求: 15.00 kW, 充电桩功率: 97.80 kW, 最终充电功率: 15.00 kW。
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
奖励各项的值：powerloss=-0.351891162826278, voltage=-1.0421305915122903, ctrl=-0.0, connection=6.72, completion=3.9285714285714284, energy=8.084662195173498, transformer=0.
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
智能体的动作为: [ 1.         -0.99335635 -1.         -0.81507385 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=119.20276165008545。
功率需求: 60.00 kW, 充电桩功率: 119.20 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=61.44失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=97.8036904335022，设置charger_power=9.960000000000008失败。
功率需求: 15.00 kW, 充电桩功率: 97.80 kW, 最终充电功率: 15.00 kW。
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
奖励各项的值：powerloss=-0.2878814661648084, voltage=-0.006198054956039201, ctrl=-0.0, connection=7.28, completion=3.8461538461538463, energy=8.069221307917644, transformer=0.
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
智能体的动作为: [ 1.        -0.9933213 -1.        -0.8150433 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=119.1985559463501。
功率需求: 80.00 kW, 充电桩功率: 119.20 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
初次设置charger_power=97.80519247055054。
功率需求: 80.00 kW, 充电桩功率: 97.81 kW, 最终充电功率: 80.00 kW。
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
奖励各项的值：powerloss=-0.2811290338003322, voltage=-0.012975056702380083, ctrl=-0.0, connection=7.44, completion=3.978494623655914, energy=8.110743430328016, transformer=-2.297816510453083.
已连接电池 batt_ev_031, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_057, 初始SOC: 8.0%, 最大功率: 80kW, 电池容量: 73kWh，并创BMS。
已连接电池 batt_ev_111, 初始SOC: 68.0%, 最大功率: 100kW, 电池容量: 83kWh，并创BMS。
智能体的动作为: [ 1.         -0.97559595 -1.         -0.8022123  -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=119.1985559463501，设置charger_power=117.07151412963867失败。
功率需求: 48.00 kW, 充电桩功率: 119.20 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=96.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=97.80519247055054，设置charger_power=96.26547574996948失败。
功率需求: 48.00 kW, 充电桩功率: 97.81 kW, 最终充电功率: 48.00 kW。
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
奖励各项的值：powerloss=-0.26498533223230325, voltage=-0.047598831033976996, ctrl=-0.0, connection=7.68, completion=4.0625, energy=8.160854126701695, transformer=0.
已连接电池 batt_ev_006, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_006 已接入
已连接电池 batt_ev_225, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 94kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_225 已接入
已连接电池 batt_ev_054, 初始SOC: 82.0%, 最大功率: 120kW, 电池容量: 85kWh，并创BMS。
智能体的动作为: [ 1.         -0.99330616 -1.         -0.8150326  -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=119.1985559463501，设置charger_power=84.16失败。
功率需求: 48.00 kW, 充电桩功率: 119.20 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=103.20000000000002。
功率需求: 36.00 kW, 充电桩功率: 103.20 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=97.80519247055054，设置charger_power=84.16失败。
功率需求: 48.00 kW, 充电桩功率: 97.81 kW, 最终充电功率: 48.00 kW。
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
奖励各项的值：powerloss=-0.2555079999362944, voltage=-0.019399909839030727, ctrl=-0.0, connection=7.92, completion=3.9393939393939394, energy=8.163597342930425, transformer=0.
已连接电池 batt_ev_129, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 94kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_129 已接入
已连接电池 batt_ev_088, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 50kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_088 已接入
已连接电池 batt_ev_007, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 84kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_007 已接入
智能体的动作为: [ 1.        -0.9933227 -1.        -0.8150445 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=119.1985559463501，设置charger_power=36.16失败。
功率需求: 20.00 kW, 充电桩功率: 119.20 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=97.80519247055054，设置charger_power=36.16失败。
功率需求: 20.00 kW, 充电桩功率: 97.81 kW, 最终充电功率: 20.00 kW。
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
奖励各项的值：powerloss=-0.26401303373641977, voltage=-0.022328572088043952, ctrl=-0.0, connection=8.48, completion=3.9622641509433967, energy=8.235684938920246, transformer=0.
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
智能体的动作为: [ 1.         -0.9933228  -1.         -0.81504434 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=119.19873476028442。
功率需求: 96.00 kW, 充电桩功率: 119.20 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=97.80532121658325。
功率需求: 36.00 kW, 充电桩功率: 97.81 kW, 最终充电功率: 36.00 kW。
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
奖励各项的值：powerloss=-0.3068212009601081, voltage=-0.061878697030568475, ctrl=-0.0, connection=8.64, completion=3.888888888888889, energy=8.206680518174066, transformer=-3.6725550439600796.
时间步 30: 电池 batt_ev_021 已错过离开时间，无法接入
已连接电池 batt_ev_209, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_209 已接入
已连接电池 batt_ev_178, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 93kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_178 已接入
智能体的动作为: [ 1.         -0.9931729  -1.         -0.81493855 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=119.19873476028442，设置charger_power=119.18074607849121失败。
功率需求: 72.00 kW, 充电桩功率: 119.20 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=110.72000000000003失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=97.7926254272461。
功率需求: 48.00 kW, 充电桩功率: 97.79 kW, 最终充电功率: 48.00 kW。
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
奖励各项的值：powerloss=-0.34759894981331024, voltage=-0.03780798385458861, ctrl=-0.0, connection=8.8, completion=3.909090909090909, energy=8.21201359966181, transformer=0.
已连接电池 batt_ev_110, 初始SOC: 22.0%, 最大功率: 100kW, 电池容量: 65kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_110 已接入
已连接电池 batt_ev_112, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 71kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_112 已接入
智能体的动作为: [ 1.        -0.9933225 -1.        -0.8150441 -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=119.19869899749756。
功率需求: 100.00 kW, 充电桩功率: 119.20 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=70.72000000000003失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=97.7926254272461，设置charger_power=95.84失败。
功率需求: 36.00 kW, 充电桩功率: 97.79 kW, 最终充电功率: 36.00 kW。
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
奖励各项的值：powerloss=-0.3967505578631445, voltage=-0.9755029004800886, ctrl=-0.0, connection=9.36, completion=3.9316239316239314, energy=8.229834232213719, transformer=0.
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
智能体的动作为: [ 1.         -0.99332255 -1.         -0.81504416 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=119.19870615005493。
功率需求: 100.00 kW, 充电桩功率: 119.20 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=97.7926254272461，设置charger_power=59.84失败。
功率需求: 24.00 kW, 充电桩功率: 97.79 kW, 最终充电功率: 24.00 kW。
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
奖励各项的值：powerloss=-0.4395160593468805, voltage=-2.0682915284284764, ctrl=-0.0, connection=9.76, completion=3.7704918032786883, energy=8.165224553505148, transformer=0.
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
智能体的动作为: [ 1.         -0.99332255 -1.         -0.81504416 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=119.19870615005493。
功率需求: 48.00 kW, 充电桩功率: 119.20 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=78.24失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=97.80529975891113。
功率需求: 60.00 kW, 充电桩功率: 97.81 kW, 最终充电功率: 60.00 kW。
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
奖励各项的值：powerloss=-0.4718031630863285, voltage=-3.016785346150541, ctrl=-0.0, connection=10.24, completion=3.671875, energy=8.125248949248434, transformer=0.
已连接电池 batt_ev_049, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
已连接电池 batt_ev_023, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [ 1.         -0.99345523 -1.         -0.8151267  -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=119.19870615005493，设置charger_power=97.91999999999999失败。
功率需求: 48.00 kW, 充电桩功率: 119.20 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=97.80529975891113，设置charger_power=97.8152060508728失败。
功率需求: 36.00 kW, 充电桩功率: 97.81 kW, 最终充电功率: 36.00 kW。
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
奖励各项的值：powerloss=-0.4847527105759661, voltage=-3.519512358780209, ctrl=-0.0, connection=10.48, completion=3.66412213740458, energy=8.114651168257586, transformer=0.
已连接电池 batt_ev_121, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [ 1.        -1.        -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -0.9750203 -0.8108746]
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
奖励各项的值：powerloss=-0.49011523685066716, voltage=-3.683118609152153, ctrl=-0.0, connection=10.72, completion=3.7313432835820897, energy=8.127035325175196, transformer=0.
智能体的动作为: [ 1.         -1.         -1.         -1.         -0.8847288  -1.
 -1.         -1.         -1.         -0.7087999  -0.77133214]
已有历史设置self.charger_power=120.0，设置charger_power=58.72失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 32.0, -6.497877140288132
SOC从 0.75 更新为 0.89。
奖励各项的值：powerloss=-0.49040449563607724, voltage=-3.809224181155421, ctrl=-0.0, connection=10.72, completion=3.7313432835820897, energy=8.127035325175196, transformer=0.
已连接电池 batt_ev_015, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
已连接电池 batt_ev_201, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [ 0.50829446 -1.         -1.         -0.7650681  -0.20635751 -0.9219653
 -0.6038404  -0.3856803  -0.03969984 -0.7713392  -0.19996503]
已有历史设置self.charger_power=120.0，设置charger_power=26.72失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=46.28163456916809。
功率需求: 36.00 kW, 充电桩功率: 46.28 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=4.763980507850647。
功率需求: 120.00 kW, 充电桩功率: 4.76 kW, 最终充电功率: 4.76 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 4.763980507850647, -0.9673675012106551
SOC从 0.89 更新为 0.97。
SOC从 0.52 更新为 0.67。
SOC从 0.18 更新为 0.19。
已断开电池: batt_ev_121
时间步 38: 电池 batt_ev_121 已离开，当前SOC: 97.2%，能量满足率: 98.3%
奖励各项的值：powerloss=-0.4883512970167324, voltage=-3.7474966300397314, ctrl=-0.0, connection=10.8, completion=3.7037037037037033, energy=8.13965364480039, transformer=0.
已连接电池 batt_ev_080, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_204, 初始SOC: 2.0%, 最大功率: 80kW, 电池容量: 81kWh，并创BMS。
智能体的动作为: [-0.88600534 -0.92790407 -1.         -0.63219666 -0.         -0.80975074
 -1.         -0.         -0.81730074 -1.         -0.        ]
初次设置charger_power=111.34848833084106。
功率需求: 80.00 kW, 充电桩功率: 111.35 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=46.28163456916809，设置charger_power=0.0失败。
功率需求: 36.00 kW, 充电桩功率: 46.28 kW, 最终充电功率: 36.00 kW。
self.charger_power=4.763980507850647 改为 98.07608842849731。
功率需求: 120.00 kW, 充电桩功率: 98.08 kW, 最终充电功率: 98.08 kW。
初次设置charger_power=0.0。
功率需求: 36.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 88.60053420066833, 29.12158730211594
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 98.07608842849731, -19.915199156512813
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.02 更新为 0.27。
SOC从 0.67 更新为 0.82。
SOC从 0.19 更新为 0.43。
SOC从 0.57 更新为 0.57。
奖励各项的值：powerloss=-0.49591957854078705, voltage=-3.798285517258253, ctrl=-0.0, connection=10.8, completion=3.7037037037037033, energy=8.13965364480039, transformer=0.
已连接电池 batt_ev_183, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 71kWh，并创BMS。
已连接电池 batt_ev_230, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [ 1.        -1.        -1.        -1.        -0.9723918 -1.
 -1.        -1.        -1.        -0.8913977 -0.8387803]
已有历史设置self.charger_power=111.34848833084106，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 111.35 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=46.28163456916809，设置charger_power=45.120000000000005失败。
功率需求: 24.00 kW, 充电桩功率: 46.28 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=98.07608842849731，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 98.08 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=106.96772575378418。
功率需求: 36.00 kW, 充电桩功率: 106.97 kW, 最终充电功率: 36.00 kW。
self.charger_power=0.0 改为 92.88。
功率需求: 36.00 kW, 充电桩功率: 92.88 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -88.6, -29.121411718847277
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_183 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.27 更新为 0.51。
SOC从 0.38 更新为 0.66。
SOC从 0.82 更新为 0.91。
SOC从 0.43 更新为 0.66。
SOC从 0.52 更新为 0.66。
SOC从 0.57 更新为 0.74。
已断开电池: batt_ev_183
时间步 40 执行前: 电池 batt_ev_183 已充满 (SOC: 66.2%)，离开
奖励各项的值：powerloss=-0.4803085825978771, voltage=-3.464793590537086, ctrl=-0.0, connection=10.88, completion=3.75, energy=8.153332662118034, transformer=0.
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
已有历史设置self.charger_power=111.34848833084106，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 111.35 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=46.28163456916809，设置charger_power=21.120000000000005失败。
功率需求: 15.00 kW, 充电桩功率: 46.28 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=98.07608842849731，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 98.08 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=106.96772575378418，设置charger_power=88.80000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 106.97 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=92.88，设置charger_power=56.879999999999995失败。
功率需求: 24.00 kW, 充电桩功率: 92.88 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.51 更新为 0.66。
SOC从 0.91 更新为 0.97。
SOC从 0.66 更新为 0.84。
SOC从 0.66 更新为 0.80。
SOC从 0.74 更新为 0.85。
已断开电池: batt_ev_201
时间步 41: 电池 batt_ev_201 已离开，当前SOC: 83.7%，能量满足率: 93.9%
已断开电池: batt_ev_204
时间步 41: 电池 batt_ev_204 已离开，当前SOC: 66.2%，能量满足率: 66.9%
已断开电池: batt_ev_230
时间步 41: 电池 batt_ev_230 已离开，当前SOC: 79.7%，能量满足率: 60.2%
奖励各项的值：powerloss=-0.47830791234255626, voltage=-3.2388274094862557, ctrl=-0.0, connection=11.120000000000001, completion=3.6690647482014387, energy=8.136342986875581, transformer=0.
智能体的动作为: [ 1.        -1.        -1.        -1.        -0.8069891 -1.
 -1.        -1.        -1.        -0.577396  -0.9455147]
已有历史设置self.charger_power=46.28163456916809，设置charger_power=6.1200000000000045失败。
功率需求: 15.00 kW, 充电桩功率: 46.28 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=92.88，设置charger_power=32.879999999999995失败。
功率需求: 24.00 kW, 充电桩功率: 92.88 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.97 更新为 1.00。
SOC从 0.85 更新为 0.96。
已断开电池: batt_ev_015
时间步 42 执行前: 电池 batt_ev_015 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_080
时间步 42 执行前: 电池 batt_ev_080 已充满 (SOC: 95.9%)，离开
奖励各项的值：powerloss=-0.48066483373712116, voltage=-3.104218771265479, ctrl=-0.0, connection=11.28, completion=3.7588652482269502, energy=8.162777838125573, transformer=0.
已连接电池 batt_ev_148, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_215, 初始SOC: 62.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_210, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [ 0.47568953 -1.         -1.         -0.7640375  -0.19053116 -0.9251785
 -0.6105799  -0.37362468 -0.06500337 -0.797999   -0.18349667]
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
初次设置charger_power=22.863739728927612。
功率需求: 72.00 kW, 充电桩功率: 22.86 kW, 最终充电功率: 22.86 kW。
初次设置charger_power=94.60000000000001。
功率需求: 36.00 kW, 充电桩功率: 94.60 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 22.863739728927612, -4.6426803664405085
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.28 更新为 0.61。
SOC从 0.62 更新为 0.70。
SOC从 0.57 更新为 0.73。
奖励各项的值：powerloss=-0.4748477325602056, voltage=-2.703368953667733, ctrl=-0.0, connection=11.28, completion=3.7588652482269502, energy=8.162777838125573, transformer=0.
智能体的动作为: [ 1.         -1.         -1.         -1.         -0.8084101  -1.
 -1.         -1.         -1.         -0.57932997 -0.94340426]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=22.863739728927612，设置charger_power=92.63999999999999失败。
功率需求: 72.00 kW, 充电桩功率: 22.86 kW, 最终充电功率: 22.86 kW。
已有历史设置self.charger_power=94.60000000000001，设置charger_power=58.599999999999994失败。
功率需求: 24.00 kW, 充电桩功率: 94.60 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 22.863739728927612, -4.6426803664405085
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.61 更新为 0.81。
SOC从 0.70 更新为 0.77。
SOC从 0.73 更新为 0.84。
已断开电池: batt_ev_210
时间步 44: 电池 batt_ev_210 已离开，当前SOC: 84.3%，能量满足率: 66.5%
奖励各项的值：powerloss=-0.4572750413631244, voltage=-2.2133840881328704, ctrl=-0.0, connection=11.36, completion=3.732394366197183, energy=8.152137745608247, transformer=0.
已连接电池 batt_ev_146, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
已连接电池 batt_ev_027, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 107kWh，并创BMS。
智能体的动作为: [ 0.97681415 -1.         -1.         -1.         -0.5825315  -1.
 -1.         -1.         -1.         -0.91667706 -0.46881387]
已有历史设置self.charger_power=120.0，设置charger_power=70.07999999999998失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=22.863739728927612，设置charger_power=69.75999999999999失败。
功率需求: 48.00 kW, 充电桩功率: 22.86 kW, 最终充电功率: 22.86 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 22.863739728927612, -4.6426803664405085
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 96.0, -19.493631420864393
SOC从 0.81 更新为 0.94。
SOC从 0.32 更新为 0.54。
SOC从 0.77 更新为 0.85。
SOC从 0.42 更新为 0.62。
已断开电池: batt_ev_148
时间步 45 执行前: 电池 batt_ev_148 已充满 (SOC: 93.9%)，离开
奖励各项的值：powerloss=-0.45612014724221783, voltage=-2.6033682511100045, ctrl=-0.0, connection=11.44, completion=3.776223776223776, energy=8.165059859275322, transformer=0.
已连接电池 batt_ev_135, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_127, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 88kWh，并创BMS。
已连接电池 batt_ev_165, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 105kWh，并创BMS。
智能体的动作为: [ 1.         -1.         -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -0.9480747  -0.81977934]
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=22.863739728927612，设置charger_power=46.879999999999995失败。
功率需求: 48.00 kW, 充电桩功率: 22.86 kW, 最终充电功率: 22.86 kW。
已有历史设置self.charger_power=120.0，设置charger_power=119.28失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=113.76896381378174。
功率需求: 120.00 kW, 充电桩功率: 113.77 kW, 最终充电功率: 113.77 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 22.863739728927612, -4.6426803664405085
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 113.76896381378174, -23.101773413745
SOC从 0.32 更新为 0.62。
SOC从 0.54 更新为 0.71。
SOC从 0.85 更新为 0.92。
SOC从 0.62 更新为 0.77。
SOC从 0.18 更新为 0.46。
SOC从 0.18 更新为 0.45。
已断开电池: batt_ev_215
时间步 46 执行前: 电池 batt_ev_215 已充满 (SOC: 92.1%)，离开
已断开电池: batt_ev_027
时间步 46: 电池 batt_ev_027 已离开，当前SOC: 71.3%，能量满足率: 65.4%
奖励各项的值：powerloss=-0.4389978309931811, voltage=-2.2319909640239777, ctrl=-0.0, connection=11.6, completion=3.793103448275862, energy=8.166521489318189, transformer=0.
已连接电池 batt_ev_003, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_001, 初始SOC: 38.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
已连接电池 batt_ev_086, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
智能体的动作为: [ 1.         -0.97391784 -1.         -0.9697246  -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=120.0，设置charger_power=82.88失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=71.28失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=113.76896381378174，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 113.77 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
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
SOC从 0.42 更新为 0.68。
SOC从 0.46 更新为 0.69。
SOC从 0.45 更新为 0.68。
SOC从 0.38 更新为 0.72。
已断开电池: batt_ev_146
时间步 47: 电池 batt_ev_146 已离开，当前SOC: 87.6%，能量满足率: 81.4%
已断开电池: batt_ev_135
时间步 47: 电池 batt_ev_135 已离开，当前SOC: 83.9%，能量满足率: 78.6%
奖励各项的值：powerloss=-0.40045297951968795, voltage=-1.5788373033316516, ctrl=-0.0, connection=11.76, completion=3.741496598639456, energy=8.164213532849503, transformer=0.
智能体的动作为: [ 1.         -0.99069077 -1.         -0.819885   -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=98.63999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=108.63999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=113.76896381378174，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 113.77 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=77.6失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.37 更新为 0.57。
SOC从 0.68 更新为 0.87。
SOC从 0.69 更新为 0.86。
SOC从 0.68 更新为 0.85。
SOC从 0.72 更新为 0.89。
已断开电池: batt_ev_165
时间步 48: 电池 batt_ev_165 已离开，当前SOC: 85.1%，能量满足率: 83.9%
奖励各项的值：powerloss=-0.34495639582995374, voltage=-0.9099978757214033, ctrl=-0.0, connection=11.84, completion=3.716216216216216, energy=8.16571015955805, transformer=0.
已连接电池 batt_ev_043, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_051, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
已连接电池 batt_ev_144, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [ 1.        -1.        -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -0.9776019 -0.8140321]
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=103.19999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=38.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=29.599999999999994失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
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
SOC从 0.87 更新为 0.96。
SOC从 0.86 更新为 0.93。
SOC从 0.89 更新为 1.00。
已断开电池: batt_ev_003
时间步 49: 电池 batt_ev_003 已离开，当前SOC: 95.6%，能量满足率: 95.7%
已断开电池: batt_ev_001
时间步 49 执行前: 电池 batt_ev_001 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_144
时间步 49 执行前: 电池 batt_ev_144 已充满 (SOC: 61.2%)，离开
奖励各项的值：powerloss=-0.27800746508093016, voltage=0.0, ctrl=-0.0, connection=12.08, completion=3.7748344370860925, energy=8.199280994339095, transformer=0.
已连接电池 batt_ev_188, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
已连接电池 batt_ev_107, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 60kWh，并创BMS。
已连接电池 batt_ev_131, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.18 更新为 0.53。
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
奖励各项的值：powerloss=-0.26334561710671295, voltage=-0.009962876885984961, ctrl=-0.0, connection=12.32, completion=3.8311688311688314, energy=8.226243052890931, transformer=0.
已连接电池 batt_ev_136, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
已连接电池 batt_ev_116, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 52kWh，并创BMS。
已连接电池 batt_ev_196, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.53 更新为 0.74。
SOC从 0.84 更新为 0.97。
SOC从 0.42 更新为 0.62。
SOC从 0.61 更新为 0.81。
SOC从 0.42 更新为 0.73。
SOC从 0.55 更新为 0.74。
SOC从 0.18 更新为 0.52。
已断开电池: batt_ev_131
时间步 51: 电池 batt_ev_131 已离开，当前SOC: 74.2%，能量满足率: 68.6%
奖励各项的值：powerloss=-0.2522660670890119, voltage=-0.03616877955270992, ctrl=-0.0, connection=12.4, completion=3.8064516129032255, energy=8.217460765829394, transformer=0.
已连接电池 batt_ev_005, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_063, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
已连接电池 batt_ev_033, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
已连接电池 batt_ev_077, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
已有历史设置self.charger_power=120.0，设置charger_power=90.08000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
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
SOC从 0.74 更新为 0.88。
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
奖励各项的值：powerloss=-0.2522684854038779, voltage=-0.021779074893790717, ctrl=-0.0, connection=12.48, completion=3.8461538461538463, energy=8.22888729938177, transformer=0.
已连接电池 batt_ev_082, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
时间步 52 执行前: 排队电池 batt_ev_082 已接入
智能体的动作为: [ 1.         -0.9011963  -1.         -0.92332774 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=120.0，设置charger_power=42.079999999999984失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
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
SOC从 0.88 更新为 0.96。
SOC从 0.38 更新为 0.69。
SOC从 0.60 更新为 0.77。
SOC从 0.76 更新为 0.86。
SOC从 0.74 更新为 0.89。
SOC从 0.95 更新为 1.00。
SOC从 0.88 更新为 0.98。
SOC从 0.57 更新为 0.75。
SOC从 0.43 更新为 0.64。
SOC从 0.73 更新为 0.86。
已断开电池: batt_ev_107
时间步 53 执行前: 电池 batt_ev_107 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_116
时间步 53: 电池 batt_ev_116 已离开，当前SOC: 97.8%，能量满足率: 99.6%
已断开电池: batt_ev_077
时间步 53: 电池 batt_ev_077 已离开，当前SOC: 63.6%，能量满足率: 57.0%
奖励各项的值：powerloss=-0.2498255874476326, voltage=-0.0082685231785673, ctrl=-0.0, connection=12.72, completion=3.836477987421384, energy=8.234977436754672, transformer=0.
已连接电池 batt_ev_159, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 53kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_159 已接入
时间步 53: 电池 batt_ev_097 已错过离开时间，无法接入
已连接电池 batt_ev_105, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_105 已接入
已连接电池 batt_ev_058, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_058 已接入
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
已有历史设置self.charger_power=120.0，设置charger_power=12.079999999999984失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=62.47999999999999失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=49.91999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=46.24000000000001失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=76.8，设置charger_power=16.80000000000001失败。
功率需求: 15.00 kW, 充电桩功率: 76.80 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=67.84。
功率需求: 48.00 kW, 充电桩功率: 67.84 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=95.83999999999997失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=24.319999999999993失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_105 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_058 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.96 更新为 1.00。
SOC从 0.69 更新为 0.93。
SOC从 0.77 更新为 0.88。
SOC从 0.86 更新为 0.92。
SOC从 0.89 更新为 0.99。
SOC从 0.68 更新为 0.91。
SOC从 0.42 更新为 0.65。
SOC从 0.75 更新为 0.88。
SOC从 0.28 更新为 0.50。
SOC从 0.86 更新为 0.95。
已断开电池: batt_ev_188
时间步 54 执行前: 电池 batt_ev_188 已充满 (SOC: 100.0%)，离开
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
奖励各项的值：powerloss=-0.2711771447931168, voltage=-0.013971475314116244, ctrl=-0.0, connection=13.280000000000001, completion=3.9156626506024095, energy=8.25810678974946, transformer=0.
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
智能体的动作为: [ 1.        -1.        -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -0.9198887]
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=14.47999999999999失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=25.919999999999987失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=67.84，设置charger_power=19.840000000000003失败。
功率需求: 20.00 kW, 充电桩功率: 67.84 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=46.56。
功率需求: 30.00 kW, 充电桩功率: 46.56 kW, 最终充电功率: 30.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 30.0, -6.091759819020124
SOC从 0.57 更新为 0.77。
SOC从 0.93 更新为 1.00。
SOC从 0.88 更新为 0.95。
SOC从 0.52 更新为 0.72。
SOC从 0.02 更新为 0.25。
SOC从 0.91 更新为 1.00。
SOC从 0.28 更新为 0.57。
SOC从 0.18 更新为 0.46。
SOC从 0.88 更新为 0.96。
已断开电池: batt_ev_005
时间步 55: 电池 batt_ev_005 已离开，当前SOC: 94.9%，能量满足率: 94.9%
已断开电池: batt_ev_082
时间步 55 执行前: 电池 batt_ev_082 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_159
时间步 55 执行前: 电池 batt_ev_159 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.31711333151121723, voltage=-0.013922998708209011, ctrl=-0.0, connection=13.52, completion=3.9644970414201186, energy=8.286014602598527, transformer=0.
已连接电池 batt_ev_029, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_195, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
已连接电池 batt_ev_213, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_133, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
已有历史设置self.charger_power=120.0，设置charger_power=82.80000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=101.68。
功率需求: 48.00 kW, 充电桩功率: 101.68 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=85.91999999999999失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=113.84失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=46.56，设置charger_power=16.560000000000002失败。
功率需求: 30.00 kW, 充电桩功率: 46.56 kW, 最终充电功率: 30.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.77 更新为 0.90。
SOC从 0.38 更新为 0.67。
SOC从 0.28 更新为 0.51。
SOC从 0.72 更新为 0.85。
SOC从 0.25 更新为 0.48。
SOC从 0.18 更新为 0.55。
SOC从 0.57 更新为 0.75。
SOC从 0.46 更新为 0.69。
SOC从 0.96 更新为 1.00。
SOC从 0.42 更新为 0.67。
已断开电池: batt_ev_175
时间步 56 执行前: 电池 batt_ev_175 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_213
时间步 56 执行前: 电池 batt_ev_213 已充满 (SOC: 50.7%)，离开
奖励各项的值：powerloss=-0.3718048208931121, voltage=-0.05766256283959881, ctrl=-0.0, connection=13.68, completion=4.035087719298246, energy=8.306061215433632, transformer=0.
已连接电池 batt_ev_145, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_044, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [ 1.         -0.99325085 -1.         -0.8153028  -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=120.0，设置charger_power=34.80000000000001失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=101.68，设置charger_power=53.68000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 101.68 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=97.83633470535278。
功率需求: 48.00 kW, 充电桩功率: 97.84 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=45.920000000000016失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=84.80000000000001失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=65.84失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=82.16失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.90 更新为 0.99。
SOC从 0.67 更新为 0.89。
SOC从 0.52 更新为 0.71。
SOC从 0.85 更新为 0.98。
SOC从 0.48 更新为 0.67。
SOC从 0.55 更新为 0.77。
SOC从 0.75 更新为 0.87。
SOC从 0.69 更新为 0.86。
SOC从 0.18 更新为 0.44。
SOC从 0.67 更新为 0.86。
已断开电池: batt_ev_118
时间步 57 执行前: 电池 batt_ev_118 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_199
时间步 57 执行前: 电池 batt_ev_199 已充满 (SOC: 98.1%)，离开
已断开电池: batt_ev_153
时间步 57: 电池 batt_ev_153 已离开，当前SOC: 66.6%，能量满足率: 67.3%
已断开电池: batt_ev_029
时间步 57 执行前: 电池 batt_ev_029 已充满 (SOC: 86.4%)，离开
奖励各项的值：powerloss=-0.40391474212114775, voltage=-0.6985903943455252, ctrl=-0.0, connection=14.0, completion=4.114285714285714, energy=8.326098497542402, transformer=0.
已连接电池 batt_ev_154, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_154 已接入
已连接电池 batt_ev_179, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_179 已接入
已连接电池 batt_ev_246, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 74kWh，并创BMS。
已连接电池 batt_ev_184, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=101.68，设置charger_power=17.680000000000007失败。
功率需求: 15.00 kW, 充电桩功率: 101.68 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=97.83633470535278，设置charger_power=71.03999999999999失败。
功率需求: 32.00 kW, 充电桩功率: 97.84 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=76.96000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=44.80000000000001失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=29.840000000000003失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.32 更新为 0.53。
SOC从 0.89 更新为 0.98。
SOC从 0.71 更新为 0.84。
SOC从 0.18 更新为 0.55。
SOC从 0.48 更新为 0.75。
SOC从 0.77 更新为 0.91。
SOC从 0.87 更新为 0.94。
SOC从 0.86 更新为 0.93。
SOC从 0.44 更新为 0.65。
SOC从 0.28 更新为 0.57。
已断开电池: batt_ev_169
时间步 58: 电池 batt_ev_169 已离开，当前SOC: 94.2%，能量满足率: 94.5%
已断开电池: batt_ev_059
时间步 58: 电池 batt_ev_059 已离开，当前SOC: 93.0%，能量满足率: 93.8%
已断开电池: batt_ev_195
时间步 58 执行前: 电池 batt_ev_195 已充满 (SOC: 98.4%)，离开
已断开电池: batt_ev_133
时间步 58: 电池 batt_ev_133 已离开，当前SOC: 91.2%，能量满足率: 91.5%
奖励各项的值：powerloss=-0.4399064115121587, voltage=-1.5113743234014854, ctrl=-0.0, connection=14.32, completion=4.078212290502793, energy=8.352191955563912, transformer=0.
已连接电池 batt_ev_066, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
时间步 58 执行前: 排队电池 batt_ev_066 已接入
已连接电池 batt_ev_233, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
已连接电池 batt_ev_219, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_249, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
智能体的动作为: [ 1.         -0.96458757 -1.         -0.96097684 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=120.0，设置charger_power=115.75050830841064失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=97.83633470535278，设置charger_power=39.03999999999999失败。
功率需求: 32.00 kW, 充电桩功率: 97.84 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=71.2失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=73.91999999999999失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=82.24000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.53 更新为 0.69。
SOC从 0.08 更新为 0.47。
SOC从 0.84 更新为 0.97。
SOC从 0.55 更新为 0.78。
SOC从 0.75 更新为 0.89。
SOC从 0.22 更新为 0.55。
SOC从 0.18 更新为 0.41。
SOC从 0.08 更新为 0.38。
SOC从 0.65 更新为 0.80。
SOC从 0.57 更新为 0.75。
已断开电池: batt_ev_145
时间步 59: 电池 batt_ev_145 已离开，当前SOC: 97.2%，能量满足率: 98.2%
已断开电池: batt_ev_044
时间步 59: 电池 batt_ev_044 已离开，当前SOC: 80.1%，能量满足率: 77.6%
已断开电池: batt_ev_179
时间步 59: 电池 batt_ev_179 已离开，当前SOC: 78.0%，能量满足率: 75.0%
不太安全
奖励各项的值：powerloss=-0.4634424707348136, voltage=-2.0159945485149287, ctrl=-0.0, connection=14.56, completion=4.010989010989011, energy=8.352300288707978, transformer=-2.448040674307447.
已连接电池 batt_ev_032, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_032 已接入
已连接电池 batt_ev_060, 初始SOC: 56.99999999999999%, 最大功率: 100kW, 电池容量: 90kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_060 已接入
已连接电池 batt_ev_103, 初始SOC: 72.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_103 已接入
智能体的动作为: [ 1.         -0.99332225 -1.         -0.8150546  -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=120.0，设置charger_power=118.39999999999998失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=97.80655145645142。
功率需求: 64.00 kW, 充电桩功率: 97.81 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=33.920000000000016失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=80.4失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=60.48000000000002。
功率需求: 24.00 kW, 充电桩功率: 60.48 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=104.63999999999999失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_060 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_103 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.69 更新为 0.85。
SOC从 0.47 更新为 0.79。
SOC从 0.48 更新为 0.68。
SOC从 0.57 更新为 0.74。
SOC从 0.89 更新为 0.97。
SOC从 0.55 更新为 0.75。
SOC从 0.41 更新为 0.60。
SOC从 0.38 更新为 0.62。
SOC从 0.72 更新为 0.83。
SOC从 0.75 更新为 0.86。
已断开电池: batt_ev_154
时间步 60: 电池 batt_ev_154 已离开，当前SOC: 84.6%，能量满足率: 79.7%
已断开电池: batt_ev_246
时间步 60: 电池 batt_ev_246 已离开，当前SOC: 97.0%，能量满足率: 98.0%
已断开电池: batt_ev_184
时间步 60: 电池 batt_ev_184 已离开，当前SOC: 86.3%，能量满足率: 83.2%
已断开电池: batt_ev_233
时间步 60: 电池 batt_ev_233 已离开，当前SOC: 75.3%，能量满足率: 70.2%
已断开电池: batt_ev_103
时间步 60: 电池 batt_ev_103 已离开，当前SOC: 83.1%，能量满足率: 55.6%
奖励各项的值：powerloss=-0.4712249130049564, voltage=-2.2397088466676296, ctrl=-0.0, connection=14.96, completion=3.9037433155080214, energy=8.335750300685094, transformer=0.
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
智能体的动作为: [ 1.         -0.9350025  -1.         -0.92939717 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=112.20030069351196。
功率需求: 96.00 kW, 充电桩功率: 112.20 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=63.68000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=97.80655145645142，设置charger_power=106.56失败。
功率需求: 48.00 kW, 充电桩功率: 97.81 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=94.80000000000001失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=105.19999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
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
SOC从 0.48 更新为 0.69。
SOC从 0.79 更新为 0.95。
SOC从 0.68 更新为 0.82。
SOC从 0.74 更新为 0.85。
SOC从 0.12 更新为 0.44。
SOC从 0.38 更新为 0.59。
SOC从 0.60 更新为 0.73。
SOC从 0.62 更新为 0.80。
SOC从 0.38 更新为 0.67。
SOC从 0.88 更新为 0.94。
已断开电池: batt_ev_066
时间步 61: 电池 batt_ev_066 已离开，当前SOC: 94.8%，能量满足率: 96.5%
已断开电池: batt_ev_060
时间步 61: 电池 batt_ev_060 已离开，当前SOC: 84.8%，能量满足率: 67.8%
已断开电池: batt_ev_217
时间步 61: 电池 batt_ev_217 已离开，当前SOC: 59.1%，能量满足率: 35.1%
奖励各项的值：powerloss=-0.47674887534446875, voltage=-2.3894372825923593, ctrl=-0.0, connection=15.200000000000001, completion=3.8421052631578947, energy=8.30904351955596, transformer=0.
已连接电池 batt_ev_073, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 106kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_073 已接入
已连接电池 batt_ev_020, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 99kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_020 已接入
已连接电池 batt_ev_208, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 61kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_208 已接入
智能体的动作为: [ 1.         -0.8904542  -1.         -0.90817404 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=112.20030069351196，设置charger_power=106.85450077056885失败。
功率需求: 72.00 kW, 充电桩功率: 112.20 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=97.80655145645142，设置charger_power=58.56失败。
功率需求: 32.00 kW, 充电桩功率: 97.81 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=69.19999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=80.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
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
SOC从 0.69 更新为 0.85。
SOC从 0.48 更新为 0.71。
SOC从 0.82 更新为 0.92。
SOC从 0.32 更新为 0.56。
SOC从 0.44 更新为 0.69。
SOC从 0.38 更新为 0.71。
SOC从 0.73 更新为 0.83。
SOC从 0.80 更新为 0.92。
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
奖励各项的值：powerloss=-0.47360001973545374, voltage=-2.3386313503715495, ctrl=-0.0, connection=15.52, completion=3.917525773195876, energy=8.33762245629129, transformer=-1.0206303096879197.
已连接电池 batt_ev_091, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_091 已接入
时间步 62: 电池 batt_ev_176 已错过离开时间，无法接入
已连接电池 batt_ev_102, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_102 已接入
已连接电池 batt_ev_236, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 92kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_236 已接入
已连接电池 batt_ev_074, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_074 已接入
智能体的动作为: [ 1.         -0.89593035 -1.         -0.89757854 -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=107.51164197921753。
功率需求: 60.00 kW, 充电桩功率: 107.51 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=107.70942449569702。
功率需求: 48.00 kW, 充电桩功率: 107.71 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=98.08000000000001失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=71.28失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=32.0失败。
功率需求: 30.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 30.00 kW。
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
SOC从 0.22 更新为 0.44。
SOC从 0.71 更新为 0.82。
SOC从 0.48 更新为 0.70。
SOC从 0.56 更新为 0.74。
SOC从 0.69 更新为 0.88。
SOC从 0.71 更新为 0.87。
SOC从 0.38 更新为 0.60。
SOC从 0.92 更新为 0.99。
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
奖励各项的值：powerloss=-0.46416856283716357, voltage=-2.1900200346366026, ctrl=-0.0, connection=15.84, completion=3.9393939393939394, energy=8.335130521062272, transformer=0.
时间步 63: 电池 batt_ev_130 已错过离开时间，无法接入
已连接电池 batt_ev_061, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 78kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_061 已接入
已连接电池 batt_ev_012, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 98kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_012 已接入
时间步 63: 电池 batt_ev_108 已错过离开时间，无法接入
已连接电池 batt_ev_228, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_228 已接入
已连接电池 batt_ev_218, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
已有历史设置self.charger_power=107.51164197921753，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 107.51 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=76.48000000000002失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=107.70942449569702，设置charger_power=66.4失败。
功率需求: 36.00 kW, 充电桩功率: 107.71 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=101.27999999999997失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=31.28失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
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
SOC从 0.44 更新为 0.62。
SOC从 0.82 更新为 0.93。
SOC从 0.70 更新为 0.86。
SOC从 0.74 更新为 0.87。
SOC从 0.28 更新为 0.60。
SOC从 0.87 更新为 0.97。
SOC从 0.48 更新为 0.72。
SOC从 0.22 更新为 0.50。
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
奖励各项的值：powerloss=-0.46438379596414275, voltage=-2.174856451180136, ctrl=-0.0, connection=16.240000000000002, completion=3.9408866995073892, energy=8.343870892745235, transformer=0.
已连接电池 batt_ev_243, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 64 执行前: 排队电池 batt_ev_243 已接入
已连接电池 batt_ev_122, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [ 1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.]
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=118.08。
功率需求: 60.00 kW, 充电桩功率: 118.08 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=107.70942449569702，设置charger_power=30.400000000000006失败。
功率需求: 15.00 kW, 充电桩功率: 107.71 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=6.280000000000001失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=105.36失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
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
SOC从 0.97 更新为 1.00。
SOC从 0.50 更新为 0.67。
SOC从 0.61 更新为 0.78。
已断开电池: batt_ev_208
时间步 65 执行前: 电池 batt_ev_208 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_102
时间步 65: 电池 batt_ev_102 已离开，当前SOC: 93.0%，能量满足率: 90.0%
已断开电池: batt_ev_122
时间步 65: 电池 batt_ev_122 已离开，当前SOC: 64.6%，能量满足率: 52.3%
奖励各项的值：powerloss=-0.4573043887632366, voltage=-2.1523909903871252, ctrl=-0.0, connection=16.48, completion=3.9320388349514563, energy=8.33996248574524, transformer=0.
已连接电池 batt_ev_139, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 84kWh，并创BMS。
智能体的动作为: [ 1.        -1.        -1.        -1.        -0.8072238 -1.
 -1.        -1.        -1.        -0.577905  -0.9453532]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=96.86685562133789。
功率需求: 80.00 kW, 充电桩功率: 96.87 kW, 最终充电功率: 80.00 kW。
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
奖励各项的值：powerloss=-0.47256904898833435, voltage=-2.488706220032678, ctrl=-0.0, connection=16.48, completion=3.9320388349514563, energy=8.33996248574524, transformer=0.
已连接电池 batt_ev_004, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_019, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
智能体的动作为: [ 1.        -1.        -1.        -1.        -0.8718227 -1.
 -1.        -1.        -1.        -0.6640795 -0.8335726]
已有历史设置self.charger_power=120.0，设置charger_power=82.08000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=96.86685562133789，设置charger_power=104.61872577667236失败。
功率需求: 64.00 kW, 充电桩功率: 96.87 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=24.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=33.360000000000014失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=29.599999999999994失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=82.56。
功率需求: 36.00 kW, 充电桩功率: 82.56 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 100.0, -20.30586606340041
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
奖励各项的值：powerloss=-0.4664948622540076, voltage=-2.2501509144010887, ctrl=-0.0, connection=16.8, completion=3.952380952380952, energy=8.362132522980238, transformer=0.
智能体的动作为: [ 1.         -1.         -1.         -1.         -0.8069593  -1.
 -1.         -1.         -1.         -0.57732505 -0.94555134]
已有历史设置self.charger_power=96.86685562133789，设置charger_power=96.83511257171631失败。
功率需求: 48.00 kW, 充电桩功率: 96.87 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=82.56，设置charger_power=46.56失败。
功率需求: 24.00 kW, 充电桩功率: 82.56 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.55 更新为 0.69。
SOC从 0.35 更新为 0.57。
SOC从 0.73 更新为 0.87。
奖励各项的值：powerloss=-0.44863724290012613, voltage=-1.8548554476922419, ctrl=-0.0, connection=16.8, completion=3.952380952380952, energy=8.362132522980238, transformer=0.
智能体的动作为: [ 0.4646541  -1.         -1.         -1.         -0.36378735 -1.
 -1.         -0.6760751  -1.         -1.         -0.3521666 ]
已有历史设置self.charger_power=96.86685562133789，设置charger_power=43.65448236465454失败。
功率需求: 48.00 kW, 充电桩功率: 96.87 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=81.12901210784912失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=82.56，设置charger_power=22.560000000000002失败。
功率需求: 15.00 kW, 充电桩功率: 82.56 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.69 更新为 0.83。
SOC从 0.57 更新为 0.74。
SOC从 0.87 更新为 0.96。
已断开电池: batt_ev_139
时间步 69: 电池 batt_ev_139 已离开，当前SOC: 83.4%，能量满足率: 83.1%
奖励各项的值：powerloss=-0.45086367272234223, voltage=-2.544124805820047, ctrl=-0.0, connection=16.88, completion=3.933649289099526, energy=8.361864823063419, transformer=0.
已连接电池 batt_ev_177, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [ 0.04891193 -1.         -1.         -0.9916715  -0.         -1.
 -1.         -0.33335382 -0.8031398  -1.         -0.25868383]
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=40.00245809555054失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=82.56，设置charger_power=7.560000000000002失败。
功率需求: 15.00 kW, 充电桩功率: 82.56 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.38 更新为 0.65。
SOC从 0.74 更新为 0.85。
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_019
时间步 70 执行前: 电池 batt_ev_019 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.4264089377830252, voltage=-2.124944831668012, ctrl=-0.0, connection=16.96, completion=3.9622641509433967, energy=8.369591875784819, transformer=0.
已连接电池 batt_ev_202, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_160, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [ 0.00585783 -1.         -1.         -0.9835392  -0.         -1.
 -1.         -0.32204288 -0.8026796  -1.         -0.2387208 ]
已有历史设置self.charger_power=120.0，设置charger_power=82.32失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=118.02470684051514。
功率需求: 80.00 kW, 充电桩功率: 118.02 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=38.645145893096924失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.65 更新为 0.85。
SOC从 0.48 更新为 0.74。
SOC从 0.18 更新为 0.55。
SOC从 0.85 更新为 0.96。
已断开电池: batt_ev_004
时间步 71 执行前: 电池 batt_ev_004 已充满 (SOC: 95.9%)，离开
奖励各项的值：powerloss=-0.39081319749262133, voltage=-1.5822609375993735, ctrl=-0.0, connection=17.04, completion=3.9906103286384975, energy=8.37724637402057, transformer=0.
智能体的动作为: [ 1.         -1.         -1.         -1.         -0.8798357  -1.
 -1.         -1.         -1.         -0.79891825 -0.6500078 ]
已有历史设置self.charger_power=120.0，设置charger_power=34.31999999999999失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=118.02470684051514，设置charger_power=78.08000000000001失败。
功率需求: 40.00 kW, 充电桩功率: 118.02 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=74.48失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.85 更新为 0.94。
SOC从 0.74 更新为 0.87。
SOC从 0.55 更新为 0.77。
已断开电池: batt_ev_202
时间步 72 执行前: 电池 batt_ev_202 已充满 (SOC: 87.5%)，离开
奖励各项的值：powerloss=-0.34341101024990695, voltage=-0.9483341372541776, ctrl=-0.0, connection=17.12, completion=4.018691588785047, energy=8.384829334889634, transformer=0.
已连接电池 batt_ev_099, 初始SOC: 68.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
已连接电池 batt_ev_100, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [-1.         -0.8619783  -1.         -0.5517273  -0.         -0.75083613
 -1.         -0.         -0.83049977 -1.         -0.        ]
初次设置charger_power=85.75999999999999。
功率需求: 36.00 kW, 充电桩功率: 85.76 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=14.319999999999993失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=90.1003360748291。
功率需求: 80.00 kW, 充电桩功率: 90.10 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=38.480000000000004失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.68 更新为 0.81。
SOC从 0.94 更新为 1.00。
SOC从 0.18 更新为 0.52。
SOC从 0.77 更新为 0.91。
已断开电池: batt_ev_177
时间步 73 执行前: 电池 batt_ev_177 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_160
时间步 73: 电池 batt_ev_160 已离开，当前SOC: 91.2%，能量满足率: 91.5%
奖励各项的值：powerloss=-0.28173694056165616, voltage=0.0, ctrl=-0.0, connection=17.28, completion=4.027777777777778, energy=8.395832495971279, transformer=0.
智能体的动作为: [ 0.47311616 -0.99910194 -1.         -1.         -0.3725492  -1.
 -1.         -0.7047342  -1.         -1.         -0.3399426 ]
已有历史设置self.charger_power=85.75999999999999，设置charger_power=49.75999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 85.76 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=90.1003360748291，设置charger_power=110.24失败。
功率需求: 48.00 kW, 充电桩功率: 90.10 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -47.31161594390869, -15.550576151089668
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.81 更新为 0.90。
SOC从 0.52 更新为 0.73。
已断开电池: batt_ev_100
时间步 74: 电池 batt_ev_100 已离开，当前SOC: 73.2%，能量满足率: 74.6%
奖励各项的值：powerloss=-0.24872160654274272, voltage=-0.0024517266530765802, ctrl=-0.0, connection=17.36, completion=4.009216589861751, energy=8.391500233748658, transformer=0.
智能体的动作为: [-0.22024679 -1.         -1.         -0.70738626 -0.         -0.9648127
 -0.6725544  -0.10850166 -0.52153075 -1.         -0.        ]
已有历史设置self.charger_power=85.75999999999999，设置charger_power=25.75999999999999失败。
功率需求: 15.00 kW, 充电桩功率: 85.76 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 22.02467918395996, 7.239161969431413
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.90 更新为 0.96。
奖励各项的值：powerloss=-0.24004737604820084, voltage=-0.006108197128009696, ctrl=-0.0, connection=17.36, completion=4.009216589861751, energy=8.391500233748658, transformer=0.
智能体的动作为: [ 1.         -1.         -1.         -0.6320503  -0.67699724 -1.
 -0.         -0.5251691  -0.         -0.36176208 -0.1188361 ]
已有历史设置self.charger_power=85.75999999999999，设置charger_power=10.759999999999991失败。
功率需求: 15.00 kW, 充电桩功率: 85.76 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -74.72000000000001, -24.559276338964658
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_099
时间步 76 执行前: 电池 batt_ev_099 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.2320536881265098, voltage=-0.06983387564554411, ctrl=-0.0, connection=17.44, completion=4.036697247706423, energy=8.39887867304339, transformer=0.
已连接电池 batt_ev_120, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [ 1.         -1.         -1.         -0.63301796 -0.6840896  -1.
 -0.         -0.52902806 -0.         -0.3570742  -0.12183143]
初次设置charger_power=0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 0.0, -0.0
SOC从 0.18 更新为 0.18。
奖励各项的值：powerloss=-0.23798384805730638, voltage=-0.011058096712588394, ctrl=-0.0, connection=17.44, completion=4.036697247706423, energy=8.39887867304339, transformer=0.
智能体的动作为: [ 1.         -1.         -0.64546275 -0.49133298 -0.97249    -1.
 -0.         -0.66715264 -0.         -0.28226286 -0.        ]
self.charger_power=0.0 改为 0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 0.0, -0.0
SOC从 0.18 更新为 0.18。
奖励各项的值：powerloss=-0.2549743061480927, voltage=-0.007666449280616661, ctrl=-0.0, connection=17.44, completion=4.036697247706423, energy=8.39887867304339, transformer=0.
已连接电池 batt_ev_035, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 77kWh，并创BMS。
智能体的动作为: [ 1.         -1.         -0.64308727 -0.49036136 -0.9738809  -1.
 -0.         -0.66766506 -0.         -0.28185818 -0.        ]
self.charger_power=0.0 改为 0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=33.822981119155884。
功率需求: 64.00 kW, 充电桩功率: 33.82 kW, 最终充电功率: 33.82 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 33.822981119155884, -6.868049244705002
SOC从 0.18 更新为 0.18。
SOC从 0.48 更新为 0.59。
已断开电池: batt_ev_120
时间步 79: 电池 batt_ev_120 已离开，当前SOC: 18.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.30407743951284766, voltage=-0.19877991535022677, ctrl=-0.0, connection=17.52, completion=4.018264840182648, energy=8.360527628874241, transformer=0.
已连接电池 batt_ev_151, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
智能体的动作为: [ 0.512107   -1.         -1.         -0.7652669  -0.20829815 -0.9216399
 -0.60256517 -0.38717166 -0.03662411 -0.76794    -0.20130207]
初次设置charger_power=24.99577760696411。
功率需求: 120.00 kW, 充电桩功率: 25.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=33.822981119155884，设置charger_power=92.15279817581177失败。
功率需求: 48.00 kW, 充电桩功率: 33.82 kW, 最终充电功率: 33.82 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 33.822981119155884, -6.868049244705002
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 24.99577760696411, -5.075609122375565
SOC从 0.28 更新为 0.35。
SOC从 0.59 更新为 0.70。
奖励各项的值：powerloss=-0.3494903583891506, voltage=-0.29937646664893736, ctrl=-0.0, connection=17.52, completion=4.018264840182648, energy=8.360527628874241, transformer=0.
智能体的动作为: [ 0.28022718 -1.         -1.         -0.7542466  -0.09636698 -0.9400292
 -0.6424958  -0.30047333 -0.20576626 -0.9447986  -0.08334167]
已有历史设置self.charger_power=24.99577760696411，设置charger_power=11.564037501811981失败。
功率需求: 96.00 kW, 充电桩功率: 25.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=33.822981119155884，设置charger_power=92.47999999999999失败。
功率需求: 48.00 kW, 充电桩功率: 33.82 kW, 最终充电功率: 33.82 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 33.822981119155884, -6.868049244705002
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 24.99577760696411, -5.075609122375565
SOC从 0.35 更新为 0.43。
SOC从 0.70 更新为 0.81。
已断开电池: batt_ev_035
时间步 81: 电池 batt_ev_035 已离开，当前SOC: 81.0%，能量满足率: 65.9%
已断开电池: batt_ev_151
时间步 81: 电池 batt_ev_151 已离开，当前SOC: 42.5%，能量满足率: 20.8%
奖励各项的值：powerloss=-0.381040945600173, voltage=-0.5553758410409271, ctrl=-0.0, connection=17.68, completion=3.9819004524886874, energy=8.324091269121265, transformer=0.
智能体的动作为: [ 0.33342433 -1.         -1.         -0.7575434  -0.12195687 -0.93656224
 -0.63501483 -0.3206136  -0.16891457 -0.90660477 -0.11069672]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.4011227295652363, voltage=-0.9440560021428002, ctrl=-0.0, connection=17.68, completion=3.9819004524886874, energy=8.324091269121265, transformer=0.
智能体的动作为: [ 1.         -1.         -0.6367816  -0.48784745 -0.9776577  -1.
 -0.         -0.6690229  -0.         -0.28074804 -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.4211532152759879, voltage=-1.4381180314854614, ctrl=-0.0, connection=17.68, completion=3.9819004524886874, energy=8.324091269121265, transformer=0.
已连接电池 batt_ev_056, 初始SOC: 62.0%, 最大功率: 80kW, 电池容量: 64kWh，并创BMS。
已连接电池 batt_ev_226, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [ 1.         -1.         -0.6361648  -0.48760408 -0.97802895 -1.
 -0.         -0.669153   -0.         -0.28064    -0.        ]
初次设置charger_power=80.2983570098877。
功率需求: 60.00 kW, 充电桩功率: 80.30 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.18 更新为 0.51。
SOC从 0.62 更新为 0.62。
奖励各项的值：powerloss=-0.4331824317617968, voltage=-1.7115297947511776, ctrl=-0.0, connection=17.68, completion=3.9819004524886874, energy=8.324091269121265, transformer=0.
已连接电池 batt_ev_048, 初始SOC: 42.0%, 最大功率: 120kW, 电池容量: 93kWh，并创BMS。
智能体的动作为: [ 0.3255756  -1.         -1.         -0.7570813  -0.11817729 -0.93709636
 -0.63617563 -0.31764787 -0.17441504 -0.91232044 -0.10666753]
初次设置charger_power=90.84975242614746。
功率需求: 96.00 kW, 充电桩功率: 90.85 kW, 最终充电功率: 90.85 kW。
已有历史设置self.charger_power=80.2983570098877，设置charger_power=38.11774492263794失败。
功率需求: 36.00 kW, 充电桩功率: 80.30 kW, 最终充电功率: 36.00 kW。
self.charger_power=0.0 改为 12.800104022026062。
功率需求: 48.00 kW, 充电桩功率: 12.80 kW, 最终充电功率: 12.80 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 12.800104022026062, -2.599171978688541
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_048 充电的有无功功率为 90.84975242614746, -18.447829046584367
SOC从 0.42 更新为 0.66。
SOC从 0.51 更新为 0.70。
SOC从 0.62 更新为 0.67。
已断开电池: batt_ev_048
时间步 85: 电池 batt_ev_048 已离开，当前SOC: 66.4%，能量满足率: 43.6%
奖励各项的值：powerloss=-0.4466599304227243, voltage=-2.0510517807351594, ctrl=-0.0, connection=17.76, completion=3.963963963963964, energy=8.306237700694329, transformer=0.
已连接电池 batt_ev_234, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_227, 初始SOC: 8.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
智能体的动作为: [ 0.0861038  -1.         -1.         -0.9995105  -0.         -1.
 -1.         -0.34788972 -0.8108862  -1.         -0.27443323]
初次设置charger_power=108.36000000000001。
功率需求: 36.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=80.2983570098877，设置charger_power=41.746766567230225失败。
功率需求: 24.00 kW, 充电桩功率: 80.30 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=12.800104022026062，设置charger_power=32.931987047195435失败。
功率需求: 48.00 kW, 充电桩功率: 12.80 kW, 最终充电功率: 12.80 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 12.800104022026062, -2.599171978688541
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.57 更新为 0.71。
SOC从 0.08 更新为 0.40。
SOC从 0.70 更新为 0.83。
SOC从 0.67 更新为 0.72。
已断开电池: batt_ev_056
时间步 86: 电池 batt_ev_056 已离开，当前SOC: 72.0%，能量满足率: 27.8%
已断开电池: batt_ev_226
时间步 86 执行前: 电池 batt_ev_226 已充满 (SOC: 83.2%)，离开
奖励各项的值：powerloss=-0.4483655083133593, voltage=-2.135325835488886, ctrl=-0.0, connection=17.92, completion=3.9732142857142856, energy=8.289118514874636, transformer=0.
智能体的动作为: [ 0.06247735 -1.         -1.         -0.9940182  -0.         -1.
 -1.         -0.33613694 -0.8020547  -1.         -0.26517245]
已有历史设置self.charger_power=108.36000000000001，设置charger_power=72.36000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=112.96失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.71 更新为 0.81。
SOC从 0.40 更新为 0.65。
奖励各项的值：powerloss=-0.442165646980599, voltage=-2.0765032973912234, ctrl=-0.0, connection=17.92, completion=3.9732142857142856, energy=8.289118514874636, transformer=0.
智能体的动作为: [-0.21928251 -1.         -1.         -0.70755696 -0.         -0.9648823
 -0.67242146 -0.10887145 -0.5209688  -1.         -0.        ]
已有历史设置self.charger_power=108.36000000000001，设置charger_power=48.360000000000014失败。
功率需求: 24.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=64.96失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 21.928250789642334, 7.20746748893129
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.81 更新为 0.90。
SOC从 0.65 更新为 0.85。
已断开电池: batt_ev_227
时间步 88: 电池 batt_ev_227 已离开，当前SOC: 84.6%，能量满足率: 85.1%
奖励各项的值：powerloss=-0.4366834732904772, voltage=-1.951633693764847, ctrl=-0.0, connection=18.0, completion=3.9555555555555557, energy=8.290103047243514, transformer=0.
智能体的动作为: [ 0.26154852 -1.         -1.         -0.7529992  -0.08739604 -0.9411687
 -0.64491224 -0.29338065 -0.21848118 -0.95791954 -0.07371312]
已有历史设置self.charger_power=108.36000000000001，设置charger_power=24.360000000000014失败。
功率需求: 15.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -21.92, -7.204755585520682
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.90 更新为 0.96。
奖励各项的值：powerloss=-0.43552182232988373, voltage=-1.8599218304866494, ctrl=-0.0, connection=18.0, completion=3.9555555555555557, energy=8.290103047243514, transformer=0.
智能体的动作为: [ 1.         -1.         -1.         -0.634019   -0.6760227  -1.
 -0.         -0.5262081  -0.         -0.36667046 -0.11940062]
已有历史设置self.charger_power=108.36000000000001，设置charger_power=9.360000000000014失败。
功率需求: 15.00 kW, 充电桩功率: 108.36 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_234
时间步 90 执行前: 电池 batt_ev_234 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.4646495592449707, voltage=-2.4095047175669237, ctrl=-0.0, connection=18.080000000000002, completion=3.982300884955752, energy=8.297668962963677, transformer=0.
智能体的动作为: [ 1.         -1.         -1.         -0.63391435 -0.67428386 -1.
 -0.         -0.5251927  -0.         -0.36742428 -0.11909677]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.45894477361187064, voltage=-2.283396453891128, ctrl=-0.0, connection=18.080000000000002, completion=3.982300884955752, energy=8.297668962963677, transformer=0.
智能体的动作为: [ 1.         -1.         -0.6379855  -0.48833728 -0.9769619  -1.
 -0.         -0.6687789  -0.         -0.28095797 -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.44625418342229806, voltage=-1.9410422845921904, ctrl=-0.0, connection=18.080000000000002, completion=3.982300884955752, energy=8.297668962963677, transformer=0.
已连接电池 batt_ev_238, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [ 1.         -1.         -0.63748366 -0.4881626  -0.9772913  -1.
 -0.         -0.66888475 -0.         -0.28087184 -0.        ]
初次设置charger_power=85.28。
功率需求: 48.00 kW, 充电桩功率: 85.28 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.48 更新为 0.77。
奖励各项的值：powerloss=-0.4520903036468624, voltage=-2.7016110875714006, ctrl=-0.0, connection=18.080000000000002, completion=3.982300884955752, energy=8.297668962963677, transformer=0.
智能体的动作为: [ 0.51129687 -1.         -1.         -0.765385   -0.2080099  -0.9216078
 -0.603007   -0.38707277 -0.03702777 -0.7683646  -0.20131417]
已有历史设置self.charger_power=85.28，设置charger_power=37.28失败。
功率需求: 24.00 kW, 充电桩功率: 85.28 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.77 更新为 0.92。
已断开电池: batt_ev_238
时间步 94 执行前: 电池 batt_ev_238 已充满 (SOC: 91.9%)，离开
奖励各项的值：powerloss=-0.42360053653934693, voltage=-2.1890502829351064, ctrl=-0.0, connection=18.16, completion=4.008810572687224, energy=8.30516821863344, transformer=0.
智能体的动作为: [ 0.68920064 -1.         -1.         -0.7531415  -0.28827563 -0.9741709
 -0.49524495 -0.40818208 -0.         -0.70446897 -0.1981412 ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.3828617448286525, voltage=-1.5235689575863742, ctrl=-0.0, connection=18.16, completion=4.008810572687224, energy=8.30516821863344, transformer=0.
已连接电池 batt_ev_025, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
已连接电池 batt_ev_013, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 89kWh，并创BMS。
已连接电池 batt_ev_117, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 111kWh，并创BMS。
已连接电池 batt_ev_166, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 114kWh，并创BMS。
智能体的动作为: [ 1.         -1.         -0.6396668  -0.4890578  -0.9760163  -1.
 -0.         -0.6684216  -0.         -0.28124145 -0.        ]
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=117.1219539642334。
功率需求: 72.00 kW, 充电桩功率: 117.12 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=33.74897360801697。
功率需求: 120.00 kW, 充电桩功率: 33.75 kW, 最终充电功率: 33.75 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_025 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_013 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_117 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_166 充电的有无功功率为 33.74897360801697, -6.85302137861628
SOC从 0.12 更新为 0.43。
SOC从 0.52 更新为 0.68。
SOC从 0.18 更新为 0.18。
SOC从 0.28 更新为 0.35。
已断开电池: batt_ev_025
时间步 96: 电池 batt_ev_025 已离开，当前SOC: 42.6%，能量满足率: 35.6%
已断开电池: batt_ev_013
时间步 96: 电池 batt_ev_013 已离开，当前SOC: 18.0%，能量满足率: 0.0%
已断开电池: batt_ev_117
时间步 96: 电池 batt_ev_117 已离开，当前SOC: 68.2%，能量满足率: 35.3%
已断开电池: batt_ev_166
时间步 96: 电池 batt_ev_166 已离开，当前SOC: 35.4%，能量满足率: 10.6%
奖励各项的值：powerloss=-0.3423919092543197, voltage=-0.9060404031792302, ctrl=-4.0, connection=18.48, completion=3.9393939393939394, energy=8.19660457790097, transformer=0.
调度记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250511_121502_13Bus_cbat_s2_1000000\test_results_20250511_172037\schedule.csv
储能放电功率记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250511_121502_13Bus_cbat_s2_1000000\test_results_20250511_172037\storage_schedule.csv
储能能量记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250511_121502_13Bus_cbat_s2_1000000\test_results_20250511_172037\storage_energy.csv
已生成GIF动画，包含96步
测试完成 - 总奖励: 2041.7197
测试结果保存在: D:\LENOVO\Documents\Python\ML\powergym\results_20250511_121502_13Bus_cbat_s2_1000000\test_results_20250511_172037
运行时间: 18388.12秒

进程已结束，退出代码为 0

```