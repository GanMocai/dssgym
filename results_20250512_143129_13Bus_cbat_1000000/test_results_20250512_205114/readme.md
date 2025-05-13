

## 测试信息

### 原始控制台输出

请使用更新的测试结果，该训练和测试时BMS存在一定问题，但是没时间重新训练，且更新的测试结果表现也很出色。

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
已从D:\LENOVO\Documents\Python\ML\powergym\results_20250512_143129_13Bus_cbat_1000000\model\ppo_model加载模型
BatteryStationManager已重置
智能体的动作为: [ 0.3097769  -1.         -0.48325253 -0.53623474 -0.49190143 -0.4778784
 -1.         -0.         -0.         -0.         -0.01275941]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -30.97769021987915, -10.181874390429002
奖励各项的值：powerloss=-0.11843371062838506, voltage=-0.16405869627552416, ctrl=-0.0, connection=0.0, completion=0.0, energy=0.0, transformer=0.
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
智能体的动作为: [ 0.33206964 -1.         -0.4891261  -0.5513312  -0.5164387  -0.4738887
 -1.         -0.         -0.         -0.         -0.01764463]
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
初次设置charger_power=39.13008689880371。
功率需求: 64.00 kW, 充电桩功率: 39.13 kW, 最终充电功率: 39.13 kW。
初次设置charger_power=33.07987332344055。
功率需求: 60.00 kW, 充电桩功率: 33.08 kW, 最终充电功率: 33.08 kW。
初次设置charger_power=30.986323356628418。
功率需求: 60.00 kW, 充电桩功率: 30.99 kW, 最终充电功率: 30.99 kW。
初次设置charger_power=28.433321714401245。
功率需求: 60.00 kW, 充电桩功率: 28.43 kW, 最终充电功率: 28.43 kW。
初次设置charger_power=100.0。
功率需求: 100.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=0.0。
功率需求: 80.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求: 96.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=2.1173550188541412。
功率需求: 120.00 kW, 充电桩功率: 2.12 kW, 最终充电功率: 2.12 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -33.206963539123535, -10.914601096563956
已在 set_all_batteries_before_solve 中设置 batt_ev_030 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 39.13008689880371, -7.945703036163272
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 33.07987332344055, -6.717154771000361
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 30.986323356628418, -6.292041318769124
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 28.433321714401245, -5.773632224702062
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 2.1173550188541412, -0.4299472742152084
SOC从 0.18 更新为 0.51。
SOC从 0.32 更新为 0.46。
SOC从 0.18 更新为 0.30。
SOC从 0.12 更新为 0.24。
SOC从 0.22 更新为 0.36。
SOC从 0.28 更新为 0.55。
SOC从 0.12 更新为 0.12。
SOC从 0.38 更新为 0.38。
SOC从 0.22 更新为 0.22。
SOC从 0.12 更新为 0.13。
已断开电池: batt_ev_030
时间步 2 执行前: 电池 batt_ev_030 已充满 (SOC: 51.3%)，离开
奖励各项的值：powerloss=-0.13335375246956727, voltage=-0.2164919426481493, ctrl=-0.0, connection=0.08, completion=10.0, energy=10.0, transformer=0.
已连接电池 batt_ev_224, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
时间步 2 执行前: 排队电池 batt_ev_224 已接入
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.21609257
 -1.         -1.         -0.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 12.97 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -95.84, -31.501084640342246
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 12.965554296970367, -2.6327680899202597
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 0.0, -0.0
SOC从 0.28 更新为 0.28。
SOC从 0.46 更新为 0.75。
SOC从 0.30 更新为 0.52。
SOC从 0.24 更新为 0.49。
SOC从 0.36 更新为 0.42。
SOC从 0.55 更新为 0.82。
SOC从 0.12 更新为 0.50。
SOC从 0.38 更新为 0.38。
SOC从 0.22 更新为 0.55。
SOC从 0.13 更新为 0.54。
已断开电池: batt_ev_064
时间步 3 执行前: 电池 batt_ev_064 已充满 (SOC: 48.7%)，离开
已断开电池: batt_ev_239
时间步 3 执行前: 电池 batt_ev_239 已充满 (SOC: 82.3%)，离开
已断开电池: batt_ev_039
时间步 3: 电池 batt_ev_039 已离开，当前SOC: 50.5%，能量满足率: 44.7%
已断开电池: batt_ev_045
时间步 3: 电池 batt_ev_045 已离开，当前SOC: 54.4%，能量满足率: 49.3%
奖励各项的值：powerloss=-0.14134891999352983, voltage=-0.32294154653150997, ctrl=-0.0, connection=0.4, completion=6.0, energy=7.880565493937587, transformer=0.
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
智能体的动作为: [ 1.        -0.        -1.        -1.        -1.        -0.2500444
 -1.        -1.        -0.        -1.        -1.       ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 68.56 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=80.0。
功率需求: 80.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 15.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=60.0。
功率需求: 36.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 36.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 68.56, -13.921701773067323
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 15.00266432762146, -3.0464209243083653
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_235 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.28 更新为 0.28。
SOC从 0.75 更新为 1.00。
SOC从 0.52 更新为 0.74。
SOC从 0.12 更新为 0.52。
SOC从 0.42 更新为 0.50。
SOC从 0.28 更新为 0.53。
SOC从 0.62 更新为 0.81。
SOC从 0.38 更新为 0.38。
SOC从 0.55 更新为 0.89。
SOC从 0.32 更新为 0.52。
已断开电池: batt_ev_149
时间步 4 执行前: 电池 batt_ev_149 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_126
时间步 4: 电池 batt_ev_126 已离开，当前SOC: 74.3%，能量满足率: 70.3%
奖励各项的值：powerloss=-0.13620185503898355, voltage=-0.30014858768399044, ctrl=-0.0, connection=0.56, completion=5.7142857142857135, energy=8.062536277182309, transformer=0.
已连接电池 batt_ev_062, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_062 已接入
时间步 4: 电池 batt_ev_200 已错过离开时间，无法接入
时间步 4: 电池 batt_ev_163 已错过离开时间，无法接入
已连接电池 batt_ev_014, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_014 已接入
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.25535136
 -1.         -1.         -0.         -1.         -1.        ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=80.0。
功率需求: 80.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 15.32 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 35.44 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 20.40 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 15.32108187675476, -3.111078365357735
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 20.400000000000006, -4.142396676933685
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_235 充电的有无功功率为 35.440000000000005, -7.196398932869105
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_062 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_014 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.28 更新为 0.28。
SOC从 0.57 更新为 0.80。
SOC从 0.28 更新为 0.53。
SOC从 0.52 更新为 0.92。
SOC从 0.50 更新为 0.57。
SOC从 0.53 更新为 0.78。
SOC从 0.81 更新为 1.00。
SOC从 0.38 更新为 0.38。
SOC从 0.89 更新为 1.00。
SOC从 0.52 更新为 0.76。
已断开电池: batt_ev_123
时间步 5: 电池 batt_ev_123 已离开，当前SOC: 57.2%，能量满足率: 46.3%
已断开电池: batt_ev_042
时间步 5 执行前: 电池 batt_ev_042 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_076
时间步 5: 电池 batt_ev_076 已离开，当前SOC: 78.0%，能量满足率: 71.4%
已断开电池: batt_ev_235
时间步 5 执行前: 电池 batt_ev_235 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_062
时间步 5: 电池 batt_ev_062 已离开，当前SOC: 80.4%，能量满足率: 57.0%
奖励各项的值：powerloss=-0.13775880793621093, voltage=-0.3161900609684465, ctrl=-0.0, connection=0.96, completion=5.0, energy=7.8256774611352, transformer=0.
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
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.25618744
 -1.         -1.         -0.         -1.         -1.        ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 16.00 kW。
初次设置charger_power=30.74249267578125。
功率需求: 72.00 kW, 充电桩功率: 30.74 kW, 最终充电功率: 30.74 kW。
初次设置charger_power=80.0。
功率需求: 80.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 57.92 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 16.0, -3.248938570144066
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 57.91999999999999, -11.761157623921513
已在 set_all_batteries_before_solve 中设置 batt_ev_014 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 30.74249267578125, -6.242529387294822
已在 set_all_batteries_before_solve 中设置 batt_ev_231 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_248 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.28 更新为 0.28。
SOC从 0.08 更新为 0.37。
SOC从 0.53 更新为 0.79。
SOC从 0.92 更新为 1.00。
SOC从 0.57 更新为 0.67。
SOC从 0.08 更新为 0.40。
SOC从 0.32 更新为 0.52。
SOC从 0.38 更新为 0.38。
SOC从 0.22 更新为 0.47。
SOC从 0.76 更新为 1.00。
已断开电池: batt_ev_081
时间步 6 执行前: 电池 batt_ev_081 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_018
时间步 6 执行前: 电池 batt_ev_018 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_014
时间步 6: 电池 batt_ev_014 已离开，当前SOC: 78.6%，能量满足率: 84.4%
已断开电池: batt_ev_231
时间步 6: 电池 batt_ev_231 已离开，当前SOC: 40.3%，能量满足率: 35.8%
已断开电池: batt_ev_248
时间步 6: 电池 batt_ev_248 已离开，当前SOC: 46.6%，能量满足率: 32.4%
奖励各项的值：powerloss=-0.1455890583951892, voltage=-0.34312519658149965, ctrl=-0.0, connection=1.36, completion=4.705882352941177, energy=7.598042669165469, transformer=0.
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
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.25637975
 -1.         -1.         -0.         -1.         -1.        ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 30.77 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=60.0。
功率需求: 36.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 36.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 30.765570402145386, -6.247215519500801
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_157 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_187 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.28 更新为 0.28。
SOC从 0.37 更新为 0.67。
SOC从 0.48 更新为 0.82。
SOC从 0.28 更新为 0.60。
SOC从 0.67 更新为 0.77。
SOC从 0.12 更新为 0.39。
SOC从 0.52 更新为 0.77。
SOC从 0.38 更新为 0.38。
SOC从 0.18 更新为 0.47。
SOC从 0.57 更新为 0.72。
已断开电池: batt_ev_242
时间步 7: 电池 batt_ev_242 已离开，当前SOC: 38.0%，能量满足率: 0.0%
已断开电池: batt_ev_224
时间步 7: 电池 batt_ev_224 已离开，当前SOC: 28.0%，能量满足率: -0.0%
已断开电池: batt_ev_036
时间步 7: 电池 batt_ev_036 已离开，当前SOC: 77.0%，能量满足率: 48.7%
已断开电池: batt_ev_157
时间步 7: 电池 batt_ev_157 已离开，当前SOC: 39.3%，能量满足率: 31.7%
已断开电池: batt_ev_187
时间步 7: 电池 batt_ev_187 已离开，当前SOC: 72.0%，能量满足率: 36.6%
奖励各项的值：powerloss=-0.1628279132726962, voltage=-0.3829760117605585, ctrl=-0.0, connection=1.76, completion=3.6363636363636367, energy=6.403101044121553, transformer=0.
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
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.25700742
 -1.         -1.         -0.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 96.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 49.60 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=25.70074200630188。
功率需求: 100.00 kW, 充电桩功率: 25.70 kW, 最终充电功率: 25.70 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 55.20 kW。
初次设置charger_power=0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 55.19999999999999, -11.208838066997025
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 49.599999999999994, -10.071709567446602
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_106 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 25.70074200630188, -5.218758249099748
已在 set_all_batteries_before_solve 中设置 batt_ev_216 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 96.0, -19.493631420864393
SOC从 0.32 更新为 0.32。
SOC从 0.67 更新为 0.96。
SOC从 0.82 更新为 1.00。
SOC从 0.60 更新为 0.92。
SOC从 0.28 更新为 0.35。
SOC从 0.42 更新为 0.65。
SOC从 0.77 更新为 1.00。
SOC从 0.18 更新为 0.18。
SOC从 0.47 更新为 0.76。
SOC从 0.48 更新为 0.72。
已断开电池: batt_ev_180
时间步 8: 电池 batt_ev_180 已离开，当前SOC: 96.2%，能量满足率: 98.0%
已断开电池: batt_ev_067
时间步 8 执行前: 电池 batt_ev_067 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_240
时间步 8 执行前: 电池 batt_ev_240 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_158
时间步 8 执行前: 电池 batt_ev_158 已充满 (SOC: 91.8%)，离开
已断开电池: batt_ev_106
时间步 8: 电池 batt_ev_106 已离开，当前SOC: 32.0%，能量满足率: 0.0%
已断开电池: batt_ev_216
时间步 8: 电池 batt_ev_216 已离开，当前SOC: 64.6%，能量满足率: 40.4%
奖励各项的值：powerloss=-0.1767688431967861, voltage=-0.3823829503480103, ctrl=-0.0, connection=2.24, completion=3.9285714285714284, energy=6.596973972283491, transformer=0.
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
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.26168734
 -1.         -1.         -0.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 64.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=95.20000000000002。
功率需求: 48.00 kW, 充电桩功率: 95.20 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=100.0。
功率需求: 100.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=100.0。
功率需求: 60.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 26.17 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=100.0。
功率需求: 100.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 100.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 50.56 kW。
功率需求计算已禁用，直接使用充电桩功率: 112.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 50.559999999999995, -10.266645881655249
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 26.168733835220337, -5.3137880430675875
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 112.0, -22.74256999100846
已在 set_all_batteries_before_solve 中设置 batt_ev_128 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_173 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_132 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.42 更新为 0.42。
SOC从 0.72 更新为 0.86。
SOC从 0.22 更新为 0.48。
SOC从 0.57 更新为 0.80。
SOC从 0.35 更新为 0.42。
SOC从 0.18 更新为 0.46。
SOC从 0.08 更新为 0.40。
SOC从 0.18 更新为 0.18。
SOC从 0.76 更新为 1.00。
SOC从 0.72 更新为 1.00。
已断开电池: batt_ev_096
时间步 9 执行前: 电池 batt_ev_096 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_055
时间步 9: 电池 batt_ev_055 已离开，当前SOC: 41.6%，能量满足率: 19.5%
已断开电池: batt_ev_247
时间步 9: 电池 batt_ev_247 已离开，当前SOC: 18.0%，能量满足率: 0.0%
已断开电池: batt_ev_090
时间步 9 执行前: 电池 batt_ev_090 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_128
时间步 9: 电池 batt_ev_128 已离开，当前SOC: 42.0%，能量满足率: 0.0%
已断开电池: batt_ev_173
时间步 9: 电池 batt_ev_173 已离开，当前SOC: 80.1%，能量满足率: 56.3%
已断开电池: batt_ev_132
时间步 9: 电池 batt_ev_132 已离开，当前SOC: 46.3%，能量满足率: 35.4%
奖励各项的值：powerloss=-0.20087891496074128, voltage=-0.47375430843398236, ctrl=-0.0, connection=2.8000000000000003, completion=3.7142857142857144, energy=6.166582773631007, transformer=0.
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
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.25996536
 -1.         -1.         -0.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 100.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 47.20 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
初次设置charger_power=80.0。
功率需求: 80.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=20.797228813171387。
功率需求: 80.00 kW, 充电桩功率: 20.80 kW, 最终充电功率: 20.80 kW。
初次设置charger_power=50.400000000000006。
功率需求: 48.00 kW, 充电桩功率: 50.40 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
初次设置charger_power=0.0。
功率需求: 100.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=100.0。
功率需求: 80.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=80.0。
功率需求: 80.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 47.19999999999999, -9.584368781924992
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_191 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_161 充电的有无功功率为 20.797228813171387, -4.2230574277015
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.18 更新为 0.18。
SOC从 0.86 更新为 1.00。
SOC从 0.48 更新为 0.75。
SOC从 0.22 更新为 0.52。
SOC从 0.22 更新为 0.29。
SOC从 0.82 更新为 0.99。
SOC从 0.40 更新为 0.72。
SOC从 0.28 更新为 0.28。
SOC从 0.38 更新为 0.62。
SOC从 0.18 更新为 0.43。
已断开电池: batt_ev_220
时间步 10 执行前: 电池 batt_ev_220 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_150
时间步 10: 电池 batt_ev_150 已离开，当前SOC: 72.1%，能量满足率: 71.2%
已断开电池: batt_ev_191
时间步 10: 电池 batt_ev_191 已离开，当前SOC: 18.0%，能量满足率: 0.0%
已断开电池: batt_ev_161
时间步 10: 电池 batt_ev_161 已离开，当前SOC: 29.2%，能量满足率: 9.5%
奖励各项的值：powerloss=-0.21372058406255384, voltage=-0.45599244052631827, ctrl=-0.0, connection=3.12, completion=3.58974358974359, energy=5.9975178614680305, transformer=0.
已连接电池 batt_ev_008, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 60kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_008 已接入
已连接电池 batt_ev_162, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_162 已接入
已连接电池 batt_ev_170, 初始SOC: 42.0%, 最大功率: 120kW, 电池容量: 99kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_170 已接入
已连接电池 batt_ev_085, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_085 已接入
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.26575363
 -1.         -1.         -0.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 96.40 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
初次设置charger_power=31.890435218811035。
功率需求: 96.00 kW, 充电桩功率: 31.89 kW, 最终充电功率: 31.89 kW。
功率需求计算已禁用，直接使用充电桩功率: 2.40 kW。
初次设置charger_power=60.0。
功率需求: 36.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 36.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 96.39999999999998, -19.574854885117993
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 2.3999999999999773, -0.4873407855216052
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_008 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 31.890435218811035, -6.4756290625672435
已在 set_all_batteries_before_solve 中设置 batt_ev_085 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.68 更新为 0.68。
SOC从 0.28 更新为 0.51。
SOC从 0.75 更新为 1.00。
SOC从 0.52 更新为 0.82。
SOC从 0.42 更新为 0.50。
SOC从 0.99 更新为 1.00。
SOC从 0.62 更新为 0.84。
SOC从 0.28 更新为 0.28。
SOC从 0.62 更新为 0.91。
SOC从 0.43 更新为 0.68。
已断开电池: batt_ev_016
时间步 11 执行前: 电池 batt_ev_016 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_193
时间步 11: 电池 batt_ev_193 已离开，当前SOC: 81.7%，能量满足率: 78.6%
已断开电池: batt_ev_186
时间步 11 执行前: 电池 batt_ev_186 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_008
时间步 11: 电池 batt_ev_008 已离开，当前SOC: 68.0%，能量满足率: 0.0%
已断开电池: batt_ev_085
时间步 11 执行前: 电池 batt_ev_085 已充满 (SOC: 84.0%)，离开
奖励各项的值：powerloss=-0.22006544802908873, voltage=-0.49084107525465104, ctrl=-0.0, connection=3.52, completion=3.8636363636363633, energy=6.176333094128102, transformer=0.
时间步 11: 电池 batt_ev_222 已错过离开时间，无法接入
已连接电池 batt_ev_114, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_114 已接入
已连接电池 batt_ev_009, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_009 已接入
已连接电池 batt_ev_113, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_065, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_203, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.29214078
 -1.         -1.         -0.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 15.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 35.06 kW。
初次设置charger_power=60.0。
功率需求: 36.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 30.80 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 30.800000000000008, -6.254206747527329
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 35.056893825531006, -7.1186059062008145
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.92 更新为 0.92。
SOC从 0.51 更新为 0.74。
SOC从 0.18 更新为 0.47。
SOC从 0.28 更新为 0.67。
SOC从 0.50 更新为 0.59。
SOC从 0.62 更新为 0.79。
SOC从 0.28 更新为 0.62。
SOC从 0.28 更新为 0.28。
SOC从 0.91 更新为 1.00。
SOC从 0.68 更新为 0.93。
已断开电池: batt_ev_194
时间步 12: 电池 batt_ev_194 已离开，当前SOC: 28.0%，能量满足率: -0.0%
已断开电池: batt_ev_078
时间步 12 执行前: 电池 batt_ev_078 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_170
时间步 12: 电池 batt_ev_170 已离开，当前SOC: 58.9%，能量满足率: 30.2%
奖励各项的值：powerloss=-0.22703578281405803, voltage=-0.5103251968625422, ctrl=-0.0, connection=3.7600000000000002, completion=3.829787234042553, energy=6.059070912964113, transformer=0.
已连接电池 batt_ev_011, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 12 执行前: 排队电池 batt_ev_011 已接入
已连接电池 batt_ev_041, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_232, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.28798753
 -1.         -1.         -0.         -1.         -1.        ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 101.76 kW。
初次设置charger_power=23.039002418518066。
功率需求: 64.00 kW, 充电桩功率: 23.04 kW, 最终充电功率: 23.04 kW。
功率需求计算已禁用，直接使用充电桩功率: 46.08 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求: 80.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 22.40 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 22.399999999999977, -4.548513998201687
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 101.75999999999999, -20.66324930611626
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 46.08000000000002, -9.356943082014913
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_011 充电的有无功功率为 23.039002418518066, -4.67826897344786
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.92 更新为 0.92。
SOC从 0.74 更新为 0.97。
SOC从 0.47 更新为 0.76。
SOC从 0.67 更新为 1.00。
SOC从 0.32 更新为 0.40。
SOC从 0.79 更新为 1.00。
SOC从 0.62 更新为 0.96。
SOC从 0.12 更新为 0.12。
SOC从 0.38 更新为 0.56。
SOC从 0.93 更新为 1.00。
已断开电池: batt_ev_000
时间步 13 执行前: 电池 batt_ev_000 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_162
时间步 13: 电池 batt_ev_162 已离开，当前SOC: 97.2%，能量满足率: 98.9%
已断开电池: batt_ev_113
时间步 13 执行前: 电池 batt_ev_113 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_065
时间步 13 执行前: 电池 batt_ev_065 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_011
时间步 13: 电池 batt_ev_011 已离开，当前SOC: 40.2%，能量满足率: 12.5%
奖励各项的值：powerloss=-0.22849862390343856, voltage=-0.5491557927646085, ctrl=-0.0, connection=4.16, completion=4.038461538461538, energy=6.267561462426468, transformer=0.
已连接电池 batt_ev_237, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_237 已接入
已连接电池 batt_ev_052, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_052 已接入
已连接电池 batt_ev_206, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 62kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_206 已接入
已连接电池 batt_ev_172, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
已连接电池 batt_ev_229, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.30257887
 -1.         -1.         -0.         -1.         -1.        ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 24.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 24.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 97.84 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=18.15473198890686。
功率需求: 60.00 kW, 充电桩功率: 18.15 kW, 最终充电功率: 18.15 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 6.72 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 97.83999999999997, -19.867259356430957
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 6.719999999999999, -1.3645541994605073
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_052 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_206 充电的有无功功率为 18.15473198890686, -3.686475561836737
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.92 更新为 0.92。
SOC从 0.78 更新为 0.87。
SOC从 0.76 更新为 1.00。
SOC从 0.38 更新为 0.58。
SOC从 0.22 更新为 0.29。
SOC从 0.38 更新为 0.68。
SOC从 0.96 更新为 1.00。
SOC从 0.12 更新为 0.12。
SOC从 0.56 更新为 0.80。
SOC从 0.38 更新为 0.58。
已断开电池: batt_ev_114
时间步 14: 电池 batt_ev_114 已离开，当前SOC: 92.0%，能量满足率: 0.0%
已断开电池: batt_ev_009
时间步 14 执行前: 电池 batt_ev_009 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_203
时间步 14 执行前: 电池 batt_ev_203 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_206
时间步 14: 电池 batt_ev_206 已离开，当前SOC: 29.3%，能量满足率: 12.2%
奖励各项的值：powerloss=-0.21831433959265967, voltage=-0.5412034349048911, ctrl=-0.0, connection=4.48, completion=4.107142857142857, energy=6.198814752744701, transformer=0.
已连接电池 batt_ev_164, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_164 已接入
已连接电池 batt_ev_134, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_214, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 80kWh，并创BMS。
已连接电池 batt_ev_143, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.33249378
 -1.         -1.         -0.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 36.72 kW。
初次设置charger_power=80.0。
功率需求: 64.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 64.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=33.2493782043457。
功率需求: 80.00 kW, 充电桩功率: 33.25 kW, 最终充电功率: 33.25 kW。
功率需求计算已禁用，直接使用充电桩功率: 51.20 kW。
初次设置charger_power=80.0。
功率需求: 64.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 64.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 53.20 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 53.19999999999998, -10.802720745729015
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 36.72, -7.456314018480629
已在 set_all_batteries_before_solve 中设置 batt_ev_052 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 51.20000000000001, -10.396603424461011
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 33.2493782043457, -6.751574205087887
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.42 更新为 0.42。
SOC从 0.87 更新为 1.00。
SOC从 0.32 更新为 0.62。
SOC从 0.58 更新为 0.83。
SOC从 0.48 更新为 0.58。
SOC从 0.68 更新为 1.00。
SOC从 0.48 更新为 0.75。
SOC从 0.12 更新为 0.12。
SOC从 0.80 更新为 1.00。
SOC从 0.58 更新为 0.83。
已断开电池: batt_ev_232
时间步 15 执行前: 电池 batt_ev_232 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_237
时间步 15 执行前: 电池 batt_ev_237 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_052
时间步 15 执行前: 电池 batt_ev_052 已充满 (SOC: 83.0%)，离开
已断开电池: batt_ev_172
时间步 15 执行前: 电池 batt_ev_172 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.2214820891631258, voltage=-0.5370076901119791, ctrl=-0.0, connection=4.8, completion=4.5, energy=6.4522271025617215, transformer=0.
已连接电池 batt_ev_245, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_245 已接入
已连接电池 batt_ev_098, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_098 已接入
已连接电池 batt_ev_190, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 63kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_190 已接入
智能体的动作为: [ 1.        -0.        -1.        -1.        -1.        -0.3067786
 -1.        -1.        -0.        -1.        -1.       ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
初次设置charger_power=80.0。
功率需求: 64.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 64.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 30.68 kW。
初次设置charger_power=100.0。
功率需求: 100.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 100.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 58.72 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 40.80 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 40.80000000000001, -8.28479335386737
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 30.677860975265503, -6.2294053607535975
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 58.72, -11.92360455242872
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.42 更新为 0.42。
SOC从 0.38 更新为 0.56。
SOC从 0.62 更新为 0.99。
SOC从 0.42 更新为 0.65。
SOC从 0.58 更新为 0.68。
SOC从 0.18 更新为 0.58。
SOC从 0.75 更新为 1.00。
SOC从 0.12 更新为 0.12。
SOC从 0.83 更新为 1.00。
已断开电池: batt_ev_229
时间步 16 执行前: 电池 batt_ev_229 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_134
时间步 16 执行前: 电池 batt_ev_134 已充满 (SOC: 98.7%)，离开
已断开电池: batt_ev_143
时间步 16 执行前: 电池 batt_ev_143 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.2206245273971255, voltage=-0.5315547754142091, ctrl=-0.0, connection=5.04, completion=4.761904761904762, energy=6.621168669106401, transformer=0.
已连接电池 batt_ev_069, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 56kWh，并创BMS。
已连接电池 batt_ev_071, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.31159836
 -1.         -1.         -0.         -1.         -1.        ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=100.0。
功率需求: 80.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 31.16 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 31.159836053848267, -6.3272745746695795
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.42 更新为 0.42。
SOC从 0.56 更新为 0.79。
SOC从 0.42 更新为 0.63。
SOC从 0.65 更新为 0.93。
SOC从 0.68 更新为 0.78。
SOC从 0.58 更新为 0.97。
SOC从 0.12 更新为 0.12。
SOC从 0.38 更新为 0.59。
已断开电池: batt_ev_214
时间步 17: 电池 batt_ev_214 已离开，当前SOC: 77.7%，能量满足率: 59.4%
已断开电池: batt_ev_245
时间步 17: 电池 batt_ev_245 已离开，当前SOC: 78.9%，能量满足率: 68.2%
已断开电池: batt_ev_190
时间步 17 执行前: 电池 batt_ev_190 已充满 (SOC: 97.4%)，离开
奖励各项的值：powerloss=-0.22232089695098478, voltage=-0.5069711377612784, ctrl=-0.0, connection=5.28, completion=4.696969696969697, energy=6.665065272301289, transformer=0.
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.34118932
 -1.         -1.         -0.         -1.         -1.        ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 18.40 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 18.399999999999977, -3.736279355665671
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.42 更新为 0.42。
SOC从 0.63 更新为 0.89。
SOC从 0.93 更新为 1.00。
SOC从 0.12 更新为 0.12。
SOC从 0.59 更新为 0.86。
已断开电池: batt_ev_098
时间步 18 执行前: 电池 batt_ev_098 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_071
时间步 18 执行前: 电池 batt_ev_071 已充满 (SOC: 88.9%)，离开
奖励各项的值：powerloss=-0.21685098502288053, voltage=-0.33880461062062217, ctrl=-0.0, connection=5.44, completion=4.852941176470588, energy=6.76315158782184, transformer=0.
已连接电池 batt_ev_083, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_174, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_167, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.7750229  -1.         -0.5186728
 -1.         -1.         -0.         -0.44426143 -0.79908586]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
初次设置charger_power=69.11999999999998。
功率需求: 48.00 kW, 充电桩功率: 69.12 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 26.66 kW。
初次设置charger_power=63.9268684387207。
功率需求: 80.00 kW, 充电桩功率: 63.93 kW, 最终充电功率: 63.93 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 26.655685901641846, -5.412667877468098
已在 set_all_batteries_before_solve 中设置 batt_ev_083 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 63.9268684387207, -12.980904283692816
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.42 更新为 0.42。
SOC从 0.32 更新为 0.56。
SOC从 0.68 更新为 0.90。
SOC从 0.12 更新为 0.12。
SOC从 0.86 更新为 0.98。
SOC从 0.18 更新为 0.42。
已断开电池: batt_ev_164
时间步 19: 电池 batt_ev_164 已离开，当前SOC: 42.0%，能量满足率: 0.0%
已断开电池: batt_ev_069
时间步 19 执行前: 电池 batt_ev_069 已充满 (SOC: 98.1%)，离开
已断开电池: batt_ev_083
时间步 19 执行前: 电池 batt_ev_083 已充满 (SOC: 90.2%)，离开
奖励各项的值：powerloss=-0.21104297429242233, voltage=-0.21241144729981398, ctrl=-0.0, connection=5.68, completion=4.929577464788732, energy=6.759074760167396, transformer=0.
已连接电池 batt_ev_115, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
已连接电池 batt_ev_181, 初始SOC: 56.99999999999999%, 最大功率: 80kW, 电池容量: 69kWh，并创BMS。
已连接电池 batt_ev_182, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 95kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.7651536  -1.         -0.52202046
 -1.         -1.         -0.         -0.4211508  -0.7876187 ]
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=91.81843042373657。
功率需求: 120.00 kW, 充电桩功率: 91.82 kW, 最终充电功率: 91.82 kW。
初次设置charger_power=31.321227550506592。
功率需求: 60.00 kW, 充电桩功率: 31.32 kW, 最终充电功率: 31.32 kW。
初次设置charger_power=80.0。
功率需求: 48.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 63.01 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 63.00949573516846, -12.794623811207302
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 31.321227550506592, -6.3600465158187385
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 91.81843042373657, -18.644527503360443
SOC从 0.56 更新为 0.85。
SOC从 0.28 更新为 0.52。
SOC从 0.12 更新为 0.29。
SOC从 0.57 更新为 0.74。
SOC从 0.12 更新为 0.12。
SOC从 0.42 更新为 0.66。
已断开电池: batt_ev_041
时间步 20: 电池 batt_ev_041 已离开，当前SOC: 12.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.20812837901417947, voltage=-0.15742662737948, ctrl=-0.0, connection=5.76, completion=4.861111111111111, energy=6.665198721831738, transformer=0.
已连接电池 batt_ev_037, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_138, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
已连接电池 batt_ev_095, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
智能体的动作为: [ 1.        -0.        -1.        -1.        -1.        -0.4254517
 -1.        -1.        -0.        -0.9276225 -0.9016167]
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 30.72 kW。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
初次设置charger_power=80.0。
功率需求: 64.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 64.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 25.53 kW。
功率需求计算已禁用，直接使用充电桩功率: 70.68 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 72.13 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 72.12933540344238, -14.646486239443865
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 30.72, -6.237962054676605
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 25.527101755142212, -5.1834990922671125
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 70.67999999999999, -14.352186133611411
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_138 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.48 更新为 0.48。
SOC从 0.85 更新为 1.00。
SOC从 0.52 更新为 0.84。
SOC从 0.32 更新为 0.57。
SOC从 0.29 更新为 0.43。
SOC从 0.74 更新为 1.00。
SOC从 0.12 更新为 0.43。
SOC从 0.66 更新为 0.93。
已断开电池: batt_ev_167
时间步 21 执行前: 电池 batt_ev_167 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_181
时间步 21 执行前: 电池 batt_ev_181 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.21516210767212632, voltage=-0.1162144392031439, ctrl=-0.0, connection=5.92, completion=5.0, energy=6.7553284861065555, transformer=0.
已连接电池 batt_ev_197, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 75kWh，并创BMS。
已连接电池 batt_ev_026, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 102kWh，并创BMS。
已连接电池 batt_ev_212, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_010, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 71kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.34506702
 -1.         -1.         -0.         -1.         -1.        ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 61.76 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 20.70 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求: 96.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=80.0。
