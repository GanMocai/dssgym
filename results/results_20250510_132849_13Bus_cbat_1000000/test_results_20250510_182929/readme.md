

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
已从D:\LENOVO\Documents\Python\ML\powergym\results_20250510_132849_13Bus_cbat_1000000\model\ppo_model加载模型
BatteryStationManager已重置
智能体的动作为: [ 1.         -1.         -1.         -0.15226293 -1.         -0.
 -0.70690495 -0.05994583 -0.79541487 -0.07349743 -1.        ]
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
智能体的动作为: [ 1.         -1.         -1.         -0.15755445 -1.         -0.
 -0.7553291  -0.11717629 -0.8053698  -0.11567235 -1.        ]
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=18.90653371810913。
功率需求: 60.00 kW, 充电桩功率: 18.91 kW, 最终充电功率: 18.91 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=90.639488697052。
功率需求: 100.00 kW, 充电桩功率: 90.64 kW, 最终充电功率: 90.64 kW。
初次设置charger_power=14.061155319213867。
功率需求: 80.00 kW, 充电桩功率: 14.06 kW, 最终充电功率: 14.06 kW。
初次设置charger_power=96.64437532424927。
功率需求: 96.00 kW, 充电桩功率: 96.64 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=13.880681991577148。
功率需求: 60.00 kW, 充电桩功率: 13.88 kW, 最终充电功率: 13.88 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -60.0, -19.721046310731793
已在 set_all_batteries_before_solve 中设置 batt_ev_030 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 18.90653371810913, -3.8391354140308778
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 90.639488697052, -18.405133175374335
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 14.061155319213867, -2.8552393660862703
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 13.880681991577148, -2.8185926938961963
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.18 更新为 0.51。
SOC从 0.32 更新为 0.55。
SOC从 0.18 更新为 0.25。
SOC从 0.12 更新为 0.36。
SOC从 0.22 更新为 0.22。
SOC从 0.28 更新为 0.53。
SOC从 0.12 更新为 0.19。
SOC从 0.38 更新为 0.64。
SOC从 0.22 更新为 0.30。
SOC从 0.12 更新为 0.54。
已断开电池: batt_ev_030
时间步 2 执行前: 电池 batt_ev_030 已充满 (SOC: 51.3%)，离开
奖励各项的值：powerloss=-0.1488608115208018, voltage=-0.24239618550281117, ctrl=-0.0, connection=0.08, completion=20.0, energy=10.0, transformer=0.
已连接电池 batt_ev_224, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
时间步 2 执行前: 排队电池 batt_ev_224 已接入
智能体的动作为: [ 1.         -0.39348575 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=47.21829056739807。
功率需求: 60.00 kW, 充电桩功率: 47.22 kW, 最终充电功率: 47.22 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=18.90653371810913，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 18.91 kW, 最终充电功率: 18.91 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
self.charger_power=0.0 改为 120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=90.639488697052，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 90.64 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=14.061155319213867，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 14.06 kW, 最终充电功率: 14.06 kW。
已有历史设置self.charger_power=96.64437532424927，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 96.64 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=13.880681991577148，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 13.88 kW, 最终充电功率: 13.88 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 18.90653371810913, -3.8391354140308778
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 14.061155319213867, -2.8552393660862703
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 13.880681991577148, -2.8185926938961963
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 47.21829056739807, -9.588082840043082
SOC从 0.28 更新为 0.54。
SOC从 0.55 更新为 0.73。
SOC从 0.25 更新为 0.32。
SOC从 0.36 更新为 0.56。
SOC从 0.22 更新为 0.51。
SOC从 0.53 更新为 0.69。
SOC从 0.19 更新为 0.26。
SOC从 0.64 更新为 0.83。
SOC从 0.30 更新为 0.37。
SOC从 0.54 更新为 0.79。
已断开电池: batt_ev_064
时间步 3 执行前: 电池 batt_ev_064 已充满 (SOC: 55.5%)，离开
已断开电池: batt_ev_039
时间步 3: 电池 batt_ev_039 已离开，当前SOC: 25.5%，能量满足率: 15.7%
已断开电池: batt_ev_242
时间步 3 执行前: 电池 batt_ev_242 已充满 (SOC: 83.2%)，离开
已断开电池: batt_ev_045
时间步 3: 电池 batt_ev_045 已离开，当前SOC: 78.7%，能量满足率: 77.5%
奖励各项的值：powerloss=-0.1393567195607571, voltage=-0.25819420121706127, ctrl=-0.0, connection=0.4, completion=12.0, energy=7.865235539654146, transformer=0.
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
智能体的动作为: [ 1.         -0.37129533 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=47.21829056739807，设置charger_power=44.555439949035645失败。
功率需求: 36.00 kW, 充电桩功率: 47.22 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=75.68失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=18.90653371810913，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 18.91 kW, 最终充电功率: 18.91 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=99.12失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=90.639488697052，设置charger_power=114.32失败。
功率需求: 60.00 kW, 充电桩功率: 90.64 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=71.44。
功率需求: 36.00 kW, 充电桩功率: 71.44 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=13.880681991577148，设置charger_power=112.64失败。
功率需求: 48.00 kW, 充电桩功率: 13.88 kW, 最终充电功率: 13.88 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 18.90653371810913, -3.8391354140308778
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 13.880681991577148, -2.8185926938961963
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_235 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.54 更新为 0.74。
SOC从 0.73 更新为 0.84。
SOC从 0.32 更新为 0.39。
SOC从 0.12 更新为 0.52。
SOC从 0.51 更新为 0.69。
SOC从 0.69 更新为 0.85。
SOC从 0.28 更新为 0.53。
SOC从 0.62 更新为 0.81。
SOC从 0.37 更新为 0.45。
SOC从 0.32 更新为 0.52。
已断开电池: batt_ev_126
时间步 4: 电池 batt_ev_126 已离开，当前SOC: 38.9%，能量满足率: 26.1%
已断开电池: batt_ev_239
时间步 4 执行前: 电池 batt_ev_239 已充满 (SOC: 85.2%)，离开
奖励各项的值：powerloss=-0.1357399988201398, voltage=-0.29999038967406744, ctrl=-0.0, connection=0.56, completion=11.428571428571427, energy=7.419233368660524, transformer=0.
已连接电池 batt_ev_062, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_062 已接入
时间步 4: 电池 batt_ev_200 已错过离开时间，无法接入
时间步 4: 电池 batt_ev_163 已错过离开时间，无法接入
已连接电池 batt_ev_014, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_014 已接入
智能体的动作为: [ 1.        -0.3472642 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=47.21829056739807，设置charger_power=41.671704053878784失败。
功率需求: 24.00 kW, 充电桩功率: 47.22 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=43.68000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=96.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=63.120000000000005失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=112.8失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=71.44，设置charger_power=35.44失败。
功率需求: 24.00 kW, 充电桩功率: 71.44 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=13.880681991577148，设置charger_power=98.76失败。
功率需求: 48.00 kW, 充电桩功率: 13.88 kW, 最终充电功率: 13.88 kW。
已有历史设置self.charger_power=120.0，设置charger_power=117.92失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 13.880681991577148, -2.8185926938961963
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_235 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_062 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_014 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.74 更新为 0.88。
SOC从 0.84 更新为 0.96。
SOC从 0.57 更新为 0.80。
SOC从 0.52 更新为 0.76。
SOC从 0.69 更新为 0.87。
SOC从 0.28 更新为 0.53。
SOC从 0.53 更新为 0.68。
SOC从 0.81 更新为 0.94。
SOC从 0.45 更新为 0.53。
SOC从 0.52 更新为 0.66。
已断开电池: batt_ev_123
时间步 5: 电池 batt_ev_123 已离开，当前SOC: 86.7%，能量满足率: 85.1%
已断开电池: batt_ev_042
时间步 5: 电池 batt_ev_042 已离开，当前SOC: 52.8%，能量满足率: 40.6%
已断开电池: batt_ev_076
时间步 5: 电池 batt_ev_076 已离开，当前SOC: 68.0%，能量满足率: 57.1%
已断开电池: batt_ev_235
时间步 5 执行前: 电池 batt_ev_235 已充满 (SOC: 93.9%)，离开
已断开电池: batt_ev_062
时间步 5: 电池 batt_ev_062 已离开，当前SOC: 80.4%，能量满足率: 57.0%
奖励各项的值：powerloss=-0.13626149475001803, voltage=-0.31534292415990484, ctrl=-0.0, connection=0.96, completion=8.333333333333334, energy=7.160245514444253, transformer=0.
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
智能体的动作为: [ 1.         -0.28536922 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=47.21829056739807，设置charger_power=22.360000000000014失败。
功率需求: 15.00 kW, 充电桩功率: 47.22 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=11.680000000000007失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=48.0失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=81.91999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
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
SOC从 0.88 更新为 0.96。
SOC从 0.96 更新为 1.00。
SOC从 0.08 更新为 0.37。
SOC从 0.76 更新为 0.92。
SOC从 0.57 更新为 0.80。
SOC从 0.53 更新为 0.69。
SOC从 0.08 更新为 0.40。
SOC从 0.32 更新为 0.52。
SOC从 0.22 更新为 0.47。
SOC从 0.66 更新为 0.81。
已断开电池: batt_ev_149
时间步 6 执行前: 电池 batt_ev_149 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_014
时间步 6: 电池 batt_ev_014 已离开，当前SOC: 68.5%，能量满足率: 67.5%
已断开电池: batt_ev_231
时间步 6: 电池 batt_ev_231 已离开，当前SOC: 40.3%，能量满足率: 35.8%
已断开电池: batt_ev_248
时间步 6: 电池 batt_ev_248 已离开，当前SOC: 46.6%，能量满足率: 32.4%
奖励各项的值：powerloss=-0.14827803891529526, voltage=-0.3445402719648061, ctrl=-0.0, connection=1.28, completion=7.5, energy=6.843361143902591, transformer=0.
已连接电池 batt_ev_240, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_240 已接入
时间步 6: 电池 batt_ev_119 已错过离开时间，无法接入
已连接电池 batt_ev_158, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_158 已接入
已连接电池 batt_ev_157, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_157 已接入
已连接电池 batt_ev_096, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_096 已接入
智能体的动作为: [ 1.         -0.26850164 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=47.21829056739807，设置charger_power=7.360000000000014失败。
功率需求: 15.00 kW, 充电桩功率: 47.22 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=16.0失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=60.44失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=115.2失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=45.91999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_157 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.96 更新为 1.00。
SOC从 0.48 更新为 0.82。
SOC从 0.37 更新为 0.61。
SOC从 0.92 更新为 1.00。
SOC从 0.80 更新为 0.96。
SOC从 0.28 更新为 0.60。
SOC从 0.12 更新为 0.39。
SOC从 0.52 更新为 0.67。
SOC从 0.18 更新为 0.47。
SOC从 0.81 更新为 0.91。
已断开电池: batt_ev_224
时间步 7 执行前: 电池 batt_ev_224 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_081
时间步 7 执行前: 电池 batt_ev_081 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_018
时间步 7: 电池 batt_ev_018 已离开，当前SOC: 91.0%，能量满足率: 89.4%
已断开电池: batt_ev_036
时间步 7: 电池 batt_ev_036 已离开，当前SOC: 96.0%，能量满足率: 95.0%
已断开电池: batt_ev_157
时间步 7: 电池 batt_ev_157 已离开，当前SOC: 39.3%，能量满足率: 31.7%
奖励各项的值：powerloss=-0.163115239239808, voltage=-0.383127045851579, ctrl=-0.0, connection=1.68, completion=7.619047619047619, energy=7.195695042075895, transformer=0.
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
智能体的动作为: [ 1.         -0.25499958 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=30.5999493598938。
功率需求: 96.00 kW, 充电桩功率: 30.60 kW, 最终充电功率: 30.60 kW。
已有历史设置self.charger_power=120.0，设置charger_power=49.599999999999994失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=79.68失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=75.36失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=79.19999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=110.56失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_106 充电的有无功功率为 30.5999493598938, -6.2135847324883855
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_216 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 96.0, -19.493631420864393
SOC从 0.32 更新为 0.40。
SOC从 0.82 更新为 0.99。
SOC从 0.61 更新为 0.79。
SOC从 0.28 更新为 0.54。
SOC从 0.42 更新为 0.65。
SOC从 0.60 更新为 0.79。
SOC从 0.18 更新为 0.52。
SOC从 0.67 更新为 0.82。
SOC从 0.47 更新为 0.70。
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
时间步 8: 电池 batt_ev_106 已离开，当前SOC: 40.3%，能量满足率: 12.6%
已断开电池: batt_ev_216
时间步 8: 电池 batt_ev_216 已离开，当前SOC: 64.6%，能量满足率: 40.4%
不太安全
奖励各项的值：powerloss=-0.18646988471959294, voltage=-0.3867001765863409, ctrl=-0.0, connection=2.16, completion=7.4074074074074066, energy=7.104870326733865, transformer=-0.539745900746749.
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
智能体的动作为: [ 1.        -0.2526471 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=30.317652225494385。
功率需求: 64.00 kW, 充电桩功率: 30.32 kW, 最终充电功率: 30.32 kW。
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
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=62.56失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=112.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_128 充电的有无功功率为 30.317652225494385, -6.156261854476424
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_173 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_132 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.42 更新为 0.51。
SOC从 0.72 更新为 0.86。
SOC从 0.22 更新为 0.48。
SOC从 0.54 更新为 0.70。
SOC从 0.57 更新为 0.80。
SOC从 0.18 更新为 0.46。
SOC从 0.52 更新为 0.73。
SOC从 0.08 更新为 0.40。
SOC从 0.70 更新为 0.87。
SOC从 0.72 更新为 0.84。
已断开电池: batt_ev_055
时间步 9: 电池 batt_ev_055 已离开，当前SOC: 70.1%，能量满足率: 60.2%
已断开电池: batt_ev_247
时间步 9: 电池 batt_ev_247 已离开，当前SOC: 73.2%，能量满足率: 69.0%
已断开电池: batt_ev_090
时间步 9: 电池 batt_ev_090 已离开，当前SOC: 84.0%，能量满足率: 72.0%
已断开电池: batt_ev_128
时间步 9: 电池 batt_ev_128 已离开，当前SOC: 51.5%，能量满足率: 16.9%
已断开电池: batt_ev_173
时间步 9: 电池 batt_ev_173 已离开，当前SOC: 80.1%，能量满足率: 56.3%
已断开电池: batt_ev_132
时间步 9: 电池 batt_ev_132 已离开，当前SOC: 46.3%，能量满足率: 35.4%
不太安全
奖励各项的值：powerloss=-0.20474878162969723, voltage=-0.4752031210824148, ctrl=-0.0, connection=2.64, completion=6.0606060606060606, energy=6.751554730252968, transformer=-1.342595471662844.
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
智能体的动作为: [ 1.         -0.25163868 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=30.19664168357849。
功率需求: 100.00 kW, 充电桩功率: 30.20 kW, 最终充电功率: 30.20 kW。
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
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=26.560000000000002失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_191 充电的有无功功率为 30.19664168357849, -6.1316896159123875
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_161 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.18 更新为 0.27。
SOC从 0.86 更新为 0.95。
SOC从 0.48 更新为 0.69。
SOC从 0.22 更新为 0.52。
SOC从 0.22 更新为 0.50。
SOC从 0.82 更新为 0.99。
SOC从 0.28 更新为 0.57。
SOC从 0.40 更新为 0.66。
SOC从 0.87 更新为 0.94。
SOC从 0.38 更新为 0.62。
已断开电池: batt_ev_096
时间步 10 执行前: 电池 batt_ev_096 已充满 (SOC: 94.4%)，离开
已断开电池: batt_ev_220
时间步 10 执行前: 电池 batt_ev_220 已充满 (SOC: 94.9%)，离开
已断开电池: batt_ev_150
时间步 10: 电池 batt_ev_150 已离开，当前SOC: 65.7%，能量满足率: 64.1%
已断开电池: batt_ev_191
时间步 10: 电池 batt_ev_191 已离开，当前SOC: 26.7%，能量满足率: 10.8%
已断开电池: batt_ev_161
时间步 10: 电池 batt_ev_161 已离开，当前SOC: 49.8%，能量满足率: 36.5%
不太安全
奖励各项的值：powerloss=-0.2181754756573242, voltage=-0.4575156632994748, ctrl=-0.0, connection=3.04, completion=6.315789473684211, energy=6.682929036415284, transformer=-1.7956138632327339.
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
智能体的动作为: [ 1.         -0.25146034 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=30.175241231918335。
功率需求: 80.00 kW, 充电桩功率: 30.18 kW, 最终充电功率: 30.18 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 30.175241231918335, -6.127344068861314
已在 set_all_batteries_before_solve 中设置 batt_ev_008 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_085 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.18 更新为 0.27。
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
奖励各项的值：powerloss=-0.22268278970724958, voltage=-0.4918933868314723, ctrl=-0.0, connection=3.44, completion=6.976744186046512, energy=6.942928379692248, transformer=0.
时间步 11: 电池 batt_ev_222 已错过离开时间，无法接入
已连接电池 batt_ev_114, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_114 已接入
已连接电池 batt_ev_009, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_009 已接入
已连接电池 batt_ev_113, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_065, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_203, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [ 1.         -0.25175658 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=30.175241231918335，设置charger_power=30.210789442062378失败。
功率需求: 80.00 kW, 充电桩功率: 30.18 kW, 最终充电功率: 30.18 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 30.175241231918335, -6.127344068861314
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.27 更新为 0.37。
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
奖励各项的值：powerloss=-0.22879032845203978, voltage=-0.5109400640208839, ctrl=-0.0, connection=3.6, completion=6.666666666666666, energy=6.98727390540124, transformer=0.
已连接电池 batt_ev_011, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 12 执行前: 排队电池 batt_ev_011 已接入
已连接电池 batt_ev_041, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [ 1.         -0.25152236 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=30.175241231918335，设置charger_power=30.18268346786499失败。
功率需求: 64.00 kW, 充电桩功率: 30.18 kW, 最终充电功率: 30.18 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 30.175241231918335, -6.127344068861314
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_011 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.37 更新为 0.46。
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
时间步 13: 电池 batt_ev_000 已离开，当前SOC: 46.3%，能量满足率: 35.3%
已断开电池: batt_ev_162
时间步 13: 电池 batt_ev_162 已离开，当前SOC: 78.8%，能量满足率: 72.5%
已断开电池: batt_ev_114
时间步 13 执行前: 电池 batt_ev_114 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_011
时间步 13: 电池 batt_ev_011 已离开，当前SOC: 54.9%，能量满足率: 34.6%
奖励各项的值：powerloss=-0.22830895829923206, voltage=-0.5490889861518444, ctrl=-0.0, connection=4.0, completion=6.800000000000001, energy=6.973553029180129, transformer=0.
已连接电池 batt_ev_232, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_232 已接入
已连接电池 batt_ev_237, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_237 已接入
已连接电池 batt_ev_052, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_052 已接入
已连接电池 batt_ev_206, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 62kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_206 已接入
已连接电池 batt_ev_172, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
智能体的动作为: [ 1.         -0.44748297 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=53.697956800460815。
功率需求: 48.00 kW, 充电桩功率: 53.70 kW, 最终充电功率: 48.00 kW。
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
奖励各项的值：powerloss=-0.2217292045483109, voltage=-0.5429938393451295, ctrl=-0.0, connection=4.32, completion=6.666666666666666, energy=7.075837610966249, transformer=0.
已连接电池 batt_ev_229, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_229 已接入
已连接电池 batt_ev_164, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_164 已接入
已连接电池 batt_ev_134, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_214, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 80kWh，并创BMS。
智能体的动作为: [ 1.        -0.4976273 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=53.697956800460815，设置charger_power=59.71527457237244失败。
功率需求: 36.00 kW, 充电桩功率: 53.70 kW, 最终充电功率: 36.00 kW。
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
奖励各项的值：powerloss=-0.2227453232181948, voltage=-0.5377245820947407, ctrl=-0.0, connection=4.5600000000000005, completion=6.666666666666666, energy=7.139401154285414, transformer=0.
已连接电池 batt_ev_143, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_143 已接入
已连接电池 batt_ev_245, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_245 已接入
已连接电池 batt_ev_098, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_098 已接入
智能体的动作为: [ 1.         -0.49526337 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=59.4316041469574。
功率需求: 64.00 kW, 充电桩功率: 59.43 kW, 最终充电功率: 59.43 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 59.4316041469574, -12.068101937411495
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.48 更新为 0.73。
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
奖励各项的值：powerloss=-0.21818432105424784, voltage=-0.5304386961643015, ctrl=-0.0, connection=4.8, completion=7.0, energy=7.278807908165347, transformer=0.
已连接电池 batt_ev_190, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 63kWh，并创BMS。
时间步 16 执行前: 排队电池 batt_ev_190 已接入
已连接电池 batt_ev_069, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 56kWh，并创BMS。
已连接电池 batt_ev_071, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
智能体的动作为: [ 1.         -0.57978773 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=59.4316041469574，设置charger_power=63.28失败。
功率需求: 32.00 kW, 充电桩功率: 59.43 kW, 最终充电功率: 32.00 kW。
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
SOC从 0.73 更新为 0.87。
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
奖励各项的值：powerloss=-0.22533007467855679, voltage=-0.5083343701582343, ctrl=-0.0, connection=5.04, completion=6.984126984126984, energy=7.318952457030971, transformer=0.
智能体的动作为: [ 1.         -0.51164293 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=59.4316041469574，设置charger_power=31.28失败。
功率需求: 20.00 kW, 充电桩功率: 59.43 kW, 最终充电功率: 20.00 kW。
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
SOC从 0.87 更新为 0.95。
SOC从 0.58 更新为 0.81。
SOC从 0.83 更新为 0.93。
SOC从 0.82 更新为 0.93。
SOC从 0.89 更新为 0.96。
SOC从 0.59 更新为 0.76。
SOC从 0.63 更新为 0.78。
已断开电池: batt_ev_229
时间步 18 执行前: 电池 batt_ev_229 已充满 (SOC: 93.0%)，离开
已断开电池: batt_ev_143
时间步 18: 电池 batt_ev_143 已离开，当前SOC: 95.2%，能量满足率: 94.4%
已断开电池: batt_ev_098
时间步 18: 电池 batt_ev_098 已离开，当前SOC: 93.4%，能量满足率: 91.8%
已断开电池: batt_ev_071
时间步 18 执行前: 电池 batt_ev_071 已充满 (SOC: 78.5%)，离开
奖励各项的值：powerloss=-0.2205757571794338, voltage=-0.3412579546826322, ctrl=-0.0, connection=5.36, completion=7.164179104477611, energy=7.458533523267895, transformer=0.
已连接电池 batt_ev_083, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_174, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_167, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [ 1.         -0.70511115 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
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
奖励各项的值：powerloss=-0.21482539389588196, voltage=-0.21466135235883366, ctrl=-0.0, connection=5.6000000000000005, completion=7.714285714285714, energy=7.567453515127843, transformer=0.
已连接电池 batt_ev_115, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
已连接电池 batt_ev_181, 初始SOC: 56.99999999999999%, 最大功率: 80kW, 电池容量: 69kWh，并创BMS。
已连接电池 batt_ev_182, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 95kWh，并创BMS。
智能体的动作为: [ 1.        -0.7050141 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=84.60169315338135。
功率需求: 60.00 kW, 充电桩功率: 84.60 kW, 最终充电功率: 60.00 kW。
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
奖励各项的值：powerloss=-0.21101247143184587, voltage=-0.15890266116693752, ctrl=-0.0, connection=5.6000000000000005, completion=7.714285714285714, energy=7.567453515127843, transformer=0.
已连接电池 batt_ev_037, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_138, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
已连接电池 batt_ev_095, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
智能体的动作为: [ 1.        -0.6997216 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=84.60169315338135，设置charger_power=83.96658897399902失败。
功率需求: 48.00 kW, 充电桩功率: 84.60 kW, 最终充电功率: 48.00 kW。
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
奖励各项的值：powerloss=-0.21219053025475168, voltage=-0.11501300343192744, ctrl=-0.0, connection=5.76, completion=8.055555555555555, energy=7.635024250818736, transformer=0.
已连接电池 batt_ev_197, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 75kWh，并创BMS。
已连接电池 batt_ev_026, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 102kWh，并创BMS。
已连接电池 batt_ev_212, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [ 1.         -0.65489423 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=84.60169315338135，设置charger_power=53.91999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 84.60 kW, 最终充电功率: 24.00 kW。
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
奖励各项的值：powerloss=-0.2037772364971311, voltage=-0.10166206113458864, ctrl=-0.0, connection=6.16, completion=8.051948051948052, energy=7.771385829442061, transformer=0.
已连接电池 batt_ev_010, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 71kWh，并创BMS。
时间步 22 执行前: 排队电池 batt_ev_010 已接入
已连接电池 batt_ev_241, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 68kWh，并创BMS。
已连接电池 batt_ev_084, 初始SOC: 78.0%, 最大功率: 100kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_038, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
已连接电池 batt_ev_040, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
智能体的动作为: [ 1.        -0.6252178 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=75.02613544464111。
功率需求: 96.00 kW, 充电桩功率: 75.03 kW, 最终充电功率: 75.03 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 75.02613544464111, -15.234706575934204
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_084 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.48 更新为 0.74。
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
奖励各项的值：powerloss=-0.18847382321271502, voltage=-0.11655470169603221, ctrl=-0.0, connection=6.24, completion=7.948717948717948, energy=7.7560981568648675, transformer=0.
已连接电池 batt_ev_046, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_046 已接入
智能体的动作为: [ 1.        -0.5836413 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=75.02613544464111，设置charger_power=70.03695487976074失败。
功率需求: 48.00 kW, 充电桩功率: 75.03 kW, 最终充电功率: 48.00 kW。
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
SOC从 0.74 更新为 0.91。
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
时间步 24 执行前: 电池 batt_ev_010 已充满 (SOC: 91.3%)，离开
已断开电池: batt_ev_084
时间步 24 执行前: 电池 batt_ev_084 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_038
时间步 24: 电池 batt_ev_038 已离开，当前SOC: 90.3%，能量满足率: 86.2%
奖励各项的值：powerloss=-0.16228738375847385, voltage=-0.18544574199059083, ctrl=-0.0, connection=6.640000000000001, completion=7.951807228915663, energy=7.860588165862437, transformer=0.
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
智能体的动作为: [ 1.         -0.70530546 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=84.6366548538208。
功率需求: 60.00 kW, 充电桩功率: 84.64 kW, 最终充电功率: 60.00 kW。
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
奖励各项的值：powerloss=-0.14597229058950417, voltage=-0.24431050290268708, ctrl=-0.0, connection=7.2, completion=7.777777777777778, energy=7.862403693250155, transformer=0.
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
智能体的动作为: [ 1.        -0.7042767 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=84.51320171356201。
功率需求: 80.00 kW, 充电桩功率: 84.51 kW, 最终充电功率: 80.00 kW。
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
奖励各项的值：powerloss=-0.15313230314115353, voltage=-0.2683655318490552, ctrl=-0.0, connection=7.36, completion=8.043478260869566, energy=7.908873178179499, transformer=-2.29611879831603.
已连接电池 batt_ev_031, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_057, 初始SOC: 8.0%, 最大功率: 80kW, 电池容量: 73kWh，并创BMS。
已连接电池 batt_ev_111, 初始SOC: 68.0%, 最大功率: 100kW, 电池容量: 83kWh，并创BMS。
智能体的动作为: [ 1.        -0.5077475 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=84.51320171356201，设置charger_power=60.929696559906006失败。
功率需求: 48.00 kW, 充电桩功率: 84.51 kW, 最终充电功率: 48.00 kW。
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
奖励各项的值：powerloss=-0.14226507653261117, voltage=-0.29817798696087916, ctrl=-0.0, connection=7.6000000000000005, completion=8.210526315789474, energy=7.965886205635485, transformer=0.
已连接电池 batt_ev_006, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_006 已接入
已连接电池 batt_ev_225, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 94kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_225 已接入
已连接电池 batt_ev_054, 初始SOC: 82.0%, 最大功率: 120kW, 电池容量: 85kWh，并创BMS。
智能体的动作为: [ 1.         -0.67085266 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=84.51320171356201，设置charger_power=80.5023193359375失败。
功率需求: 48.00 kW, 充电桩功率: 84.51 kW, 最终充电功率: 48.00 kW。
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
奖励各项的值：powerloss=-0.133287339913423, voltage=-0.27988724920259056, ctrl=-0.0, connection=7.84, completion=7.959183673469388, energy=7.9746258196134745, transformer=0.
已连接电池 batt_ev_129, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 94kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_129 已接入
已连接电池 batt_ev_088, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 50kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_088 已接入
已连接电池 batt_ev_007, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 84kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_007 已接入
智能体的动作为: [ 1.         -0.70531726 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=84.51320171356201，设置charger_power=36.16失败。
功率需求: 20.00 kW, 充电桩功率: 84.51 kW, 最终充电功率: 20.00 kW。
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
奖励各项的值：powerloss=-0.1367279194754694, voltage=-0.2832393985552373, ctrl=-0.0, connection=8.4, completion=8.0, energy=8.059998065690994, transformer=0.
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
智能体的动作为: [ 1.        -0.7053243 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=84.63891506195068。
功率需求: 96.00 kW, 充电桩功率: 84.64 kW, 最终充电功率: 84.64 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 84.63891506195068, -17.18666472999494
已在 set_all_batteries_before_solve 中设置 batt_ev_147 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.32 更新为 0.53。
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
奖励各项的值：powerloss=-0.16104367271166198, voltage=-0.30682939697010303, ctrl=-0.0, connection=8.56, completion=7.850467289719626, energy=8.03400644238138, transformer=-3.0931469358429013.
时间步 30: 电池 batt_ev_021 已错过离开时间，无法接入
已连接电池 batt_ev_209, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_209 已接入
已连接电池 batt_ev_178, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 93kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_178 已接入
智能体的动作为: [ 1.        -0.5897225 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=84.63891506195068，设置charger_power=70.76670169830322失败。
功率需求: 72.00 kW, 充电桩功率: 84.64 kW, 最终充电功率: 72.00 kW。
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
SOC从 0.53 更新为 0.71。
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
时间步 31: 电池 batt_ev_142 已离开，当前SOC: 71.2%，能量满足率: 65.3%
已断开电池: batt_ev_211
时间步 31 执行前: 电池 batt_ev_211 已充满 (SOC: 90.3%)，离开
奖励各项的值：powerloss=-0.16869341513808336, voltage=-0.2577461991513763, ctrl=-0.0, connection=8.72, completion=7.889908256880735, energy=8.038214275242883, transformer=0.
已连接电池 batt_ev_110, 初始SOC: 22.0%, 最大功率: 100kW, 电池容量: 65kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_110 已接入
已连接电池 batt_ev_112, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 71kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_112 已接入
智能体的动作为: [ 1.         -0.70517766 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=84.62131977081299。
功率需求: 100.00 kW, 充电桩功率: 84.62 kW, 最终充电功率: 84.62 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_110 充电的有无功功率为 84.62131977081299, -17.18309185374306
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.22 更新为 0.55。
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
时间步 32: 电池 batt_ev_110 已离开，当前SOC: 54.5%，能量满足率: 54.2%
奖励各项的值：powerloss=-0.18493727537839397, voltage=-0.24086367899144312, ctrl=-0.0, connection=9.28, completion=7.931034482758621, energy=8.05816625621121, transformer=0.
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
智能体的动作为: [ 1.         -0.70532584 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=84.63910102844238。
功率需求: 100.00 kW, 充电桩功率: 84.64 kW, 最终充电功率: 84.64 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_223 充电的有无功功率为 84.63910102844238, -17.18670249210167
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_198 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.22 更新为 0.48。
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
时间步 33: 电池 batt_ev_223 已离开，当前SOC: 48.1%，能量满足率: 52.2%
已断开电池: batt_ev_198
时间步 33: 电池 batt_ev_198 已离开，当前SOC: 36.4%，能量满足率: 33.8%
奖励各项的值：powerloss=-0.20376343289515372, voltage=-0.31209810422587747, ctrl=-0.0, connection=9.68, completion=7.603305785123967, energy=7.992280396123764, transformer=0.
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
智能体的动作为: [ 1.        -0.7053263 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=84.63915824890137。
功率需求: 48.00 kW, 充电桩功率: 84.64 kW, 最终充电功率: 48.00 kW。
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
奖励各项的值：powerloss=-0.2169248552809035, voltage=-0.33157807576227105, ctrl=-0.0, connection=10.16, completion=7.4015748031496065, energy=7.960160613442101, transformer=0.
已连接电池 batt_ev_049, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
已连接电池 batt_ev_023, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [ 1.        -0.7053132 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=84.63915824890137，设置charger_power=84.6375846862793失败。
功率需求: 48.00 kW, 充电桩功率: 84.64 kW, 最终充电功率: 48.00 kW。
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
奖励各项的值：powerloss=-0.2146105830786368, voltage=-0.30218211482822, ctrl=-0.0, connection=10.4, completion=7.384615384615385, energy=7.953291041885317, transformer=0.
已连接电池 batt_ev_121, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [ 1.        -0.6737331 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -0.9927838 -1.       ]
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
奖励各项的值：powerloss=-0.2143711802209658, voltage=-0.3841076976691449, ctrl=-0.0, connection=10.64, completion=7.518796992481203, energy=7.969408014863335, transformer=0.
智能体的动作为: [ 0.18143761 -0.48817906 -1.         -1.         -1.         -1.
 -0.9394353  -1.         -0.79353255 -0.69206464 -0.5342232 ]
已有历史设置self.charger_power=120.0，设置charger_power=58.72失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 32.0, -6.497877140288132
SOC从 0.75 更新为 0.89。
奖励各项的值：powerloss=-0.211431535722439, voltage=-0.417962319379237, ctrl=-0.0, connection=10.64, completion=7.518796992481203, energy=7.969408014863335, transformer=0.
已连接电池 batt_ev_015, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
已连接电池 batt_ev_201, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.85827816 -0.22490114 -0.74869806 -1.
 -0.17218441 -0.74153376 -0.28228828 -0.81507903 -0.        ]
已有历史设置self.charger_power=120.0，设置charger_power=20.662128925323486失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=88.98405075073242。
功率需求: 36.00 kW, 充电桩功率: 88.98 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=33.87459397315979。
功率需求: 120.00 kW, 充电桩功率: 33.87 kW, 最终充电功率: 33.87 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 33.87459397315979, -6.878529681710535
SOC从 0.89 更新为 0.97。
SOC从 0.52 更新为 0.67。
SOC从 0.18 更新为 0.26。
已断开电池: batt_ev_121
时间步 38: 电池 batt_ev_121 已离开，当前SOC: 97.2%，能量满足率: 98.3%
奖励各项的值：powerloss=-0.2193783662490285, voltage=-0.3832588147599991, ctrl=-0.0, connection=10.72, completion=7.462686567164179, energy=7.983296824264179, transformer=0.
已连接电池 batt_ev_080, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_204, 初始SOC: 2.0%, 最大功率: 80kW, 电池容量: 81kWh，并创BMS。
智能体的动作为: [-1.         -0.14855906 -1.         -0.9285381  -0.7632584  -1.
 -0.6765038  -1.         -0.5171692  -0.84992033 -0.1668704 ]
初次设置charger_power=17.82708764076233。
功率需求: 80.00 kW, 充电桩功率: 17.83 kW, 最终充电功率: 17.83 kW。
已有历史设置self.charger_power=88.98405075073242，设置charger_power=81.12失败。
功率需求: 36.00 kW, 充电桩功率: 88.98 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=33.87459397315979，设置charger_power=62.060301303863525失败。
功率需求: 120.00 kW, 充电桩功率: 33.87 kW, 最终充电功率: 33.87 kW。
初次设置charger_power=20.024448037147522。
功率需求: 36.00 kW, 充电桩功率: 20.02 kW, 最终充电功率: 20.02 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 33.87459397315979, -6.878529681710535
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 20.024448037147522, -4.066137598358388
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 17.82708764076233, -3.6199445393382064
SOC从 0.02 更新为 0.08。
SOC从 0.67 更新为 0.82。
SOC从 0.26 更新为 0.34。
SOC从 0.57 更新为 0.66。
奖励各项的值：powerloss=-0.21922227410727224, voltage=-0.38287873608821243, ctrl=-0.0, connection=10.72, completion=7.462686567164179, energy=7.983296824264179, transformer=0.
已连接电池 batt_ev_183, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 71kWh，并创BMS。
已连接电池 batt_ev_230, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [ 0.02165353 -0.402187   -1.         -1.         -1.         -1.
 -0.88777876 -1.         -0.74739444 -0.70467573 -0.48015612]
已有历史设置self.charger_power=17.82708764076233，设置charger_power=48.26243877410889失败。
功率需求: 80.00 kW, 充电桩功率: 17.83 kW, 最终充电功率: 17.83 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=88.98405075073242，设置charger_power=45.120000000000005失败。
功率需求: 24.00 kW, 充电桩功率: 88.98 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=33.87459397315979，设置charger_power=89.68733310699463失败。
功率需求: 96.00 kW, 充电桩功率: 33.87 kW, 最终充电功率: 33.87 kW。
初次设置charger_power=84.56108808517456。
功率需求: 36.00 kW, 充电桩功率: 84.56 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=20.024448037147522，设置charger_power=57.61873483657837失败。
功率需求: 36.00 kW, 充电桩功率: 20.02 kW, 最终充电功率: 20.02 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -2.165353298187256, -0.7117172112107784
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 33.87459397315979, -6.878529681710535
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 20.024448037147522, -4.066137598358388
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 17.82708764076233, -3.6199445393382064
已在 set_all_batteries_before_solve 中设置 batt_ev_183 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.08 更新为 0.13。
SOC从 0.38 更新为 0.66。
SOC从 0.82 更新为 0.91。
SOC从 0.34 更新为 0.43。
SOC从 0.52 更新为 0.66。
SOC从 0.66 更新为 0.76。
已断开电池: batt_ev_183
时间步 40 执行前: 电池 batt_ev_183 已充满 (SOC: 66.2%)，离开
奖励各项的值：powerloss=-0.21180692251161964, voltage=-0.47377318278199354, ctrl=-0.0, connection=10.8, completion=7.555555555555555, energy=7.998235366306666, transformer=0.
智能体的动作为: [ 1.         -0.78566396 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -0.88674253 -0.97362685]
已有历史设置self.charger_power=17.82708764076233，设置charger_power=94.27967548370361失败。
功率需求: 80.00 kW, 充电桩功率: 17.83 kW, 最终充电功率: 17.83 kW。
已有历史设置self.charger_power=88.98405075073242，设置charger_power=21.120000000000005失败。
功率需求: 15.00 kW, 充电桩功率: 88.98 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=33.87459397315979，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 33.87 kW, 最终充电功率: 33.87 kW。
已有历史设置self.charger_power=84.56108808517456，设置charger_power=88.80000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 84.56 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=20.024448037147522，设置charger_power=52.80000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 20.02 kW, 最终充电功率: 20.02 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -100.0, -32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 33.87459397315979, -6.878529681710535
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 20.024448037147522, -4.066137598358388
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 17.82708764076233, -3.6199445393382064
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.13 更新为 0.19。
SOC从 0.91 更新为 0.97。
SOC从 0.43 更新为 0.51。
SOC从 0.66 更新为 0.80。
SOC从 0.76 更新为 0.85。
已断开电池: batt_ev_201
时间步 41: 电池 batt_ev_201 已离开，当前SOC: 50.9%，能量满足率: 47.0%
已断开电池: batt_ev_204
时间步 41: 电池 batt_ev_204 已离开，当前SOC: 18.5%，能量满足率: 17.2%
已断开电池: batt_ev_230
时间步 41: 电池 batt_ev_230 已离开，当前SOC: 79.7%，能量满足率: 60.2%
奖励各项的值：powerloss=-0.1999474437688201, voltage=-0.4420828468312843, ctrl=-0.0, connection=11.040000000000001, completion=7.391304347826086, energy=7.9145039817361695, transformer=0.
智能体的动作为: [ 0.16586924 -0.48388207 -1.         -1.         -1.         -1.
 -0.9352277  -1.         -0.7902608  -0.6895498  -0.52381766]
已有历史设置self.charger_power=88.98405075073242，设置charger_power=6.1200000000000045失败。
功率需求: 15.00 kW, 充电桩功率: 88.98 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=20.024448037147522，设置charger_power=32.75999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 20.02 kW, 最终充电功率: 20.02 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -16.586923599243164, -5.451858140887408
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 20.024448037147522, -4.066137598358388
SOC从 0.97 更新为 1.00。
SOC从 0.85 更新为 0.94。
已断开电池: batt_ev_015
时间步 42 执行前: 电池 batt_ev_015 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_080
时间步 42 执行前: 电池 batt_ev_080 已充满 (SOC: 94.1%)，离开
奖励各项的值：powerloss=-0.20435076778903855, voltage=-0.2384036382983057, ctrl=-0.0, connection=11.200000000000001, completion=7.571428571428571, energy=7.944296781997082, transformer=0.
已连接电池 batt_ev_148, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_215, 初始SOC: 62.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_210, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.87731904 -0.20440575 -0.74978966 -1.
 -0.16727287 -0.7274341  -0.29044074 -0.8542887  -0.        ]
初次设置charger_power=105.27828454971313。
功率需求: 120.00 kW, 充电桩功率: 105.28 kW, 最终充电功率: 105.28 kW。
初次设置charger_power=89.97475862503052。
功率需求: 72.00 kW, 充电桩功率: 89.97 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=94.60000000000001。
功率需求: 36.00 kW, 充电桩功率: 94.60 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 105.27828454971313, -21.377667454510316
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.28 更新为 0.57。
SOC从 0.62 更新为 0.86。
SOC从 0.57 更新为 0.73。
奖励各项的值：powerloss=-0.2167018469647618, voltage=-0.06519858834595826, ctrl=-0.0, connection=11.200000000000001, completion=7.571428571428571, energy=7.944296781997082, transformer=0.
智能体的动作为: [ 0.91911817 -0.6329211  -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -0.85923845 -0.90075666]
已有历史设置self.charger_power=105.27828454971313，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 105.28 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=89.97475862503052，设置charger_power=43.51999999999998失败。
功率需求: 30.00 kW, 充电桩功率: 89.97 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=94.60000000000001，设置charger_power=58.599999999999994失败。
功率需求: 24.00 kW, 充电桩功率: 94.60 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -91.91181659698486, -30.20995319354376
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 30.0, -6.091759819020124
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.57 更新为 0.77。
SOC从 0.86 更新为 0.96。
SOC从 0.73 更新为 0.84。
已断开电池: batt_ev_215
时间步 44 执行前: 电池 batt_ev_215 已充满 (SOC: 95.6%)，离开
已断开电池: batt_ev_210
时间步 44: 电池 batt_ev_210 已离开，当前SOC: 84.3%，能量满足率: 66.5%
奖励各项的值：powerloss=-0.19079257587158951, voltage=-0.16081002962886615, ctrl=-0.0, connection=11.36, completion=7.605633802816901, energy=7.949672071691949, transformer=0.
已连接电池 batt_ev_146, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
已连接电池 batt_ev_027, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 107kWh，并创BMS。
智能体的动作为: [ 0.16584384 -0.48362523 -1.         -1.         -1.         -1.
 -0.93515867 -1.         -0.7903173  -0.68949944 -0.52379817]
已有历史设置self.charger_power=105.27828454971313，设置charger_power=84.80000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 105.28 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=112.21904039382935。
功率需求: 64.00 kW, 充电桩功率: 112.22 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -16.584384441375732, -5.4510235600558445
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 96.0, -19.493631420864393
SOC从 0.77 更新为 0.90。
SOC从 0.32 更新为 0.54。
SOC从 0.42 更新为 0.62。
已断开电池: batt_ev_148
时间步 45 执行前: 电池 batt_ev_148 已充满 (SOC: 89.9%)，离开
奖励各项的值：powerloss=-0.1964514206918636, voltage=-0.07027172875912369, ctrl=-0.0, connection=11.44, completion=7.6923076923076925, energy=7.964010029232565, transformer=0.
已连接电池 batt_ev_135, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_127, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 88kWh，并创BMS。
已连接电池 batt_ev_165, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 105kWh，并创BMS。
智能体的动作为: [ 0.6225351  -0.51891154 -1.         -1.         -1.         -1.
 -1.         -1.         -0.98002344 -0.8152475  -0.81526095]
初次设置charger_power=62.26938486099243。
功率需求: 64.00 kW, 充电桩功率: 62.27 kW, 最终充电功率: 62.27 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=112.21904039382935，设置charger_power=119.28失败。
功率需求: 48.00 kW, 充电桩功率: 112.22 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=117.60281324386597。
功率需求: 100.00 kW, 充电桩功率: 117.60 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=97.8296971321106。
功率需求: 120.00 kW, 充电桩功率: 97.83 kW, 最终充电功率: 97.83 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -62.25351095199585, -20.461739541499316
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 62.26938486099243, -12.644337888376452
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 97.8296971321106, -19.86516726987665
SOC从 0.32 更新为 0.61。
SOC从 0.54 更新为 0.71。
SOC从 0.62 更新为 0.77。
SOC从 0.18 更新为 0.46。
SOC从 0.18 更新为 0.41。
已断开电池: batt_ev_027
时间步 46: 电池 batt_ev_027 已离开，当前SOC: 71.3%，能量满足率: 65.4%
奖励各项的值：powerloss=-0.1914085582444065, voltage=-0.10598024804084893, ctrl=-0.0, connection=11.52, completion=7.638888888888888, energy=7.9541353489932165, transformer=0.
已连接电池 batt_ev_003, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_001, 初始SOC: 38.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
已连接电池 batt_ev_086, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
智能体的动作为: [ 1.       -0.523687 -1.       -1.       -1.       -1.       -1.
 -1.       -1.       -1.       -1.      ]
已有历史设置self.charger_power=62.26938486099243，设置charger_power=62.842440605163574失败。
功率需求: 48.00 kW, 充电桩功率: 62.27 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=112.21904039382935，设置charger_power=71.28失败。
功率需求: 32.00 kW, 充电桩功率: 112.22 kW, 最终充电功率: 32.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=117.60281324386597，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 117.60 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=97.8296971321106，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 97.83 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -10.48, -3.444609422274487
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.61 更新为 0.83。
SOC从 0.12 更新为 0.37。
SOC从 0.77 更新为 0.88。
SOC从 0.42 更新为 0.68。
SOC从 0.46 更新为 0.69。
SOC从 0.41 更新为 0.64。
SOC从 0.38 更新为 0.72。
已断开电池: batt_ev_146
时间步 47: 电池 batt_ev_146 已离开，当前SOC: 87.6%，能量满足率: 81.4%
已断开电池: batt_ev_135
时间步 47: 电池 batt_ev_135 已离开，当前SOC: 83.1%，能量满足率: 77.4%
奖励各项的值：powerloss=-0.18467238827718557, voltage=-0.14463677186860702, ctrl=-0.0, connection=11.68, completion=7.534246575342466, energy=7.953894607388894, transformer=0.
智能体的动作为: [ 1.        -0.7052742 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=98.63999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=117.60281324386597，设置charger_power=108.63999999999999失败。
功率需求: 60.00 kW, 充电桩功率: 117.60 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=97.8296971321106，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 97.83 kW, 最终充电功率: 72.00 kW。
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
SOC从 0.64 更新为 0.81。
SOC从 0.72 更新为 0.89。
已断开电池: batt_ev_165
时间步 48: 电池 batt_ev_165 已离开，当前SOC: 81.3%，能量满足率: 79.1%
奖励各项的值：powerloss=-0.1542524866293103, voltage=-0.17684316524019694, ctrl=-0.0, connection=11.76, completion=7.482993197278912, energy=7.9536089621815185, transformer=0.
已连接电池 batt_ev_043, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_051, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
已连接电池 batt_ev_144, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [ 1.        -0.6642492 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -0.9991022 -1.       ]
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=103.19999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=38.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=117.60281324386597，设置charger_power=48.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 117.60 kW, 最终充电功率: 25.00 kW。
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
SOC从 0.48 更新为 0.69。
SOC从 0.22 更新为 0.61。
SOC从 0.57 更新为 0.72。
SOC从 0.42 更新为 0.66。
SOC从 0.87 更新为 0.96。
SOC从 0.86 更新为 0.93。
SOC从 0.89 更新为 1.00。
已断开电池: batt_ev_003
时间步 49: 电池 batt_ev_003 已离开，当前SOC: 95.6%，能量满足率: 95.7%
已断开电池: batt_ev_001
时间步 49 执行前: 电池 batt_ev_001 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_144
时间步 49 执行前: 电池 batt_ev_144 已充满 (SOC: 61.2%)，离开
奖励各项的值：powerloss=-0.1334880557563723, voltage=-0.22646655786266345, ctrl=-0.0, connection=12.0, completion=7.6, energy=7.991645626475304, transformer=0.
已连接电池 batt_ev_188, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
已连接电池 batt_ev_107, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 60kWh，并创BMS。
已连接电池 batt_ev_131, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [ 1.         -0.66421354 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -0.9991779  -1.        ]
初次设置charger_power=79.7056245803833。
功率需求: 120.00 kW, 充电桩功率: 79.71 kW, 最终充电功率: 79.71 kW。
已有历史设置self.charger_power=120.0，设置charger_power=119.68失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=67.19999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=89.12失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=117.60281324386597，设置charger_power=23.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 117.60 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=119.90134477615356。
功率需求: 60.00 kW, 充电桩功率: 119.90 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 79.7056245803833, -16.184917372289387
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.18 更新为 0.41。
SOC从 0.69 更新为 0.84。
SOC从 0.72 更新为 0.82。
SOC从 0.66 更新为 0.84。
SOC从 0.28 更新为 0.61。
SOC从 0.93 更新为 1.00。
SOC从 0.22 更新为 0.55。
已断开电池: batt_ev_127
时间步 50 执行前: 电池 batt_ev_127 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_086
时间步 50: 电池 batt_ev_086 已离开，当前SOC: 82.0%，能量满足率: 87.5%
已断开电池: batt_ev_051
时间步 50 执行前: 电池 batt_ev_051 已充满 (SOC: 84.5%)，离开
奖励各项的值：powerloss=-0.13046789378626616, voltage=-0.26005075503424235, ctrl=-0.0, connection=12.24, completion=7.712418300653595, energy=8.022855189354871, transformer=0.
已连接电池 batt_ev_136, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
已连接电池 batt_ev_116, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 52kWh，并创BMS。
已连接电池 batt_ev_196, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [ 1.        -0.6588502 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=79.7056245803833，设置charger_power=79.0620231628418失败。
功率需求: 96.00 kW, 充电桩功率: 79.71 kW, 最终充电功率: 79.71 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=41.120000000000005失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=92.80000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=119.90134477615356，设置charger_power=83.52失败。
功率需求: 36.00 kW, 充电桩功率: 119.90 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 79.7056245803833, -16.184917372289387
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.41 更新为 0.64。
SOC从 0.42 更新为 0.62。
SOC从 0.84 更新为 0.97。
SOC从 0.61 更新为 0.81。
SOC从 0.42 更新为 0.73。
SOC从 0.55 更新为 0.74。
SOC从 0.18 更新为 0.52。
已断开电池: batt_ev_131
时间步 51: 电池 batt_ev_131 已离开，当前SOC: 74.2%，能量满足率: 68.6%
奖励各项的值：powerloss=-0.12765640000995387, voltage=-0.29319140623423445, ctrl=-0.0, connection=12.32, completion=7.662337662337663, energy=8.015336574867844, transformer=0.
已连接电池 batt_ev_005, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_063, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
已连接电池 batt_ev_033, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
已连接电池 batt_ev_077, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
智能体的动作为: [ 1.         -0.65478027 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=79.7056245803833，设置charger_power=78.57363224029541失败。
功率需求: 72.00 kW, 充电桩功率: 79.71 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=120.0。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=76.8。
功率需求: 36.00 kW, 充电桩功率: 76.80 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=9.120000000000005失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.64 更新为 0.85。
SOC从 0.38 更新为 0.60。
SOC从 0.62 更新为 0.76。
SOC从 0.52 更新为 0.74。
SOC从 0.97 更新为 1.00。
SOC从 0.81 更新为 0.95。
SOC从 0.73 更新为 0.88。
SOC从 0.32 更新为 0.57。
SOC从 0.18 更新为 0.43。
SOC从 0.52 更新为 0.73。
已断开电池: batt_ev_043
时间步 52 执行前: 电池 batt_ev_043 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.13372069937283484, voltage=-0.2902438380056882, ctrl=-0.0, connection=12.4, completion=7.741935483870968, energy=8.028140855029985, transformer=0.
已连接电池 batt_ev_082, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
时间步 52 执行前: 排队电池 batt_ev_082 已接入
智能体的动作为: [ 1.         -0.70494103 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=79.7056245803833，设置charger_power=50.639999999999986失败。
功率需求: 30.00 kW, 充电桩功率: 79.71 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=85.91999999999999失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=78.24000000000001失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=76.8，设置charger_power=40.8失败。
功率需求: 24.00 kW, 充电桩功率: 76.80 kW, 最终充电功率: 24.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
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
SOC从 0.85 更新为 0.94。
SOC从 0.60 更新为 0.77。
SOC从 0.76 更新为 0.86。
SOC从 0.74 更新为 0.89。
SOC从 0.38 更新为 0.69。
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
奖励各项的值：powerloss=-0.1267368866322345, voltage=-0.2620463152099006, ctrl=-0.0, connection=12.64, completion=7.7215189873417724, energy=8.038081178924587, transformer=0.
已连接电池 batt_ev_159, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 53kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_159 已接入
时间步 53: 电池 batt_ev_097 已错过离开时间，无法接入
已连接电池 batt_ev_105, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_105 已接入
已连接电池 batt_ev_058, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_058 已接入
智能体的动作为: [ 1.        -0.6620296 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=79.7056245803833，设置charger_power=20.639999999999986失败。
功率需求: 30.00 kW, 充电桩功率: 79.71 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=49.91999999999999失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=46.24000000000001失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=76.8，设置charger_power=16.80000000000001失败。
功率需求: 15.00 kW, 充电桩功率: 76.80 kW, 最终充电功率: 15.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=62.47999999999999失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
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
SOC从 0.94 更新为 1.00。
SOC从 0.77 更新为 0.88。
SOC从 0.86 更新为 0.92。
SOC从 0.89 更新为 0.99。
SOC从 0.69 更新为 0.93。
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
奖励各项的值：powerloss=-0.13247393832933993, voltage=-0.26801604373397403, ctrl=-0.0, connection=13.200000000000001, completion=7.878787878787879, energy=8.069703884390924, transformer=0.
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
智能体的动作为: [ 1.         -0.66420317 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -0.9991416  -1.        ]
初次设置charger_power=79.70438003540039。
功率需求: 72.00 kW, 充电桩功率: 79.70 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=25.919999999999987失败。
功率需求: 15.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=14.47999999999999失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
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
SOC从 0.88 更新为 0.95。
SOC从 0.52 更新为 0.72。
SOC从 0.02 更新为 0.25。
SOC从 0.93 更新为 1.00。
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
奖励各项的值：powerloss=-0.15319101280163783, voltage=-0.2580153997069323, ctrl=-0.0, connection=13.44, completion=7.976190476190476, energy=8.101142152769304, transformer=0.
已连接电池 batt_ev_029, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_195, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
已连接电池 batt_ev_213, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_133, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [ 1.         -0.52688766 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=79.70438003540039，设置charger_power=63.226518630981445失败。
功率需求: 48.00 kW, 充电桩功率: 79.70 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=101.68。
功率需求: 48.00 kW, 充电桩功率: 101.68 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=85.91999999999999失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
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
SOC从 0.72 更新为 0.85。
SOC从 0.25 更新为 0.48。
SOC从 0.28 更新为 0.51。
SOC从 0.18 更新为 0.55。
SOC从 0.57 更新为 0.75。
SOC从 0.46 更新为 0.69。
SOC从 0.96 更新为 1.00。
SOC从 0.42 更新为 0.67。
已断开电池: batt_ev_175
时间步 56 执行前: 电池 batt_ev_175 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_213
时间步 56 执行前: 电池 batt_ev_213 已充满 (SOC: 50.7%)，离开
奖励各项的值：powerloss=-0.18044319163892542, voltage=-0.23447052549630643, ctrl=-0.0, connection=13.6, completion=8.117647058823529, energy=8.123481656854372, transformer=0.
已连接电池 batt_ev_145, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_044, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [ 1.        -0.7053118 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=79.70438003540039，设置charger_power=34.80000000000001失败。
功率需求: 30.00 kW, 充电桩功率: 79.70 kW, 最终充电功率: 30.00 kW。
已有历史设置self.charger_power=101.68，设置charger_power=53.68000000000001失败。
功率需求: 36.00 kW, 充电桩功率: 101.68 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=45.920000000000016失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=119.03999999999999。
功率需求: 48.00 kW, 充电桩功率: 119.04 kW, 最终充电功率: 48.00 kW。
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
SOC从 0.85 更新为 0.98。
SOC从 0.48 更新为 0.67。
SOC从 0.52 更新为 0.71。
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
奖励各项的值：powerloss=-0.18786873953461072, voltage=-0.24818045225827312, ctrl=-0.0, connection=13.92, completion=8.275862068965518, energy=8.147831326988577, transformer=0.
已连接电池 batt_ev_154, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_154 已接入
已连接电池 batt_ev_179, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_179 已接入
已连接电池 batt_ev_246, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 74kWh，并创BMS。
已连接电池 batt_ev_184, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [ 1.        -0.5175109 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
初次设置charger_power=62.1013069152832。
功率需求: 80.00 kW, 充电桩功率: 62.10 kW, 最终充电功率: 62.10 kW。
已有历史设置self.charger_power=101.68，设置charger_power=17.680000000000007失败。
功率需求: 15.00 kW, 充电桩功率: 101.68 kW, 最终充电功率: 15.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=119.03999999999999，设置charger_power=71.03999999999999失败。
功率需求: 32.00 kW, 充电桩功率: 119.04 kW, 最终充电功率: 32.00 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 62.1013069152832, -12.610208205838623
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.32 更新为 0.48。
SOC从 0.89 更新为 0.98。
SOC从 0.18 更新为 0.55。
SOC从 0.48 更新为 0.75。
SOC从 0.71 更新为 0.84。
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
奖励各项的值：powerloss=-0.20527501967245756, voltage=-0.2596072157281082, ctrl=-0.0, connection=14.24, completion=8.202247191011235, energy=8.17807738130355, transformer=0.
已连接电池 batt_ev_066, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
时间步 58 执行前: 排队电池 batt_ev_066 已接入
已连接电池 batt_ev_233, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
已连接电池 batt_ev_219, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_249, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
智能体的动作为: [ 1.        -0.5374043 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=62.1013069152832，设置charger_power=64.48851585388184失败。
功率需求: 80.00 kW, 充电桩功率: 62.10 kW, 最终充电功率: 62.10 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=71.2失败。
功率需求: 36.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=73.91999999999999失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=119.03999999999999，设置charger_power=39.03999999999999失败。
功率需求: 32.00 kW, 充电桩功率: 119.04 kW, 最终充电功率: 32.00 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 62.1013069152832, -12.610208205838623
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.48 更新为 0.65。
SOC从 0.08 更新为 0.47。
SOC从 0.55 更新为 0.78。
SOC从 0.75 更新为 0.89。
SOC从 0.84 更新为 0.97。
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
奖励各项的值：powerloss=-0.22243957924781638, voltage=-0.28026398223288007, ctrl=-0.0, connection=14.48, completion=8.066298342541437, energy=8.181072189894717, transformer=-2.5551947696482276.
已连接电池 batt_ev_032, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_032 已接入
已连接电池 batt_ev_060, 初始SOC: 56.99999999999999%, 最大功率: 100kW, 电池容量: 90kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_060 已接入
已连接电池 batt_ev_103, 初始SOC: 72.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_103 已接入
智能体的动作为: [ 1.        -0.7053256 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=62.1013069152832，设置charger_power=84.63907241821289失败。
功率需求: 60.00 kW, 充电桩功率: 62.10 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=120.0。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=33.920000000000016失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
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
SOC从 0.65 更新为 0.80。
SOC从 0.47 更新为 0.79。
SOC从 0.48 更新为 0.68。
SOC从 0.89 更新为 0.97。
SOC从 0.57 更新为 0.74。
SOC从 0.55 更新为 0.75。
SOC从 0.41 更新为 0.60。
SOC从 0.38 更新为 0.62。
SOC从 0.72 更新为 0.83。
SOC从 0.75 更新为 0.86。
已断开电池: batt_ev_154
时间步 60: 电池 batt_ev_154 已离开，当前SOC: 80.5%，能量满足率: 73.4%
已断开电池: batt_ev_246
时间步 60: 电池 batt_ev_246 已离开，当前SOC: 97.0%，能量满足率: 98.0%
已断开电池: batt_ev_184
时间步 60: 电池 batt_ev_184 已离开，当前SOC: 86.3%，能量满足率: 83.2%
已断开电池: batt_ev_233
时间步 60: 电池 batt_ev_233 已离开，当前SOC: 75.3%，能量满足率: 70.2%
已断开电池: batt_ev_103
时间步 60: 电池 batt_ev_103 已离开，当前SOC: 83.1%，能量满足率: 55.6%
奖励各项的值：powerloss=-0.2226205570834387, voltage=-0.2886588256612721, ctrl=-0.0, connection=14.88, completion=7.849462365591398, energy=8.165640543585141, transformer=0.
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
智能体的动作为: [ 1.         -0.69812393 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=83.77487182617188。
功率需求: 96.00 kW, 充电桩功率: 83.77 kW, 最终充电功率: 83.77 kW。
已有历史设置self.charger_power=120.0，设置charger_power=63.68000000000001失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=106.56失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=94.80000000000001失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
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
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 83.77487182617188, -17.01121326780783
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_217 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 20.0, -4.061173212680082
SOC从 0.48 更新为 0.66。
SOC从 0.79 更新为 0.95。
SOC从 0.68 更新为 0.82。
SOC从 0.12 更新为 0.44。
SOC从 0.74 更新为 0.85。
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
奖励各项的值：powerloss=-0.22511469288848288, voltage=-0.29554109544005724, ctrl=-0.0, connection=15.120000000000001, completion=7.724867724867725, energy=8.141492611610348, transformer=0.
已连接电池 batt_ev_073, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 106kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_073 已接入
已连接电池 batt_ev_020, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 99kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_020 已接入
已连接电池 batt_ev_208, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 61kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_208 已接入
智能体的动作为: [ 1.         -0.70274484 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
已有历史设置self.charger_power=83.77487182617188，设置charger_power=84.3293809890747失败。
功率需求: 72.00 kW, 充电桩功率: 83.77 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=58.56失败。
功率需求: 32.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 32.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
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
SOC从 0.66 更新为 0.82。
SOC从 0.48 更新为 0.71。
SOC从 0.82 更新为 0.92。
SOC从 0.44 更新为 0.69。
SOC从 0.32 更新为 0.56。
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
时间步 62 执行前: 电池 batt_ev_205 已充满 (SOC: 82.2%)，离开
已断开电池: batt_ev_189
时间步 62 执行前: 电池 batt_ev_189 已充满 (SOC: 100.0%)，离开
不太安全
奖励各项的值：powerloss=-0.22534400413787442, voltage=-0.2976638051773328, ctrl=-0.0, connection=15.44, completion=7.875647668393783, energy=8.173692183415719, transformer=-1.020550966563343.
已连接电池 batt_ev_091, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_091 已接入
时间步 62: 电池 batt_ev_176 已错过离开时间，无法接入
已连接电池 batt_ev_102, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_102 已接入
已连接电池 batt_ev_236, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 92kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_236 已接入
已连接电池 batt_ev_074, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_074 已接入
智能体的动作为: [ 1.       -0.704993 -1.       -1.       -1.       -1.       -1.
 -1.       -1.       -1.       -1.      ]
初次设置charger_power=84.59916114807129。
功率需求: 60.00 kW, 充电桩功率: 84.60 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=114.4。
功率需求: 48.00 kW, 充电桩功率: 114.40 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=98.08000000000001失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
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
SOC从 0.69 更新为 0.88。
SOC从 0.56 更新为 0.74。
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
奖励各项的值：powerloss=-0.21635235308617595, voltage=-0.3050898862200113, ctrl=-0.0, connection=15.76, completion=7.9187817258883255, energy=8.174516132228696, transformer=0.
时间步 63: 电池 batt_ev_130 已错过离开时间，无法接入
已连接电池 batt_ev_061, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 78kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_061 已接入
已连接电池 batt_ev_012, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 98kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_012 已接入
时间步 63: 电池 batt_ev_108 已错过离开时间，无法接入
已连接电池 batt_ev_228, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_228 已接入
已连接电池 batt_ev_218, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
智能体的动作为: [ 1.        -0.5230359 -1.        -1.        -1.        -1.
 -1.        -1.        -1.        -1.        -1.       ]
已有历史设置self.charger_power=84.59916114807129，设置charger_power=62.76430606842041失败。
功率需求: 48.00 kW, 充电桩功率: 84.60 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=76.48000000000002失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=114.4，设置charger_power=66.4失败。
功率需求: 36.00 kW, 充电桩功率: 114.40 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=101.27999999999997失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
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
SOC从 0.28 更新为 0.60。
SOC从 0.74 更新为 0.87。
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
奖励各项的值：powerloss=-0.21899212327847156, voltage=-0.3227683803391934, ctrl=-0.0, connection=16.16, completion=7.920792079207921, energy=8.187275376762406, transformer=0.
已连接电池 batt_ev_243, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 64 执行前: 排队电池 batt_ev_243 已接入
已连接电池 batt_ev_122, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [ 1.         -0.51803255 -1.         -1.         -1.         -1.
 -1.         -1.         -1.         -1.         -1.        ]
初次设置charger_power=62.16390609741211。
功率需求: 60.00 kW, 充电桩功率: 62.16 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=118.08。
功率需求: 60.00 kW, 充电桩功率: 118.08 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=114.4，设置charger_power=30.400000000000006失败。
功率需求: 15.00 kW, 充电桩功率: 114.40 kW, 最终充电功率: 15.00 kW。
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
奖励各项的值：powerloss=-0.20494550593224023, voltage=-0.2914943989853436, ctrl=-0.0, connection=16.4, completion=7.902439024390244, energy=8.185639546059722, transformer=0.
已连接电池 batt_ev_139, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 84kWh，并创BMS。
智能体的动作为: [ 0.5854672  -0.49868584 -1.         -1.         -1.         -1.
 -1.         -1.         -0.9791277  -0.8148287  -0.8047732 ]
已有历史设置self.charger_power=62.16390609741211，设置charger_power=59.84230041503906失败。
功率需求: 48.00 kW, 充电桩功率: 62.16 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=64.63999999999999失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
初次设置charger_power=120.0。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
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
SOC从 0.79 更新为 0.92。
SOC从 0.12 更新为 0.36。
SOC从 0.67 更新为 0.84。
SOC从 0.78 更新为 0.89。
奖励各项的值：powerloss=-0.20999094179835143, voltage=-0.1987193916864105, ctrl=-0.0, connection=16.4, completion=7.902439024390244, energy=8.185639546059722, transformer=0.
已连接电池 batt_ev_004, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_019, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
智能体的动作为: [ 0.3897909  -0.5749841  -1.         -1.         -1.         -1.
 -0.9996611  -1.         -0.8368638  -0.73436844 -0.6812834 ]
已有历史设置self.charger_power=62.16390609741211，设置charger_power=68.99808883666992失败。
功率需求: 36.00 kW, 充电桩功率: 62.16 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=24.639999999999986失败。
功率需求: 25.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 25.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 64.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=120.0。
功率需求: 100.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=33.360000000000014失败。
功率需求: 24.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=29.599999999999994失败。
功率需求: 20.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=81.75400972366333。
功率需求: 36.00 kW, 充电桩功率: 81.75 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.62 更新为 0.79。
SOC从 0.92 更新为 1.00。
SOC从 0.36 更新为 0.55。
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
奖励各项的值：powerloss=-0.2097472837978509, voltage=-0.12128040636505188, ctrl=-0.0, connection=16.72, completion=7.942583732057416, energy=8.210869209112792, transformer=0.
智能体的动作为: [ 0.5607573  -0.48631912 -1.         -1.         -1.         -1.
 -1.         -1.         -0.9680274  -0.8110114  -0.7975102 ]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 80.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 80.00 kW。
已有历史设置self.charger_power=81.75400972366333，设置charger_power=46.56失败。
功率需求: 24.00 kW, 充电桩功率: 81.75 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.55 更新为 0.69。
SOC从 0.35 更新为 0.57。
SOC从 0.73 更新为 0.87。
奖励各项的值：powerloss=-0.19618330085743155, voltage=-0.09811593761635873, ctrl=-0.0, connection=16.72, completion=7.942583732057416, energy=8.210869209112792, transformer=0.
智能体的动作为: [-0.888644   -0.0942137  -1.         -0.9522444  -0.7860273  -1.
 -0.6801632  -1.         -0.5211659  -0.8085307  -0.21985826]
已有历史设置self.charger_power=120.0，设置charger_power=103.68失败。
功率需求: 48.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 48.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=81.75400972366333，设置charger_power=22.560000000000002失败。
功率需求: 15.00 kW, 充电桩功率: 81.75 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 88.86439800262451, 29.208315139750994
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.69 更新为 0.83。
SOC从 0.57 更新为 0.74。
SOC从 0.87 更新为 0.96。
已断开电池: batt_ev_139
时间步 69: 电池 batt_ev_139 已离开，当前SOC: 83.4%，能量满足率: 83.1%
奖励各项的值：powerloss=-0.20147747430565913, voltage=-0.01632194150121835, ctrl=-0.0, connection=16.8, completion=7.904761904761904, energy=8.211320535929072, transformer=0.
已连接电池 batt_ev_177, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [-1.         -0.6793895  -0.84007376 -0.55850875 -0.5728288  -1.
 -0.56281483 -0.85605097 -0.4204339  -1.         -0.        ]
初次设置charger_power=100.80885171890259。
功率需求: 64.00 kW, 充电桩功率: 100.81 kW, 最终充电功率: 64.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=94.88失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已有历史设置self.charger_power=81.75400972366333，设置charger_power=0.0失败。
功率需求: 15.00 kW, 充电桩功率: 81.75 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 15.0, -3.045879909510062
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.38 更新为 0.65。
SOC从 0.74 更新为 0.85。
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_019
时间步 70 执行前: 电池 batt_ev_019 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.1909119335378731, voltage=-0.013155806141329496, ctrl=-0.0, connection=16.88, completion=7.9620853080568725, energy=8.219797689787228, transformer=0.
已连接电池 batt_ev_202, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_160, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [-1.         -0.71069837 -0.81558347 -0.5333353  -0.5566424  -1.
 -0.5581277  -0.8055007  -0.41616648 -1.         -0.        ]
已有历史设置self.charger_power=100.80885171890259，设置charger_power=82.32失败。
功率需求: 48.00 kW, 充电桩功率: 100.81 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=64.00023937225342。
功率需求: 80.00 kW, 充电桩功率: 64.00 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=66.97532415390015。
功率需求: 60.00 kW, 充电桩功率: 66.98 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=54.879999999999995失败。
功率需求: 40.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 40.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 64.00023937225342, -12.995802887185434
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.65 更新为 0.85。
SOC从 0.48 更新为 0.69。
SOC从 0.18 更新为 0.55。
SOC从 0.85 更新为 0.96。
已断开电池: batt_ev_004
时间步 71 执行前: 电池 batt_ev_004 已充满 (SOC: 95.9%)，离开
奖励各项的值：powerloss=-0.17946952724280313, voltage=-0.026621708015424073, ctrl=-0.0, connection=16.96, completion=8.018867924528303, energy=8.228194870495779, transformer=0.
智能体的动作为: [ 0.16782224 -0.48337182 -1.         -1.         -1.         -1.
 -0.93520665 -1.         -0.79086655 -0.6890181  -0.52455246]
已有历史设置self.charger_power=100.80885171890259，设置charger_power=34.31999999999999失败。
功率需求: 20.00 kW, 充电桩功率: 100.81 kW, 最终充电功率: 20.00 kW。
已有历史设置self.charger_power=64.00023937225342，设置charger_power=94.08000000000001失败。
功率需求: 60.00 kW, 充电桩功率: 64.00 kW, 最终充电功率: 60.00 kW。
已有历史设置self.charger_power=66.97532415390015，设置charger_power=74.48失败。
功率需求: 36.00 kW, 充电桩功率: 66.98 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -16.78222417831421, -5.516050336960289
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.85 更新为 0.94。
SOC从 0.69 更新为 0.89。
SOC从 0.55 更新为 0.77。
已断开电池: batt_ev_202
时间步 72 执行前: 电池 batt_ev_202 已充满 (SOC: 88.8%)，离开
奖励各项的值：powerloss=-0.14895330964014994, voltage=-0.140357845428154, ctrl=-0.0, connection=17.04, completion=8.075117370892018, energy=8.236513204437113, transformer=0.
已连接电池 batt_ev_099, 初始SOC: 68.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
已连接电池 batt_ev_100, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [-1.         -0.7165768  -0.8111508  -0.52904934 -0.55324626 -1.
 -0.5574086  -0.79529965 -0.41596928 -1.         -0.        ]
初次设置charger_power=85.75999999999999。
功率需求: 36.00 kW, 充电桩功率: 85.76 kW, 最终充电功率: 36.00 kW。
已有历史设置self.charger_power=100.80885171890259，设置charger_power=14.319999999999993失败。
功率需求: 20.00 kW, 充电桩功率: 100.81 kW, 最终充电功率: 20.00 kW。
初次设置charger_power=66.38955116271973。
功率需求: 80.00 kW, 充电桩功率: 66.39 kW, 最终充电功率: 66.39 kW。
已有历史设置self.charger_power=66.97532415390015，设置charger_power=38.480000000000004失败。
功率需求: 24.00 kW, 充电桩功率: 66.98 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 20.0, -4.061173212680082
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 66.38955116271973, -13.480973339194557
SOC从 0.68 更新为 0.81。
SOC从 0.94 更新为 1.00。
SOC从 0.18 更新为 0.47。
SOC从 0.77 更新为 0.91。
已断开电池: batt_ev_177
时间步 73 执行前: 电池 batt_ev_177 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_160
时间步 73: 电池 batt_ev_160 已离开，当前SOC: 91.2%，能量满足率: 91.5%
奖励各项的值：powerloss=-0.13307085529291268, voltage=-0.12764930702489075, ctrl=-0.0, connection=17.2, completion=8.093023255813954, energy=8.248947227946603, transformer=0.
智能体的动作为: [-0.97694165 -0.10371196 -1.         -0.9385442  -0.7678134  -1.
 -0.6746586  -1.         -0.5050249  -0.8250138  -0.19275598]
已有历史设置self.charger_power=85.75999999999999，设置charger_power=12.445435523986816失败。
功率需求: 24.00 kW, 充电桩功率: 85.76 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=66.38955116271973，设置charger_power=92.13760614395142失败。
功率需求: 64.00 kW, 充电桩功率: 66.39 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 97.69416451454164, 32.110519044658766
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.81 更新为 0.90。
SOC从 0.47 更新为 0.74。
已断开电池: batt_ev_100
时间步 74: 电池 batt_ev_100 已离开，当前SOC: 74.2%，能量满足率: 76.0%
奖励各项的值：powerloss=-0.12330730363097764, voltage=-0.16211979626144402, ctrl=-0.0, connection=17.28, completion=8.055555555555555, energy=8.245922132266498, transformer=0.
智能体的动作为: [-1.         -1.         -0.8076483  -0.24797308 -0.514818   -1.
 -0.21922784 -0.529722   -0.39948356 -1.         -0.        ]
已有历史设置self.charger_power=85.75999999999999，设置charger_power=25.75999999999999失败。
功率需求: 15.00 kW, 充电桩功率: 85.76 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 100.0, 32.86841051788632
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.90 更新为 0.96。
奖励各项的值：powerloss=-0.11509784921614655, voltage=-0.18332775660709455, ctrl=-0.0, connection=17.28, completion=8.055555555555555, energy=8.245922132266498, transformer=0.
智能体的动作为: [-0.27821505 -1.         -1.         -0.02810566 -1.         -0.6058294
 -0.01360365 -0.64006895 -0.24950682 -0.7758325  -0.        ]
已有历史设置self.charger_power=85.75999999999999，设置charger_power=10.759999999999991失败。
功率需求: 15.00 kW, 充电桩功率: 85.76 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 27.821505069732666, 9.144486498574288
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_099
时间步 76 执行前: 电池 batt_ev_099 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.11055828267758522, voltage=-0.2536073599480315, ctrl=-0.0, connection=17.36, completion=8.110599078341014, energy=8.254005440412735, transformer=0.
已连接电池 batt_ev_120, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [-0.27836722 -1.         -1.         -0.02810859 -1.         -0.6058446
 -0.0136108  -0.6400662  -0.24949408 -0.7758395  -0.        ]
初次设置charger_power=29.939289093017578。
功率需求: 120.00 kW, 充电桩功率: 29.94 kW, 最终充电功率: 29.94 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 27.836722135543823, 9.149488106233877
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 29.939289093017578, -6.079431943562398
SOC从 0.18 更新为 0.27。
奖励各项的值：powerloss=-0.11174406734179328, voltage=-0.2323508338372804, ctrl=-0.0, connection=17.36, completion=8.110599078341014, energy=8.254005440412735, transformer=0.
智能体的动作为: [-0.617526   -1.         -1.         -0.08330804 -1.         -0.6571327
 -0.07736272 -0.69890094 -0.19924486 -0.7712636  -0.        ]
已有历史设置self.charger_power=29.939289093017578，设置charger_power=23.909382820129395失败。
功率需求: 120.00 kW, 充电桩功率: 29.94 kW, 最终充电功率: 29.94 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 61.752599477767944, 20.297097901818894
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 29.939289093017578, -6.079431943562398
SOC从 0.27 更新为 0.36。
奖励各项的值：powerloss=-0.11959463963354597, voltage=-0.201911389339422, ctrl=-0.0, connection=17.36, completion=8.110599078341014, energy=8.254005440412735, transformer=0.
已连接电池 batt_ev_035, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 77kWh，并创BMS。
智能体的动作为: [-0.62758154 -1.         -1.         -0.08470652 -1.         -0.6584288
 -0.07920144 -0.7002089  -0.19794227 -0.77103674 -0.        ]
已有历史设置self.charger_power=29.939289093017578，设置charger_power=23.75307261943817失败。
功率需求: 96.00 kW, 充电桩功率: 29.94 kW, 最终充电功率: 29.94 kW。
初次设置charger_power=92.52440929412842。
功率需求: 64.00 kW, 充电桩功率: 92.52 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 62.758153676986694, 20.627607583997957
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 29.939289093017578, -6.079431943562398
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.36 更新为 0.45。
SOC从 0.48 更新为 0.69。
已断开电池: batt_ev_120
时间步 79: 电池 batt_ev_120 已离开，当前SOC: 45.4%，能量满足率: 34.2%
奖励各项的值：powerloss=-0.1406420012873264, voltage=-0.3184197759329166, ctrl=-0.0, connection=17.44, completion=8.073394495412845, energy=8.231834459985691, transformer=0.
已连接电池 batt_ev_151, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
智能体的动作为: [-1.         -0.9657421  -0.77617776 -0.35579064 -0.49449804 -1.
 -0.32826644 -0.6250475  -0.38881755 -1.         -0.        ]
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
已有历史设置self.charger_power=92.52440929412842，设置charger_power=96.16失败。
功率需求: 48.00 kW, 充电桩功率: 92.52 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 50.039999999999964, 16.4473526231503
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.28 更新为 0.63。
SOC从 0.69 更新为 0.84。
奖励各项的值：powerloss=-0.16008512289835175, voltage=-0.36279710700744205, ctrl=-0.0, connection=17.44, completion=8.073394495412845, energy=8.231834459985691, transformer=0.
智能体的动作为: [-0.3485455 -0.2042675 -1.        -1.        -0.9341827 -1.
 -0.750803  -1.        -0.6291236 -0.7291371 -0.3617603]
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
已有历史设置self.charger_power=92.52440929412842，设置charger_power=48.160000000000025失败。
功率需求: 32.00 kW, 充电桩功率: 92.52 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 32.0, -6.497877140288132
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 72.0, -14.620223565648296
SOC从 0.63 更新为 0.84。
SOC从 0.84 更新为 0.95。
已断开电池: batt_ev_035
时间步 81: 电池 batt_ev_035 已离开，当前SOC: 94.8%，能量满足率: 93.5%
已断开电池: batt_ev_151
时间步 81: 电池 batt_ev_151 已离开，当前SOC: 83.8%，能量满足率: 79.7%
奖励各项的值：powerloss=-0.16554787841147448, voltage=-0.3423761368956968, ctrl=-0.0, connection=17.6, completion=8.0, energy=8.23574537979291, transformer=0.
智能体的动作为: [-1.         -0.7663537  -0.79695404 -0.5000814  -0.53762674 -1.
 -0.5205557  -0.7636623  -0.40666124 -1.         -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.16965088811217255, voltage=-0.29895344906986754, ctrl=-0.0, connection=17.6, completion=8.0, energy=8.23574537979291, transformer=0.
智能体的动作为: [-0.27097833 -1.         -1.         -0.02724925 -1.         -0.60350907
 -0.01293534 -0.63959205 -0.24976377 -0.7753657  -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.17849156051229095, voltage=-0.33903245507016955, ctrl=-0.0, connection=17.6, completion=8.0, energy=8.23574537979291, transformer=0.
已连接电池 batt_ev_056, 初始SOC: 62.0%, 最大功率: 80kW, 电池容量: 64kWh，并创BMS。
已连接电池 batt_ev_226, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [-0.27107418 -1.         -1.         -0.02723192 -1.         -0.603521
 -0.01294203 -0.6395607  -0.24974681 -0.77537894 -0.        ]
初次设置charger_power=76.74728393554688。
功率需求: 60.00 kW, 充电桩功率: 76.75 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.18 更新为 0.51。
SOC从 0.62 更新为 0.62。
奖励各项的值：powerloss=-0.1859513560434649, voltage=-0.342508811820732, ctrl=-0.0, connection=17.6, completion=8.0, energy=8.23574537979291, transformer=0.
已连接电池 batt_ev_048, 初始SOC: 42.0%, 最大功率: 120kW, 电池容量: 93kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.9035512  -0.14574888 -0.77994    -1.
 -0.18243234 -0.7064085  -0.26485386 -0.93302536 -0.        ]
初次设置charger_power=17.489866018295288。
功率需求: 96.00 kW, 充电桩功率: 17.49 kW, 最终充电功率: 17.49 kW。
已有历史设置self.charger_power=76.74728393554688，设置charger_power=84.7690200805664失败。
功率需求: 36.00 kW, 充电桩功率: 76.75 kW, 最终充电功率: 36.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_048 充电的有无功功率为 17.489866018295288, -3.5514687683432236
SOC从 0.42 更新为 0.47。
SOC从 0.51 更新为 0.70。
SOC从 0.62 更新为 0.62。
已断开电池: batt_ev_048
时间步 85: 电池 batt_ev_048 已离开，当前SOC: 46.7%，能量满足率: 8.4%
奖励各项的值：powerloss=-0.1911676337788684, voltage=-0.412897429966792, ctrl=-0.0, connection=17.68, completion=7.963800904977375, energy=8.202276367676186, transformer=0.
已连接电池 batt_ev_234, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_227, 初始SOC: 8.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
智能体的动作为: [-1.         -1.         -0.8452929  -0.23104382 -0.73694634 -1.
 -0.17915355 -0.745426   -0.28724334 -0.8126974  -0.        ]
初次设置charger_power=101.43515110015869。
功率需求: 36.00 kW, 充电桩功率: 101.44 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=21.498425602912903。
功率需求: 60.00 kW, 充电桩功率: 21.50 kW, 最终充电功率: 21.50 kW。
已有历史设置self.charger_power=76.74728393554688，设置charger_power=54.879999999999995失败。
功率需求: 24.00 kW, 充电桩功率: 76.75 kW, 最终充电功率: 24.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 21.498425602912903, -4.365441508667276
SOC从 0.57 更新为 0.71。
SOC从 0.08 更新为 0.19。
SOC从 0.70 更新为 0.83。
SOC从 0.62 更新为 0.62。
已断开电池: batt_ev_056
时间步 86: 电池 batt_ev_056 已离开，当前SOC: 62.0%，能量满足率: 0.0%
已断开电池: batt_ev_226
时间步 86 执行前: 电池 batt_ev_226 已充满 (SOC: 83.2%)，离开
奖励各项的值：powerloss=-0.1931871318900452, voltage=-0.3898597013877936, ctrl=-0.0, connection=17.84, completion=7.982062780269058, energy=8.173556400253082, transformer=0.
智能体的动作为: [-1.         -1.         -0.79578346 -0.2070671  -0.5036918  -1.
 -0.17526285 -0.49707645 -0.38961607 -1.         -0.        ]
已有历史设置self.charger_power=101.43515110015869，设置charger_power=72.36000000000001失败。
功率需求: 24.00 kW, 充电桩功率: 101.44 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=21.498425602912903，设置charger_power=21.031542420387268失败。
功率需求: 60.00 kW, 充电桩功率: 21.50 kW, 最终充电功率: 21.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 21.498425602912903, -4.365441508667276
SOC从 0.71 更新为 0.81。
SOC从 0.19 更新为 0.31。
奖励各项的值：powerloss=-0.18899338805729865, voltage=-0.3438769233264116, ctrl=-0.0, connection=17.84, completion=7.982062780269058, energy=8.173556400253082, transformer=0.
智能体的动作为: [-1.         -1.         -0.8444352  -0.23518363 -0.7510336  -1.
 -0.17388386 -0.7484394  -0.2714312  -0.7839082  -0.        ]
已有历史设置self.charger_power=101.43515110015869，设置charger_power=48.360000000000014失败。
功率需求: 24.00 kW, 充电桩功率: 101.44 kW, 最终充电功率: 24.00 kW。
已有历史设置self.charger_power=21.498425602912903，设置charger_power=20.8660626411438失败。
功率需求: 48.00 kW, 充电桩功率: 21.50 kW, 最终充电功率: 21.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 21.498425602912903, -4.365441508667276
SOC从 0.81 更新为 0.90。
SOC从 0.31 更新为 0.42。
已断开电池: batt_ev_227
时间步 88: 电池 batt_ev_227 已离开，当前SOC: 42.3%，能量满足率: 38.1%
奖励各项的值：powerloss=-0.1858463781073983, voltage=-0.3451691315837624, ctrl=-0.0, connection=17.92, completion=7.946428571428571, energy=8.154069588815782, transformer=0.
智能体的动作为: [-1.         -1.         -0.8458917  -0.23389313 -0.7547458  -1.
 -0.17402878 -0.74904007 -0.2685718  -0.7836686  -0.        ]
已有历史设置self.charger_power=101.43515110015869，设置charger_power=24.360000000000014失败。
功率需求: 15.00 kW, 充电桩功率: 101.44 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.90 更新为 0.96。
奖励各项的值：powerloss=-0.1858699772311947, voltage=-0.28165253716332606, ctrl=-0.0, connection=17.92, completion=7.946428571428571, energy=8.154069588815782, transformer=0.
智能体的动作为: [-0.28035462 -1.         -1.         -0.02815773 -1.         -0.6060127
 -0.01374394 -0.6400422  -0.24934025 -0.7759472  -0.        ]
已有历史设置self.charger_power=101.43515110015869，设置charger_power=9.360000000000014失败。
功率需求: 15.00 kW, 充电桩功率: 101.44 kW, 最终充电功率: 15.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_234
时间步 90 执行前: 电池 batt_ev_234 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.19973830039026155, voltage=-0.20601247407508572, ctrl=-0.0, connection=18.0, completion=8.0, energy=8.1622737239766, transformer=0.
智能体的动作为: [-0.27917218 -1.         -1.         -0.02813351 -1.         -0.6059146
 -0.01367104 -0.640063   -0.24942994 -0.7758834  -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.19617676489659625, voltage=-0.07846179492185579, ctrl=-0.0, connection=18.0, completion=8.0, energy=8.1622737239766, transformer=0.
智能体的动作为: [-0.27052605 -1.         -1.         -0.02733507 -1.         -0.60349965
 -0.01292532 -0.6397247  -0.24984656 -0.77531207 -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.19009302252927626, voltage=-0.05499017312744492, ctrl=-0.0, connection=18.0, completion=8.0, energy=8.1622737239766, transformer=0.
已连接电池 batt_ev_238, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [-0.27051157 -1.         -1.         -0.0273148  -1.         -0.6034636
 -0.01291643 -0.63972765 -0.24982753 -0.7753411  -0.        ]
初次设置charger_power=85.28。
功率需求: 48.00 kW, 充电桩功率: 85.28 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.48 更新为 0.77。
奖励各项的值：powerloss=-0.1933757686861727, voltage=-0.019533419754007575, ctrl=-0.0, connection=18.0, completion=8.0, energy=8.1622737239766, transformer=0.
智能体的动作为: [-1.         -1.         -0.83993906 -0.23844221 -0.73291665 -1.
 -0.16961423 -0.7418075  -0.28693256 -0.78569305 -0.        ]
已有历史设置self.charger_power=85.28，设置charger_power=37.28失败。
功率需求: 24.00 kW, 充电桩功率: 85.28 kW, 最终充电功率: 24.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.77 更新为 0.92。
已断开电池: batt_ev_238
时间步 94 执行前: 电池 batt_ev_238 已充满 (SOC: 91.9%)，离开
奖励各项的值：powerloss=-0.1796318388749922, voltage=-0.01570718688241657, ctrl=-0.0, connection=18.080000000000002, completion=8.053097345132743, energy=8.170405256171394, transformer=0.
智能体的动作为: [-0.31753117 -1.         -1.         -0.03240731 -1.         -0.6107188
 -0.01876109 -0.6442116  -0.24469334 -0.7767085  -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.16154578307502943, voltage=-0.08384762050086092, ctrl=-0.0, connection=18.080000000000002, completion=8.053097345132743, energy=8.170405256171394, transformer=0.
已连接电池 batt_ev_025, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
已连接电池 batt_ev_013, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 89kWh，并创BMS。
已连接电池 batt_ev_117, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 111kWh，并创BMS。
已连接电池 batt_ev_166, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 114kWh，并创BMS。
智能体的动作为: [-0.27064848 -1.         -1.         -0.02723718 -1.         -0.60337204
 -0.01291773 -0.6397     -0.24976419 -0.7754733  -0.        ]
初次设置charger_power=120.0。
功率需求: 60.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=72.40464448928833。
功率需求: 72.00 kW, 充电桩功率: 72.40 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=29.971702694892883。
功率需求: 120.00 kW, 充电桩功率: 29.97 kW, 最终充电功率: 29.97 kW。
初次设置charger_power=93.05679559707642。
功率需求: 120.00 kW, 充电桩功率: 93.06 kW, 最终充电功率: 93.06 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_025 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_013 充电的有无功功率为 29.971702694892883, -6.086013806145521
已在 set_all_batteries_before_solve 中设置 batt_ev_117 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_166 充电的有无功功率为 93.05679559707642, -18.895988276834625
SOC从 0.12 更新为 0.43。
SOC从 0.52 更新为 0.68。
SOC从 0.18 更新为 0.26。
SOC从 0.28 更新为 0.48。
已断开电池: batt_ev_025
时间步 96: 电池 batt_ev_025 已离开，当前SOC: 42.6%，能量满足率: 35.6%
已断开电池: batt_ev_013
时间步 96: 电池 batt_ev_013 已离开，当前SOC: 26.4%，能量满足率: 10.5%
已断开电池: batt_ev_117
时间步 96: 电池 batt_ev_117 已离开，当前SOC: 68.2%，能量满足率: 35.3%
已断开电池: batt_ev_166
时间步 96: 电池 batt_ev_166 已离开，当前SOC: 48.4%，能量满足率: 29.1%
奖励各项的值：powerloss=-0.15668928799940995, voltage=-0.15841680647988854, ctrl=-4.0, connection=18.400000000000002, completion=7.913043478260869, energy=8.076361603953679, transformer=0.
调度记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250510_132849_13Bus_cbat_1000000\test_results_20250510_182929\schedule.csv
储能放电功率记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250510_132849_13Bus_cbat_1000000\test_results_20250510_182929\storage_schedule.csv
储能能量记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250510_132849_13Bus_cbat_1000000\test_results_20250510_182929\storage_energy.csv
已生成GIF动画，包含96步
测试完成 - 总奖励: 2554.1846
测试结果保存在: D:\LENOVO\Documents\Python\ML\powergym\results_20250510_132849_13Bus_cbat_1000000\test_results_20250510_182929
运行时间: 18084.13秒

进程已结束，退出代码为 0
```