功率需求: 48.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 17.44 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 17.439999999999998, -3.541343041457031
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 20.704021453857422, -4.204130866157976
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 61.76, -12.540902880756093
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_138 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_212 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 96.0, -19.493631420864393
SOC从 0.48 更新为 0.48。
SOC从 0.22 更新为 0.50。
SOC从 0.84 更新为 1.00。
SOC从 0.57 更新为 0.87。
SOC从 0.43 更新为 0.54。
SOC从 0.48 更新为 0.82。
SOC从 0.43 更新为 0.74。
SOC从 0.32 更新为 0.32。
SOC从 0.52 更新为 0.68。
SOC从 0.93 更新为 1.00。
已断开电池: batt_ev_174
时间步 22 执行前: 电池 batt_ev_174 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_182
时间步 22 执行前: 电池 batt_ev_182 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_138
时间步 22: 电池 batt_ev_138 已离开，当前SOC: 48.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.20351825036569735, voltage=-0.10156686872761389, ctrl=-0.0, connection=6.16, completion=5.064935064935065, energy=6.751874129505001, transformer=0.
已连接电池 batt_ev_241, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 68kWh，并创BMS。
已连接电池 batt_ev_084, 初始SOC: 78.0%, 最大功率: 100kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_038, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.35570854
 -1.         -1.         -0.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=54.56。
功率需求: 40.00 kW, 充电桩功率: 54.56 kW, 最终充电功率: 40.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 32.80 kW。
功率需求计算已禁用，直接使用充电桩功率: 21.34 kW。
功率需求计算已禁用，直接使用充电桩功率: 51.68 kW。
功率需求计算已禁用，直接使用充电桩功率: 48.96 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
初次设置charger_power=80.0。
功率需求: 64.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 21.342512369155884, -4.33378197624546
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 32.80000000000001, -6.660324068795337
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 48.96000000000001, -9.941752024640845
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_212 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 51.68, -10.494071581565333
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_084 充电的有无功功率为 40.0, -8.122346425360163
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.48 更新为 0.48。
SOC从 0.50 更新为 0.78。
SOC从 0.78 更新为 0.94。
SOC从 0.87 更新为 1.00。
SOC从 0.54 更新为 0.66。
SOC从 0.82 更新为 1.00。
SOC从 0.74 更新为 1.00。
SOC从 0.32 更新为 0.32。
SOC从 0.68 更新为 0.95。
SOC从 0.42 更新为 0.70。
已断开电池: batt_ev_037
时间步 23 执行前: 电池 batt_ev_037 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_095
时间步 23 执行前: 电池 batt_ev_095 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_212
时间步 23: 电池 batt_ev_212 已离开，当前SOC: 77.6%，能量满足率: 73.1%
已断开电池: batt_ev_010
时间步 23 执行前: 电池 batt_ev_010 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.18271293023729368, voltage=-0.11413831725179957, ctrl=-0.0, connection=6.48, completion=5.185185185185185, energy=6.879064808547567, transformer=0.
已连接电池 batt_ev_040, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_040 已接入
已连接电池 batt_ev_046, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_046 已接入
已连接电池 batt_ev_050, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_050 已接入
已连接电池 batt_ev_125, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.4114955
 -1.         -1.         -0.         -0.9656114  -0.93524194]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=50.16。
功率需求: 24.00 kW, 充电桩功率: 50.16 kW, 最终充电功率: 24.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 14.56 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 24.69 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 16.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 70.56 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 24.689730405807495, -5.013463587617917
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 16.0, -3.248938570144066
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_084 充电的有无功功率为 14.560000000000002, -2.9565340988310997
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 70.56, -14.327819094335332
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_046 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_050 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_125 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.48 更新为 0.48。
SOC从 0.78 更新为 0.89。
SOC从 0.94 更新为 1.00。
SOC从 0.42 更新为 0.66。
SOC从 0.66 更新为 0.79。
SOC从 0.28 更新为 0.59。
SOC从 0.28 更新为 0.50。
SOC从 0.32 更新为 0.32。
SOC从 0.95 更新为 1.00。
SOC从 0.70 更新为 1.00。
已断开电池: batt_ev_115
时间步 24: 电池 batt_ev_115 已离开，当前SOC: 79.2%，能量满足率: 96.0%
已断开电池: batt_ev_197
时间步 24 执行前: 电池 batt_ev_197 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_084
时间步 24 执行前: 电池 batt_ev_084 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_038
时间步 24 执行前: 电池 batt_ev_038 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.1611985051015155, voltage=-0.18484790847185684, ctrl=-0.0, connection=6.8, completion=5.294117647058823, energy=7.02118262099151, transformer=0.
已连接电池 batt_ev_137, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 84kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_137 已接入
已连接电池 batt_ev_221, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 75kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_221 已接入
已连接电池 batt_ev_109, 初始SOC: 88.0%, 最大功率: 100kW, 电池容量: 70kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_109 已接入
已连接电池 batt_ev_034, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 68kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_034 已接入
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.44241595
 -1.         -1.         -0.         -0.8475675  -0.85101104]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 26.16 kW。
初次设置charger_power=80.0。
功率需求: 48.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=53.089914321899414。
功率需求: 120.00 kW, 充电桩功率: 53.09 kW, 最终充电功率: 53.09 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=33.599999999999994。
功率需求: 25.00 kW, 充电桩功率: 33.60 kW, 最终充电功率: 25.00 kW。
初次设置charger_power=68.08088302612305。
功率需求: 80.00 kW, 充电桩功率: 68.08 kW, 最终充电功率: 68.08 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 26.159999999999997, -5.312014562185546
已在 set_all_batteries_before_solve 中设置 batt_ev_046 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_050 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_125 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 53.089914321899414, -10.78036689537893
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 25.0, -5.076466515850102
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 68.08088302612305, -13.824412922064852
SOC从 0.48 更新为 0.48。
SOC从 0.89 更新为 1.00。
SOC从 0.52 更新为 0.66。
SOC从 0.66 更新为 0.97。
SOC从 0.28 更新为 0.46。
SOC从 0.59 更新为 0.90。
SOC从 0.50 更新为 0.73。
SOC从 0.32 更新为 0.32。
SOC从 0.88 更新为 0.97。
SOC从 0.22 更新为 0.47。
已断开电池: batt_ev_026
时间步 25: 电池 batt_ev_026 已离开，当前SOC: 32.0%，能量满足率: 0.0%
已断开电池: batt_ev_241
时间步 25: 电池 batt_ev_241 已离开，当前SOC: 48.0%，能量满足率: 0.0%
已断开电池: batt_ev_040
时间步 25 执行前: 电池 batt_ev_040 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_046
时间步 25: 电池 batt_ev_046 已离开，当前SOC: 97.1%，能量满足率: 98.4%
已断开电池: batt_ev_050
时间步 25 执行前: 电池 batt_ev_050 已充满 (SOC: 90.5%)，离开
已断开电池: batt_ev_125
时间步 25: 电池 batt_ev_125 已离开，当前SOC: 72.8%，能量满足率: 70.0%
奖励各项的值：powerloss=-0.14242306535248037, voltage=-0.24239396476274822, ctrl=-0.0, connection=7.28, completion=5.164835164835165, energy=6.963037819634806, transformer=0.
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
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.42410338
 -1.         -1.         -0.         -0.9313873  -0.9042187 ]
初次设置charger_power=0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=80.0。
功率需求: 80.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
初次设置charger_power=100.0。
功率需求: 80.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 50.89 kW。
初次设置charger_power=100.0。
功率需求: 80.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 8.60 kW。
功率需求计算已禁用，直接使用充电桩功率: 72.34 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 50.89240550994873, -10.334143699292799
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 8.600000000000021, -1.74630448145244
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 72.33749389648438, -14.688754624240564
已在 set_all_batteries_before_solve 中设置 batt_ev_141 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_075 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.28 更新为 0.28。
SOC从 0.22 更新为 0.51。
SOC从 0.66 更新为 0.90。
SOC从 0.42 更新为 0.64。
SOC从 0.46 更新为 0.63。
SOC从 0.38 更新为 0.64。
SOC从 0.38 更新为 0.59。
SOC从 0.97 更新为 1.00。
SOC从 0.47 更新为 0.74。
已断开电池: batt_ev_109
时间步 26 执行前: 电池 batt_ev_109 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_075
时间步 26 执行前: 电池 batt_ev_075 已充满 (SOC: 64.0%)，离开
奖励各项的值：powerloss=-0.14322867774134143, voltage=-0.2641030680972989, ctrl=-0.0, connection=7.44, completion=5.268817204301075, energy=7.028348834266317, transformer=0.
已连接电池 batt_ev_031, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_057, 初始SOC: 8.0%, 最大功率: 80kW, 电池容量: 73kWh，并创BMS。
已连接电池 batt_ev_111, 初始SOC: 68.0%, 最大功率: 100kW, 电池容量: 83kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.37656128
 -1.         -1.         -0.         -1.         -1.        ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 33.28 kW。
初次设置charger_power=80.0。
功率需求: 80.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 45.19 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求: 64.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=100.0。
功率需求: 60.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 71.76 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 33.27999999999997, -6.757792225899651
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 45.18735408782959, -9.175683598669167
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 71.75999999999999, -14.571489487096134
已在 set_all_batteries_before_solve 中设置 batt_ev_141 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_031 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.28 更新为 0.28。
SOC从 0.51 更新为 0.81。
SOC从 0.90 更新为 1.00。
SOC从 0.08 更新为 0.35。
SOC从 0.63 更新为 0.78。
SOC从 0.64 更新为 0.97。
SOC从 0.59 更新为 0.86。
SOC从 0.42 更新为 0.42。
SOC从 0.68 更新为 0.86。
SOC从 0.74 更新为 1.00。
已断开电池: batt_ev_137
时间步 27 执行前: 电池 batt_ev_137 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_034
时间步 27 执行前: 电池 batt_ev_034 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_141
时间步 27: 电池 batt_ev_141 已离开，当前SOC: 28.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.14228121431760146, voltage=-0.2981786801366981, ctrl=-0.0, connection=7.68, completion=5.3125, energy=7.017046266528828, transformer=0.
已连接电池 batt_ev_006, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_006 已接入
已连接电池 batt_ev_225, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 94kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_225 已接入
已连接电池 batt_ev_054, 初始SOC: 82.0%, 最大功率: 120kW, 电池容量: 85kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.37469065
 -1.         -1.         -0.         -1.         -1.        ]
初次设置charger_power=0.0。
功率需求: 36.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 52.16 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 44.96 kW。
功率需求计算已禁用，直接使用充电桩功率: 8.48 kW。
功率需求计算已禁用，直接使用充电桩功率: 30.88 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 46.24 kW。
初次设置charger_power=61.19999999999999。
功率需求: 48.00 kW, 充电桩功率: 61.20 kW, 最终充电功率: 48.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 44.96287822723389, -9.130101831071938
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 52.16, -10.591539738669653
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 8.480000000000018, -1.7219374421763582
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 30.88, -6.2704514403780465
已在 set_all_batteries_before_solve 中设置 batt_ev_031 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 46.24000000000001, -9.38943246771635
已在 set_all_batteries_before_solve 中设置 batt_ev_006 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_225 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.57 更新为 0.57。
SOC从 0.81 更新为 1.00。
SOC从 0.52 更新为 0.71。
SOC从 0.35 更新为 0.63。
SOC从 0.78 更新为 0.93。
SOC从 0.97 更新为 1.00。
SOC从 0.86 更新为 1.00。
SOC从 0.42 更新为 0.42。
SOC从 0.86 更新为 1.00。
SOC从 0.82 更新为 0.96。
已断开电池: batt_ev_221
时间步 28: 电池 batt_ev_221 已离开，当前SOC: 92.7%，能量满足率: 92.4%
已断开电池: batt_ev_101
时间步 28 执行前: 电池 batt_ev_101 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_093
时间步 28 执行前: 电池 batt_ev_093 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_047
时间步 28 执行前: 电池 batt_ev_047 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_111
时间步 28 执行前: 电池 batt_ev_111 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_006
时间步 28: 电池 batt_ev_006 已离开，当前SOC: 57.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.1303104031654512, voltage=-0.2781419796241935, ctrl=-0.0, connection=8.16, completion=5.3921568627450975, energy=7.087061285397814, transformer=0.
已连接电池 batt_ev_129, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 94kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_129 已接入
已连接电池 batt_ev_088, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 50kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_088 已接入
已连接电池 batt_ev_007, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 84kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_007 已接入
已连接电池 batt_ev_142, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_142 已接入
已连接电池 batt_ev_147, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_147 已接入
已连接电池 batt_ev_079, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 78kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.44119668
 -1.         -1.         -0.         -0.84301597 -0.84981275]
初次设置charger_power=0.0。
功率需求: 100.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 108.48 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
初次设置charger_power=44.11966800689697。
功率需求: 80.00 kW, 充电桩功率: 44.12 kW, 最终充电功率: 44.12 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=60.0。
功率需求: 36.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 36.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=84.3015968799591。
功率需求: 100.00 kW, 充电桩功率: 84.30 kW, 最终充电功率: 84.30 kW。
功率需求计算已禁用，直接使用充电桩功率: 13.20 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_031 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_225 充电的有无功功率为 108.48000000000003, -22.02780350557677
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 13.19999999999999, -2.680374320368852
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_007 充电的有无功功率为 44.11966800689697, -8.958880693097422
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_147 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 84.3015968799591, -17.118169351752236
SOC从 0.28 更新为 0.28。
SOC从 0.38 更新为 0.62。
SOC从 0.71 更新为 1.00。
SOC从 0.63 更新为 0.90。
SOC从 0.32 更新为 0.45。
SOC从 0.32 更新为 0.56。
SOC从 0.52 更新为 0.67。
SOC从 0.42 更新为 0.42。
SOC从 0.08 更新为 0.35。
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_057
时间步 29 执行前: 电池 batt_ev_057 已充满 (SOC: 90.2%)，离开
已断开电池: batt_ev_225
时间步 29 执行前: 电池 batt_ev_225 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_054
时间步 29 执行前: 电池 batt_ev_054 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.1414967699555777, voltage=-0.28570600821459013, ctrl=-0.0, connection=8.4, completion=5.523809523809524, energy=7.170288105815019, transformer=0.
时间步 29: 电池 batt_ev_156 已错过离开时间，无法接入
已连接电池 batt_ev_053, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_053 已接入
已连接电池 batt_ev_211, 初始SOC: 62.0%, 最大功率: 120kW, 电池容量: 106kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_211 已接入
已连接电池 batt_ev_017, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.41773677
 -1.         -1.         -0.         -0.9489307  -0.92011416]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=100.0。
功率需求: 80.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 41.77 kW。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 94.89 kW。
初次设置charger_power=55.206849575042725。
功率需求: 60.00 kW, 充电桩功率: 55.21 kW, 最终充电功率: 55.21 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_031 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_007 充电的有无功功率为 41.77367687225342, -8.482506875437455
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_147 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 94.89306807518005, -19.268859306797438
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 55.206849575042725, -11.210228932531116
SOC从 0.28 更新为 0.28。
SOC从 0.62 更新为 0.92。
SOC从 0.32 更新为 0.53。
SOC从 0.62 更新为 0.79。
SOC从 0.45 更新为 0.58。
SOC从 0.56 更新为 0.86。
SOC从 0.67 更新为 0.91。
SOC从 0.42 更新为 0.42。
SOC从 0.35 更新为 0.65。
SOC从 0.28 更新为 0.49。
已断开电池: batt_ev_007
时间步 30: 电池 batt_ev_007 已离开，当前SOC: 57.6%，能量满足率: 38.7%
已断开电池: batt_ev_147
时间步 30 执行前: 电池 batt_ev_147 已充满 (SOC: 91.3%)，离开
奖励各项的值：powerloss=-0.15624525409067128, voltage=-0.30496174867656434, ctrl=-0.0, connection=8.56, completion=5.5140186915887845, energy=7.165915011525534, transformer=0.
已连接电池 batt_ev_087, 初始SOC: 62.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_087 已接入
时间步 30: 电池 batt_ev_021 已错过离开时间，无法接入
已连接电池 batt_ev_209, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_209 已接入
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.37951934
 -1.         -1.         -0.         -1.         -1.        ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 16.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 89.12 kW。
初次设置charger_power=37.95193433761597。
功率需求: 60.00 kW, 充电桩功率: 37.95 kW, 最终充电功率: 37.95 kW。
功率需求计算已禁用，直接使用充电桩功率: 56.00 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_031 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 16.0, -3.248938570144066
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 56.0, -11.37128499550423
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 89.12, -18.09658783570245
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 37.95193433761597, -7.706468955065968
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 48.0, -9.746815710432196
SOC从 0.28 更新为 0.28。
SOC从 0.92 更新为 1.00。
SOC从 0.53 更新为 0.79。
SOC从 0.79 更新为 1.00。
SOC从 0.62 更新为 0.72。
SOC从 0.86 更新为 1.00。
SOC从 0.38 更新为 0.59。
SOC从 0.42 更新为 0.42。
SOC从 0.65 更新为 0.97。
SOC从 0.49 更新为 0.72。
已断开电池: batt_ev_088
时间步 31 执行前: 电池 batt_ev_088 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_142
时间步 31 执行前: 电池 batt_ev_142 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_211
时间步 31 执行前: 电池 batt_ev_211 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.16724159255362497, voltage=-0.25712891558208106, ctrl=-0.0, connection=8.8, completion=5.636363636363636, energy=7.243208238483929, transformer=0.
已连接电池 batt_ev_178, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 93kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_178 已接入
已连接电池 batt_ev_110, 初始SOC: 22.0%, 最大功率: 100kW, 电池容量: 65kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_110 已接入
已连接电池 batt_ev_112, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 71kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_112 已接入
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.42391926
 -1.         -1.         -0.         -0.93183964 -0.9046211 ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=100.0。
功率需求: 80.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 81.12 kW。
初次设置charger_power=100.0。
功率需求: 100.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 100.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 42.39 kW。
初次设置charger_power=80.0。
功率需求: 80.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 7.84 kW。
功率需求计算已禁用，直接使用充电桩功率: 54.28 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_031 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 7.839999999999975, -1.5919798993705871
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 81.12, -16.472118550630412
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 54.27726745605469, -11.021469232500085
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 42.39192605018616, -8.608047725446548
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_178 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_110 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.28 更新为 0.28。
SOC从 0.42 更新为 0.64。
SOC从 0.79 更新为 1.00。
SOC从 0.22 更新为 0.60。
SOC从 0.72 更新为 0.84。
SOC从 0.22 更新为 0.50。
SOC从 0.59 更新为 0.85。
SOC从 0.42 更新为 0.42。
SOC从 0.97 更新为 1.00。
SOC从 0.72 更新为 0.92。
已断开电池: batt_ev_031
时间步 32: 电池 batt_ev_031 已离开，当前SOC: 42.0%，能量满足率: 0.0%
已断开电池: batt_ev_129
时间步 32: 电池 batt_ev_129 已离开，当前SOC: 28.0%，能量满足率: 0.0%
已断开电池: batt_ev_079
时间步 32 执行前: 电池 batt_ev_079 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_053
时间步 32 执行前: 电池 batt_ev_053 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_087
时间步 32: 电池 batt_ev_087 已离开，当前SOC: 84.1%，能量满足率: 73.6%
已断开电池: batt_ev_178
时间步 32: 电池 batt_ev_178 已离开，当前SOC: 63.5%，能量满足率: 38.4%
已断开电池: batt_ev_110
时间步 32: 电池 batt_ev_110 已离开，当前SOC: 60.5%，能量满足率: 64.1%
奖励各项的值：powerloss=-0.18553790925714714, voltage=-0.24111275428293721, ctrl=-0.0, connection=9.36, completion=5.47008547008547, energy=7.131302416907629, transformer=0.
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
智能体的动作为: [ 1.         -0.         -1.         -1.         -1.         -0.4248839
 -1.         -1.         -0.         -0.9291444  -0.90217096]
初次设置charger_power=0.0。
功率需求: 100.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=100.0。
功率需求: 100.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=60.0。
功率需求: 36.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 36.00 kW。
初次设置charger_power=25.49303412437439。
功率需求: 60.00 kW, 充电桩功率: 25.49 kW, 最终充电功率: 25.49 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 35.84 kW。
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=41.04000000000002。
功率需求: 24.00 kW, 充电桩功率: 41.04 kW, 最终充电功率: 24.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 20.60 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 20.599999999999994, -4.183008409060482
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 35.839999999999996, -7.277622397122709
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_223 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_198 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 25.49303412437439, -5.176581364792426
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 24.0, -4.873407855216098
SOC从 0.22 更新为 0.22。
SOC从 0.28 更新为 0.59。
SOC从 0.08 更新为 0.36。
SOC从 0.68 更新为 0.86。
SOC从 0.12 更新为 0.27。
SOC从 0.50 更新为 0.78。
SOC从 0.85 更新为 1.00。
SOC从 0.32 更新为 0.32。
SOC从 0.82 更新为 0.93。
SOC从 0.92 更新为 1.00。
已断开电池: batt_ev_017
时间步 33 执行前: 电池 batt_ev_017 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_209
时间步 33 执行前: 电池 batt_ev_209 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_112
时间步 33: 电池 batt_ev_112 已离开，当前SOC: 78.3%，能量满足率: 93.9%
已断开电池: batt_ev_223
时间步 33: 电池 batt_ev_223 已离开，当前SOC: 22.0%，能量满足率: 0.0%
已断开电池: batt_ev_198
时间步 33: 电池 batt_ev_198 已离开，当前SOC: 36.4%，能量满足率: 33.8%
奖励各项的值：powerloss=-0.19574927769736375, voltage=-0.3085054827467415, ctrl=-0.0, connection=9.76, completion=5.409836065573771, energy=7.107656465342044, transformer=0.
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
智能体的动作为: [ 1.         -0.         -1.         -0.9682847  -1.         -0.4743356
 -1.         -1.         -0.         -0.67498446 -0.7815852 ]
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=58.097083568573。
功率需求: 60.00 kW, 充电桩功率: 58.10 kW, 最终充电功率: 58.10 kW。
功率需求计算已禁用，直接使用充电桩功率: 29.28 kW。
功率需求计算已禁用，直接使用充电桩功率: 28.46 kW。
初次设置charger_power=100.0。
功率需求: 80.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 80.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 17.04 kW。
初次设置charger_power=46.89511299133301。
功率需求: 48.00 kW, 充电桩功率: 46.90 kW, 最终充电功率: 46.90 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 29.28, -5.94555758336364
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 28.460136651992798, -5.779077230014387
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 17.039999999999992, -3.4601195772034288
已在 set_all_batteries_before_solve 中设置 batt_ev_155 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_094 充电的有无功功率为 58.097083568573, -11.79711597617624
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_068 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_185 充电的有无功功率为 46.89511299133301, -9.522458834300366
SOC从 0.52 更新为 0.52。
SOC从 0.59 更新为 0.90。
SOC从 0.28 更新为 0.54。
SOC从 0.86 更新为 1.00。
SOC从 0.27 更新为 0.43。
SOC从 0.38 更新为 0.68。
SOC从 0.18 更新为 0.42。
SOC从 0.32 更新为 0.32。
SOC从 0.93 更新为 1.00。
SOC从 0.48 更新为 0.77。
已断开电池: batt_ev_207
时间步 34: 电池 batt_ev_207 已离开，当前SOC: 90.5%，能量满足率: 89.3%
已断开电池: batt_ev_152
时间步 34 执行前: 电池 batt_ev_152 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_171
时间步 34: 电池 batt_ev_171 已离开，当前SOC: 43.3%，能量满足率: 39.2%
已断开电池: batt_ev_022
时间步 34: 电池 batt_ev_022 已离开，当前SOC: 32.0%，能量满足率: 0.0%
已断开电池: batt_ev_028
时间步 34 执行前: 电池 batt_ev_028 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_068
时间步 34: 电池 batt_ev_068 已离开，当前SOC: 42.2%，能量满足率: 40.3%
奖励各项的值：powerloss=-0.21215506370251572, voltage=-0.32928467544075746, ctrl=-0.0, connection=10.24, completion=5.3125, energy=7.062605647781092, transformer=0.
已连接电池 batt_ev_049, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
已连接电池 batt_ev_023, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.8074876  -1.         -0.5091415
 -1.         -1.         -0.         -0.50649357 -0.8175704 ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 48.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 48.45 kW。
初次设置charger_power=17.599999999999994。
功率需求: 15.00 kW, 充电桩功率: 17.60 kW, 最终充电功率: 15.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 86.16 kW。
功率需求计算已禁用，直接使用充电桩功率: 36.32 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_155 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_094 充电的有无功功率为 48.4492564201355, -9.83804111738614
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 86.16, -17.495534200225794
已在 set_all_batteries_before_solve 中设置 batt_ev_185 充电的有无功功率为 36.31999999999999, -7.375090554227028
已在 set_all_batteries_before_solve 中设置 batt_ev_049 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_023 充电的有无功功率为 15.0, -3.045879909510062
SOC从 0.52 更新为 0.52。
SOC从 0.32 更新为 0.55。
SOC从 0.54 更新为 0.76。
SOC从 0.92 更新为 0.99。
SOC从 0.68 更新为 1.00。
SOC从 0.77 更新为 1.00。
已断开电池: batt_ev_155
时间步 35: 电池 batt_ev_155 已离开，当前SOC: 52.0%，能量满足率: 0.0%
已断开电池: batt_ev_094
时间步 35: 电池 batt_ev_094 已离开，当前SOC: 75.6%，能量满足率: 67.9%
已断开电池: batt_ev_140
时间步 35 执行前: 电池 batt_ev_140 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_185
时间步 35 执行前: 电池 batt_ev_185 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.21476525803662852, voltage=-0.3022564697610841, ctrl=-0.0, connection=10.56, completion=5.303030303030303, energy=7.051567350476656, transformer=0.
已连接电池 batt_ev_121, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [ 1.         -0.13358267 -1.         -0.6591669  -0.847341   -0.82117337
 -1.         -1.         -0.         -0.22182837 -0.8757619 ]
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 2.60 kW。
初次设置charger_power=65.69386959075928。
功率需求: 64.00 kW, 充电桩功率: 65.69 kW, 最终充电功率: 64.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_049 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_023 充电的有无功功率为 2.5999999999999943, -0.5279525176484094
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.55 更新为 0.83。
SOC从 0.99 更新为 1.00。
SOC从 0.48 更新为 0.75。
已断开电池: batt_ev_049
时间步 36: 电池 batt_ev_049 已离开，当前SOC: 82.9%，能量满足率: 77.2%
已断开电池: batt_ev_023
时间步 36 执行前: 电池 batt_ev_023 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.21371468837785082, voltage=-0.3835400144056833, ctrl=-0.0, connection=10.72, completion=5.298507462686567, energy=7.078549154185524, transformer=0.
智能体的动作为: [ 1.         -0.         -1.         -0.42556703 -0.59483683 -0.8556508
 -1.         -1.         -0.         -0.1580778  -0.7820036 ]
功率需求计算已禁用，直接使用充电桩功率: 58.72 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 58.72, -11.92360455242872
SOC从 0.75 更新为 1.00。
已断开电池: batt_ev_121
时间步 37 执行前: 电池 batt_ev_121 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.2126268811972161, voltage=-0.41941839586350893, ctrl=-0.0, connection=10.8, completion=5.333333333333333, energy=7.100189530821187, transformer=0.
已连接电池 batt_ev_015, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
已连接电池 batt_ev_201, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [ 0.47110486 -0.39362797 -0.8506187  -0.40604082 -0.52607423 -0.66909105
 -0.98421955 -0.         -0.19579718 -0.         -0.03148349]
初次设置charger_power=0.0。
功率需求: 36.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=23.49566102027893。
功率需求: 120.00 kW, 充电桩功率: 23.50 kW, 最终充电功率: 23.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 23.49566102027893, -4.770997457488418
SOC从 0.52 更新为 0.52。
SOC从 0.18 更新为 0.24。
奖励各项的值：powerloss=-0.20928615004842718, voltage=-0.4431163269722571, ctrl=-0.0, connection=10.8, completion=5.333333333333333, energy=7.100189530821187, transformer=0.
已连接电池 batt_ev_080, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_204, 初始SOC: 2.0%, 最大功率: 80kW, 电池容量: 81kWh，并创BMS。
智能体的动作为: [ 0.7408893  -0.38722193 -1.         -0.31846756 -0.8226223  -0.6216463
 -0.6657749  -0.18176845 -0.         -0.         -0.        ]
初次设置charger_power=30.977754592895508。
功率需求: 80.00 kW, 充电桩功率: 30.98 kW, 最终充电功率: 30.98 kW。
功率需求计算已禁用，直接使用充电桩功率: 10.91 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求: 36.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 10.90610682964325, -2.214579445558723
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 30.977754592895508, -6.29030135708223
SOC从 0.02 更新为 0.12。
SOC从 0.52 更新为 0.56。
SOC从 0.24 更新为 0.24。
SOC从 0.57 更新为 0.57。
奖励各项的值：powerloss=-0.20890644699064598, voltage=-0.4428430847092324, ctrl=-0.0, connection=10.8, completion=5.333333333333333, energy=7.100189530821187, transformer=0.
已连接电池 batt_ev_183, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 71kWh，并创BMS。
已连接电池 batt_ev_230, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [ 0.6991557  -0.41119367 -1.         -0.33468127 -0.70793694 -0.59510666
 -0.6913165  -0.10882221 -0.04726534 -0.         -0.        ]
功率需求计算已禁用，直接使用充电桩功率: 32.90 kW。
初次设置charger_power=33.46812725067139。
功率需求: 80.00 kW, 充电桩功率: 33.47 kW, 最终充电功率: 33.47 kW。
初次设置charger_power=41.478989124298096。
功率需求: 36.00 kW, 充电桩功率: 41.48 kW, 最终充电功率: 36.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 6.53 kW。
功率需求计算已禁用，直接使用充电桩功率: 5.67 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 6.52933269739151, -1.3258375523661292
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 5.671841204166412, -1.1517164782467888
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 32.895493507385254, -6.679714852504227
已在 set_all_batteries_before_solve 中设置 batt_ev_183 充电的有无功功率为 33.46812725067139, -6.795993093449746
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 36.0, -7.310111782824148
SOC从 0.12 更新为 0.22。
SOC从 0.38 更新为 0.50。
SOC从 0.52 更新为 0.66。
SOC从 0.56 更新为 0.59。
SOC从 0.24 更新为 0.25。
SOC从 0.57 更新为 0.57。
奖励各项的值：powerloss=-0.20713673073145683, voltage=-0.4680611773059429, ctrl=-0.0, connection=10.8, completion=5.333333333333333, energy=7.100189530821187, transformer=0.
智能体的动作为: [ 1.         -0.         -1.         -0.4409753  -0.54582685 -0.7947134
 -1.         -0.9892752  -0.         -0.15318921 -0.7643007 ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 44.10 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 59.36 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 9.19 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 59.356513023376465, -12.052854034431647
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 9.191352725028992, -1.866383773759091
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_183 充电的有无功功率为 44.09753084182739, -8.954385550008158
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.22 更新为 0.22。
SOC从 0.50 更新为 0.65。
SOC从 0.66 更新为 0.89。
SOC从 0.59 更新为 0.83。
SOC从 0.25 更新为 0.25。
SOC从 0.57 更新为 0.61。
已断开电池: batt_ev_201
时间步 41: 电池 batt_ev_201 已离开，当前SOC: 25.1%，能量满足率: 10.1%
已断开电池: batt_ev_204
时间步 41: 电池 batt_ev_204 已离开，当前SOC: 21.7%，能量满足率: 20.5%
已断开电池: batt_ev_183
时间步 41 执行前: 电池 batt_ev_183 已充满 (SOC: 65.3%)，离开
已断开电池: batt_ev_230
时间步 41: 电池 batt_ev_230 已离开，当前SOC: 88.9%，能量满足率: 80.3%
奖励各项的值：powerloss=-0.20932981881706414, voltage=-0.38164419720243314, ctrl=-0.0, connection=11.120000000000001, completion=5.2517985611510785, energy=7.047596455754832, transformer=0.
智能体的动作为: [ 1.         -0.01316973 -1.         -0.43043497 -0.6716375  -0.9061588
 -1.         -1.         -0.         -0.13930862 -0.7887451 ]
功率需求计算已禁用，直接使用充电桩功率: 40.32 kW。
功率需求计算已禁用，直接使用充电桩功率: 8.36 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 40.31999999999999, -8.187325196763044
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 8.358516991138458, -1.697269265107141
SOC从 0.83 更新为 1.00。
SOC从 0.61 更新为 0.65。
已断开电池: batt_ev_015
时间步 42 执行前: 电池 batt_ev_015 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_080
时间步 42: 电池 batt_ev_080 已离开，当前SOC: 65.1%，能量满足率: 23.2%
奖励各项的值：powerloss=-0.20614051937013783, voltage=-0.23003550275489948, ctrl=-0.0, connection=11.28, completion=5.24822695035461, energy=7.035025948033143, transformer=0.
已连接电池 batt_ev_148, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_215, 初始SOC: 62.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_210, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [ 0.5406002  -0.45685077 -0.8605265  -0.3916525  -0.52512896 -0.56193966
 -0.79856074 -0.         -0.2301925  -0.         -0.        ]
初次设置charger_power=103.26318025588989。
功率需求: 72.00 kW, 充电桩功率: 103.26 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=31.507737636566162。
功率需求: 36.00 kW, 充电桩功率: 31.51 kW, 最终充电功率: 31.51 kW。
初次设置charger_power=0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 31.507737636566162, -6.3979190040887275
SOC从 0.62 更新为 0.86。
SOC从 0.57 更新为 0.71。
SOC从 0.28 更新为 0.28。
奖励各项的值：powerloss=-0.20343353823816565, voltage=-0.11673717162511643, ctrl=-0.0, connection=11.28, completion=5.24822695035461, energy=7.035025948033143, transformer=0.
智能体的动作为: [ 1.         -0.         -1.         -0.48122767 -0.5123891  -0.73867065
 -1.         -0.7961833  -0.         -0.12033449 -0.73368907]
功率需求计算已禁用，直接使用充电桩功率: 43.52 kW。
功率需求计算已禁用，直接使用充电桩功率: 30.74 kW。
功率需求计算已禁用，直接使用充电桩功率: 88.04 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 88.04268836975098, -17.877830378978643
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 43.51999999999999, -8.837112910791856
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 30.74334740638733, -6.242702947746896
SOC从 0.86 更新为 1.00。
SOC从 0.71 更新为 0.85。
SOC从 0.28 更新为 0.52。
已断开电池: batt_ev_215
时间步 44 执行前: 电池 batt_ev_215 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_210
时间步 44: 电池 batt_ev_210 已离开，当前SOC: 85.3%，能量满足率: 69.0%
奖励各项的值：powerloss=-0.19896965063421895, voltage=-0.11218745680809938, ctrl=-0.0, connection=11.44, completion=5.244755244755245, energy=7.054848356587158, transformer=0.
已连接电池 batt_ev_146, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
已连接电池 batt_ev_027, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 107kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.421192   -0.67741543 -0.9005763
 -1.         -1.         -0.         -0.14952253 -0.78087336]
初次设置charger_power=0.0。
功率需求: 96.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=72.04610347747803。
功率需求: 64.00 kW, 充电桩功率: 72.05 kW, 最终充电功率: 64.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 93.70 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 93.70480298995972, -19.027571790114443
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 0.0, -0.0
SOC从 0.32 更新为 0.32。
SOC从 0.42 更新为 0.62。
SOC从 0.52 更新为 0.78。
奖励各项的值：powerloss=-0.19503899114725387, voltage=-0.05895883558803883, ctrl=-0.0, connection=11.44, completion=5.244755244755245, energy=7.054848356587158, transformer=0.
已连接电池 batt_ev_135, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_127, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 88kWh，并创BMS。
已连接电池 batt_ev_165, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 105kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.4212589  -0.6762864  -0.90013707
 -1.         -1.         -0.         -0.14976586 -0.7809421 ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=33.700711727142334。
功率需求: 64.00 kW, 充电桩功率: 33.70 kW, 最终充电功率: 33.70 kW。
功率需求计算已禁用，直接使用充电桩功率: 72.01 kW。
初次设置charger_power=100.0。
功率需求: 100.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.32 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 80.32, -16.309671622123208
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 72.01096534729004, -14.622450174382397
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 33.700711727142334, -6.843221385726198
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 0.0, -0.0
SOC从 0.32 更新为 0.32。
SOC从 0.32 更新为 0.48。
SOC从 0.62 更新为 0.85。
SOC从 0.18 更新为 0.46。
SOC从 0.18 更新为 0.18。
SOC从 0.78 更新为 1.00。
已断开电池: batt_ev_148
时间步 46 执行前: 电池 batt_ev_148 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_027
时间步 46: 电池 batt_ev_027 已离开，当前SOC: 32.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.19054052600537785, voltage=-0.06832409974722342, ctrl=-0.0, connection=11.6, completion=5.241379310344828, energy=7.026505620634231, transformer=0.
已连接电池 batt_ev_003, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_001, 初始SOC: 38.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
已连接电池 batt_ev_086, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
智能体的动作为: [ 1.         -0.06060549 -1.         -0.7408422  -0.985311   -0.7518431
 -1.         -1.         -0.         -0.29047948 -0.8721844 ]
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 59.27 kW。
功率需求计算已禁用，直接使用充电桩功率: 47.28 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
初次设置charger_power=100.0。
功率需求: 80.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=34.85753774642944。
功率需求: 96.00 kW, 充电桩功率: 34.86 kW, 最终充电功率: 34.86 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 47.27999999999997, -9.60061347477571
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 59.267377853393555, -12.034754366199536
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 34.85753774642944, -7.078124927789204
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.12 更新为 0.37。
SOC从 0.48 更新为 0.75。
SOC从 0.85 更新为 1.00。
SOC从 0.46 更新为 0.75。
SOC从 0.42 更新为 0.68。
SOC从 0.18 更新为 0.18。
SOC从 0.38 更新为 0.50。
已断开电池: batt_ev_146
时间步 47 执行前: 电池 batt_ev_146 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_135
时间步 47: 电池 batt_ev_135 已离开，当前SOC: 75.1%，能量满足率: 65.2%
奖励各项的值：powerloss=-0.17845626454879793, voltage=-0.13542925324026678, ctrl=-0.0, connection=11.76, completion=5.238095238095238, energy=7.043312136160084, transformer=0.
智能体的动作为: [ 1.         -0.         -1.         -0.75933826 -1.         -0.52089214
 -1.         -1.         -0.         -0.4154024  -0.78663987]
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 88.64 kW。
功率需求计算已禁用，直接使用充电桩功率: 98.64 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 49.85 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 88.63999999999999, -17.99911967859812
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 98.63999999999999, -20.02970628493816
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 49.848289489746094, -10.122126898683945
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.37 更新为 0.62。
SOC从 0.75 更新为 1.00。
SOC从 0.68 更新为 1.00。
SOC从 0.18 更新为 0.18。
SOC从 0.50 更新为 0.68。
已断开电池: batt_ev_127
时间步 48 执行前: 电池 batt_ev_127 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_165
时间步 48: 电池 batt_ev_165 已离开，当前SOC: 18.0%，能量满足率: 0.0%
已断开电池: batt_ev_003
时间步 48 执行前: 电池 batt_ev_003 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.1547971470926374, voltage=-0.17719364422961625, ctrl=-0.0, connection=12.0, completion=5.266666666666666, energy=7.035779226770217, transformer=0.
已连接电池 batt_ev_043, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_051, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
已连接电池 batt_ev_144, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [ 1.         -0.01400742 -1.         -0.74570733 -1.         -0.7400777
 -1.         -1.         -0.         -0.2662773  -0.8347171 ]
初次设置charger_power=1.4007419347763062。
功率需求: 80.00 kW, 充电桩功率: 1.40 kW, 最终充电功率: 1.40 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=80.0。
功率需求: 64.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 64.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 31.95 kW。
初次设置charger_power=66.77736759185791。
功率需求: 80.00 kW, 充电桩功率: 66.78 kW, 最终充电功率: 66.78 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 31.953277587890625, -6.488389749863612
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 1.4007419347763062, -0.2844327811695603
已在 set_all_batteries_before_solve 中设置 batt_ev_144 充电的有无功功率为 66.77736759185791, -13.559722823867217
SOC从 0.48 更新为 0.48。
SOC从 0.62 更新为 0.87。
SOC从 0.42 更新为 0.66。
SOC从 0.68 更新为 0.80。
SOC从 0.22 更新为 0.55。
已断开电池: batt_ev_001
时间步 49: 电池 batt_ev_001 已离开，当前SOC: 79.7%，能量满足率: 69.4%
已断开电池: batt_ev_144
时间步 49 执行前: 电池 batt_ev_144 已充满 (SOC: 54.7%)，离开
奖励各项的值：powerloss=-0.126203982945958, voltage=-0.22144471798660748, ctrl=-0.0, connection=12.16, completion=5.263157894736842, energy=7.054669349726247, transformer=0.
已连接电池 batt_ev_188, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
已连接电池 batt_ev_107, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 60kWh，并创BMS。
已连接电池 batt_ev_131, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [ 1.         -0.18850222 -1.         -0.4977282  -0.63078064 -0.91254896
 -1.         -0.95370597 -0.         -0.07478671 -0.82857025]
功率需求计算已禁用，直接使用充电桩功率: 18.85 kW。
功率需求计算已禁用，直接使用充电桩功率: 31.20 kW。
初次设置charger_power=59.727383852005005。
功率需求: 120.00 kW, 充电桩功率: 59.73 kW, 最终充电功率: 59.73 kW。
功率需求计算已禁用，直接使用充电桩功率: 50.46 kW。
初次设置charger_power=73.00391674041748。
功率需求: 80.00 kW, 充电桩功率: 73.00 kW, 最终充电功率: 73.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 31.19999999999999, -6.335430211780926
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 50.46245098114014, -10.246837708539402
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 18.85022222995758, -3.827700878668516
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 59.727383852005005, -12.128162568161184
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 73.00391674041748, -14.824077554345525
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.48 更新为 0.53。
SOC从 0.87 更新为 1.00。
SOC从 0.18 更新为 0.35。
SOC从 0.66 更新为 0.85。
SOC从 0.28 更新为 0.58。
SOC从 0.22 更新为 0.55。
已断开电池: batt_ev_086
时间步 50 执行前: 电池 batt_ev_086 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_051
时间步 50: 电池 batt_ev_051 已离开，当前SOC: 53.3%，能量满足率: 15.5%
奖励各项的值：powerloss=-0.12494365282486034, voltage=-0.25618804587713484, ctrl=-0.0, connection=12.32, completion=5.25974025974026, energy=7.03805185880798, transformer=0.
已连接电池 batt_ev_136, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
已连接电池 batt_ev_116, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 52kWh，并创BMS。
已连接电池 batt_ev_196, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [ 1.         -0.08867539 -1.         -0.7366339  -0.9558617  -0.7590253
 -1.         -1.         -0.         -0.300937   -0.8908719 ]
功率需求计算已禁用，直接使用充电桩功率: 88.40 kW。
功率需求计算已禁用，直接使用充电桩功率: 38.64 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.72 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=80.0。
功率需求: 64.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 64.00 kW。
初次设置charger_power=0.0。
功率需求: 64.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=18.056219816207886。
功率需求: 60.00 kW, 充电桩功率: 18.06 kW, 最终充电功率: 18.06 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 38.639999999999986, -7.846186646897916
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 88.39606761932373, -17.949587096092735
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 60.72202205657959, -12.330132469797505
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 64.0, -12.995754280576264
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 18.056219816207886, -3.666471811992337
SOC从 0.35 更新为 0.61。
SOC从 0.85 更新为 1.00。
SOC从 0.58 更新为 0.84。
SOC从 0.55 更新为 0.87。
SOC从 0.42 更新为 0.62。
SOC从 0.42 更新为 0.42。
SOC从 0.18 更新为 0.28。
已断开电池: batt_ev_043
时间步 51 执行前: 电池 batt_ev_043 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_131
时间步 51: 电池 batt_ev_131 已离开，当前SOC: 87.2%，能量满足率: 85.8%
奖励各项的值：powerloss=-0.12405801982731542, voltage=-0.29066972786594203, ctrl=-0.0, connection=12.48, completion=5.256410256410256, energy=7.066930909963905, transformer=0.
已连接电池 batt_ev_005, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_063, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
已连接电池 batt_ev_033, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
已连接电池 batt_ev_077, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
已连接电池 batt_ev_082, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.75998765 -1.         -0.6641191
 -1.         -1.         -0.         -0.23192608 -0.72587246]
初次设置charger_power=0.0。
功率需求: 36.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 91.20 kW。
初次设置charger_power=80.0。
功率需求: 80.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 39.08 kW。
初次设置charger_power=80.0。
功率需求: 64.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 64.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 13.92 kW。
初次设置charger_power=43.55234742164612。
功率需求: 48.00 kW, 充电桩功率: 43.55 kW, 最终充电功率: 43.55 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 91.1985182762146, -18.51864897297388
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 39.08000000000002, -7.935532457576883
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 13.915565013885498, -2.8256759936849956
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 43.55234742164612, -8.843681334906282
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.52 更新为 0.52。
SOC从 0.32 更新为 0.57。
SOC从 0.61 更新为 0.88。
SOC从 0.18 更新为 0.43。
SOC从 0.84 更新为 1.00。
SOC从 0.38 更新为 0.69。
SOC从 0.62 更新为 0.86。
SOC从 0.42 更新为 0.42。
SOC从 0.28 更新为 0.36。
SOC从 0.38 更新为 0.58。
已断开电池: batt_ev_107
时间步 52 执行前: 电池 batt_ev_107 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.13427174224447042, voltage=-0.29050660893074953, ctrl=-0.0, connection=12.56, completion=5.286624203821656, energy=7.085612878690251, transformer=0.
已连接电池 batt_ev_159, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 53kWh，并创BMS。
时间步 52 执行前: 排队电池 batt_ev_159 已接入
智能体的动作为: [ 1.         -0.         -1.         -0.98580086 -1.         -0.46230936
 -1.         -1.         -0.00419441 -0.71426    -0.78982   ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 42.76 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
初次设置charger_power=36.98474884033203。
功率需求: 48.00 kW, 充电桩功率: 36.98 kW, 最终充电功率: 36.98 kW。
功率需求计算已禁用，直接使用充电桩功率: 62.48 kW。
功率需求计算已禁用，直接使用充电桩功率: 46.24 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.34 kW。
功率需求计算已禁用，直接使用充电桩功率: 42.86 kW。
功率需求计算已禁用，直接使用充电桩功率: 47.39 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 42.75999999999999, -8.682788328710014
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 46.24000000000001, -9.38943246771635
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 0.3355530649423599, -0.06813695593883061
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 42.85559892654419, -8.702200518692127
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 47.389200925827026, -9.622787668514142
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 62.47999999999999, -12.687105116412575
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 36.98474884033203, -7.510073563402859
SOC从 0.52 更新为 0.52。
SOC从 0.57 更新为 0.88。
SOC从 0.88 更新为 1.00。
SOC从 0.43 更新为 0.69。
SOC从 0.68 更新为 0.85。
SOC从 0.69 更新为 1.00。
SOC从 0.86 更新为 1.00。
SOC从 0.42 更新为 0.42。
SOC从 0.36 更新为 0.60。
SOC从 0.58 更新为 0.80。
已断开电池: batt_ev_188
时间步 53 执行前: 电池 batt_ev_188 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_136
时间步 53 执行前: 电池 batt_ev_136 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_116
时间步 53: 电池 batt_ev_116 已离开，当前SOC: 42.2%，能量满足率: 0.3%
已断开电池: batt_ev_077
时间步 53: 电池 batt_ev_077 已离开，当前SOC: 68.6%，能量满足率: 63.3%
已断开电池: batt_ev_082
时间步 53 执行前: 电池 batt_ev_082 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.13319576980823206, voltage=-0.26597756342667367, ctrl=-0.0, connection=12.96, completion=5.3086419753086425, energy=7.09134449633267, transformer=0.
时间步 53: 电池 batt_ev_097 已错过离开时间，无法接入
已连接电池 batt_ev_105, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_105 已接入
已连接电池 batt_ev_058, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_058 已接入
已连接电池 batt_ev_118, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 90kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_118 已接入
已连接电池 batt_ev_199, 初始SOC: 52.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_153, 初始SOC: 2.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.78662694 -1.         -0.51073223
 -1.         -1.         -0.         -0.4851364  -0.8220267 ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 47.84 kW。
初次设置charger_power=47.19761610031128。
功率需求: 48.00 kW, 充电桩功率: 47.20 kW, 最终充电功率: 47.20 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 30.84 kW。
初次设置charger_power=120.0。
功率需求: 72.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=100.0。
功率需求: 60.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 29.11 kW。
功率需求计算已禁用，直接使用充电桩功率: 42.96 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 29.10818338394165, -5.910668731432166
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 42.96000000000001, -8.723400060836818
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 47.839999999999975, -9.71432632473075
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 30.84000000000001, -6.262329093952687
已在 set_all_batteries_before_solve 中设置 batt_ev_105 充电的有无功功率为 47.19761610031128, -9.583884710447116
已在 set_all_batteries_before_solve 中设置 batt_ev_058 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 0.0, -0.0
SOC从 0.52 更新为 0.52。
SOC从 0.88 更新为 1.00。
SOC从 0.42 更新为 0.65。
SOC从 0.28 更新为 0.50。
SOC从 0.85 更新为 1.00。
SOC从 0.57 更新为 0.77。
SOC从 0.52 更新为 0.72。
SOC从 0.02 更新为 0.02。
SOC从 0.60 更新为 0.77。
SOC从 0.80 更新为 1.00。
已断开电池: batt_ev_005
时间步 54 执行前: 电池 batt_ev_005 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_033
时间步 54 执行前: 电池 batt_ev_033 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_159
时间步 54 执行前: 电池 batt_ev_159 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_105
时间步 54: 电池 batt_ev_105 已离开，当前SOC: 64.7%，能量满足率: 40.5%
已断开电池: batt_ev_058
时间步 54 执行前: 电池 batt_ev_058 已充满 (SOC: 49.7%)，离开
奖励各项的值：powerloss=-0.1347286555087274, voltage=-0.2695413497339483, ctrl=-0.0, connection=13.36, completion=5.389221556886228, energy=7.142814408431678, transformer=0.
已连接电池 batt_ev_169, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 85kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_169 已接入
已连接电池 batt_ev_059, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
已连接电池 batt_ev_175, 初始SOC: 88.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.75275123 -1.         -0.52477896
 -1.         -1.         -0.         -0.3967141  -0.77621174]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=100.0。
功率需求: 100.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=45.16507387161255。
功率需求: 60.00 kW, 充电桩功率: 45.17 kW, 最终充电功率: 45.17 kW。
初次设置charger_power=46.56。
功率需求: 30.00 kW, 充电桩功率: 46.56 kW, 最终充电功率: 30.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 82.80 kW。
功率需求计算已禁用，直接使用充电桩功率: 85.92 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 23.80 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 23.80284547805786, -4.833373922052591
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 82.80000000000001, -16.81325710049554
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 85.91999999999999, -17.446800121673633
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 45.16507387161255, -9.171159407805499
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 30.0, -6.091759819020124
SOC从 0.52 更新为 0.52。
SOC从 0.28 更新为 0.57。
SOC从 0.18 更新为 0.39。
SOC从 0.88 更新为 0.96。
SOC从 0.77 更新为 1.00。
SOC从 0.72 更新为 1.00。
SOC从 0.02 更新为 0.02。
SOC从 0.77 更新为 0.91。
已断开电池: batt_ev_196
时间步 55: 电池 batt_ev_196 已离开，当前SOC: 90.6%，能量满足率: 98.1%
已断开电池: batt_ev_063
时间步 55: 电池 batt_ev_063 已离开，当前SOC: 52.0%，能量满足率: 0.0%
已断开电池: batt_ev_118
时间步 55 执行前: 电池 batt_ev_118 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_199
时间步 55 执行前: 电池 batt_ev_199 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.14864234271780935, voltage=-0.25541902132334204, ctrl=-0.0, connection=13.68, completion=5.380116959064328, energy=7.150038112658487, transformer=0.
已连接电池 batt_ev_029, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_195, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
已连接电池 batt_ev_213, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_133, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [ 1.        -0.        -1.        -0.7640681 -1.        -0.6422221
 -1.        -1.        -0.        -0.2601313 -0.7355767]
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 45.84 kW。
功率需求计算已禁用，直接使用充电桩功率: 16.56 kW。
初次设置charger_power=51.37776851654053。
功率需求: 64.00 kW, 充电桩功率: 51.38 kW, 最终充电功率: 51.38 kW。
初次设置charger_power=120.0。
功率需求: 120.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 120.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=44.134601354599。
功率需求: 48.00 kW, 充电桩功率: 44.13 kW, 最终充电功率: 44.13 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 45.84408760070801, -9.309039026187722
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 16.560000000000002, -3.362651420099108
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 51.37776851654053, -10.432700861332624
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 44.134601354599, -8.961913038680574
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.28 更新为 0.28。
SOC从 0.57 更新为 0.87。
SOC从 0.39 更新为 0.61。
SOC从 0.96 更新为 1.00。
SOC从 0.42 更新为 0.62。
SOC从 0.18 更新为 0.55。
SOC从 0.02 更新为 0.02。
SOC从 0.38 更新为 0.65。
已断开电池: batt_ev_175
时间步 56 执行前: 电池 batt_ev_175 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.16714405666253285, voltage=-0.22804411188138252, ctrl=-0.0, connection=13.76, completion=5.406976744186046, energy=7.166607658515124, transformer=0.
已连接电池 batt_ev_145, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_044, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
已连接电池 batt_ev_154, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.7632604  -1.         -0.57679486
 -1.         -1.         -0.         -0.3389107  -0.7601202 ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 44.80 kW。
功率需求计算已禁用，直接使用充电桩功率: 45.80 kW。
初次设置charger_power=100.0。
功率需求: 80.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 46.14 kW。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
初次设置charger_power=80.0。
功率需求: 48.00 kW, 充电桩功率: 80.00 kW, 最终充电功率: 48.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=20.334641933441162。
功率需求: 60.00 kW, 充电桩功率: 20.33 kW, 最终充电功率: 20.33 kW。
功率需求计算已禁用，直接使用充电桩功率: 45.61 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 44.80000000000001, -9.097027996403385
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 45.79562544822693, -9.299198366413474
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 46.14358901977539, -9.369855383201529
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 45.60721278190613, -9.260939542743891
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 48.0, -9.746815710432196
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 20.334641933441162, -4.129125155476618
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.28 更新为 0.28。
SOC从 0.87 更新为 1.00。
SOC从 0.61 更新为 0.83。
SOC从 0.32 更新为 0.53。
SOC从 0.62 更新为 0.81。
SOC从 0.55 更新为 0.91。
SOC从 0.52 更新为 0.71。
SOC从 0.02 更新为 0.02。
SOC从 0.18 更新为 0.27。
SOC从 0.65 更新为 0.93。
已断开电池: batt_ev_153
时间步 57: 电池 batt_ev_153 已离开，当前SOC: 2.0%，能量满足率: 0.0%
已断开电池: batt_ev_169
时间步 57 执行前: 电池 batt_ev_169 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_029
时间步 57 执行前: 电池 batt_ev_029 已充满 (SOC: 80.7%)，离开
奖励各项的值：powerloss=-0.18738853304102543, voltage=-0.24791470298752394, ctrl=-0.0, connection=14.0, completion=5.428571428571428, energy=7.158037241512007, transformer=0.
已连接电池 batt_ev_179, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_179 已接入
已连接电池 batt_ev_246, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 74kWh，并创BMS。
已连接电池 batt_ev_184, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.75385517 -1.         -0.52299404
 -1.         -1.         -0.         -0.4016189  -0.7786789 ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 37.04 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
初次设置charger_power=52.29940414428711。
功率需求: 80.00 kW, 充电桩功率: 52.30 kW, 最终充电功率: 52.30 kW。
功率需求计算已禁用，直接使用充电桩功率: 28.96 kW。
功率需求计算已禁用，直接使用充电桩功率: 71.04 kW。
初次设置charger_power=0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 24.10 kW。
功率需求计算已禁用，直接使用充电桩功率: 11.96 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 37.03999999999999, -7.521292789883512
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 11.960000000000008, -2.4285815811826907
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 28.95999999999998, -5.8805788119607545
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 71.03999999999999, -14.425287251439652
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 24.09713387489319, -4.8931317297541
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 52.29940414428711, -10.619846957495424
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 0.0, -0.0
SOC从 0.28 更新为 0.28。
SOC从 0.18 更新为 0.55。
SOC从 0.83 更新为 1.00。
SOC从 0.53 更新为 0.79。
SOC从 0.48 更新为 0.66。
SOC从 0.91 更新为 1.00。
SOC从 0.71 更新为 1.00。
SOC从 0.28 更新为 0.28。
SOC从 0.27 更新为 0.37。
SOC从 0.93 更新为 1.00。
已断开电池: batt_ev_059
时间步 58 执行前: 电池 batt_ev_059 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_195
时间步 58 执行前: 电池 batt_ev_195 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_133
时间步 58 执行前: 电池 batt_ev_133 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_145
时间步 58 执行前: 电池 batt_ev_145 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.19764553360676146, voltage=-0.2561943995677507, ctrl=-0.0, connection=14.32, completion=5.5307262569832405, energy=7.221544789187718, transformer=0.
已连接电池 batt_ev_066, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
时间步 58 执行前: 排队电池 batt_ev_066 已接入
已连接电池 batt_ev_233, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
已连接电池 batt_ev_219, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_249, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.7655877  -1.         -0.6242667
 -1.         -1.         -0.         -0.28262156 -0.74304205]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=91.87052249908447。
功率需求: 120.00 kW, 充电桩功率: 91.87 kW, 最终充电功率: 91.87 kW。
功率需求计算已禁用，直接使用充电桩功率: 78.40 kW。
功率需求计算已禁用，直接使用充电桩功率: 62.43 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 16.96 kW。
初次设置charger_power=89.16504621505737。
功率需求: 120.00 kW, 充电桩功率: 89.17 kW, 最终充电功率: 89.17 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 16.95729374885559, -3.4433253566199866
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 78.39999999999998, -15.919798993705918
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 62.42666840553284, -12.6762756742706
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 91.87052249908447, -18.655105250410234
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 89.16504621505737, -18.10573485979863
SOC从 0.28 更新为 0.28。
SOC从 0.55 更新为 0.93。
SOC从 0.08 更新为 0.38。
SOC从 0.79 更新为 1.00。
SOC从 0.66 更新为 0.87。
SOC从 0.22 更新为 0.55。
SOC从 0.18 更新为 0.41。
SOC从 0.28 更新为 0.28。
SOC从 0.37 更新为 0.44。
SOC从 0.08 更新为 0.30。
已断开电池: batt_ev_213
时间步 59: 电池 batt_ev_213 已离开，当前SOC: 28.0%，能量满足率: 0.0%
已断开电池: batt_ev_044
时间步 59: 电池 batt_ev_044 已离开，当前SOC: 44.4%，能量满足率: 33.1%
已断开电池: batt_ev_154
时间步 59 执行前: 电池 batt_ev_154 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_179
时间步 59: 电池 batt_ev_179 已离开，当前SOC: 93.0%，能量满足率: 93.8%
奖励各项的值：powerloss=-0.21447937632890465, voltage=-0.2776473335192575, ctrl=-0.0, connection=14.64, completion=5.464480874316941, energy=7.187636894794317, transformer=0.
已连接电池 batt_ev_032, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_032 已接入
已连接电池 batt_ev_060, 初始SOC: 56.99999999999999%, 最大功率: 100kW, 电池容量: 90kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_060 已接入
已连接电池 batt_ev_103, 初始SOC: 72.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_103 已接入
已连接电池 batt_ev_205, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 114kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.77152276 -1.         -0.51607513
 -1.         -1.         -0.         -0.44713163 -0.8040326 ]
初次设置charger_power=0.0。
功率需求: 64.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
初次设置charger_power=100.0。
功率需求: 60.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 92.58 kW。
初次设置charger_power=60.0。
功率需求: 24.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 24.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 39.20 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=53.65579605102539。
功率需求: 96.00 kW, 充电桩功率: 53.66 kW, 最终充电功率: 53.66 kW。
功率需求计算已禁用，直接使用充电桩功率: 96.48 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 39.19999999999999, -7.959899496852959
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 92.58273124694824, -18.799725404843272
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 96.48391485214233, -19.591894522601322
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_060 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_103 充电的有无功功率为 24.0, -4.873407855216098
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 53.65579605102539, -10.895274081372502
SOC从 0.48 更新为 0.48。
SOC从 0.57 更新为 0.74。
SOC从 0.38 更新为 0.69。
SOC从 0.72 更新为 0.83。
SOC从 0.87 更新为 1.00。
SOC从 0.55 更新为 0.89。
SOC从 0.41 更新为 0.64。
SOC从 0.28 更新为 0.28。
SOC从 0.48 更新为 0.60。
SOC从 0.30 更新为 0.54。
已断开电池: batt_ev_246
时间步 60 执行前: 电池 batt_ev_246 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_184
时间步 60: 电池 batt_ev_184 已离开，当前SOC: 28.0%，能量满足率: -0.0%
已断开电池: batt_ev_233
时间步 60: 电池 batt_ev_233 已离开，当前SOC: 88.7%，能量满足率: 87.7%
已断开电池: batt_ev_103
时间步 60: 电池 batt_ev_103 已离开，当前SOC: 83.1%，能量满足率: 55.6%
奖励各项的值：powerloss=-0.21800607952861373, voltage=-0.28695267710416417, ctrl=-0.0, connection=14.96, completion=5.401069518716578, energy=7.1639841557619075, transformer=0.
已连接电池 batt_ev_072, 初始SOC: 12.0%, 最大功率: 100kW, 电池容量: 79kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_072 已接入
已连接电池 batt_ev_217, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_217 已接入
已连接电池 batt_ev_124, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 70kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_124 已接入
已连接电池 batt_ev_189, 初始SOC: 88.0%, 最大功率: 80kW, 电池容量: 78kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_189 已接入
智能体的动作为: [ 1.         -0.         -1.         -0.7549134  -1.         -0.52257854
 -1.         -1.         -0.         -0.4042788  -0.7802321 ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 94.80 kW。
功率需求计算已禁用，直接使用充电桩功率: 90.59 kW。
初次设置charger_power=100.0。
功率需求: 100.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 100.00 kW。
初次设置charger_power=31.35471224784851。
功率需求: 48.00 kW, 充电桩功率: 31.35 kW, 最终充电功率: 31.35 kW。
初次设置charger_power=100.0。
功率需求: 80.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求: 20.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 48.51 kW。
功率需求计算已禁用，直接使用充电桩功率: 93.63 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 90.58960676193237, -18.395004216439112
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 93.6278486251831, -19.011945539872965
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_060 充电的有无功功率为 94.80000000000001, -19.24996102810359
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 48.51345777511597, -9.851077758539361
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_217 充电的有无功功率为 31.35471224784851, -6.366845873612721
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 0.0, -0.0
SOC从 0.48 更新为 0.48。
SOC从 0.74 更新为 1.00。
SOC从 0.69 更新为 0.98。
SOC从 0.12 更新为 0.44。
SOC从 0.38 更新为 0.52。
SOC从 0.38 更新为 0.67。
SOC从 0.64 更新为 0.87。
SOC从 0.88 更新为 0.88。
SOC从 0.60 更新为 0.70。
SOC从 0.54 更新为 0.78。
已断开电池: batt_ev_066
时间步 61 执行前: 电池 batt_ev_066 已充满 (SOC: 98.5%)，离开
已断开电池: batt_ev_219
时间步 61 执行前: 电池 batt_ev_219 已充满 (SOC: 87.2%)，离开
已断开电池: batt_ev_060
时间步 61 执行前: 电池 batt_ev_060 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_217
时间步 61: 电池 batt_ev_217 已离开，当前SOC: 51.8%，能量满足率: 22.9%
不太安全
奖励各项的值：powerloss=-0.22664174103516663, voltage=-0.29598886861567975, ctrl=-0.0, connection=15.280000000000001, completion=5.445026178010472, energy=7.183023218786887, transformer=-0.5550473986894986.
已连接电池 batt_ev_073, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 106kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_073 已接入
已连接电池 batt_ev_020, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 99kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_020 已接入
已连接电池 batt_ev_208, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 61kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_208 已接入
已连接电池 batt_ev_091, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_091 已接入
智能体的动作为: [ 1.         -0.         -1.         -0.94367373 -1.         -0.4715278
 -1.         -1.         -0.00135504 -0.684987   -0.8135372 ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
初次设置charger_power=113.24084758758545。
功率需求: 96.00 kW, 充电桩功率: 113.24 kW, 最终充电功率: 96.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
初次设置charger_power=47.15278148651123。
功率需求: 80.00 kW, 充电桩功率: 47.15 kW, 最终充电功率: 47.15 kW。
功率需求计算已禁用，直接使用充电桩功率: 93.60 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.11 kW。
功率需求计算已禁用，直接使用充电桩功率: 82.20 kW。
功率需求计算已禁用，直接使用充电桩功率: 88.72 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 88.72000000000003, -18.01536437144885
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 82.19844102859497, -16.691105341469665
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 93.6, -19.006290635342783
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 0.10840311646461487, -0.022012191637856657
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 47.15278148651123, -9.574780653818836
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.48 更新为 0.48。
SOC从 0.48 更新为 0.71。
SOC从 0.32 更新为 0.56。
SOC从 0.44 更新为 0.75。
SOC从 0.38 更新为 0.57。
SOC从 0.67 更新为 1.00。
SOC从 0.22 更新为 0.44。
SOC从 0.88 更新为 0.88。
SOC从 0.70 更新为 0.88。
SOC从 0.78 更新为 1.00。
已断开电池: batt_ev_249
时间步 62 执行前: 电池 batt_ev_249 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_032
时间步 62: 电池 batt_ev_032 已离开，当前SOC: 48.0%，能量满足率: 0.0%
已断开电池: batt_ev_205
时间步 62 执行前: 电池 batt_ev_205 已充满 (SOC: 88.4%)，离开
已断开电池: batt_ev_124
时间步 62 执行前: 电池 batt_ev_124 已充满 (SOC: 100.0%)，离开
不太安全
奖励各项的值：powerloss=-0.22913242477931295, voltage=-0.2989162482202179, ctrl=-0.0, connection=15.6, completion=5.487179487179487, energy=7.189525306606644, transformer=-3.8670118207228086.
时间步 62: 电池 batt_ev_176 已错过离开时间，无法接入
已连接电池 batt_ev_102, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_102 已接入
已连接电池 batt_ev_236, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 92kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_236 已接入
已连接电池 batt_ev_074, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_074 已接入
已连接电池 batt_ev_130, 初始SOC: 82.0%, 最大功率: 80kW, 电池容量: 52kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_130 已接入
智能体的动作为: [ 1.         -0.         -1.         -0.9903231  -1.         -0.4547509
 -1.         -1.         -0.00761481 -0.7370458  -0.7993781 ]
初次设置charger_power=0.0。
功率需求: 48.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 118.84 kW。
功率需求计算已禁用，直接使用充电桩功率: 78.08 kW。
功率需求计算已禁用，直接使用充电桩功率: 45.48 kW。
初次设置charger_power=100.0。
功率需求: 80.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 80.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.61 kW。
初次设置charger_power=44.22274947166443。
功率需求: 48.00 kW, 充电桩功率: 44.22 kW, 最终充电功率: 44.22 kW。
初次设置charger_power=37.44。
功率需求: 32.00 kW, 充电桩功率: 37.44 kW, 最终充电功率: 32.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 78.08000000000001, -15.854820222303042
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 0.6091847270727158, -0.12370023475807701
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 118.83877515792847, -24.13124251495452
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 45.47508955001831, -9.234110776238115
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_236 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_074 充电的有无功功率为 44.22274947166443, -8.979812277269291
已在 set_all_batteries_before_solve 中设置 batt_ev_130 充电的有无功功率为 32.0, -6.497877140288132
SOC从 0.48 更新为 0.48。
SOC从 0.71 更新为 0.99。
SOC从 0.56 更新为 0.86。
SOC从 0.75 更新为 1.00。
SOC从 0.57 更新为 0.76。
SOC从 0.38 更新为 0.60。
SOC从 0.44 更新为 0.67。
SOC从 0.88 更新为 0.88。
SOC从 0.48 更新为 0.68。
SOC从 0.82 更新为 0.97。
已断开电池: batt_ev_072
时间步 63 执行前: 电池 batt_ev_072 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_189
时间步 63: 电池 batt_ev_189 已离开，当前SOC: 88.2%，能量满足率: 1.9%
已断开电池: batt_ev_073
时间步 63 执行前: 电池 batt_ev_073 已充满 (SOC: 98.9%)，离开
已断开电池: batt_ev_236
时间步 63: 电池 batt_ev_236 已离开，当前SOC: 59.7%，能量满足率: 40.3%
已断开电池: batt_ev_130
时间步 63: 电池 batt_ev_130 已离开，当前SOC: 97.4%，能量满足率: 85.5%
奖励各项的值：powerloss=-0.22080212256585147, voltage=-0.3067116627452715, ctrl=-0.0, connection=16.0, completion=5.45, energy=7.1736125796147086, transformer=0.
已连接电池 batt_ev_061, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 78kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_061 已接入
已连接电池 batt_ev_012, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 98kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_012 已接入
时间步 63: 电池 batt_ev_108 已错过离开时间，无法接入
已连接电池 batt_ev_228, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
时间步 63 执行前: 排队电池 batt_ev_228 已接入
已连接电池 batt_ev_218, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
已连接电池 batt_ev_243, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.7848432  -1.         -0.5107315
 -1.         -1.         -0.         -0.48384488 -0.8228794 ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=100.0。
功率需求: 100.00 kW, 充电桩功率: 100.00 kW, 最终充电功率: 100.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 54.44 kW。
初次设置charger_power=120.0。
功率需求: 96.00 kW, 充电桩功率: 120.00 kW, 最终充电功率: 96.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 51.07 kW。
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求: 64.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 29.03 kW。
初次设置charger_power=49.37276244163513。
功率需求: 60.00 kW, 充电桩功率: 49.37 kW, 最终充电功率: 49.37 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 54.440000000000005, -11.054513484915184
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 51.07315182685852, -10.37084580431903
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_074 充电的有无功功率为 29.03069257736206, -5.8949335520366635
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_012 充电的有无功功率为 96.0, -19.493631420864393
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 49.37276244163513, -10.025567013199293
SOC从 0.48 更新为 0.48。
SOC从 0.28 更新为 0.60。
SOC从 0.86 更新为 1.00。
SOC从 0.48 更新为 0.72。
SOC从 0.76 更新为 0.97。
SOC从 0.22 更新为 0.50。
SOC从 0.67 更新为 0.89。
SOC从 0.38 更新为 0.38。
SOC从 0.68 更新为 0.82。
SOC从 0.12 更新为 0.35。
已断开电池: batt_ev_020
时间步 64 执行前: 电池 batt_ev_020 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_091
时间步 64: 电池 batt_ev_091 已离开，当前SOC: 89.2%，能量满足率: 88.4%
已断开电池: batt_ev_074
时间步 64 执行前: 电池 batt_ev_074 已充满 (SOC: 81.9%)，离开
已断开电池: batt_ev_012
时间步 64 执行前: 电池 batt_ev_012 已充满 (SOC: 72.5%)，离开
奖励各项的值：powerloss=-0.21583557956534938, voltage=-0.32194836900599766, ctrl=-0.0, connection=16.32, completion=5.490196078431373, energy=7.223332881913594, transformer=0.
已连接电池 batt_ev_122, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.75270367 -1.         -0.52348995
 -1.         -1.         -0.         -0.39866346 -0.77695495]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
初次设置charger_power=45.1622200012207。
功率需求: 60.00 kW, 充电桩功率: 45.16 kW, 最终充电功率: 45.16 kW。
功率需求计算已禁用，直接使用充电桩功率: 7.56 kW。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 46.62 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 7.560000000000001, -1.5351234743930715
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 46.61729693412781, -9.466045877821658
已在 set_all_batteries_before_solve 中设置 batt_ev_122 充电的有无功功率为 45.1622200012207, -9.17057990470611
SOC从 0.48 更新为 0.48。
SOC从 0.60 更新为 0.92。
SOC从 0.28 更新为 0.56。
SOC从 0.97 更新为 1.00。
SOC从 0.50 更新为 0.79。
SOC从 0.38 更新为 0.38。
SOC从 0.35 更新为 0.56。
已断开电池: batt_ev_208
时间步 65 执行前: 电池 batt_ev_208 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_102
时间步 65: 电池 batt_ev_102 已离开，当前SOC: 48.0%，能量满足率: 0.0%
已断开电池: batt_ev_122
时间步 65: 电池 batt_ev_122 已离开，当前SOC: 55.5%，能量满足率: 39.3%
奖励各项的值：powerloss=-0.2023844938322249, voltage=-0.28996466012673805, ctrl=-0.0, connection=16.56, completion=5.458937198067632, energy=7.185959931496525, transformer=0.
已连接电池 batt_ev_139, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 84kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.4213649  -0.6776342  -0.9008323
 -1.         -1.         -0.         -0.14924036 -0.78102255]
功率需求计算已禁用，直接使用充电桩功率: 24.64 kW。
初次设置charger_power=54.210734367370605。
功率需求: 80.00 kW, 充电桩功率: 54.21 kW, 最终充电功率: 54.21 kW。
功率需求计算已禁用，直接使用充电桩功率: 45.36 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 46.86 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 24.639999999999986, -5.003365398021859
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 45.36000000000002, -9.21074084635843
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 46.86135292053223, -9.515603559540649
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 54.210734367370605, -11.00795911262405
SOC从 0.92 更新为 1.00。
SOC从 0.12 更新为 0.28。
SOC从 0.79 更新为 1.00。
SOC从 0.38 更新为 0.38。
SOC从 0.56 更新为 0.78。
已断开电池: batt_ev_061
时间步 66 执行前: 电池 batt_ev_061 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_228
时间步 66 执行前: 电池 batt_ev_228 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.20644823462424616, voltage=-0.1964399459832733, ctrl=-0.0, connection=16.72, completion=5.502392344497608, energy=7.212888544592252, transformer=0.
已连接电池 batt_ev_004, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_019, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.49700803 -0.6702854  -0.78863
 -1.         -0.9761359  -0.02015306 -0.14479636 -0.7180533 ]
功率需求计算已禁用，直接使用充电桩功率: 53.62 kW。
初次设置charger_power=97.61359095573425。
功率需求: 100.00 kW, 充电桩功率: 97.61 kW, 最终充电功率: 97.61 kW。
功率需求计算已禁用，直接使用充电桩功率: 1.61 kW。
初次设置charger_power=8.687781393527985。
功率需求: 36.00 kW, 充电桩功率: 8.69 kW, 最终充电功率: 8.69 kW。
功率需求计算已禁用，直接使用充电桩功率: 43.08 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 1.6122445464134216, -0.32738021820918684
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 43.08319687843323, -8.748416253965758
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 53.62283229827881, -10.88858050589031
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 97.61359095573427, -19.821285039146932
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 8.687781393527985, -1.7641292536508142
SOC从 0.28 更新为 0.44。
SOC从 0.08 更新为 0.35。
SOC从 0.38 更新为 0.39。
SOC从 0.52 更新为 0.57。
SOC从 0.78 更新为 0.98。
已断开电池: batt_ev_243
时间步 67 执行前: 电池 batt_ev_243 已充满 (SOC: 98.1%)，离开
奖励各项的值：powerloss=-0.20404895416618526, voltage=-0.1179879656128957, ctrl=-0.0, connection=16.8, completion=5.523809523809524, energy=7.226160503903718, transformer=0.
智能体的动作为: [ 1.         -0.         -1.         -0.42390868 -0.5203129  -0.8011386
 -1.         -0.99655247 -0.         -0.1580829  -0.7746254 ]
功率需求计算已禁用，直接使用充电桩功率: 41.63 kW。
功率需求计算已禁用，直接使用充电桩功率: 99.66 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 9.48 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 41.62503242492676, -8.45232333305262
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 99.65524673461914, -20.235860927082975
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 9.484974145889282, -1.9260061462124347
SOC从 0.44 更新为 0.56。
SOC从 0.35 更新为 0.62。
SOC从 0.39 更新为 0.39。
SOC从 0.57 更新为 0.63。
奖励各项的值：powerloss=-0.19611450401228936, voltage=-0.09803969466291029, ctrl=-0.0, connection=16.8, completion=5.523809523809524, energy=7.226160503903718, transformer=0.
智能体的动作为: [ 1.         -0.         -1.         -0.47954628 -0.49697962 -0.7322759
 -1.         -0.7794486  -0.         -0.11858431 -0.7331921 ]
功率需求计算已禁用，直接使用充电桩功率: 39.76 kW。
功率需求计算已禁用，直接使用充电桩功率: 77.94 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 7.12 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 39.75836992263794, -8.073281345482133
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 77.94486284255981, -15.827379452111352
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 7.1150583028793335, -1.4447742093155278
SOC从 0.56 更新为 0.68。
SOC从 0.62 更新为 0.84。
SOC从 0.39 更新为 0.39。
SOC从 0.63 更新为 0.67。
已断开电池: batt_ev_218
时间步 69: 电池 batt_ev_218 已离开，当前SOC: 38.6%，能量满足率: 1.1%
已断开电池: batt_ev_139
时间步 69: 电池 batt_ev_139 已离开，当前SOC: 68.3%，能量满足率: 65.5%
奖励各项的值：powerloss=-0.19503921385706785, voltage=-0.04995246817267596, ctrl=-0.0, connection=16.96, completion=5.471698113207547, energy=7.189379854942734, transformer=0.
已连接电池 batt_ev_177, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [ 1.         -0.         -1.         -0.47319373 -0.51627946 -0.74901676
 -1.         -0.66282696 -0.         -0.08737177 -0.6522965 ]
初次设置charger_power=0.0。
功率需求: 64.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 59.68 kW。
功率需求计算已禁用，直接使用充电桩功率: 5.24 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 59.68000000000001, -12.118540866637366
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 5.242306441068649, -1.0644957245564126
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 0.0, -0.0
SOC从 0.38 更新为 0.38。
SOC从 0.84 更新为 1.00。
SOC从 0.67 更新为 0.70。
已断开电池: batt_ev_004
时间步 70 执行前: 电池 batt_ev_004 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_019
时间步 70: 电池 batt_ev_019 已离开，当前SOC: 69.7%，能量满足率: 38.6%
奖励各项的值：powerloss=-0.18088438756846376, voltage=-0.03978861405478096, ctrl=-0.0, connection=17.12, completion=5.4672897196261685, energy=7.186943742977109, transformer=0.
已连接电池 batt_ev_202, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_160, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [ 0.7261205  -0.40344328 -1.         -0.32315484 -0.748878   -0.59530973
 -0.6684406  -0.1489061  -0.01148747 -0.         -0.        ]
功率需求计算已禁用，直接使用充电桩功率: 32.28 kW。
初次设置charger_power=32.31548368930817。
功率需求: 80.00 kW, 充电桩功率: 32.32 kW, 最终充电功率: 32.32 kW。
初次设置charger_power=35.718584060668945。
功率需求: 60.00 kW, 充电桩功率: 35.72 kW, 最终充电功率: 35.72 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 32.27546215057373, -6.553812115638995
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 32.31548368930817, -6.5619388356909205
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 35.718584060668945, -7.252967839102524
SOC从 0.38 更新为 0.52。
SOC从 0.48 更新为 0.59。
SOC从 0.18 更新为 0.40。
奖励各项的值：powerloss=-0.16588308739268376, voltage=-0.07673947584419638, ctrl=-0.0, connection=17.12, completion=5.4672897196261685, energy=7.186943742977109, transformer=0.
智能体的动作为: [ 0.7127255  -0.063502   -1.         -0.23792458 -0.5000644  -0.76232636
 -1.         -0.1546963  -0.00255205 -0.         -0.19737926]
功率需求计算已禁用，直接使用充电桩功率: 5.08 kW。
功率需求计算已禁用，直接使用充电桩功率: 23.79 kW。
功率需求计算已禁用，直接使用充电桩功率: 45.74 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 5.080159902572632, -1.0315704656229712
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 23.792457580566406, -4.8312645695011724
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 45.73958158493042, -9.28781817459573
SOC从 0.52 更新为 0.54。
SOC从 0.59 更新为 0.66。
SOC从 0.40 更新为 0.68。
奖励各项的值：powerloss=-0.14782616279187372, voltage=-0.12949906578239467, ctrl=-0.0, connection=17.12, completion=5.4672897196261685, energy=7.186943742977109, transformer=0.
已连接电池 batt_ev_099, 初始SOC: 68.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
已连接电池 batt_ev_100, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [ 0.57567537 -0.46539384 -0.8826656  -0.3638632  -0.50052637 -0.52086216
 -0.7403151  -0.         -0.24359336 -0.         -0.        ]
功率需求计算已禁用，直接使用充电桩功率: 37.23 kW。
初次设置charger_power=52.95993447303772。
功率需求: 36.00 kW, 充电桩功率: 52.96 kW, 最终充电功率: 36.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 36.39 kW。
功率需求计算已禁用，直接使用充电桩功率: 31.25 kW。
初次设置charger_power=59.22520637512207。
功率需求: 80.00 kW, 充电桩功率: 59.23 kW, 最终充电功率: 59.23 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 37.231507301330566, -7.560180005993329
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 36.38631999492645, -7.388557403570049
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 31.251729726791382, -6.34593438081815
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 59.22520637512207, -12.026191082304768
SOC从 0.54 更新为 0.70。
SOC从 0.68 更新为 0.81。
SOC从 0.66 更新为 0.78。
SOC从 0.68 更新为 0.87。
SOC从 0.18 更新为 0.44。
已断开电池: batt_ev_177
时间步 73: 电池 batt_ev_177 已离开，当前SOC: 69.6%，能量满足率: 52.7%
已断开电池: batt_ev_160
时间步 73: 电池 batt_ev_160 已离开，当前SOC: 86.7%，能量满足率: 85.9%
奖励各项的值：powerloss=-0.1297287400449837, voltage=-0.1839192221273933, ctrl=-0.0, connection=17.28, completion=5.416666666666666, energy=7.184563824044706, transformer=0.
智能体的动作为: [ 1.         -0.         -1.         -0.42305756 -0.50298417 -0.7872363
 -1.         -0.9871725  -0.         -0.15724328 -0.7718203 ]
功率需求计算已禁用，直接使用充电桩功率: 49.76 kW。
功率需求计算已禁用，直接使用充电桩功率: 42.31 kW。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 42.305755615234375, -8.59055007233899
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 49.76, -10.104198953148044
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.81 更新为 1.00。
SOC从 0.78 更新为 0.92。
SOC从 0.44 更新为 0.78。
已断开电池: batt_ev_202
时间步 74 执行前: 电池 batt_ev_202 已充满 (SOC: 92.4%)，离开
已断开电池: batt_ev_099
时间步 74 执行前: 电池 batt_ev_099 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_100
时间步 74: 电池 batt_ev_100 已离开，当前SOC: 78.0%，能量满足率: 81.1%
奖励各项的值：powerloss=-0.12223362770375612, voltage=-0.21900191090336696, ctrl=-0.0, connection=17.52, completion=5.4337899543379, energy=7.214503306017752, transformer=0.
智能体的动作为: [ 1.         -0.         -1.         -0.4997132  -0.64713234 -0.77802426
 -1.         -0.9406329  -0.01723602 -0.13974549 -0.72318614]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.10846490021058514, voltage=-0.24070756321381115, ctrl=-0.0, connection=17.52, completion=5.4337899543379, energy=7.214503306017752, transformer=0.
智能体的动作为: [ 0.4540763  -0.32764474 -1.         -0.05714007 -0.8524419  -0.3872187
 -0.25502226 -0.41696775 -0.07717122 -0.         -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.10822517631461505, voltage=-0.2695566130902938, ctrl=-0.0, connection=17.52, completion=5.4337899543379, energy=7.214503306017752, transformer=0.
已连接电池 batt_ev_120, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [ 0.46059012 -0.32830083 -1.         -0.05625595 -0.8542112  -0.38844866
 -0.25502378 -0.418732   -0.07570105 -0.         -0.        ]
初次设置charger_power=0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 0.0, -0.0
SOC从 0.18 更新为 0.18。
奖励各项的值：powerloss=-0.10857013118186461, voltage=-0.2475870067524033, ctrl=-0.0, connection=17.52, completion=5.4337899543379, energy=7.214503306017752, transformer=0.
智能体的动作为: [ 0.4624945  -0.32870346 -1.         -0.05589481 -0.85486263 -0.3886975
 -0.25451836 -0.41941252 -0.07522599 -0.         -0.        ]
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 0.0, -0.0
SOC从 0.18 更新为 0.18。
奖励各项的值：powerloss=-0.11438181004034306, voltage=-0.23715841235078639, ctrl=-0.0, connection=17.52, completion=5.4337899543379, energy=7.214503306017752, transformer=0.
已连接电池 batt_ev_035, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 77kWh，并创BMS。
智能体的动作为: [ 0.4773302  -0.33025026 -1.         -0.05388557 -0.8588863  -0.3914854
 -0.2544834  -0.4234216  -0.07187288 -0.         -0.        ]
初次设置charger_power=68.71090412139893。
功率需求: 64.00 kW, 充电桩功率: 68.71 kW, 最终充电功率: 64.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 64.0, -12.995754280576264
SOC从 0.48 更新为 0.69。
SOC从 0.18 更新为 0.18。
已断开电池: batt_ev_120
时间步 79: 电池 batt_ev_120 已离开，当前SOC: 18.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.13514653864756537, voltage=-0.3554356740989095, ctrl=-0.0, connection=17.6, completion=5.409090909090909, energy=7.181710109172217, transformer=0.
已连接电池 batt_ev_151, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
智能体的动作为: [ 0.7429956  -0.3932651  -1.         -0.32147405 -0.8091462  -0.6179169
 -0.6670387  -0.17563933 -0.         -0.         -0.        ]
功率需求计算已禁用，直接使用充电桩功率: 64.73 kW。
初次设置charger_power=0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 64.73169803619385, -13.144331903794317
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 0.0, -0.0
SOC从 0.69 更新为 0.90。
SOC从 0.28 更新为 0.28。
奖励各项的值：powerloss=-0.15130948542166378, voltage=-0.3885960025240931, ctrl=-0.0, connection=17.6, completion=5.409090909090909, energy=7.181710109172217, transformer=0.
智能体的动作为: [ 0.741066   -0.3944038  -1.         -0.3216774  -0.8015861  -0.6151304
 -0.66728175 -0.17222816 -0.         -0.         -0.        ]
功率需求计算已禁用，直接使用充电桩功率: 31.44 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 31.439999999999998, -6.384164290333089
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 0.0, -0.0
SOC从 0.90 更新为 1.00。
SOC从 0.28 更新为 0.28。
已断开电池: batt_ev_035
时间步 81 执行前: 电池 batt_ev_035 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_151
时间步 81: 电池 batt_ev_151 已离开，当前SOC: 28.0%，能量满足率: -0.0%
奖励各项的值：powerloss=-0.16186102559983717, voltage=-0.33864823265785216, ctrl=-0.0, connection=17.76, completion=5.405405405405405, energy=7.1620550631436375, transformer=0.
智能体的动作为: [ 0.6969954  -0.32752302 -1.         -0.29797447 -0.831642   -0.6063356
 -0.6687683  -0.19397566 -0.         -0.         -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.16964931455194, voltage=-0.2989341743692475, ctrl=-0.0, connection=17.76, completion=5.405405405405405, energy=7.1620550631436375, transformer=0.
智能体的动作为: [ 0.50580764 -0.33310995 -1.         -0.05004907 -0.86641556 -0.3969136
 -0.25475278 -0.4309402  -0.06547589 -0.         -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.17849155866172434, voltage=-0.3390324356588792, ctrl=-0.0, connection=17.76, completion=5.405405405405405, energy=7.1620550631436375, transformer=0.
已连接电池 batt_ev_056, 初始SOC: 62.0%, 最大功率: 80kW, 电池容量: 64kWh，并创BMS。
已连接电池 batt_ev_226, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [ 0.51271915 -0.3338599  -1.         -0.04908804 -0.8682468  -0.39820623
 -0.25470367 -0.43278676 -0.06391688 -0.         -0.        ]
初次设置charger_power=34.62294101715088。
功率需求: 48.00 kW, 充电桩功率: 34.62 kW, 最终充电功率: 34.62 kW。
初次设置charger_power=0.0。
功率需求: 60.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 34.62294101715088, -7.030488030152782
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 0.0, -0.0
SOC从 0.62 更新为 0.76。
SOC从 0.18 更新为 0.18。
奖励各项的值：powerloss=-0.18471613555028765, voltage=-0.34127340913765014, ctrl=-0.0, connection=17.76, completion=5.405405405405405, energy=7.1620550631436375, transformer=0.
已连接电池 batt_ev_048, 初始SOC: 42.0%, 最大功率: 120kW, 电池容量: 93kWh，并创BMS。
智能体的动作为: [ 0.7219939  -0.3586993  -1.         -0.30957913 -0.82808626 -0.61442345
 -0.66793764 -0.18847987 -0.         -0.         -0.        ]
初次设置charger_power=43.043915033340454。
功率需求: 96.00 kW, 充电桩功率: 43.04 kW, 最终充电功率: 43.04 kW。
功率需求计算已禁用，直接使用充电桩功率: 15.08 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 15.078389644622803, -3.061797605754743
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_048 充电的有无功功率为 43.043915033340454, -8.740439735113984
SOC从 0.42 更新为 0.54。
SOC从 0.76 更新为 0.81。
SOC从 0.18 更新为 0.18。
已断开电池: batt_ev_048
时间步 85: 电池 batt_ev_048 已离开，当前SOC: 53.6%，能量满足率: 20.7%
奖励各项的值：powerloss=-0.19139080590470403, voltage=-0.41310943941148537, ctrl=-0.0, connection=17.84, completion=5.381165919282511, energy=7.139203032489822, transformer=0.
已连接电池 batt_ev_234, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_227, 初始SOC: 8.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
智能体的动作为: [ 0.7464415  -0.39127612 -1.         -0.32104784 -0.82302743 -0.62289554
 -0.6663959  -0.18207616 -0.         -0.         -0.        ]
初次设置charger_power=60.0。
功率需求: 60.00 kW, 充电桩功率: 60.00 kW, 最终充电功率: 60.00 kW。
初次设置charger_power=37.37373232841492。
功率需求: 36.00 kW, 充电桩功率: 37.37 kW, 最终充电功率: 36.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 14.57 kW。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 14.566092491149902, -2.9577712319239238
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 36.0, -7.310111782824148
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.08 更新为 0.40。
SOC从 0.57 更新为 0.71。
SOC从 0.81 更新为 0.87。
SOC从 0.18 更新为 0.18。
已断开电池: batt_ev_056
时间步 86: 电池 batt_ev_056 已离开，当前SOC: 87.1%，能量满足率: 69.7%
已断开电池: batt_ev_226
时间步 86: 电池 batt_ev_226 已离开，当前SOC: 18.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.19465222039711977, voltage=-0.39117733489480777, ctrl=-0.0, connection=18.0, completion=5.333333333333333, energy=7.106742678373862, transformer=0.
智能体的动作为: [ 0.81432164 -0.         -1.         -0.2244932  -0.5037868  -0.758184
 -1.         -0.3107317  -0.         -0.         -0.25564077]
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
功率需求计算已禁用，直接使用充电桩功率: 45.49 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 45.4910409450531, -9.237349845149122
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.40 更新为 0.72。
SOC从 0.71 更新为 0.89。
奖励各项的值：powerloss=-0.19199963312739876, voltage=-0.3466550975180316, ctrl=-0.0, connection=18.0, completion=5.333333333333333, energy=7.106742678373862, transformer=0.
智能体的动作为: [ 0.7528386  -0.         -1.         -0.21989241 -0.5071072  -0.7619343
 -1.         -0.21595868 -0.         -0.         -0.21778864]
功率需求计算已禁用，直接使用充电桩功率: 52.96 kW。
功率需求计算已禁用，直接使用充电桩功率: 26.88 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 26.879999999999995, -5.458216797842029
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 52.96000000000001, -10.75398666717686
SOC从 0.72 更新为 1.00。
SOC从 0.89 更新为 1.00。
已断开电池: batt_ev_234
时间步 88 执行前: 电池 batt_ev_234 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_227
时间步 88 执行前: 电池 batt_ev_227 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.18755483402325884, voltage=-0.3468165831207859, ctrl=-0.0, connection=18.16, completion=5.3744493392070485, energy=7.132233932308894, transformer=0.
智能体的动作为: [ 0.52058005 -0.45599675 -0.84495914 -0.39942458 -0.5185105  -0.56907606
 -0.821978   -0.         -0.23846199 -0.         -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.1851664069470748, voltage=-0.28111354764514207, ctrl=-0.0, connection=18.16, completion=5.3744493392070485, energy=7.132233932308894, transformer=0.
智能体的动作为: [ 0.4930054  -0.3317466  -1.         -0.05176979 -0.8630757  -0.39447492
 -0.2546538  -0.42758682 -0.06834552 -0.         -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.199014373982753, voltage=-0.20539130428496533, ctrl=-0.0, connection=18.16, completion=5.3744493392070485, energy=7.132233932308894, transformer=0.
智能体的动作为: [ 0.48376894 -0.33086014 -1.         -0.05299569 -0.86065775 -0.39269555
 -0.2544835  -0.42517313 -0.07041036 -0.         -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.1961764287763906, voltage=-0.07845309400606792, ctrl=-0.0, connection=18.16, completion=5.3744493392070485, energy=7.132233932308894, transformer=0.
智能体的动作为: [ 0.478315   -0.33034348 -1.         -0.05371538 -0.8592122  -0.39164555
 -0.25438163 -0.42374092 -0.0716337  -0.         -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
奖励各项的值：powerloss=-0.19009264577045487, voltage=-0.054979111789486, ctrl=-0.0, connection=18.16, completion=5.3744493392070485, energy=7.132233932308894, transformer=0.
已连接电池 batt_ev_238, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [ 0.48379934 -0.3307406  -1.         -0.05302013 -0.8605725  -0.39275354
 -0.25471073 -0.4251088  -0.0704377  -0.         -0.        ]
初次设置charger_power=3.181208074092865。
功率需求: 48.00 kW, 充电桩功率: 3.18 kW, 最终充电功率: 3.18 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 3.181208074092865, -0.6459718507233769
SOC从 0.48 更新为 0.50。
奖励各项的值：powerloss=-0.19118455169344004, voltage=-0.019110750515083375, ctrl=-0.0, connection=18.16, completion=5.3744493392070485, energy=7.132233932308894, transformer=0.
智能体的动作为: [ 0.29556227 -0.30560303 -1.         -0.08180808 -0.80144536 -0.36144567
 -0.2742213  -0.36585066 -0.11499654 -0.         -0.        ]
功率需求计算已禁用，直接使用充电桩功率: 4.91 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 4.908484518527985, -0.996710292075037
SOC从 0.50 更新为 0.53。
奖励各项的值：powerloss=-0.1787008169283683, voltage=-0.015516588382180618, ctrl=-0.0, connection=18.16, completion=5.3744493392070485, energy=7.132233932308894, transformer=0.
智能体的动作为: [ 0.27196944 -0.286878   -1.         -0.09211881 -0.77874404 -0.36655438
 -0.31880498 -0.3414962  -0.12441664 -0.         -0.        ]
功率需求计算已禁用，直接使用充电桩功率: 5.53 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 5.527128428220749, -1.1223312957866336
SOC从 0.53 更新为 0.56。
奖励各项的值：powerloss=-0.16181773597361437, voltage=-0.08412145620963152, ctrl=-0.0, connection=18.16, completion=5.3744493392070485, energy=7.132233932308894, transformer=0.
已连接电池 batt_ev_025, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
已连接电池 batt_ev_013, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 89kWh，并创BMS。
已连接电池 batt_ev_117, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 111kWh，并创BMS。
已连接电池 batt_ev_166, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 114kWh，并创BMS。
智能体的动作为: [ 0.28207088 -0.27628073 -1.         -0.09515648 -0.7697958  -0.37520278
 -0.35003385 -0.330803   -0.12461201 -0.         -0.        ]
功率需求计算已禁用，直接使用充电桩功率: 5.71 kW。
初次设置charger_power=92.37549304962158。
功率需求: 72.00 kW, 充电桩功率: 92.38 kW, 最终充电功率: 72.00 kW。
初次设置charger_power=21.002030968666077。
功率需求: 60.00 kW, 充电桩功率: 21.00 kW, 最终充电功率: 21.00 kW。
初次设置charger_power=14.953441321849823。
功率需求: 120.00 kW, 充电桩功率: 14.95 kW, 最终充电功率: 14.95 kW。
初次设置charger_power=0.0。
功率需求: 120.00 kW, 充电桩功率: 0.00 kW, 最终充电功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 5.709389001131058, -1.159340883608187
已在 set_all_batteries_before_solve 中设置 batt_ev_025 充电的有无功功率为 21.002030968666077, -4.264644279091209
已在 set_all_batteries_before_solve 中设置 batt_ev_013 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_117 充电的有无功功率为 72.0, -14.620223565648296
已在 set_all_batteries_before_solve 中设置 batt_ev_166 充电的有无功功率为 14.953441321849823, -3.036425766683997
SOC从 0.56 更新为 0.60。
SOC从 0.52 更新为 0.68。
SOC从 0.12 更新为 0.23。
SOC从 0.28 更新为 0.31。
SOC从 0.18 更新为 0.18。
已断开电池: batt_ev_238
时间步 96: 电池 batt_ev_238 已离开，当前SOC: 59.8%，能量满足率: 29.5%
已断开电池: batt_ev_025
时间步 96: 电池 batt_ev_025 已离开，当前SOC: 22.7%，能量满足率: 12.5%
已断开电池: batt_ev_013
时间步 96: 电池 batt_ev_013 已离开，当前SOC: 18.0%，能量满足率: 0.0%
已断开电池: batt_ev_117
时间步 96: 电池 batt_ev_117 已离开，当前SOC: 68.2%，能量满足率: 35.3%
已断开电池: batt_ev_166
时间步 96: 电池 batt_ev_166 已离开，当前SOC: 31.3%，能量满足率: 4.7%
奖励各项的值：powerloss=-0.14845856230818064, voltage=-0.1526999913134408, ctrl=-1.0, connection=18.56, completion=5.258620689655173, energy=7.013828040501816, transformer=0.
调度记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250512_143129_13Bus_cbat_1000000\test_results_20250512_205114\schedule.csv
储能放电功率记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250512_143129_13Bus_cbat_1000000\test_results_20250512_205114\storage_schedule.csv
储能能量记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250512_143129_13Bus_cbat_1000000\test_results_20250512_205114\storage_energy.csv
已生成GIF动画，包含96步
测试完成 - 总奖励: 2239.1207
测试结果保存在: D:\LENOVO\Documents\Python\ML\powergym\results_20250512_143129_13Bus_cbat_1000000\test_results_20250512_205114
运行时间: 22820.46秒

进程已结束，退出代码为 0

```