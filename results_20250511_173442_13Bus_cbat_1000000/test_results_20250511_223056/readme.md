

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
已从D:\LENOVO\Documents\Python\ML\powergym\results_20250511_173442_13Bus_cbat_1000000\model\ppo_model加载模型
BatteryStationManager已重置
智能体的动作为: [ 0.5319879  -1.         -0.20700523 -0.         -0.         -0.3716416
 -0.74636894 -0.32877576 -0.30276543 -0.         -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -53.198790550231934, -17.485596868600744
奖励各项的值：powerloss=-0.1171688281834083, voltage=-0.1758393871699937, ctrl=-0.0, connection=0.0, completion=0.0, energy=0.0, transformer=0.
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
智能体的动作为: [ 0.5291177  -1.         -0.19048291 -0.         -0.         -0.37674275
 -0.74832076 -0.34289804 -0.3011576  -0.         -0.        ]
初次设置charger_power=120.0。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
初次设置charger_power=15.238633155822754。
功率需求计算已禁用，直接使用充电桩功率: 15.24 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=22.604565024375916。
功率需求计算已禁用，直接使用充电桩功率: 22.60 kW。
初次设置charger_power=74.83207583427429。
功率需求计算已禁用，直接使用充电桩功率: 74.83 kW。
初次设置charger_power=27.431843280792236。
功率需求计算已禁用，直接使用充电桩功率: 27.43 kW。
初次设置charger_power=36.13891124725342。
功率需求计算已禁用，直接使用充电桩功率: 36.14 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -52.91177034378052, -17.39125788887501
已在 set_all_batteries_before_solve 中设置 batt_ev_030 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 15.238633155822754, -3.0943364385142953
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 22.604565024375916, -4.590052698064028
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 74.83207583427429, -15.195301091369963
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 27.431843280792236, -5.570273355319577
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 36.13891124725342, -7.3383189146384264
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 0.0, -0.0
SOC从 0.18 更新为 0.51。
SOC从 0.32 更新为 0.38。
SOC从 0.18 更新为 0.18。
SOC从 0.12 更新为 0.12。
SOC从 0.22 更新为 0.33。
SOC从 0.28 更新为 0.48。
SOC从 0.12 更新为 0.25。
SOC从 0.38 更新为 0.48。
SOC从 0.22 更新为 0.22。
SOC从 0.12 更新为 0.12。
已断开电池: batt_ev_030
时间步 2 执行前: 电池 batt_ev_030 已充满 (SOC: 51.3%)，离开
奖励各项的值：powerloss=-0.1282074096942133, voltage=-0.2262000482365112, ctrl=-0.0, connection=0.08, completion=10.0, energy=10.0, transformer=0.
已连接电池 batt_ev_224, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
时间步 2 执行前: 排队电池 batt_ev_224 已接入
智能体的动作为: [ 1.         -0.6264813  -0.         -0.7815433  -0.69494206 -0.8742586
 -1.         -1.         -0.         -0.         -1.        ]
初次设置charger_power=37.58887767791748。
功率需求计算已禁用，直接使用充电桩功率: 37.59 kW。
已有历史设置self.charger_power=15.238633155822754，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 15.24 kW。
self.charger_power=0.0 改为 46.89259886741638。
功率需求计算已禁用，直接使用充电桩功率: 46.89 kW。
self.charger_power=0.0 改为 41.69652342796326。
功率需求计算已禁用，直接使用充电桩功率: 41.70 kW。
已有历史设置self.charger_power=22.604565024375916，设置charger_power=52.455514669418335失败。
功率需求计算已禁用，直接使用充电桩功率: 22.60 kW。
已有历史设置self.charger_power=74.83207583427429，设置charger_power=100.0失败。
功率需求计算已禁用，直接使用充电桩功率: 74.83 kW。
已有历史设置self.charger_power=27.431843280792236，设置charger_power=80.0失败。
功率需求计算已禁用，直接使用充电桩功率: 27.43 kW。
已有历史设置self.charger_power=36.13891124725342，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 36.14 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 120.0。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -53.88, -17.70949958703715
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 15.238633155822754, -3.0943364385142953
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 46.89259886741638, -9.521948319665189
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 41.69652342796326, -8.466840200376595
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 22.604565024375916, -4.590052698064028
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 74.83207583427429, -15.195301091369963
已在 set_all_batteries_before_solve 中设置 batt_ev_039 充电的有无功功率为 27.431843280792236, -5.570273355319577
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 36.13891124725342, -7.3383189146384264
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_045 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 37.58887767791748, -7.6327471560133375
SOC从 0.28 更新为 0.49。
SOC从 0.38 更新为 0.43。
SOC从 0.18 更新为 0.35。
SOC从 0.12 更新为 0.29。
SOC从 0.33 更新为 0.44。
SOC从 0.48 更新为 0.69。
SOC从 0.25 更新为 0.38。
SOC从 0.48 更新为 0.57。
SOC从 0.22 更新为 0.22。
SOC从 0.12 更新为 0.54。
已断开电池: batt_ev_039
时间步 3: 电池 batt_ev_039 已离开，当前SOC: 38.4%，能量满足率: 30.7%
已断开电池: batt_ev_045
时间步 3: 电池 batt_ev_045 已离开，当前SOC: 53.7%，能量满足率: 48.4%
奖励各项的值：powerloss=-0.13343419714134103, voltage=-0.29073111091579396, ctrl=-0.0, connection=0.24, completion=3.333333333333333, energy=5.970979924468297, transformer=0.
时间步 3: 电池 batt_ev_092 已错过离开时间，无法接入
已连接电池 batt_ev_081, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 50kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_081 已接入
已连接电池 batt_ev_076, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 3 执行前: 排队电池 batt_ev_076 已接入
智能体的动作为: [ 1.         -0.6241031  -0.         -0.77849877 -0.6945169  -0.8716024
 -1.         -1.         -0.         -0.         -1.        ]
已有历史设置self.charger_power=37.58887767791748，设置charger_power=37.44618773460388失败。
功率需求计算已禁用，直接使用充电桩功率: 37.59 kW。
已有历史设置self.charger_power=15.238633155822754，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 15.24 kW。
已有历史设置self.charger_power=46.89259886741638，设置charger_power=46.70992612838745失败。
功率需求计算已禁用，直接使用充电桩功率: 46.89 kW。
已有历史设置self.charger_power=41.69652342796326，设置charger_power=41.671013832092285失败。
功率需求计算已禁用，直接使用充电桩功率: 41.70 kW。
已有历史设置self.charger_power=22.604565024375916，设置charger_power=52.29614496231079失败。
功率需求计算已禁用，直接使用充电桩功率: 22.60 kW。
已有历史设置self.charger_power=74.83207583427429，设置charger_power=100.0失败。
功率需求计算已禁用，直接使用充电桩功率: 74.83 kW。
初次设置charger_power=80.0。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已有历史设置self.charger_power=36.13891124725342，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 36.14 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 15.238633155822754, -3.0943364385142953
已在 set_all_batteries_before_solve 中设置 batt_ev_126 充电的有无功功率为 46.89259886741638, -9.521948319665189
已在 set_all_batteries_before_solve 中设置 batt_ev_064 充电的有无功功率为 41.69652342796326, -8.466840200376595
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 22.604565024375916, -4.590052698064028
已在 set_all_batteries_before_solve 中设置 batt_ev_239 充电的有无功功率为 74.83207583427429, -15.195301091369963
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 36.13891124725342, -7.3383189146384264
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 37.58887767791748, -7.6327471560133375
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.49 更新为 0.70。
SOC从 0.43 更新为 0.49。
SOC从 0.35 更新为 0.52。
SOC从 0.29 更新为 0.46。
SOC从 0.44 更新为 0.55。
SOC从 0.69 更新为 0.89。
SOC从 0.12 更新为 0.52。
SOC从 0.57 更新为 0.67。
SOC从 0.22 更新为 0.22。
SOC从 0.28 更新为 0.53。
已断开电池: batt_ev_126
时间步 4: 电池 batt_ev_126 已离开，当前SOC: 52.5%，能量满足率: 43.1%
已断开电池: batt_ev_064
时间步 4 执行前: 电池 batt_ev_064 已充满 (SOC: 45.6%)，离开
已断开电池: batt_ev_239
时间步 4 执行前: 电池 batt_ev_239 已充满 (SOC: 89.0%)，离开
奖励各项的值：powerloss=-0.1353125000589334, voltage=-0.29962138525467585, ctrl=-0.0, connection=0.48, completion=5.0, energy=7.036960550469442, transformer=0.
已连接电池 batt_ev_235, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_235 已接入
时间步 4: 电池 batt_ev_104 已错过离开时间，无法接入
已连接电池 batt_ev_018, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_018 已接入
已连接电池 batt_ev_062, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
时间步 4 执行前: 排队电池 batt_ev_062 已接入
智能体的动作为: [ 1.         -0.6697977  -0.         -0.79108804 -0.68540615 -0.87081915
 -1.         -1.         -0.         -0.         -1.        ]
已有历史设置self.charger_power=37.58887767791748，设置charger_power=40.18786311149597失败。
功率需求计算已禁用，直接使用充电桩功率: 37.59 kW。
已有历史设置self.charger_power=15.238633155822754，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 15.24 kW。
初次设置charger_power=47.465282678604126。
功率需求计算已禁用，直接使用充电桩功率: 47.47 kW。
初次设置charger_power=41.12436890602112。
功率需求计算已禁用，直接使用充电桩功率: 41.12 kW。
已有历史设置self.charger_power=22.604565024375916，设置charger_power=52.24914908409119失败。
功率需求计算已禁用，直接使用充电桩功率: 22.60 kW。
初次设置charger_power=120.0。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已有历史设置self.charger_power=80.0，设置charger_power=80.0失败。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已有历史设置self.charger_power=36.13891124725342，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 36.14 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=60.0，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 15.238633155822754, -3.0943364385142953
已在 set_all_batteries_before_solve 中设置 batt_ev_123 充电的有无功功率为 22.604565024375916, -4.590052698064028
已在 set_all_batteries_before_solve 中设置 batt_ev_242 充电的有无功功率为 36.13891124725342, -7.3383189146384264
已在 set_all_batteries_before_solve 中设置 batt_ev_042 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 37.58887767791748, -7.6327471560133375
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_076 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_235 充电的有无功功率为 47.465282678604126, -9.638236727331748
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 41.12436890602112, -8.350659269475333
已在 set_all_batteries_before_solve 中设置 batt_ev_062 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.70 更新为 0.91。
SOC从 0.49 更新为 0.54。
SOC从 0.62 更新为 0.87。
SOC从 0.32 更新为 0.49。
SOC从 0.55 更新为 0.66。
SOC从 0.57 更新为 0.96。
SOC从 0.52 更新为 0.92。
SOC从 0.67 更新为 0.77。
SOC从 0.22 更新为 0.22。
SOC从 0.53 更新为 0.78。
已断开电池: batt_ev_123
时间步 5: 电池 batt_ev_123 已离开，当前SOC: 66.3%，能量满足率: 58.3%
已断开电池: batt_ev_242
时间步 5 执行前: 电池 batt_ev_242 已充满 (SOC: 76.9%)，离开
已断开电池: batt_ev_042
时间步 5: 电池 batt_ev_042 已离开，当前SOC: 22.0%，能量满足率: 0.0%
已断开电池: batt_ev_076
时间步 5: 电池 batt_ev_076 已离开，当前SOC: 78.0%，能量满足率: 71.4%
已断开电池: batt_ev_235
时间步 5: 电池 batt_ev_235 已离开，当前SOC: 87.3%，能量满足率: 84.2%
已断开电池: batt_ev_062
时间步 5: 电池 batt_ev_062 已离开，当前SOC: 96.0%，能量满足率: 95.0%
奖励各项的值：powerloss=-0.14039302197194317, voltage=-0.3176078996786824, ctrl=-0.0, connection=0.96, completion=3.333333333333333, energy=6.926375495456726, transformer=0.
时间步 5: 电池 batt_ev_200 已错过离开时间，无法接入
时间步 5: 电池 batt_ev_163 已错过离开时间，无法接入
已连接电池 batt_ev_014, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
时间步 5 执行前: 排队电池 batt_ev_014 已接入
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
智能体的动作为: [ 1.         -0.7437688  -0.         -0.8080527  -0.66858184 -0.86089855
 -1.         -1.         -0.         -0.         -1.        ]
已有历史设置self.charger_power=37.58887767791748，设置charger_power=16.80000000000001失败。
功率需求计算已禁用，直接使用充电桩功率: 37.59 kW。
已有历史设置self.charger_power=15.238633155822754，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 15.24 kW。
初次设置charger_power=64.6442174911499。
功率需求计算已禁用，直接使用充电桩功率: 64.64 kW。
已有历史设置self.charger_power=41.12436890602112，设置charger_power=40.11491060256958失败。
功率需求计算已禁用，直接使用充电桩功率: 41.12 kW。
初次设置charger_power=51.653913259506226。
功率需求计算已禁用，直接使用充电桩功率: 51.65 kW。
初次设置charger_power=120.0。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已有历史设置self.charger_power=80.0，设置charger_power=16.0失败。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_149 充电的有无功功率为 15.238633155822754, -3.0943364385142953
已在 set_all_batteries_before_solve 中设置 batt_ev_224 充电的有无功功率为 37.58887767791748, -7.6327471560133375
已在 set_all_batteries_before_solve 中设置 batt_ev_081 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 41.12436890602112, -8.350659269475333
已在 set_all_batteries_before_solve 中设置 batt_ev_014 充电的有无功功率为 64.6442174911499, -13.12656822148616
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 51.653913259506226, -10.488774442980358
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_231 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_248 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.91 更新为 1.00。
SOC从 0.54 更新为 0.60。
SOC从 0.28 更新为 0.48。
SOC从 0.49 更新为 0.66。
SOC从 0.08 更新为 0.33。
SOC从 0.57 更新为 0.96。
SOC从 0.92 更新为 1.00。
SOC从 0.08 更新为 0.08。
SOC从 0.32 更新为 0.32。
SOC从 0.22 更新为 0.47。
已断开电池: batt_ev_149
时间步 6: 电池 batt_ev_149 已离开，当前SOC: 59.6%，能量满足率: 41.8%
已断开电池: batt_ev_224
时间步 6 执行前: 电池 batt_ev_224 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_081
时间步 6 执行前: 电池 batt_ev_081 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_014
时间步 6: 电池 batt_ev_014 已离开，当前SOC: 48.5%，能量满足率: 34.1%
已断开电池: batt_ev_231
时间步 6: 电池 batt_ev_231 已离开，当前SOC: 8.0%，能量满足率: 0.0%
已断开电池: batt_ev_248
时间步 6: 电池 batt_ev_248 已离开，当前SOC: 46.6%，能量满足率: 32.4%
奖励各项的值：powerloss=-0.14822539649921349, voltage=-0.3445172074025127, ctrl=-0.0, connection=1.44, completion=3.333333333333333, energy=6.330248457604791, transformer=0.
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
已连接电池 batt_ev_106, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 92kWh，并创BMS。
时间步 6 执行前: 排队电池 batt_ev_106 已接入
智能体的动作为: [ 1.         -0.78095335 -0.         -0.8149392  -0.6591529  -0.85172457
 -1.         -1.         -0.         -0.         -1.        ]
初次设置charger_power=93.71440172195435。
功率需求计算已禁用，直接使用充电桩功率: 93.71 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=48.8963520526886。
功率需求计算已禁用，直接使用充电桩功率: 48.90 kW。
已有历史设置self.charger_power=41.12436890602112，设置charger_power=39.54917550086975失败。
功率需求计算已禁用，直接使用充电桩功率: 41.12 kW。
已有历史设置self.charger_power=51.653913259506226，设置charger_power=51.10347390174866失败。
功率需求计算已禁用，直接使用充电桩功率: 51.65 kW。
已有历史设置self.charger_power=120.0，设置charger_power=12.439999999999998失败。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_018 充电的有无功功率为 41.12436890602112, -8.350659269475333
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 51.653913259506226, -10.488774442980358
已在 set_all_batteries_before_solve 中设置 batt_ev_036 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 93.71440172195435, -19.029520895777058
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_157 充电的有无功功率为 48.8963520526886, -9.928827757707683
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_187 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_106 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.48 更新为 0.81。
SOC从 0.28 更新为 0.28。
SOC从 0.12 更新为 0.34。
SOC从 0.66 更新为 0.83。
SOC从 0.33 更新为 0.59。
SOC从 0.96 更新为 1.00。
SOC从 0.18 更新为 0.47。
SOC从 0.57 更新为 0.57。
SOC从 0.32 更新为 0.32。
SOC从 0.32 更新为 0.65。
已断开电池: batt_ev_018
时间步 7: 电池 batt_ev_018 已离开，当前SOC: 82.6%，能量满足率: 76.6%
已断开电池: batt_ev_036
时间步 7 执行前: 电池 batt_ev_036 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_157
时间步 7: 电池 batt_ev_157 已离开，当前SOC: 34.2%，能量满足率: 25.8%
已断开电池: batt_ev_187
时间步 7: 电池 batt_ev_187 已离开，当前SOC: 57.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.16781881123574144, voltage=-0.385377130017015, ctrl=-0.0, connection=1.76, completion=3.1818181818181817, energy=6.099463199747433, transformer=0.
已连接电池 batt_ev_055, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_055 已接入
已连接电池 batt_ev_216, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_216 已接入
已连接电池 batt_ev_247, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 87kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_247 已接入
时间步 7: 电池 batt_ev_244 已错过离开时间，无法接入
已连接电池 batt_ev_090, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
时间步 7 执行前: 排队电池 batt_ev_090 已接入
智能体的动作为: [ 1.         -0.784383   -0.         -0.8155061  -0.65824044 -0.8507092
 -1.         -1.         -0.         -0.         -1.        ]
已有历史设置self.charger_power=93.71440172195435，设置charger_power=51.879999999999995失败。
功率需求计算已禁用，直接使用充电桩功率: 93.71 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=81.5506100654602。
功率需求计算已禁用，直接使用充电桩功率: 81.55 kW。
初次设置charger_power=39.494426250457764。
功率需求计算已禁用，直接使用充电桩功率: 39.49 kW。
已有历史设置self.charger_power=51.653913259506226，设置charger_power=51.04255199432373失败。
功率需求计算已禁用，直接使用充电桩功率: 51.65 kW。
初次设置charger_power=120.0。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已有历史设置self.charger_power=60.0，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_180 充电的有无功功率为 51.653913259506226, -10.488774442980358
已在 set_all_batteries_before_solve 中设置 batt_ev_067 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_240 充电的有无功功率为 93.71440172195435, -19.029520895777058
已在 set_all_batteries_before_solve 中设置 batt_ev_158 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_106 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 81.5506100654602, -16.55955765377828
已在 set_all_batteries_before_solve 中设置 batt_ev_216 充电的有无功功率为 39.494426250457764, -8.019685296926406
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 0.0, -0.0
SOC从 0.81 更新为 1.00。
SOC从 0.28 更新为 0.28。
SOC从 0.28 更新为 0.49。
SOC从 0.42 更新为 0.61。
SOC从 0.59 更新为 0.84。
SOC从 0.18 更新为 0.52。
SOC从 0.47 更新为 0.76。
SOC从 0.48 更新为 0.48。
SOC从 0.32 更新为 0.32。
SOC从 0.65 更新为 0.97。
已断开电池: batt_ev_180
时间步 8: 电池 batt_ev_180 已离开，当前SOC: 83.9%，能量满足率: 84.4%
已断开电池: batt_ev_067
时间步 8: 电池 batt_ev_067 已离开，当前SOC: 32.0%，能量满足率: 0.0%
已断开电池: batt_ev_240
时间步 8 执行前: 电池 batt_ev_240 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_158
时间步 8: 电池 batt_ev_158 已离开，当前SOC: 28.0%，能量满足率: 0.0%
已断开电池: batt_ev_106
时间步 8: 电池 batt_ev_106 已离开，当前SOC: 97.2%，能量满足率: 98.8%
已断开电池: batt_ev_216
时间步 8: 电池 batt_ev_216 已离开，当前SOC: 60.6%，能量满足率: 33.3%
奖励各项的值：powerloss=-0.18425589546207383, voltage=-0.38583833755386765, ctrl=-0.0, connection=2.24, completion=2.8571428571428568, energy=5.922606911221068, transformer=0.
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
智能体的动作为: [ 1.        -0.7863517 -0.        -0.8158321 -0.6577164 -0.8501198
 -1.        -1.        -0.        -0.        -1.       ]
初次设置charger_power=62.90813446044922。
功率需求计算已禁用，直接使用充电桩功率: 62.91 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=81.5506100654602，设置charger_power=81.58320784568787失败。
功率需求计算已禁用，直接使用充电桩功率: 81.55 kW。
初次设置charger_power=65.77163934707642。
功率需求计算已禁用，直接使用充电桩功率: 65.77 kW。
初次设置charger_power=85.01198291778564。
功率需求计算已禁用，直接使用充电桩功率: 85.01 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已有历史设置self.charger_power=60.0，设置charger_power=50.56失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=100.0。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_096 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_055 充电的有无功功率为 81.5506100654602, -16.55955765377828
已在 set_all_batteries_before_solve 中设置 batt_ev_247 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_090 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_128 充电的有无功功率为 62.90813446044922, -12.774041526522655
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 65.77163934707642, -13.3555009935201
已在 set_all_batteries_before_solve 中设置 batt_ev_173 充电的有无功功率为 85.01198291778564, -17.262419389126393
已在 set_all_batteries_before_solve 中设置 batt_ev_132 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.42 更新为 0.62。
SOC从 0.72 更新为 0.72。
SOC从 0.49 更新为 0.71。
SOC从 0.22 更新为 0.39。
SOC从 0.57 更新为 0.90。
SOC从 0.52 更新为 0.87。
SOC从 0.76 更新为 1.00。
SOC从 0.48 更新为 0.48。
SOC从 0.18 更新为 0.18。
SOC从 0.08 更新为 0.40。
已断开电池: batt_ev_096
时间步 9 执行前: 电池 batt_ev_096 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_055
时间步 9: 电池 batt_ev_055 已离开，当前SOC: 70.9%，能量满足率: 61.3%
已断开电池: batt_ev_247
时间步 9: 电池 batt_ev_247 已离开，当前SOC: 87.0%，能量满足率: 86.2%
已断开电池: batt_ev_090
时间步 9: 电池 batt_ev_090 已离开，当前SOC: 48.0%，能量满足率: 0.0%
已断开电池: batt_ev_128
时间步 9: 电池 batt_ev_128 已离开，当前SOC: 61.7%，能量满足率: 35.1%
已断开电池: batt_ev_173
时间步 9: 电池 batt_ev_173 已离开，当前SOC: 89.7%，能量满足率: 79.7%
已断开电池: batt_ev_132
时间步 9: 电池 batt_ev_132 已离开，当前SOC: 18.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.20211377699835226, voltage=-0.4742400084931808, ctrl=-0.0, connection=2.8000000000000003, completion=2.571428571428571, energy=5.773454522691583, transformer=0.
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
智能体的动作为: [ 1.         -0.78671724 -0.         -0.8158922  -0.6576188  -0.8500094
 -1.         -1.         -0.         -0.         -1.        ]
初次设置charger_power=78.67172360420227。
功率需求计算已禁用，直接使用充电桩功率: 78.67 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=65.27137756347656。
功率需求计算已禁用，直接使用充电桩功率: 65.27 kW。
已有历史设置self.charger_power=65.77163934707642，设置charger_power=65.76188206672668失败。
功率需求计算已禁用，直接使用充电桩功率: 65.77 kW。
初次设置charger_power=68.00075054168701。
功率需求计算已禁用，直接使用充电桩功率: 68.00 kW。
初次设置charger_power=50.400000000000006。
功率需求计算已禁用，直接使用充电桩功率: 50.40 kW。
初次设置charger_power=100.0。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=100.0，设置charger_power=100.0失败。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 65.77163934707642, -13.3555009935201
已在 set_all_batteries_before_solve 中设置 batt_ev_150 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_191 充电的有无功功率为 78.67172360420227, -15.97497482483788
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 65.27137756347656, -13.253918505775935
已在 set_all_batteries_before_solve 中设置 batt_ev_161 充电的有无功功率为 68.00075054168701, -13.808141327101993
已在 set_all_batteries_before_solve 中设置 batt_ev_186 充电的有无功功率为 50.40000000000001, -10.234156495953808
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 0.0, -0.0
SOC从 0.18 更新为 0.41。
SOC从 0.72 更新为 0.72。
SOC从 0.22 更新为 0.46。
SOC从 0.39 更新为 0.57。
SOC从 0.22 更新为 0.46。
SOC从 0.82 更新为 1.00。
SOC从 0.28 更新为 0.57。
SOC从 0.38 更新为 0.38。
SOC从 0.18 更新为 0.18。
SOC从 0.40 更新为 0.72。
已断开电池: batt_ev_150
时间步 10: 电池 batt_ev_150 已离开，当前SOC: 72.1%，能量满足率: 71.2%
已断开电池: batt_ev_191
时间步 10: 电池 batt_ev_191 已离开，当前SOC: 40.6%，能量满足率: 28.3%
已断开电池: batt_ev_161
时间步 10: 电池 batt_ev_161 已离开，当前SOC: 45.6%，能量满足率: 31.1%
已断开电池: batt_ev_186
时间步 10 执行前: 电池 batt_ev_186 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.21189122418668468, voltage=-0.4552970717420801, ctrl=-0.0, connection=3.12, completion=2.564102564102564, energy=5.772468974056377, transformer=0.
已连接电池 batt_ev_008, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 60kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_008 已接入
已连接电池 batt_ev_162, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_162 已接入
已连接电池 batt_ev_170, 初始SOC: 42.0%, 最大功率: 120kW, 电池容量: 99kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_170 已接入
已连接电池 batt_ev_085, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
时间步 10 执行前: 排队电池 batt_ev_085 已接入
智能体的动作为: [ 1.         -0.78675026 -0.         -0.8158975  -0.65760994 -0.84999925
 -1.         -1.         -0.         -0.         -1.        ]
初次设置charger_power=62.94002056121826。
功率需求计算已禁用，直接使用充电桩功率: 62.94 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=65.27137756347656，设置charger_power=65.27180194854736失败。
功率需求计算已禁用，直接使用充电桩功率: 65.27 kW。
已有历史设置self.charger_power=65.77163934707642，设置charger_power=65.76099395751953失败。
功率需求计算已禁用，直接使用充电桩功率: 65.77 kW。
初次设置charger_power=50.99995493888855。
功率需求计算已禁用，直接使用充电桩功率: 51.00 kW。
初次设置charger_power=120.0。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已有历史设置self.charger_power=100.0，设置charger_power=100.0失败。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_220 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_016 充电的有无功功率为 65.77163934707642, -13.3555009935201
已在 set_all_batteries_before_solve 中设置 batt_ev_193 充电的有无功功率为 65.27137756347656, -13.253918505775935
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_008 充电的有无功功率为 62.94002056121826, -12.780516275437659
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 50.99995493888855, -10.355982542285272
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_085 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.68 更新为 0.94。
SOC从 0.72 更新为 0.72。
SOC从 0.46 更新为 0.71。
SOC从 0.57 更新为 0.74。
SOC从 0.28 更新为 0.48。
SOC从 0.42 更新为 0.72。
SOC从 0.57 更新为 0.86。
SOC从 0.38 更新为 0.38。
SOC从 0.18 更新为 0.18。
SOC从 0.62 更新为 0.99。
已断开电池: batt_ev_220
时间步 11: 电池 batt_ev_220 已离开，当前SOC: 72.0%，能量满足率: 0.0%
已断开电池: batt_ev_016
时间步 11: 电池 batt_ev_016 已离开，当前SOC: 73.9%，能量满足率: 68.3%
已断开电池: batt_ev_193
时间步 11: 电池 batt_ev_193 已离开，当前SOC: 70.7%，能量满足率: 64.1%
已断开电池: batt_ev_008
时间步 11 执行前: 电池 batt_ev_008 已充满 (SOC: 94.2%)，离开
已断开电池: batt_ev_085
时间步 11 执行前: 电池 batt_ev_085 已充满 (SOC: 98.6%)，离开
奖励各项的值：powerloss=-0.22247587313445463, voltage=-0.49178519015183886, ctrl=-0.0, connection=3.52, completion=2.727272727272727, energy=5.871985679708259, transformer=0.
时间步 11: 电池 batt_ev_222 已错过离开时间，无法接入
已连接电池 batt_ev_114, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_114 已接入
已连接电池 batt_ev_009, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
时间步 11 执行前: 排队电池 batt_ev_009 已接入
已连接电池 batt_ev_113, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_065, 初始SOC: 62.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_203, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [ 1.         -0.78675336 -0.         -0.815898   -0.6576091  -0.84999835
 -1.         -1.         -0.         -0.         -1.        ]
初次设置charger_power=16.319999999999993。
功率需求计算已禁用，直接使用充电桩功率: 16.32 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=97.90776014328003。
功率需求计算已禁用，直接使用充电桩功率: 97.91 kW。
初次设置charger_power=39.45654630661011。
功率需求计算已禁用，直接使用充电桩功率: 39.46 kW。
已有历史设置self.charger_power=50.99995493888855，设置charger_power=50.99990129470825失败。
功率需求计算已禁用，直接使用充电桩功率: 51.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=109.68失败。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已有历史设置self.charger_power=100.0，设置charger_power=47.68000000000001失败。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_194 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 50.99995493888855, -10.355982542285272
已在 set_all_batteries_before_solve 中设置 batt_ev_170 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_114 充电的有无功功率为 16.319999999999993, -3.313917341546946
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 97.90776014328003, -19.88101864036977
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 39.45654630661011, -8.011993446263812
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.92 更新为 1.00。
SOC从 0.18 更新为 0.18。
SOC从 0.28 更新为 0.60。
SOC从 0.62 更新为 0.80。
SOC从 0.48 更新为 0.67。
SOC从 0.72 更新为 1.00。
SOC从 0.86 更新为 1.00。
SOC从 0.38 更新为 0.38。
SOC从 0.18 更新为 0.18。
SOC从 0.28 更新为 0.62。
已断开电池: batt_ev_194
时间步 12 执行前: 电池 batt_ev_194 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_170
时间步 12 执行前: 电池 batt_ev_170 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_114
时间步 12 执行前: 电池 batt_ev_114 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.22343631030380964, voltage=-0.5089610656674393, ctrl=-0.0, connection=3.7600000000000002, completion=3.1914893617021276, energy=6.135475955471562, transformer=0.
已连接电池 batt_ev_011, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 12 执行前: 排队电池 batt_ev_011 已接入
已连接电池 batt_ev_041, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_232, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [ 1.         -0.78675395 -0.         -0.8158981  -0.65760887 -0.8499982
 -1.         -1.         -0.         -0.         -1.        ]
初次设置charger_power=62.94031620025635。
功率需求计算已禁用，直接使用充电桩功率: 62.94 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=97.90776014328003，设置charger_power=97.90777444839478失败。
功率需求计算已禁用，直接使用充电桩功率: 97.91 kW。
已有历史设置self.charger_power=39.45654630661011，设置charger_power=39.45653200149536失败。
功率需求计算已禁用，直接使用充电桩功率: 39.46 kW。
已有历史设置self.charger_power=50.99995493888855，设置charger_power=50.99989056587219失败。
功率需求计算已禁用，直接使用充电桩功率: 51.00 kW。
初次设置charger_power=80.0。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=60.0，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_078 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_000 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_162 充电的有无功功率为 50.99995493888855, -10.355982542285272
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 97.90776014328003, -19.88101864036977
已在 set_all_batteries_before_solve 中设置 batt_ev_065 充电的有无功功率为 39.45654630661011, -8.011993446263812
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_011 充电的有无功功率为 62.94031620025635, -12.780576307504766
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.32 更新为 0.54。
SOC从 0.18 更新为 0.18。
SOC从 0.60 更新为 0.92。
SOC从 0.80 更新为 0.99。
SOC从 0.67 更新为 0.87。
SOC从 0.12 更新为 0.49。
SOC从 0.38 更新为 0.61。
SOC从 0.38 更新为 0.38。
SOC从 0.18 更新为 0.18。
SOC从 0.62 更新为 0.96。
已断开电池: batt_ev_078
时间步 13: 电池 batt_ev_078 已离开，当前SOC: 38.0%，能量满足率: -0.0%
已断开电池: batt_ev_000
时间步 13: 电池 batt_ev_000 已离开，当前SOC: 18.0%，能量满足率: 0.0%
已断开电池: batt_ev_162
时间步 13: 电池 batt_ev_162 已离开，当前SOC: 86.8%，能量满足率: 84.1%
已断开电池: batt_ev_065
时间步 13 执行前: 电池 batt_ev_065 已充满 (SOC: 98.5%)，离开
已断开电池: batt_ev_011
时间步 13: 电池 batt_ev_011 已离开，当前SOC: 54.5%，能量满足率: 34.0%
奖励各项的值：powerloss=-0.2266626189035203, voltage=-0.5483539061177445, ctrl=-0.0, connection=4.16, completion=3.076923076923077, energy=5.964975484971514, transformer=0.
已连接电池 batt_ev_237, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_237 已接入
已连接电池 batt_ev_052, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_052 已接入
已连接电池 batt_ev_206, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 62kWh，并创BMS。
时间步 13 执行前: 排队电池 batt_ev_206 已接入
已连接电池 batt_ev_172, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
已连接电池 batt_ev_229, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
智能体的动作为: [ 1.         -0.78675354 -0.         -0.8158981  -0.65760946 -0.84999734
 -1.         -1.         -0.         -0.         -1.        ]
初次设置charger_power=47.205212116241455。
功率需求计算已禁用，直接使用充电桩功率: 47.21 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=97.90776014328003，设置charger_power=25.920000000000016失败。
功率需求计算已禁用，直接使用充电桩功率: 97.91 kW。
初次设置charger_power=39.45656776428223。
功率需求计算已禁用，直接使用充电桩功率: 39.46 kW。
初次设置charger_power=50.99984049797058。
功率需求计算已禁用，直接使用充电桩功率: 51.00 kW。
已有历史设置self.charger_power=80.0，设置charger_power=80.0失败。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已有历史设置self.charger_power=60.0，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=60.0，设置charger_power=6.719999999999999失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_113 充电的有无功功率为 97.90776014328003, -19.88101864036977
已在 set_all_batteries_before_solve 中设置 batt_ev_203 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 47.205212116241455, -9.585427147268053
已在 set_all_batteries_before_solve 中设置 batt_ev_052 充电的有无功功率为 39.45656776428223, -8.01199780342997
已在 set_all_batteries_before_solve 中设置 batt_ev_206 充电的有无功功率为 50.99984049797058, -10.355959304065749
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 0.0, -0.0
SOC从 0.78 更新为 0.95。
SOC从 0.18 更新为 0.18。
SOC从 0.92 更新为 1.00。
SOC从 0.38 更新为 0.54。
SOC从 0.22 更新为 0.43。
SOC从 0.49 更新为 0.86。
SOC从 0.61 更新为 0.84。
SOC从 0.38 更新为 0.38。
SOC从 0.38 更新为 0.38。
SOC从 0.96 更新为 1.00。
已断开电池: batt_ev_113
时间步 14 执行前: 电池 batt_ev_113 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_203
时间步 14 执行前: 电池 batt_ev_203 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_206
时间步 14: 电池 batt_ev_206 已离开，当前SOC: 42.6%，能量满足率: 34.3%
奖励各项的值：powerloss=-0.22332061812684798, voltage=-0.5437416819685126, ctrl=-0.0, connection=4.4, completion=3.2727272727272725, energy=6.065566264970135, transformer=0.
已连接电池 batt_ev_164, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 14 执行前: 排队电池 batt_ev_164 已接入
已连接电池 batt_ev_134, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_214, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 80kWh，并创BMS。
智能体的动作为: [ 1.         -0.78675544 -0.         -0.81590044 -0.6576138  -0.84999025
 -1.         -1.         -0.         -0.         -1.        ]
已有历史设置self.charger_power=47.205212116241455，设置charger_power=13.519999999999982失败。
功率需求计算已禁用，直接使用充电桩功率: 47.21 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=48.95402669906616。
功率需求计算已禁用，直接使用充电桩功率: 48.95 kW。
已有历史设置self.charger_power=39.45656776428223，设置charger_power=39.45682883262634失败。
功率需求计算已禁用，直接使用充电桩功率: 39.46 kW。
初次设置charger_power=67.99921989440918。
功率需求计算已禁用，直接使用充电桩功率: 68.00 kW。
已有历史设置self.charger_power=80.0，设置charger_power=30.080000000000013失败。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已有历史设置self.charger_power=60.0，设置charger_power=41.19999999999999失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=100.0。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_009 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_041 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_232 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_237 充电的有无功功率为 47.205212116241455, -9.585427147268053
已在 set_all_batteries_before_solve 中设置 batt_ev_052 充电的有无功功率为 39.45656776428223, -8.01199780342997
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 48.95402669906616, -9.940539094153653
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 67.99921989440918, -13.807830515915853
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.95 更新为 1.00。
SOC从 0.18 更新为 0.18。
SOC从 0.42 更新为 0.63。
SOC从 0.54 更新为 0.71。
SOC从 0.32 更新为 0.63。
SOC从 0.86 更新为 1.00。
SOC从 0.84 更新为 1.00。
SOC从 0.38 更新为 0.38。
SOC从 0.38 更新为 0.38。
SOC从 0.48 更新为 0.79。
已断开电池: batt_ev_009
时间步 15: 电池 batt_ev_009 已离开，当前SOC: 18.0%，能量满足率: 0.0%
已断开电池: batt_ev_041
时间步 15 执行前: 电池 batt_ev_041 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_232
时间步 15 执行前: 电池 batt_ev_232 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_237
时间步 15 执行前: 电池 batt_ev_237 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_052
时间步 15 执行前: 电池 batt_ev_052 已充满 (SOC: 70.9%)，离开
奖励各项的值：powerloss=-0.22279259781847033, voltage=-0.5378331947173898, ctrl=-0.0, connection=4.8, completion=3.6666666666666665, energy=6.226769076222624, transformer=0.
已连接电池 batt_ev_143, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_143 已接入
已连接电池 batt_ev_245, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_245 已接入
已连接电池 batt_ev_098, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 70kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_098 已接入
已连接电池 batt_ev_190, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 63kWh，并创BMS。
时间步 15 执行前: 排队电池 batt_ev_190 已接入
智能体的动作为: [ 1.        -0.7867985 -0.        -0.8159412 -0.6576482 -0.8499274
 -1.        -1.        -0.        -0.        -1.       ]
初次设置charger_power=62.943878173828125。
功率需求计算已禁用，直接使用充电桩功率: 62.94 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=48.95402669906616，设置charger_power=48.956472873687744失败。
功率需求计算已禁用，直接使用充电桩功率: 48.95 kW。
初次设置charger_power=52.61185646057129。
功率需求计算已禁用，直接使用充电桩功率: 52.61 kW。
已有历史设置self.charger_power=67.99921989440918，设置charger_power=67.99419403076172失败。
功率需求计算已禁用，直接使用充电桩功率: 68.00 kW。
初次设置charger_power=100.0。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=100.0，设置charger_power=66.4失败。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_172 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 48.95402669906616, -9.940539094153653
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 67.99921989440918, -13.807830515915853
已在 set_all_batteries_before_solve 中设置 batt_ev_214 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 62.943878173828125, -12.781299597087465
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 52.61185646057129, -10.683293106352082
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.48 更新为 0.75。
SOC从 0.38 更新为 0.38。
SOC从 0.63 更新为 0.85。
SOC从 0.42 更新为 0.61。
SOC从 0.63 更新为 0.95。
SOC从 0.18 更新为 0.58。
SOC从 0.38 更新为 0.38。
SOC从 0.38 更新为 0.38。
SOC从 0.79 更新为 1.00。
已断开电池: batt_ev_172
时间步 16: 电池 batt_ev_172 已离开，当前SOC: 38.0%，能量满足率: 0.0%
已断开电池: batt_ev_214
时间步 16 执行前: 电池 batt_ev_214 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.22125344228207827, voltage=-0.5318913521091551, ctrl=-0.0, connection=4.96, completion=3.709677419354839, energy=6.187195880215443, transformer=0.
已连接电池 batt_ev_069, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 56kWh，并创BMS。
已连接电池 batt_ev_071, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
智能体的动作为: [ 1.        -0.7870537 -0.        -0.8179967 -0.6577679 -0.8494611
 -1.        -1.        -0.        -0.        -1.       ]
已有历史设置self.charger_power=62.943878173828125，设置charger_power=59.75999999999999失败。
功率需求计算已禁用，直接使用充电桩功率: 62.94 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=48.95402669906616，设置charger_power=34.31999999999999失败。
功率需求计算已禁用，直接使用充电桩功率: 48.95 kW。
已有历史设置self.charger_power=52.61185646057129，设置charger_power=52.62143135070801失败。
功率需求计算已禁用，直接使用充电桩功率: 52.61 kW。
已有历史设置self.charger_power=67.99921989440918，设置charger_power=10.879999999999995失败。
功率需求计算已禁用，直接使用充电桩功率: 68.00 kW。
已有历史设置self.charger_power=100.0，设置charger_power=100.0失败。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_164 充电的有无功功率为 48.95402669906616, -9.940539094153653
已在 set_all_batteries_before_solve 中设置 batt_ev_134 充电的有无功功率为 67.99921989440918, -13.807830515915853
已在 set_all_batteries_before_solve 中设置 batt_ev_143 充电的有无功功率为 62.943878173828125, -12.781299597087465
已在 set_all_batteries_before_solve 中设置 batt_ev_245 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 52.61185646057129, -10.683293106352082
已在 set_all_batteries_before_solve 中设置 batt_ev_190 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 0.0, -0.0
SOC从 0.75 更新为 1.00。
SOC从 0.38 更新为 0.38。
SOC从 0.85 更新为 1.00。
SOC从 0.61 更新为 0.80。
SOC从 0.95 更新为 1.00。
SOC从 0.58 更新为 0.97。
SOC从 0.38 更新为 0.65。
SOC从 0.42 更新为 0.42。
SOC从 0.38 更新为 0.38。
已断开电池: batt_ev_164
时间步 17 执行前: 电池 batt_ev_164 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_134
时间步 17 执行前: 电池 batt_ev_134 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_143
时间步 17 执行前: 电池 batt_ev_143 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_245
时间步 17: 电池 batt_ev_245 已离开，当前SOC: 38.0%，能量满足率: -0.0%
已断开电池: batt_ev_190
时间步 17 执行前: 电池 batt_ev_190 已充满 (SOC: 97.4%)，离开
奖励各项的值：powerloss=-0.221925371053214, voltage=-0.5067816083163734, ctrl=-0.0, connection=5.36, completion=4.029850746268656, energy=6.322479769751603, transformer=0.
智能体的动作为: [ 1.         -0.8717471  -0.         -0.7991334  -0.6261299  -0.75753784
 -1.         -1.         -0.         -0.         -1.        ]
已有历史设置self.charger_power=52.61185646057129，设置charger_power=50.090394020080566失败。
功率需求计算已禁用，直接使用充电桩功率: 52.61 kW。
已有历史设置self.charger_power=60.0，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_229 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_098 充电的有无功功率为 52.61185646057129, -10.683293106352082
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 0.0, -0.0
SOC从 0.80 更新为 0.98。
SOC从 0.65 更新为 0.92。
SOC从 0.42 更新为 0.42。
SOC从 0.38 更新为 0.38。
已断开电池: batt_ev_229
时间步 18: 电池 batt_ev_229 已离开，当前SOC: 38.0%，能量满足率: 0.0%
已断开电池: batt_ev_098
时间步 18 执行前: 电池 batt_ev_098 已充满 (SOC: 98.4%)，离开
奖励各项的值：powerloss=-0.21344701048813425, voltage=-0.3362390920233871, ctrl=-0.0, connection=5.5200000000000005, completion=4.057971014492754, energy=6.284147022802281, transformer=0.
已连接电池 batt_ev_083, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_174, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_167, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [ 1.         -0.72012466 -0.         -0.52180153 -0.5794875  -0.2913173
 -0.8998104  -0.51109225 -0.         -0.         -0.8498886 ]
初次设置charger_power=57.60997295379639。
功率需求计算已禁用，直接使用充电桩功率: 57.61 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=60.0，设置charger_power=18.879999999999995失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=67.99108982086182。
功率需求计算已禁用，直接使用充电桩功率: 67.99 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_069 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_071 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_083 充电的有无功功率为 67.99108982086182, -13.806179634070473
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 57.60997295379639, -11.698203947159097
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 0.0, -0.0
SOC从 0.18 更新为 0.40。
SOC从 0.32 更新为 0.32。
SOC从 0.92 更新为 1.00。
SOC从 0.42 更新为 0.42。
SOC从 0.68 更新为 0.99。
已断开电池: batt_ev_069
时间步 19 执行前: 电池 batt_ev_069 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_071
时间步 19: 电池 batt_ev_071 已离开，当前SOC: 42.0%，能量满足率: 0.0%
已断开电池: batt_ev_083
时间步 19 执行前: 电池 batt_ev_083 已充满 (SOC: 99.5%)，离开
奖励各项的值：powerloss=-0.21098749422377422, voltage=-0.21235739650069307, ctrl=-0.0, connection=5.76, completion=4.166666666666667, energy=6.300085341296631, transformer=0.
已连接电池 batt_ev_115, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
已连接电池 batt_ev_181, 初始SOC: 56.99999999999999%, 最大功率: 80kW, 电池容量: 69kWh，并创BMS。
已连接电池 batt_ev_182, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 95kWh，并创BMS。
智能体的动作为: [ 1.         -0.7343682  -0.         -0.5288674  -0.6732933  -0.46219933
 -0.96130824 -0.4610282  -0.         -0.         -1.        ]
已有历史设置self.charger_power=57.60997295379639，设置charger_power=58.74945640563965失败。
功率需求计算已禁用，直接使用充电桩功率: 57.61 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=31.7320454120636。
功率需求计算已禁用，直接使用充电桩功率: 31.73 kW。
初次设置charger_power=36.9759464263916。
功率需求计算已禁用，直接使用充电桩功率: 36.98 kW。
初次设置charger_power=115.35698890686035。
功率需求计算已禁用，直接使用充电桩功率: 115.36 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 57.60997295379639, -11.698203947159097
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 31.7320454120636, -6.443466640551028
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 36.9759464263916, -7.508286157017769
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 115.35698890686035, -23.424235662198733
SOC从 0.40 更新为 0.62。
SOC从 0.32 更新为 0.32。
SOC从 0.12 更新为 0.29。
SOC从 0.57 更新为 0.70。
SOC从 0.28 更新为 0.58。
奖励各项的值：powerloss=-0.20512090027601362, voltage=-0.1557455143145714, ctrl=-0.0, connection=5.76, completion=4.166666666666667, energy=6.300085341296631, transformer=0.
已连接电池 batt_ev_037, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 65kWh，并创BMS。
已连接电池 batt_ev_138, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
已连接电池 batt_ev_095, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
智能体的动作为: [ 1.        -0.7825387 -0.        -0.7085867 -0.5810612 -0.5317323
 -1.        -1.        -0.        -0.        -1.       ]
已有历史设置self.charger_power=57.60997295379639，设置charger_power=62.6030969619751失败。
功率需求计算已禁用，直接使用充电桩功率: 57.61 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=31.7320454120636，设置charger_power=42.515201568603516失败。
功率需求计算已禁用，直接使用充电桩功率: 31.73 kW。
初次设置charger_power=46.48489475250244。
功率需求计算已禁用，直接使用充电桩功率: 46.48 kW。
已有历史设置self.charger_power=36.9759464263916，设置charger_power=42.5385856628418失败。
功率需求计算已禁用，直接使用充电桩功率: 36.98 kW。
已有历史设置self.charger_power=115.35698890686035，设置charger_power=120.0失败。
功率需求计算已禁用，直接使用充电桩功率: 115.36 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 57.60997295379639, -11.698203947159097
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 31.7320454120636, -6.443466640551028
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 36.9759464263916, -7.508286157017769
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 115.35698890686035, -23.424235662198733
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 46.48489475250244, -9.439160468155793
已在 set_all_batteries_before_solve 中设置 batt_ev_138 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.62 更新为 0.83。
SOC从 0.32 更新为 0.32。
SOC从 0.29 更新为 0.46。
SOC从 0.32 更新为 0.50。
SOC从 0.70 更新为 0.84。
SOC从 0.58 更新为 0.89。
SOC从 0.12 更新为 0.43。
SOC从 0.48 更新为 0.48。
奖励各项的值：powerloss=-0.20935645559583793, voltage=-0.11370985343895468, ctrl=-0.0, connection=5.76, completion=4.166666666666667, energy=6.300085341296631, transformer=0.
已连接电池 batt_ev_197, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 75kWh，并创BMS。
已连接电池 batt_ev_026, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 102kWh，并创BMS。
智能体的动作为: [ 1.         -0.81380475 -0.         -0.76095575 -0.6150513  -0.7098002
 -1.         -1.         -0.         -0.         -1.        ]
已有历史设置self.charger_power=57.60997295379639，设置charger_power=43.68000000000001失败。
功率需求计算已禁用，直接使用充电桩功率: 57.61 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=31.7320454120636，设置charger_power=45.65734505653381失败。
功率需求计算已禁用，直接使用充电桩功率: 31.73 kW。
已有历史设置self.charger_power=46.48489475250244，设置charger_power=49.20410633087158失败。
功率需求计算已禁用，直接使用充电桩功率: 46.48 kW。
已有历史设置self.charger_power=36.9759464263916，设置charger_power=44.75999999999999失败。
功率需求计算已禁用，直接使用充电桩功率: 36.98 kW。
已有历史设置self.charger_power=115.35698890686035，设置charger_power=42.879999999999995失败。
功率需求计算已禁用，直接使用充电桩功率: 115.36 kW。
已有历史设置self.charger_power=60.0，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_174 充电的有无功功率为 57.60997295379639, -11.698203947159097
已在 set_all_batteries_before_solve 中设置 batt_ev_167 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 31.7320454120636, -6.443466640551028
已在 set_all_batteries_before_solve 中设置 batt_ev_181 充电的有无功功率为 36.9759464263916, -7.508286157017769
已在 set_all_batteries_before_solve 中设置 batt_ev_182 充电的有无功功率为 115.35698890686035, -23.424235662198733
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 46.48489475250244, -9.439160468155793
已在 set_all_batteries_before_solve 中设置 batt_ev_138 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.83 更新为 1.00。
SOC从 0.32 更新为 0.32。
SOC从 0.46 更新为 0.64。
SOC从 0.50 更新为 0.68。
SOC从 0.84 更新为 0.97。
SOC从 0.89 更新为 1.00。
SOC从 0.43 更新为 0.74。
SOC从 0.52 更新为 0.52。
SOC从 0.48 更新为 0.48。
SOC从 0.32 更新为 0.61。
已断开电池: batt_ev_174
时间步 22 执行前: 电池 batt_ev_174 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_167
时间步 22: 电池 batt_ev_167 已离开，当前SOC: 32.0%，能量满足率: 0.0%
已断开电池: batt_ev_181
时间步 22 执行前: 电池 batt_ev_181 已充满 (SOC: 97.2%)，离开
已断开电池: batt_ev_182
时间步 22 执行前: 电池 batt_ev_182 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_138
时间步 22: 电池 batt_ev_138 已离开，当前SOC: 48.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.2050641253764697, voltage=-0.10215449623290906, ctrl=-0.0, connection=6.16, completion=4.285714285714286, energy=6.280599280173473, transformer=0.
已连接电池 batt_ev_212, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
时间步 22 执行前: 排队电池 batt_ev_212 已接入
已连接电池 batt_ev_010, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 71kWh，并创BMS。
时间步 22 执行前: 排队电池 batt_ev_010 已接入
已连接电池 batt_ev_241, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 68kWh，并创BMS。
已连接电池 batt_ev_084, 初始SOC: 78.0%, 最大功率: 100kW, 电池容量: 62kWh，并创BMS。
已连接电池 batt_ev_038, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [ 1.         -0.858503   -0.         -0.80710036 -0.6295592  -0.76929057
 -1.         -1.         -0.         -0.         -1.        ]
初次设置charger_power=51.51017904281616。
功率需求计算已禁用，直接使用充电桩功率: 51.51 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=31.7320454120636，设置charger_power=48.426021337509155失败。
功率需求计算已禁用，直接使用充电桩功率: 31.73 kW。
已有历史设置self.charger_power=46.48489475250244，设置charger_power=50.36473751068115失败。
功率需求计算已禁用，直接使用充电桩功率: 46.48 kW。
初次设置charger_power=46.15743398666382。
功率需求计算已禁用，直接使用充电桩功率: 46.16 kW。
初次设置charger_power=54.56。
功率需求计算已禁用，直接使用充电桩功率: 54.56 kW。
已有历史设置self.charger_power=60.0，设置charger_power=48.96000000000001失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 31.7320454120636, -6.443466640551028
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 46.48489475250244, -9.439160468155793
已在 set_all_batteries_before_solve 中设置 batt_ev_095 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_212 充电的有无功功率为 51.51017904281616, -10.459587965451995
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 46.15743398666382, -9.372666723634415
已在 set_all_batteries_before_solve 中设置 batt_ev_084 充电的有无功功率为 54.56, -11.078880524191266
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 0.0, -0.0
SOC从 0.22 更新为 0.46。
SOC从 0.48 更新为 0.48。
SOC从 0.64 更新为 0.81。
SOC从 0.68 更新为 0.86。
SOC从 0.48 更新为 0.65。
SOC从 0.78 更新为 1.00。
SOC从 0.74 更新为 1.00。
SOC从 0.52 更新为 0.52。
SOC从 0.42 更新为 0.42。
SOC从 0.61 更新为 0.91。
已断开电池: batt_ev_095
时间步 23 执行前: 电池 batt_ev_095 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_212
时间步 23: 电池 batt_ev_212 已离开，当前SOC: 45.9%，能量满足率: 31.4%
已断开电池: batt_ev_084
时间步 23 执行前: 电池 batt_ev_084 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.18346166222627114, voltage=-0.11447952530014849, ctrl=-0.0, connection=6.4, completion=4.375, energy=6.334306826660145, transformer=0.
已连接电池 batt_ev_040, 初始SOC: 78.0%, 最大功率: 60kW, 电池容量: 57kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_040 已接入
已连接电池 batt_ev_046, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_046 已接入
已连接电池 batt_ev_050, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 48kWh，并创BMS。
时间步 23 执行前: 排队电池 batt_ev_050 已接入
智能体的动作为: [ 1.         -0.81474614 -0.         -0.76164633 -0.61517435 -0.7105313
 -1.         -1.         -0.         -0.         -1.        ]
初次设置charger_power=48.88476848602295。
功率需求计算已禁用，直接使用充电桩功率: 48.88 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=31.7320454120636，设置charger_power=35.03999999999999失败。
功率需求计算已禁用，直接使用充电桩功率: 31.73 kW。
已有历史设置self.charger_power=46.48489475250244，设置charger_power=37.360000000000014失败。
功率需求计算已禁用，直接使用充电桩功率: 46.48 kW。
已有历史设置self.charger_power=46.15743398666382，设置charger_power=42.63187766075134失败。
功率需求计算已禁用，直接使用充电桩功率: 46.16 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=37.44失败。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_115 充电的有无功功率为 31.7320454120636, -6.443466640551028
已在 set_all_batteries_before_solve 中设置 batt_ev_037 充电的有无功功率为 46.48489475250244, -9.439160468155793
已在 set_all_batteries_before_solve 中设置 batt_ev_197 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_026 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 46.15743398666382, -9.372666723634415
已在 set_all_batteries_before_solve 中设置 batt_ev_038 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_040 充电的有无功功率为 48.88476848602295, -9.926475614175194
已在 set_all_batteries_before_solve 中设置 batt_ev_046 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_050 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.78 更新为 0.99。
SOC从 0.48 更新为 0.48。
SOC从 0.81 更新为 0.98。
SOC从 0.86 更新为 1.00。
SOC从 0.65 更新为 0.82。
SOC从 0.42 更新为 0.73。
SOC从 0.28 更新为 0.59。
SOC从 0.52 更新为 0.52。
SOC从 0.42 更新为 0.42。
SOC从 0.91 更新为 1.00。
已断开电池: batt_ev_115
时间步 24 执行前: 电池 batt_ev_115 已充满 (SOC: 98.2%)，离开
已断开电池: batt_ev_037
时间步 24 执行前: 电池 batt_ev_037 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_197
时间步 24: 电池 batt_ev_197 已离开，当前SOC: 52.0%，能量满足率: 0.0%
已断开电池: batt_ev_026
时间步 24 执行前: 电池 batt_ev_026 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_038
时间步 24: 电池 batt_ev_038 已离开，当前SOC: 42.0%，能量满足率: 0.0%
已断开电池: batt_ev_040
时间步 24 执行前: 电池 batt_ev_040 已充满 (SOC: 99.4%)，离开
奖励各项的值：powerloss=-0.1673599060178334, voltage=-0.1879757504179147, ctrl=-0.0, connection=6.88, completion=4.534883720930233, energy=6.357494722474554, transformer=0.
已连接电池 batt_ev_125, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_125 已接入
已连接电池 batt_ev_137, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 84kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_137 已接入
已连接电池 batt_ev_221, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 75kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_221 已接入
已连接电池 batt_ev_109, 初始SOC: 88.0%, 最大功率: 100kW, 电池容量: 70kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_109 已接入
已连接电池 batt_ev_034, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 68kWh，并创BMS。
时间步 24 执行前: 排队电池 batt_ev_034 已接入
已连接电池 batt_ev_141, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 75kWh，并创BMS。
智能体的动作为: [ 1.        -0.8131341 -0.        -0.7605011 -0.6149273 -0.7093153
 -1.        -1.        -0.        -0.        -1.       ]
初次设置charger_power=48.788044452667236。
功率需求计算已禁用，直接使用充电桩功率: 48.79 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.840086936950684。
功率需求计算已禁用，直接使用充电桩功率: 60.84 kW。
初次设置charger_power=73.79127502441406。
功率需求计算已禁用，直接使用充电桩功率: 73.79 kW。
已有历史设置self.charger_power=46.15743398666382，设置charger_power=42.55891799926758失败。
功率需求计算已禁用，直接使用充电桩功率: 46.16 kW。
已有历史设置self.charger_power=60.0，设置charger_power=53.68000000000001失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已有历史设置self.charger_power=60.0，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=120.0。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_241 充电的有无功功率为 46.15743398666382, -9.372666723634415
已在 set_all_batteries_before_solve 中设置 batt_ev_046 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_050 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_125 充电的有无功功率为 48.788044452667236, -9.906834961510862
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 60.840086936950684, -12.354106566273575
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 73.79127502441406, -14.983957472932957
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_141 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.28 更新为 0.46。
SOC从 0.48 更新为 0.48。
SOC从 0.52 更新为 0.70。
SOC从 0.28 更新为 0.53。
SOC从 0.82 更新为 0.99。
SOC从 0.73 更新为 1.00。
SOC从 0.59 更新为 0.90。
SOC从 0.88 更新为 0.88。
SOC从 0.22 更新为 0.22。
SOC从 0.28 更新为 0.68。
已断开电池: batt_ev_241
时间步 25 执行前: 电池 batt_ev_241 已充满 (SOC: 98.9%)，离开
已断开电池: batt_ev_046
时间步 25 执行前: 电池 batt_ev_046 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_050
时间步 25 执行前: 电池 batt_ev_050 已充满 (SOC: 90.5%)，离开
已断开电池: batt_ev_125
时间步 25: 电池 batt_ev_125 已离开，当前SOC: 46.2%，能量满足率: 28.5%
奖励各项的值：powerloss=-0.14729200270327775, voltage=-0.24498612720098345, ctrl=-0.0, connection=7.2, completion=4.666666666666667, energy=6.439885504294923, transformer=0.
已连接电池 batt_ev_101, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 68kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_101 已接入
已连接电池 batt_ev_075, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_075 已接入
已连接电池 batt_ev_093, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_093 已接入
已连接电池 batt_ev_047, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 56kWh，并创BMS。
时间步 25 执行前: 排队电池 batt_ev_047 已接入
智能体的动作为: [ 1.         -0.8137115  -0.         -0.76094913 -0.6149808  -0.70978546
 -1.         -1.         -0.         -0.         -1.        ]
初次设置charger_power=65.09692192077637。
功率需求计算已禁用，直接使用充电桩功率: 65.10 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=60.840086936950684，设置charger_power=60.87593078613281失败。
功率需求计算已禁用，直接使用充电桩功率: 60.84 kW。
已有历史设置self.charger_power=73.79127502441406，设置charger_power=73.79769802093506失败。
功率需求计算已禁用，直接使用充电桩功率: 73.79 kW。
初次设置charger_power=70.97854614257812。
功率需求计算已禁用，直接使用充电桩功率: 70.98 kW。
初次设置charger_power=100.0。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=96.0失败。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 60.840086936950684, -12.354106566273575
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 73.79127502441406, -14.983957472932957
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_141 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 65.09692192077637, -13.218493776629188
已在 set_all_batteries_before_solve 中设置 batt_ev_075 充电的有无功功率为 70.97854614257812, -14.41280851346077
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.22 更新为 0.46。
SOC从 0.48 更新为 0.48。
SOC从 0.70 更新为 0.88。
SOC从 0.53 更新为 0.77。
SOC从 0.42 更新为 0.61。
SOC从 0.38 更新为 0.71。
SOC从 0.38 更新为 0.65。
SOC从 0.88 更新为 0.88。
SOC从 0.22 更新为 0.22。
SOC从 0.68 更新为 1.00。
已断开电池: batt_ev_141
时间步 26 执行前: 电池 batt_ev_141 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.1469633959988813, voltage=-0.26583936856691803, ctrl=-0.0, connection=7.28, completion=4.725274725274725, energy=6.479007641610362, transformer=0.
已连接电池 batt_ev_031, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [ 1.         -0.8595996  -0.         -0.79848653 -0.62533057 -0.7557129
 -1.         -1.         -0.         -0.         -1.        ]
已有历史设置self.charger_power=65.09692192077637，设置charger_power=68.7679672241211失败。
功率需求计算已禁用，直接使用充电桩功率: 65.10 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=60.840086936950684，设置charger_power=39.60000000000002失败。
功率需求计算已禁用，直接使用充电桩功率: 60.84 kW。
已有历史设置self.charger_power=73.79127502441406，设置charger_power=68.4失败。
功率需求计算已禁用，直接使用充电桩功率: 73.79 kW。
已有历史设置self.charger_power=70.97854614257812，设置charger_power=75.57129263877869失败。
功率需求计算已禁用，直接使用充电桩功率: 70.98 kW。
已有历史设置self.charger_power=100.0，设置charger_power=88.47999999999999失败。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
已有历史设置self.charger_power=60.0，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=80.0。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_010 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_137 充电的有无功功率为 60.840086936950684, -12.354106566273575
已在 set_all_batteries_before_solve 中设置 batt_ev_221 充电的有无功功率为 73.79127502441406, -14.983957472932957
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 65.09692192077637, -13.218493776629188
已在 set_all_batteries_before_solve 中设置 batt_ev_075 充电的有无功功率为 70.97854614257812, -14.41280851346077
已在 set_all_batteries_before_solve 中设置 batt_ev_093 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_031 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.46 更新为 0.70。
SOC从 0.48 更新为 0.48。
SOC从 0.88 更新为 1.00。
SOC从 0.77 更新为 1.00。
SOC从 0.61 更新为 0.81。
SOC从 0.71 更新为 1.00。
SOC从 0.65 更新为 0.92。
SOC从 0.88 更新为 0.88。
SOC从 0.22 更新为 0.22。
SOC从 0.42 更新为 0.79。
已断开电池: batt_ev_010
时间步 27: 电池 batt_ev_010 已离开，当前SOC: 48.0%，能量满足率: 0.0%
已断开电池: batt_ev_137
时间步 27 执行前: 电池 batt_ev_137 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_221
时间步 27 执行前: 电池 batt_ev_221 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_075
时间步 27 执行前: 电池 batt_ev_075 已充满 (SOC: 81.0%)，离开
已断开电池: batt_ev_093
时间步 27 执行前: 电池 batt_ev_093 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_031
时间步 27 执行前: 电池 batt_ev_031 已充满 (SOC: 79.0%)，离开
奖励各项的值：powerloss=-0.14084772981685512, voltage=-0.2974926001272604, ctrl=-0.0, connection=7.76, completion=4.948453608247423, energy=6.593708199861268, transformer=0.
已连接电池 batt_ev_057, 初始SOC: 8.0%, 最大功率: 80kW, 电池容量: 73kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_057 已接入
已连接电池 batt_ev_111, 初始SOC: 68.0%, 最大功率: 100kW, 电池容量: 83kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_111 已接入
已连接电池 batt_ev_006, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_006 已接入
已连接电池 batt_ev_225, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 94kWh，并创BMS。
时间步 27 执行前: 排队电池 batt_ev_225 已接入
已连接电池 batt_ev_054, 初始SOC: 82.0%, 最大功率: 120kW, 电池容量: 85kWh，并创BMS。
已连接电池 batt_ev_129, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 94kWh，并创BMS。
智能体的动作为: [ 1.         -0.8136946  -0.         -0.7609384  -0.61497676 -0.7097738
 -1.         -1.         -0.         -0.         -1.        ]
已有历史设置self.charger_power=65.09692192077637，设置charger_power=65.09556770324707失败。
功率需求计算已禁用，直接使用充电桩功率: 65.10 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=76.09384059906006。
功率需求计算已禁用，直接使用充电桩功率: 76.09 kW。
初次设置charger_power=36.898605823516846。
功率需求计算已禁用，直接使用充电桩功率: 36.90 kW。
初次设置charger_power=85.17285346984863。
功率需求计算已禁用，直接使用充电桩功率: 85.17 kW。
初次设置charger_power=61.19999999999999。
功率需求计算已禁用，直接使用充电桩功率: 61.20 kW。
已有历史设置self.charger_power=60.0，设置charger_power=18.879999999999995失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=100.0。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_109 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 65.09692192077637, -13.218493776629188
已在 set_all_batteries_before_solve 中设置 batt_ev_047 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 76.09384059906006, -15.451513354542538
已在 set_all_batteries_before_solve 中设置 batt_ev_006 充电的有无功功率为 36.898605823516846, -7.492581477785395
已在 set_all_batteries_before_solve 中设置 batt_ev_225 充电的有无功功率为 85.17285346984863, -17.29508554796375
已在 set_all_batteries_before_solve 中设置 batt_ev_054 充电的有无功功率为 61.19999999999999, -12.42719003080105
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.70 更新为 0.94。
SOC从 0.08 更新为 0.08。
SOC从 0.68 更新为 0.91。
SOC从 0.57 更新为 0.72。
SOC从 0.52 更新为 0.75。
SOC从 0.82 更新为 1.00。
SOC从 0.92 更新为 1.00。
SOC从 0.88 更新为 0.88。
SOC从 0.22 更新为 0.22。
SOC从 0.28 更新为 0.55。
已断开电池: batt_ev_109
时间步 28: 电池 batt_ev_109 已离开，当前SOC: 88.0%，能量满足率: 0.0%
已断开电池: batt_ev_047
时间步 28 执行前: 电池 batt_ev_047 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_006
时间步 28: 电池 batt_ev_006 已离开，当前SOC: 72.4%，能量满足率: 73.2%
已断开电池: batt_ev_054
时间步 28 执行前: 电池 batt_ev_054 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.13756168805446162, voltage=-0.2821903089681044, ctrl=-0.0, connection=8.08, completion=4.9504950495049505, energy=6.603041145584191, transformer=0.
已连接电池 batt_ev_088, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 50kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_088 已接入
已连接电池 batt_ev_007, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 84kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_007 已接入
已连接电池 batt_ev_142, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_142 已接入
已连接电池 batt_ev_147, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
时间步 28 执行前: 排队电池 batt_ev_147 已接入
智能体的动作为: [ 1.        -0.8128164 -0.        -0.760317  -0.6148385 -0.7091148
 -1.        -1.        -0.        -0.        -1.       ]
已有历史设置self.charger_power=65.09692192077637，设置charger_power=16.919999999999987失败。
功率需求计算已禁用，直接使用充电桩功率: 65.10 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=76.09384059906006，设置charger_power=30.160000000000025失败。
功率需求计算已禁用，直接使用充电桩功率: 76.09 kW。
初次设置charger_power=36.89030885696411。
功率需求计算已禁用，直接使用充电桩功率: 36.89 kW。
已有历史设置self.charger_power=85.17285346984863，设置charger_power=85.09377479553223失败。
功率需求计算已禁用，直接使用充电桩功率: 85.17 kW。
初次设置charger_power=100.0。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
初次设置charger_power=120.0。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=100.0，设置charger_power=100.0失败。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_034 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_101 充电的有无功功率为 65.09692192077637, -13.218493776629188
已在 set_all_batteries_before_solve 中设置 batt_ev_057 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_111 充电的有无功功率为 76.09384059906006, -15.451513354542538
已在 set_all_batteries_before_solve 中设置 batt_ev_225 充电的有无功功率为 85.17285346984863, -17.29508554796375
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 36.89030885696411, -7.490896706869872
已在 set_all_batteries_before_solve 中设置 batt_ev_007 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_147 充电的有无功功率为 0.0, -0.0
SOC从 0.94 更新为 1.00。
SOC从 0.08 更新为 0.08。
SOC从 0.91 更新为 1.00。
SOC从 0.38 更新为 0.56。
SOC从 0.75 更新为 0.97。
SOC从 0.32 更新为 0.62。
SOC从 0.32 更新为 0.62。
SOC从 0.52 更新为 0.52。
SOC从 0.22 更新为 0.22。
SOC从 0.55 更新为 0.81。
已断开电池: batt_ev_034
时间步 29: 电池 batt_ev_034 已离开，当前SOC: 22.0%，能量满足率: 0.0%
已断开电池: batt_ev_101
时间步 29 执行前: 电池 batt_ev_101 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_057
时间步 29: 电池 batt_ev_057 已离开，当前SOC: 8.0%，能量满足率: 0.0%
已断开电池: batt_ev_111
时间步 29 执行前: 电池 batt_ev_111 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_225
时间步 29: 电池 batt_ev_225 已离开，当前SOC: 97.3%，能量满足率: 98.5%
奖励各项的值：powerloss=-0.146905288960094, voltage=-0.28818782154074185, ctrl=-0.0, connection=8.48, completion=4.90566037735849, energy=6.57315584204028, transformer=0.
已连接电池 batt_ev_079, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 78kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_079 已接入
时间步 29: 电池 batt_ev_156 已错过离开时间，无法接入
已连接电池 batt_ev_053, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_053 已接入
已连接电池 batt_ev_211, 初始SOC: 62.0%, 最大功率: 120kW, 电池容量: 106kWh，并创BMS。
时间步 29 执行前: 排队电池 batt_ev_211 已接入
已连接电池 batt_ev_017, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_087, 初始SOC: 62.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
智能体的动作为: [ 1.         -0.81424576 -0.         -0.7613271  -0.61507285 -0.71018916
 -1.         -1.         -0.         -0.         -1.        ]
初次设置charger_power=81.42457604408264。
功率需求计算已禁用，直接使用充电桩功率: 81.42 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=91.35925054550171。
功率需求计算已禁用，直接使用充电桩功率: 91.36 kW。
已有历史设置self.charger_power=36.89030885696411，设置charger_power=36.90437078475952失败。
功率需求计算已禁用，直接使用充电桩功率: 36.89 kW。
初次设置charger_power=42.6113498210907。
功率需求计算已禁用，直接使用充电桩功率: 42.61 kW。
已有历史设置self.charger_power=100.0，设置charger_power=100.0失败。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
已有历史设置self.charger_power=120.0，设置charger_power=120.0失败。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=100.0，设置charger_power=70.72000000000003失败。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_129 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 36.89030885696411, -7.490896706869872
已在 set_all_batteries_before_solve 中设置 batt_ev_007 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_142 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_147 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 81.42457604408264, -16.533965354203033
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 91.35925054550171, -18.551287052295987
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 42.6113498210907, -8.652603622477688
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 0.0, -0.0
SOC从 0.08 更新为 0.34。
SOC从 0.32 更新为 0.32。
SOC从 0.62 更新为 0.84。
SOC从 0.56 更新为 0.75。
SOC从 0.28 更新为 0.44。
SOC从 0.62 更新为 0.92。
SOC从 0.62 更新为 0.92。
SOC从 0.52 更新为 0.52。
SOC从 0.62 更新为 0.62。
SOC从 0.81 更新为 1.00。
已断开电池: batt_ev_129
时间步 30 执行前: 电池 batt_ev_129 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_007
时间步 30: 电池 batt_ev_007 已离开，当前SOC: 91.5%，能量满足率: 90.2%
已断开电池: batt_ev_142
时间步 30 执行前: 电池 batt_ev_142 已充满 (SOC: 92.0%)，离开
已断开电池: batt_ev_147
时间步 30: 电池 batt_ev_147 已离开，当前SOC: 52.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.15539730575970362, voltage=-0.30460937451454173, ctrl=-0.0, connection=8.8, completion=4.909090909090909, energy=6.597938893409352, transformer=0.
时间步 30: 电池 batt_ev_021 已错过离开时间，无法接入
已连接电池 batt_ev_209, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_209 已接入
已连接电池 batt_ev_178, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 93kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_178 已接入
已连接电池 batt_ev_110, 初始SOC: 22.0%, 最大功率: 100kW, 电池容量: 65kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_110 已接入
已连接电池 batt_ev_112, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 71kWh，并创BMS。
时间步 30 执行前: 排队电池 batt_ev_112 已接入
智能体的动作为: [ 1.         -0.8129425  -0.         -0.76041794 -0.61484706 -0.70922005
 -1.         -1.         -0.         -0.         -1.        ]
已有历史设置self.charger_power=81.42457604408264，设置charger_power=81.29425048828125失败。
功率需求计算已禁用，直接使用充电桩功率: 81.42 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=91.35925054550171，设置charger_power=69.75999999999999失败。
功率需求计算已禁用，直接使用充电桩功率: 91.36 kW。
已有历史设置self.charger_power=36.89030885696411，设置charger_power=36.89082384109497失败。
功率需求计算已禁用，直接使用充电桩功率: 36.89 kW。
已有历史设置self.charger_power=42.6113498210907，设置charger_power=42.553203105926514失败。
功率需求计算已禁用，直接使用充电桩功率: 42.61 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=100.0。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=80.0。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 36.89030885696411, -7.490896706869872
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 81.42457604408264, -16.533965354203033
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_211 充电的有无功功率为 91.35925054550171, -18.551287052295987
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 42.6113498210907, -8.652603622477688
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_178 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_110 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.34 更新为 0.60。
SOC从 0.32 更新为 0.32。
SOC从 0.84 更新为 1.00。
SOC从 0.75 更新为 0.93。
SOC从 0.44 更新为 0.60。
SOC从 0.38 更新为 0.64。
SOC从 0.42 更新为 0.69。
SOC从 0.22 更新为 0.22。
SOC从 0.62 更新为 0.62。
SOC从 0.22 更新为 0.50。
已断开电池: batt_ev_211
时间步 31 执行前: 电池 batt_ev_211 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.16622326592766373, voltage=-0.25668458735730093, ctrl=-0.0, connection=8.88, completion=4.954954954954955, energy=6.628588092567826, transformer=0.
已连接电池 batt_ev_223, 初始SOC: 22.0%, 最大功率: 100kW, 电池容量: 81kWh，并创BMS。
时间步 31 执行前: 排队电池 batt_ev_223 已接入
智能体的动作为: [ 1.         -0.8128295  -0.         -0.76029533 -0.6148703  -0.7090959
 -1.         -1.         -0.         -0.         -1.        ]
已有历史设置self.charger_power=81.42457604408264，设置charger_power=81.28294944763184失败。
功率需求计算已禁用，直接使用充电桩功率: 81.42 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=76.02953314781189。
功率需求计算已禁用，直接使用充电桩功率: 76.03 kW。
已有历史设置self.charger_power=36.89030885696411，设置charger_power=13.360000000000014失败。
功率需求计算已禁用，直接使用充电桩功率: 36.89 kW。
已有历史设置self.charger_power=42.6113498210907，设置charger_power=42.545753717422485失败。
功率需求计算已禁用，直接使用充电桩功率: 42.61 kW。
已有历史设置self.charger_power=60.0，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已有历史设置self.charger_power=100.0，设置charger_power=100.0失败。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=80.0，设置charger_power=80.0失败。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_088 充电的有无功功率为 36.89030885696411, -7.490896706869872
已在 set_all_batteries_before_solve 中设置 batt_ev_079 充电的有无功功率为 81.42457604408264, -16.533965354203033
已在 set_all_batteries_before_solve 中设置 batt_ev_053 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 42.6113498210907, -8.652603622477688
已在 set_all_batteries_before_solve 中设置 batt_ev_087 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_178 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_110 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_223 充电的有无功功率为 76.02953314781189, -15.438455169623301
SOC从 0.60 更新为 0.86。
SOC从 0.32 更新为 0.32。
SOC从 0.22 更新为 0.45。
SOC从 0.93 更新为 1.00。
SOC从 0.60 更新为 0.76。
SOC从 0.64 更新为 0.90。
SOC从 0.69 更新为 0.96。
SOC从 0.22 更新为 0.22。
SOC从 0.62 更新为 0.62。
SOC从 0.50 更新为 0.78。
已断开电池: batt_ev_088
时间步 32 执行前: 电池 batt_ev_088 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_079
时间步 32: 电池 batt_ev_079 已离开，当前SOC: 86.3%，能量满足率: 87.0%
已断开电池: batt_ev_053
时间步 32: 电池 batt_ev_053 已离开，当前SOC: 32.0%，能量满足率: 0.0%
已断开电池: batt_ev_087
时间步 32: 电池 batt_ev_087 已离开，当前SOC: 62.0%，能量满足率: 0.0%
已断开电池: batt_ev_178
时间步 32: 电池 batt_ev_178 已离开，当前SOC: 95.8%，能量满足率: 96.0%
已断开电池: batt_ev_110
时间步 32: 电池 batt_ev_110 已离开，当前SOC: 22.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.1836324530646946, voltage=-0.2402960579740676, ctrl=-0.0, connection=9.36, completion=4.786324786324786, energy=6.530553396711176, transformer=0.
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
智能体的动作为: [ 1.         -0.81316155 -0.         -0.7602124  -0.61521834 -0.70903647
 -1.         -1.         -0.         -0.         -1.        ]
初次设置charger_power=48.789693117141724。
功率需求计算已禁用，直接使用充电桩功率: 48.79 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=76.02953314781189，设置charger_power=76.02124214172363失败。
功率需求计算已禁用，直接使用充电桩功率: 76.03 kW。
初次设置charger_power=36.913100481033325。
功率需求计算已禁用，直接使用充电桩功率: 36.91 kW。
已有历史设置self.charger_power=42.6113498210907，设置charger_power=42.54218816757202失败。
功率需求计算已禁用，直接使用充电桩功率: 42.61 kW。
已有历史设置self.charger_power=60.0，设置charger_power=23.840000000000003失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=80.0，设置charger_power=61.52000000000001失败。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_017 充电的有无功功率为 42.6113498210907, -8.652603622477688
已在 set_all_batteries_before_solve 中设置 batt_ev_209 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_112 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_223 充电的有无功功率为 76.02953314781189, -15.438455169623301
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 48.789693117141724, -9.907169737110888
已在 set_all_batteries_before_solve 中设置 batt_ev_198 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 36.913100481033325, -7.495524743527039
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 0.0, -0.0
SOC从 0.28 更新为 0.53。
SOC从 0.08 更新为 0.08。
SOC从 0.45 更新为 0.69。
SOC从 0.68 更新为 0.86。
SOC从 0.76 更新为 0.93。
SOC从 0.90 更新为 1.00。
SOC从 0.12 更新为 0.47。
SOC从 0.32 更新为 0.32。
SOC从 0.82 更新为 0.82。
SOC从 0.78 更新为 1.00。
已断开电池: batt_ev_017
时间步 33: 电池 batt_ev_017 已离开，当前SOC: 92.5%，能量满足率: 92.2%
已断开电池: batt_ev_209
时间步 33 执行前: 电池 batt_ev_209 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_112
时间步 33 执行前: 电池 batt_ev_112 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_223
时间步 33: 电池 batt_ev_223 已离开，当前SOC: 68.9%，能量满足率: 93.9%
已断开电池: batt_ev_198
时间步 33: 电池 batt_ev_198 已离开，当前SOC: 8.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.19713143331739913, voltage=-0.30919054434272564, ctrl=-0.0, connection=9.76, completion=4.754098360655737, energy=6.579370335712905, transformer=0.
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
智能体的动作为: [ 1.         -0.7763112  -0.         -0.68277216 -0.57918304 -0.47220838
 -1.         -0.98634744 -0.         -0.         -1.        ]
已有历史设置self.charger_power=48.789693117141724，设置charger_power=46.578673124313354失败。
功率需求计算已禁用，直接使用充电桩功率: 48.79 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=40.96632957458496。
功率需求计算已禁用，直接使用充电桩功率: 40.97 kW。
已有历史设置self.charger_power=36.913100481033325，设置charger_power=28.360000000000014失败。
功率需求计算已禁用，直接使用充电桩功率: 36.91 kW。
初次设置charger_power=47.22083806991577。
功率需求计算已禁用，直接使用充电桩功率: 47.22 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已有历史设置self.charger_power=60.0，设置charger_power=59.180846214294434失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_207 充电的有无功功率为 48.789693117141724, -9.907169737110888
已在 set_all_batteries_before_solve 中设置 batt_ev_152 充电的有无功功率为 36.913100481033325, -7.495524743527039
已在 set_all_batteries_before_solve 中设置 batt_ev_171 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_022 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_028 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_155 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_094 充电的有无功功率为 40.96632957458496, -8.318568014506411
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 47.22083806991577, -9.588600132492289
已在 set_all_batteries_before_solve 中设置 batt_ev_068 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_185 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.53 更新为 0.79。
SOC从 0.52 更新为 0.52。
SOC从 0.28 更新为 0.46。
SOC从 0.86 更新为 1.00。
SOC从 0.38 更新为 0.56。
SOC从 0.18 更新为 0.42。
SOC从 0.47 更新为 0.82。
SOC从 0.32 更新为 0.32。
SOC从 0.82 更新为 0.82。
SOC从 0.48 更新为 0.86。
已断开电池: batt_ev_207
时间步 34: 电池 batt_ev_207 已离开，当前SOC: 78.8%，能量满足率: 72.6%
已断开电池: batt_ev_152
时间步 34 执行前: 电池 batt_ev_152 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_171
时间步 34: 电池 batt_ev_171 已离开，当前SOC: 81.8%，能量满足率: 87.2%
已断开电池: batt_ev_022
时间步 34: 电池 batt_ev_022 已离开，当前SOC: 32.0%，能量满足率: 0.0%
已断开电池: batt_ev_028
时间步 34: 电池 batt_ev_028 已离开，当前SOC: 82.0%，能量满足率: 0.0%
已断开电池: batt_ev_068
时间步 34: 电池 batt_ev_068 已离开，当前SOC: 42.2%，能量满足率: 40.3%
已断开电池: batt_ev_185
时间步 34 执行前: 电池 batt_ev_185 已充满 (SOC: 85.5%)，离开
奖励各项的值：powerloss=-0.21061945777780622, voltage=-0.3284581115317753, ctrl=-0.0, connection=10.32, completion=4.651162790697675, energy=6.532544759813593, transformer=0.
已连接电池 batt_ev_049, 初始SOC: 32.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
已连接电池 batt_ev_023, 初始SOC: 92.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [ 1.         -0.7341003  -0.         -0.5258379  -0.6759574  -0.46225446
 -0.9577903  -0.4538252  -0.         -0.         -1.        ]
初次设置charger_power=44.04601693153381。
功率需求计算已禁用，直接使用充电桩功率: 44.05 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=40.96632957458496，设置charger_power=31.550273895263672失败。
功率需求计算已禁用，直接使用充电桩功率: 40.97 kW。
初次设置charger_power=17.599999999999994。
功率需求计算已禁用，直接使用充电桩功率: 17.60 kW。
已有历史设置self.charger_power=47.22083806991577，设置charger_power=46.225446462631226失败。
功率需求计算已禁用，直接使用充电桩功率: 47.22 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_155 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_094 充电的有无功功率为 40.96632957458496, -8.318568014506411
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 47.22083806991577, -9.588600132492289
已在 set_all_batteries_before_solve 中设置 batt_ev_049 充电的有无功功率为 44.04601693153381, -8.943925204379923
已在 set_all_batteries_before_solve 中设置 batt_ev_023 充电的有无功功率为 17.599999999999994, -3.573832427158471
SOC从 0.32 更新为 0.53。
SOC从 0.52 更新为 0.52。
SOC从 0.46 更新为 0.65。
SOC从 0.92 更新为 1.00。
SOC从 0.56 更新为 0.73。
已断开电池: batt_ev_155
时间步 35: 电池 batt_ev_155 已离开，当前SOC: 52.0%，能量满足率: 0.0%
已断开电池: batt_ev_094
时间步 35: 电池 batt_ev_094 已离开，当前SOC: 64.6%，能量满足率: 52.2%
已断开电池: batt_ev_023
时间步 35 执行前: 电池 batt_ev_023 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.21035394637426572, voltage=-0.29929328519561205, ctrl=-0.0, connection=10.56, completion=4.621212121212121, energy=6.499414877362666, transformer=0.
已连接电池 batt_ev_121, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [ 0.87678456 -0.44503608 -0.         -0.33184168 -0.08992311 -0.
 -0.58363956 -1.         -0.5947612  -0.         -0.        ]
已有历史设置self.charger_power=44.04601693153381，设置charger_power=26.702165007591248失败。
功率需求计算已禁用，直接使用充电桩功率: 44.05 kW。
已有历史设置self.charger_power=47.22083806991577，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 47.22 kW。
初次设置charger_power=46.69116497039795。
功率需求计算已禁用，直接使用充电桩功率: 46.69 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_140 充电的有无功功率为 47.22083806991577, -9.588600132492289
已在 set_all_batteries_before_solve 中设置 batt_ev_049 充电的有无功功率为 44.04601693153381, -8.943925204379923
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 46.69116497039795, -9.48104542233034
SOC从 0.53 更新为 0.74。
SOC从 0.73 更新为 0.91。
SOC从 0.48 更新为 0.68。
已断开电池: batt_ev_140
时间步 36: 电池 batt_ev_140 已离开，当前SOC: 90.9%，能量满足率: 88.1%
已断开电池: batt_ev_049
时间步 36: 电池 batt_ev_049 已离开，当前SOC: 73.5%，能量满足率: 63.0%
奖励各项的值：powerloss=-0.2142667983445505, voltage=-0.38398925216829527, ctrl=-0.0, connection=10.72, completion=4.552238805970149, energy=6.515139812048446, transformer=0.
智能体的动作为: [ 0.6705148  -0.43291992 -0.         -0.30649352 -0.05785131 -0.
 -0.56080383 -1.         -0.6370783  -0.         -0.        ]
已有历史设置self.charger_power=46.69116497039795，设置charger_power=44.86430644989014失败。
功率需求计算已禁用，直接使用充电桩功率: 46.69 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 46.69116497039795, -9.48104542233034
SOC从 0.68 更新为 0.88。
奖励各项的值：powerloss=-0.21208317903668752, voltage=-0.4186583302355018, ctrl=-0.0, connection=10.72, completion=4.552238805970149, energy=6.515139812048446, transformer=0.
已连接电池 batt_ev_015, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 61kWh，并创BMS。
已连接电池 batt_ev_201, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
智能体的动作为: [ 0.5702696  -0.419135   -0.         -0.13803758 -0.21228853 -0.
 -0.38099837 -1.         -0.81191814 -0.         -0.        ]
已有历史设置self.charger_power=46.69116497039795，设置charger_power=29.360000000000014失败。
功率需求计算已禁用，直接使用充电桩功率: 46.69 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
初次设置charger_power=97.43017673492432。
功率需求计算已禁用，直接使用充电桩功率: 97.43 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_121 充电的有无功功率为 46.69116497039795, -9.48104542233034
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 97.43017673492432, -19.78404119312804
SOC从 0.88 更新为 1.00。
SOC从 0.52 更新为 0.77。
SOC从 0.18 更新为 0.42。
已断开电池: batt_ev_121
时间步 38 执行前: 电池 batt_ev_121 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.2178028675246596, voltage=-0.45119845030564765, ctrl=-0.0, connection=10.8, completion=4.592592592592593, energy=6.540953591218458, transformer=0.
已连接电池 batt_ev_080, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_204, 初始SOC: 2.0%, 最大功率: 80kW, 电池容量: 81kWh，并创BMS。
智能体的动作为: [ 1.         -0.718861   -0.         -0.5229711  -0.5793937  -0.2936542
 -0.89510876 -0.50148445 -0.         -0.         -0.85850155]
已有历史设置self.charger_power=60.0，设置charger_power=30.089067220687866失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已有历史设置self.charger_power=97.43017673492432，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 97.43 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=68.68012428283691。
功率需求计算已禁用，直接使用充电桩功率: 68.68 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_015 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 97.43017673492432, -19.78404119312804
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 68.68012428283691, -13.946094049049805
SOC从 0.77 更新为 1.00。
SOC从 0.42 更新为 0.65。
SOC从 0.57 更新为 0.57。
SOC从 0.02 更新为 0.23。
已断开电池: batt_ev_015
时间步 39 执行前: 电池 batt_ev_015 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.21794572841476278, voltage=-0.4508309343013961, ctrl=-0.0, connection=10.88, completion=4.632352941176471, energy=6.56638775598891, transformer=0.
已连接电池 batt_ev_183, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 71kWh，并创BMS。
已连接电池 batt_ev_230, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
智能体的动作为: [ 1.         -0.71846926 -0.         -0.52371556 -0.5820801  -0.29475424
 -0.89508027 -0.5000069  -0.         -0.         -0.862795  ]
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=31.422933340072632。
功率需求计算已禁用，直接使用充电桩功率: 31.42 kW。
已有历史设置self.charger_power=97.43017673492432，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 97.43 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=68.68012428283691，设置charger_power=69.02359962463379失败。
功率需求计算已禁用，直接使用充电桩功率: 68.68 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_201 充电的有无功功率为 97.43017673492432, -19.78404119312804
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 68.68012428283691, -13.946094049049805
已在 set_all_batteries_before_solve 中设置 batt_ev_183 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 31.422933340072632, -6.380698757226742
SOC从 0.38 更新为 0.38。
SOC从 0.52 更新为 0.64。
SOC从 0.65 更新为 0.89。
SOC从 0.57 更新为 0.57。
SOC从 0.23 更新为 0.44。
已断开电池: batt_ev_201
时间步 40 执行前: 电池 batt_ev_201 已充满 (SOC: 89.0%)，离开
奖励各项的值：powerloss=-0.21122718426619302, voltage=-0.4717775163577831, ctrl=-0.0, connection=10.96, completion=4.671532846715328, energy=6.591450619083882, transformer=0.
智能体的动作为: [ 1.         -0.7172533  -0.         -0.5218575  -0.561959   -0.28579098
 -0.88265926 -0.50916314 -0.         -0.         -0.8363434 ]
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=31.422933340072632，设置charger_power=31.311450004577637失败。
功率需求计算已禁用，直接使用充电桩功率: 31.42 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=68.68012428283691，设置charger_power=66.90747261047363失败。
功率需求计算已禁用，直接使用充电桩功率: 68.68 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_204 充电的有无功功率为 68.68012428283691, -13.946094049049805
已在 set_all_batteries_before_solve 中设置 batt_ev_183 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_230 充电的有无功功率为 31.422933340072632, -6.380698757226742
SOC从 0.38 更新为 0.38。
SOC从 0.64 更新为 0.76。
SOC从 0.57 更新为 0.57。
SOC从 0.44 更新为 0.66。
已断开电池: batt_ev_204
时间步 41: 电池 batt_ev_204 已离开，当前SOC: 65.6%，能量满足率: 66.2%
已断开电池: batt_ev_183
时间步 41: 电池 batt_ev_183 已离开，当前SOC: 38.0%，能量满足率: 0.0%
已断开电池: batt_ev_230
时间步 41: 电池 batt_ev_230 已离开，当前SOC: 76.2%，能量满足率: 52.6%
奖励各项的值：powerloss=-0.2057210312098481, voltage=-0.37853392107819905, ctrl=-0.0, connection=11.200000000000001, completion=4.571428571428571, energy=6.535074916379755, transformer=0.
智能体的动作为: [ 0.1302129  -0.11843437 -0.         -0.16586152 -0.1930763  -0.
 -0.19677608 -1.         -0.75045735 -0.         -0.        ]
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_080 充电的有无功功率为 0.0, -0.0
SOC从 0.57 更新为 0.57。
已断开电池: batt_ev_080
时间步 42: 电池 batt_ev_080 已离开，当前SOC: 57.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.20394123885133214, voltage=-0.2279076542115277, ctrl=-0.0, connection=11.28, completion=4.539007092198581, energy=6.488726867327416, transformer=0.
已连接电池 batt_ev_148, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_215, 初始SOC: 62.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_210, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
智能体的动作为: [ 0.10169756 -0.32646814 -0.         -0.12821054 -0.4863486  -0.
 -0.35938084 -0.6928614  -1.         -0.3169088  -0.        ]
初次设置charger_power=39.17617678642273。
功率需求计算已禁用，直接使用充电桩功率: 39.18 kW。
初次设置charger_power=58.36183190345764。
功率需求计算已禁用，直接使用充电桩功率: 58.36 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 58.36183190345764, -11.850875418463001
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 39.17617678642273, -7.9550619870119625
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 0.0, -0.0
SOC从 0.62 更新为 0.75。
SOC从 0.28 更新为 0.44。
SOC从 0.57 更新为 0.57。
奖励各项的值：powerloss=-0.20313824547597342, voltage=-0.11648283510544477, ctrl=-0.0, connection=11.28, completion=4.539007092198581, energy=6.488726867327416, transformer=0.
智能体的动作为: [ 0.12924111 -0.11945548 -0.         -0.16308054 -0.19316164 -0.
 -0.19401933 -1.         -0.75215095 -0.         -0.        ]
已有历史设置self.charger_power=39.17617678642273，设置charger_power=14.334657490253448失败。
功率需求计算已禁用，直接使用充电桩功率: 39.18 kW。
已有历史设置self.charger_power=58.36183190345764，设置charger_power=23.179396390914917失败。
功率需求计算已禁用，直接使用充电桩功率: 58.36 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 58.36183190345764, -11.850875418463001
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 39.17617678642273, -7.9550619870119625
已在 set_all_batteries_before_solve 中设置 batt_ev_210 充电的有无功功率为 0.0, -0.0
SOC从 0.75 更新为 0.88。
SOC从 0.44 更新为 0.60。
SOC从 0.57 更新为 0.57。
已断开电池: batt_ev_210
时间步 44: 电池 batt_ev_210 已离开，当前SOC: 57.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.19572503816702652, voltage=-0.10955737813985067, ctrl=-0.0, connection=11.36, completion=4.507042253521127, energy=6.44303160769835, transformer=0.
已连接电池 batt_ev_146, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
已连接电池 batt_ev_027, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 107kWh，并创BMS。
智能体的动作为: [ 0.12917078 -0.11952704 -0.         -0.16287121 -0.19316962 -0.
 -0.19381182 -1.         -0.7522794  -0.         -0.        ]
已有历史设置self.charger_power=39.17617678642273，设置charger_power=14.343245029449463失败。
功率需求计算已禁用，直接使用充电桩功率: 39.18 kW。
已有历史设置self.charger_power=58.36183190345764，设置charger_power=23.180354833602905失败。
功率需求计算已禁用，直接使用充电桩功率: 58.36 kW。
初次设置charger_power=15.504945516586304。
功率需求计算已禁用，直接使用充电桩功率: 15.50 kW。
初次设置charger_power=120.0。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 58.36183190345764, -11.850875418463001
已在 set_all_batteries_before_solve 中设置 batt_ev_215 充电的有无功功率为 39.17617678642273, -7.9550619870119625
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 15.504945516586304, -3.148413469801222
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 120.0, -24.367039276080497
SOC从 0.88 更新为 1.00。
SOC从 0.60 更新为 0.76。
SOC从 0.42 更新为 0.47。
SOC从 0.32 更新为 0.60。
已断开电池: batt_ev_215
时间步 45 执行前: 电池 batt_ev_215 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.19898358429191496, voltage=-0.06183218933175638, ctrl=-0.0, connection=11.44, completion=4.545454545454545, energy=6.46790551253962, transformer=0.
已连接电池 batt_ev_135, 初始SOC: 32.0%, 最大功率: 80kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_127, 初始SOC: 18.0%, 最大功率: 100kW, 电池容量: 88kWh，并创BMS。
已连接电池 batt_ev_165, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 105kWh，并创BMS。
智能体的动作为: [ 1.         -0.71847206 -0.         -0.52370685 -0.5820522  -0.29474947
 -0.89507985 -0.49999595 -0.         -0.         -0.86277086]
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=62.8448224067688。
功率需求计算已禁用，直接使用充电桩功率: 62.84 kW。
已有历史设置self.charger_power=58.36183190345764，设置charger_power=69.84626054763794失败。
功率需求计算已禁用，直接使用充电桩功率: 58.36 kW。
已有历史设置self.charger_power=15.504945516586304，设置charger_power=71.60638809204102失败。
功率需求计算已禁用，直接使用充电桩功率: 15.50 kW。
已有历史设置self.charger_power=120.0，设置charger_power=59.99951362609863失败。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_148 充电的有无功功率为 58.36183190345764, -11.850875418463001
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 15.504945516586304, -3.148413469801222
已在 set_all_batteries_before_solve 中设置 batt_ev_027 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 62.8448224067688, -12.761185465700322
SOC从 0.18 更新为 0.18。
SOC从 0.18 更新为 0.33。
SOC从 0.76 更新为 0.92。
SOC从 0.47 更新为 0.52。
SOC从 0.60 更新为 0.88。
SOC从 0.32 更新为 0.32。
已断开电池: batt_ev_148
时间步 46 执行前: 电池 batt_ev_148 已充满 (SOC: 92.1%)，离开
已断开电池: batt_ev_027
时间步 46: 电池 batt_ev_027 已离开，当前SOC: 88.1%，能量满足率: 93.5%
奖励各项的值：powerloss=-0.18889380794993693, voltage=-0.06729359140609681, ctrl=-0.0, connection=11.6, completion=4.551724137931035, energy=6.512112294384062, transformer=0.
已连接电池 batt_ev_003, 初始SOC: 42.0%, 最大功率: 100kW, 电池容量: 77kWh，并创BMS。
已连接电池 batt_ev_001, 初始SOC: 38.0%, 最大功率: 120kW, 电池容量: 70kWh，并创BMS。
已连接电池 batt_ev_086, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 60kWh，并创BMS。
智能体的动作为: [ 1.         -0.7184241  -0.         -0.5237708  -0.5822177  -0.29480696
 -0.8950147  -0.49994785 -0.         -0.         -0.8630244 ]
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=62.8448224067688，设置charger_power=62.85249710083008失败。
功率需求计算已禁用，直接使用充电桩功率: 62.84 kW。
初次设置charger_power=17.688417434692383。
功率需求计算已禁用，直接使用充电桩功率: 17.69 kW。
已有历史设置self.charger_power=15.504945516586304，设置charger_power=71.60117626190186失败。
功率需求计算已禁用，直接使用充电桩功率: 15.50 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=86.30244135856628。
功率需求计算已禁用，直接使用充电桩功率: 86.30 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_146 充电的有无功功率为 15.504945516586304, -3.148413469801222
已在 set_all_batteries_before_solve 中设置 batt_ev_135 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 62.8448224067688, -12.761185465700322
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 86.30244135856628, -17.524458151715155
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 17.688417434692383, -3.5917863530238017
SOC从 0.18 更新为 0.18。
SOC从 0.33 更新为 0.48。
SOC从 0.12 更新为 0.19。
SOC从 0.52 更新为 0.57。
SOC从 0.32 更新为 0.32。
SOC从 0.38 更新为 0.38。
SOC从 0.42 更新为 0.70。
已断开电池: batt_ev_146
时间步 47: 电池 batt_ev_146 已离开，当前SOC: 56.7%，能量满足率: 26.3%
已断开电池: batt_ev_135
时间步 47: 电池 batt_ev_135 已离开，当前SOC: 32.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.16689432192138395, voltage=-0.12804157947077455, ctrl=-0.0, connection=11.76, completion=4.489795918367347, energy=6.441410787481837, transformer=0.
智能体的动作为: [ 1.         -0.54580647 -0.         -0.4142512  -0.19931285 -0.04078074
 -0.6269479  -0.8746956  -0.39773902 -0.         -0.19710271]
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=62.8448224067688，设置charger_power=49.710144996643066失败。
功率需求计算已禁用，直接使用充电桩功率: 62.84 kW。
已有历史设置self.charger_power=17.688417434692383，设置charger_power=2.4468442797660828失败。
功率需求计算已禁用，直接使用充电桩功率: 17.69 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=86.30244135856628，设置charger_power=19.710271060466766失败。
功率需求计算已禁用，直接使用充电桩功率: 86.30 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_165 充电的有无功功率为 62.8448224067688, -12.761185465700322
已在 set_all_batteries_before_solve 中设置 batt_ev_003 充电的有无功功率为 86.30244135856628, -17.524458151715155
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 17.688417434692383, -3.5917863530238017
SOC从 0.18 更新为 0.18。
SOC从 0.48 更新为 0.63。
SOC从 0.19 更新为 0.27。
SOC从 0.38 更新为 0.38。
SOC从 0.70 更新为 0.98。
已断开电池: batt_ev_165
时间步 48: 电池 batt_ev_165 已离开，当前SOC: 62.9%，能量满足率: 56.1%
已断开电池: batt_ev_003
时间步 48 执行前: 电池 batt_ev_003 已充满 (SOC: 98.1%)，离开
奖励各项的值：powerloss=-0.1473343632760347, voltage=-0.17175945772021084, ctrl=-0.0, connection=11.92, completion=4.496644295302014, energy=6.459718792251975, transformer=0.
已连接电池 batt_ev_043, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 66kWh，并创BMS。
已连接电池 batt_ev_051, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 96kWh，并创BMS。
已连接电池 batt_ev_144, 初始SOC: 22.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
智能体的动作为: [ 0.83161235 -0.42055166 -0.         -0.3273021  -0.08223577 -0.
 -0.5761554  -1.         -0.6058885  -0.         -0.        ]
初次设置charger_power=33.64413261413574。
功率需求计算已禁用，直接使用充电桩功率: 33.64 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=8.223576843738556。
功率需求计算已禁用，直接使用充电桩功率: 8.22 kW。
已有历史设置self.charger_power=17.688417434692383，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 17.69 kW。
初次设置charger_power=80.0。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_001 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 17.688417434692383, -3.5917863530238017
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 33.64413261413574, -6.831732506819218
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 8.223576843738556, -1.669868499510362
已在 set_all_batteries_before_solve 中设置 batt_ev_144 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.42 更新为 0.55。
SOC从 0.18 更新为 0.18。
SOC从 0.48 更新为 0.50。
SOC从 0.27 更新为 0.34。
SOC从 0.22 更新为 0.61。
SOC从 0.38 更新为 0.38。
已断开电池: batt_ev_001
时间步 49: 电池 batt_ev_001 已离开，当前SOC: 38.0%，能量满足率: 0.0%
已断开电池: batt_ev_144
时间步 49 执行前: 电池 batt_ev_144 已充满 (SOC: 61.2%)，离开
奖励各项的值：powerloss=-0.12125221965317204, voltage=-0.21741964505988864, ctrl=-0.0, connection=12.08, completion=4.503311258278146, energy=6.440384768513539, transformer=0.
已连接电池 batt_ev_188, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
已连接电池 batt_ev_107, 初始SOC: 28.000000000000004%, 最大功率: 80kW, 电池容量: 60kWh，并创BMS。
已连接电池 batt_ev_131, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [ 0.20518076 -0.13222514 -0.         -0.28435147 -0.16245106 -0.
 -0.34989387 -1.         -0.6687436  -0.         -0.        ]
已有历史设置self.charger_power=33.64413261413574，设置charger_power=10.578011274337769失败。
功率需求计算已禁用，直接使用充电桩功率: 33.64 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=17.06108808517456。
功率需求计算已禁用，直接使用充电桩功率: 17.06 kW。
self.charger_power=8.223576843738556 改为 16.245105862617493。
功率需求计算已禁用，直接使用充电桩功率: 16.25 kW。
已有历史设置self.charger_power=17.688417434692383，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 17.69 kW。
初次设置charger_power=41.98726415634155。
功率需求计算已禁用，直接使用充电桩功率: 41.99 kW。
初次设置charger_power=53.499488830566406。
功率需求计算已禁用，直接使用充电桩功率: 53.50 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_127 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_086 充电的有无功功率为 17.688417434692383, -3.5917863530238017
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 33.64413261413574, -6.831732506819218
已在 set_all_batteries_before_solve 中设置 batt_ev_051 充电的有无功功率为 16.245105862617493, -3.2987094383207163
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 41.98726415634155, -8.525877623272844
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 53.499488830566406, -10.863534546538677
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 17.06108808517456, -3.4644016955343115
SOC从 0.55 更新为 0.67。
SOC从 0.18 更新为 0.18。
SOC从 0.22 更新为 0.31。
SOC从 0.50 更新为 0.54。
SOC从 0.34 更新为 0.41。
SOC从 0.18 更新为 0.30。
SOC从 0.28 更新为 0.50。
已断开电池: batt_ev_127
时间步 50: 电池 batt_ev_127 已离开，当前SOC: 18.0%，能量满足率: 0.0%
已断开电池: batt_ev_086
时间步 50: 电池 batt_ev_086 已离开，当前SOC: 41.5%，能量满足率: 36.8%
已断开电池: batt_ev_051
时间步 50: 电池 batt_ev_051 已离开，当前SOC: 54.4%，能量满足率: 18.8%
奖励各项的值：powerloss=-0.11789662140124296, voltage=-0.25040409350765236, ctrl=-0.0, connection=12.32, completion=4.415584415584416, energy=6.351015801161544, transformer=0.
已连接电池 batt_ev_136, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
已连接电池 batt_ev_116, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 52kWh，并创BMS。
已连接电池 batt_ev_196, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 44kWh，并创BMS。
智能体的动作为: [ 0.9235971  -0.446759   -0.         -0.33879113 -0.09674573 -0.
 -0.58741134 -1.         -0.57994115 -0.         -0.        ]
已有历史设置self.charger_power=33.64413261413574，设置charger_power=35.740718841552734失败。
功率需求计算已禁用，直接使用充电桩功率: 33.64 kW。
已有历史设置self.charger_power=17.06108808517456，设置charger_power=20.327467918395996失败。
功率需求计算已禁用，直接使用充电桩功率: 17.06 kW。
已有历史设置self.charger_power=41.98726415634155，设置charger_power=70.48936128616333失败。
功率需求计算已禁用，直接使用充电桩功率: 41.99 kW。
初次设置charger_power=80.0。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已有历史设置self.charger_power=53.499488830566406，设置charger_power=46.39529228210449失败。
功率需求计算已禁用，直接使用充电桩功率: 53.50 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 33.64413261413574, -6.831732506819218
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 41.98726415634155, -8.525877623272844
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 53.499488830566406, -10.863534546538677
已在 set_all_batteries_before_solve 中设置 batt_ev_131 充电的有无功功率为 17.06108808517456, -3.4644016955343115
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 0.0, -0.0
SOC从 0.67 更新为 0.80。
SOC从 0.31 更新为 0.41。
SOC从 0.30 更新为 0.42。
SOC从 0.42 更新为 0.80。
SOC从 0.50 更新为 0.73。
SOC从 0.18 更新为 0.18。
SOC从 0.42 更新为 0.42。
已断开电池: batt_ev_131
时间步 51: 电池 batt_ev_131 已离开，当前SOC: 40.6%，能量满足率: 24.4%
奖励各项的值：powerloss=-0.11745665744143996, voltage=-0.28539932325331696, ctrl=-0.0, connection=12.4, completion=4.387096774193548, energy=6.325801452521881, transformer=0.
已连接电池 batt_ev_005, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
已连接电池 batt_ev_063, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
已连接电池 batt_ev_033, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
已连接电池 batt_ev_077, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 79kWh，并创BMS。
智能体的动作为: [ 1.         -0.71653235 -0.         -0.52453583 -0.5522434  -0.2789347
 -0.8684774  -0.51487505 -0.         -0.         -0.82430494]
已有历史设置self.charger_power=33.64413261413574，设置charger_power=52.19999999999999失败。
功率需求计算已禁用，直接使用充电桩功率: 33.64 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=41.96286678314209。
功率需求计算已禁用，直接使用充电桩功率: 41.96 kW。
初次设置charger_power=33.134604692459106。
功率需求计算已禁用，直接使用充电桩功率: 33.13 kW。
初次设置charger_power=33.47216248512268。
功率需求计算已禁用，直接使用充电桩功率: 33.47 kW。
已有历史设置self.charger_power=41.98726415634155，设置charger_power=104.21728849411011失败。
功率需求计算已禁用，直接使用充电桩功率: 41.99 kW。
已有历史设置self.charger_power=80.0，设置charger_power=40.639999999999986失败。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已有历史设置self.charger_power=53.499488830566406，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 53.50 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 65.94439506530762。
功率需求计算已禁用，直接使用充电桩功率: 65.94 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_043 充电的有无功功率为 33.64413261413574, -6.831732506819218
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 41.98726415634155, -8.525877623272844
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 53.499488830566406, -10.863534546538677
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 65.94439506530762, -13.390580538280997
已在 set_all_batteries_before_solve 中设置 batt_ev_116 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 33.134604692459106, -6.728268449487933
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 33.47216248512268, -6.7968124827527685
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 41.96286678314209, -8.520923525347975
SOC从 0.80 更新为 0.93。
SOC从 0.38 更新为 0.38。
SOC从 0.18 更新为 0.31。
SOC从 0.52 更新为 0.73。
SOC从 0.32 更新为 0.41。
SOC从 0.42 更新为 0.55。
SOC从 0.80 更新为 1.00。
SOC从 0.73 更新为 0.95。
SOC从 0.18 更新为 0.18。
SOC从 0.42 更新为 0.62。
已断开电池: batt_ev_043
时间步 52: 电池 batt_ev_043 已离开，当前SOC: 93.0%，能量满足率: 91.0%
已断开电池: batt_ev_116
时间步 52 执行前: 电池 batt_ev_116 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.12560503601982584, voltage=-0.28518298150282284, ctrl=-0.0, connection=12.56, completion=4.3949044585987265, energy=6.366885074793778, transformer=0.
已连接电池 batt_ev_082, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 51kWh，并创BMS。
时间步 52 执行前: 排队电池 batt_ev_082 已接入
已连接电池 batt_ev_159, 初始SOC: 68.0%, 最大功率: 80kW, 电池容量: 53kWh，并创BMS。
时间步 52 执行前: 排队电池 batt_ev_159 已接入
智能体的动作为: [ 1.         -0.72958654 -0.         -0.51393986 -0.6663168  -0.475022
 -0.9183153  -0.3798541  -0.         -0.         -1.        ]
初次设置charger_power=58.366923332214355。
功率需求计算已禁用，直接使用充电桩功率: 58.37 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=41.96286678314209，设置charger_power=41.11518859863281失败。
功率需求计算已禁用，直接使用充电桩功率: 41.96 kW。
已有历史设置self.charger_power=33.134604692459106，设置charger_power=39.979008436203失败。
功率需求计算已禁用，直接使用充电桩功率: 33.13 kW。
已有历史设置self.charger_power=33.47216248512268，设置charger_power=57.00263857841492失败。
功率需求计算已禁用，直接使用充电桩功率: 33.47 kW。
已有历史设置self.charger_power=41.98726415634155，设置charger_power=110.1978349685669失败。
功率需求计算已禁用，直接使用充电桩功率: 41.99 kW。
初次设置charger_power=30.388329029083252。
功率需求计算已禁用，直接使用充电桩功率: 30.39 kW。
已有历史设置self.charger_power=53.499488830566406，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 53.50 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=65.94439506530762，设置charger_power=80.0失败。
功率需求计算已禁用，直接使用充电桩功率: 65.94 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 41.98726415634155, -8.525877623272844
已在 set_all_batteries_before_solve 中设置 batt_ev_107 充电的有无功功率为 53.499488830566406, -10.863534546538677
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 65.94439506530762, -13.390580538280997
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 33.134604692459106, -6.728268449487933
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 33.47216248512268, -6.7968124827527685
已在 set_all_batteries_before_solve 中设置 batt_ev_077 充电的有无功功率为 41.96286678314209, -8.520923525347975
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 58.366923332214355, -11.851909277167051
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 30.388329029083252, -6.17061339155107
SOC从 0.38 更新为 0.67。
SOC从 0.38 更新为 0.38。
SOC从 0.31 更新为 0.45。
SOC从 0.73 更新为 0.93。
SOC从 0.41 更新为 0.49。
SOC从 0.55 更新为 0.67。
SOC从 0.68 更新为 0.82。
SOC从 0.95 更新为 1.00。
SOC从 0.18 更新为 0.18。
SOC从 0.62 更新为 0.82。
已断开电池: batt_ev_107
时间步 53 执行前: 电池 batt_ev_107 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_077
时间步 53: 电池 batt_ev_077 已离开，当前SOC: 44.6%，能量满足率: 33.2%
奖励各项的值：powerloss=-0.12489338028681644, voltage=-0.2607094409070587, ctrl=-0.0, connection=12.72, completion=4.40251572327044, energy=6.370569666640174, transformer=0.
时间步 53: 电池 batt_ev_097 已错过离开时间，无法接入
已连接电池 batt_ev_105, 初始SOC: 42.0%, 最大功率: 60kW, 电池容量: 52kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_105 已接入
已连接电池 batt_ev_058, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 69kWh，并创BMS。
时间步 53 执行前: 排队电池 batt_ev_058 已接入
智能体的动作为: [ 1.         -0.7295478  -0.         -0.51388925 -0.6662332  -0.47487292
 -0.918091   -0.37961805 -0.         -0.         -1.        ]
已有历史设置self.charger_power=58.366923332214355，设置charger_power=58.363823890686035失败。
功率需求计算已禁用，直接使用充电桩功率: 58.37 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=30.83335518836975。
功率需求计算已禁用，直接使用充电桩功率: 30.83 kW。
已有历史设置self.charger_power=33.134604692459106，设置charger_power=10.560000000000002失败。
功率需求计算已禁用，直接使用充电桩功率: 33.13 kW。
已有历史设置self.charger_power=33.47216248512268，设置charger_power=56.98475003242493失败。
功率需求计算已禁用，直接使用充电桩功率: 33.47 kW。
已有历史设置self.charger_power=41.98726415634155，设置charger_power=110.17091989517212失败。
功率需求计算已禁用，直接使用充电桩功率: 41.99 kW。
已有历史设置self.charger_power=30.388329029083252，设置charger_power=30.369443893432617失败。
功率需求计算已禁用，直接使用充电桩功率: 30.39 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=65.94439506530762，设置charger_power=58.31999999999999失败。
功率需求计算已禁用，直接使用充电桩功率: 65.94 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_188 充电的有无功功率为 41.98726415634155, -8.525877623272844
已在 set_all_batteries_before_solve 中设置 batt_ev_136 充电的有无功功率为 65.94439506530762, -13.390580538280997
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_063 充电的有无功功率为 33.134604692459106, -6.728268449487933
已在 set_all_batteries_before_solve 中设置 batt_ev_033 充电的有无功功率为 33.47216248512268, -6.7968124827527685
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 58.366923332214355, -11.851909277167051
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 30.388329029083252, -6.17061339155107
已在 set_all_batteries_before_solve 中设置 batt_ev_105 充电的有无功功率为 30.83335518836975, -6.260979807402882
已在 set_all_batteries_before_solve 中设置 batt_ev_058 充电的有无功功率为 0.0, -0.0
SOC从 0.67 更新为 0.95。
SOC从 0.38 更新为 0.38。
SOC从 0.42 更新为 0.57。
SOC从 0.93 更新为 1.00。
SOC从 0.49 更新为 0.58。
SOC从 0.67 更新为 0.79。
SOC从 0.82 更新为 0.97。
SOC从 0.28 更新为 0.28。
SOC从 0.18 更新为 0.18。
SOC从 0.82 更新为 1.00。
已断开电池: batt_ev_188
时间步 54: 电池 batt_ev_188 已离开，当前SOC: 79.0%，能量满足率: 76.3%
已断开电池: batt_ev_136
时间步 54 执行前: 电池 batt_ev_136 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_063
时间步 54 执行前: 电池 batt_ev_063 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_033
时间步 54: 电池 batt_ev_033 已离开，当前SOC: 57.9%，能量满足率: 39.2%
已断开电池: batt_ev_105
时间步 54: 电池 batt_ev_105 已离开，当前SOC: 56.8%，能量满足率: 26.5%
奖励各项的值：powerloss=-0.128471848267599, voltage=-0.26509770222201245, ctrl=-0.0, connection=13.120000000000001, completion=4.390243902439025, energy=6.384885778007625, transformer=0.
已连接电池 batt_ev_118, 初始SOC: 56.99999999999999%, 最大功率: 120kW, 电池容量: 90kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_118 已接入
已连接电池 batt_ev_199, 初始SOC: 52.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_199 已接入
已连接电池 batt_ev_153, 初始SOC: 2.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_153 已接入
已连接电池 batt_ev_169, 初始SOC: 28.000000000000004%, 最大功率: 100kW, 电池容量: 85kWh，并创BMS。
时间步 54 执行前: 排队电池 batt_ev_169 已接入
已连接电池 batt_ev_059, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 53kWh，并创BMS。
智能体的动作为: [ 1.         -0.7184221  -0.         -0.52377176 -0.5822204  -0.2948106
 -0.89501196 -0.49994183 -0.         -0.         -0.86303324]
已有历史设置self.charger_power=58.366923332214355，设置charger_power=9.759999999999991失败。
功率需求计算已禁用，直接使用充电桩功率: 58.37 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=62.85261154174805。
功率需求计算已禁用，直接使用充电桩功率: 62.85 kW。
初次设置charger_power=58.22203755378723。
功率需求计算已禁用，直接使用充电桩功率: 58.22 kW。
初次设置charger_power=17.68863558769226。
功率需求计算已禁用，直接使用充电桩功率: 17.69 kW。
初次设置charger_power=89.50119614601135。
功率需求计算已禁用，直接使用充电桩功率: 89.50 kW。
已有历史设置self.charger_power=30.388329029083252，设置charger_power=7.039999999999992失败。
功率需求计算已禁用，直接使用充电桩功率: 30.39 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=51.781994104385376。
功率需求计算已禁用，直接使用充电桩功率: 51.78 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_196 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_005 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_082 充电的有无功功率为 58.366923332214355, -11.851909277167051
已在 set_all_batteries_before_solve 中设置 batt_ev_159 充电的有无功功率为 30.388329029083252, -6.17061339155107
已在 set_all_batteries_before_solve 中设置 batt_ev_058 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 62.85261154174805, -12.762767117016704
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 58.22203755378723, -11.822488965054726
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 17.68863558769226, -3.5918306508797713
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 89.50119614601135, -18.173993014550355
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 51.781994104385376, -10.51478236779439
SOC从 0.95 更新为 1.00。
SOC从 0.38 更新为 0.38。
SOC从 0.57 更新为 0.74。
SOC从 0.52 更新为 0.71。
SOC从 0.02 更新为 0.09。
SOC从 0.28 更新为 0.54。
SOC从 0.97 更新为 1.00。
SOC从 0.28 更新为 0.28。
SOC从 0.18 更新为 0.18。
SOC从 0.18 更新为 0.42。
已断开电池: batt_ev_196
时间步 55: 电池 batt_ev_196 已离开，当前SOC: 18.0%，能量满足率: 0.0%
已断开电池: batt_ev_005
时间步 55: 电池 batt_ev_005 已离开，当前SOC: 38.0%，能量满足率: 0.0%
已断开电池: batt_ev_082
时间步 55 执行前: 电池 batt_ev_082 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_159
时间步 55 执行前: 电池 batt_ev_159 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.14871345186936838, voltage=-0.25545339633402, ctrl=-0.0, connection=13.44, completion=4.404761904761905, energy=6.3519123071026815, transformer=0.
已连接电池 batt_ev_175, 初始SOC: 88.0%, 最大功率: 120kW, 电池容量: 97kWh，并创BMS。
时间步 55 执行前: 排队电池 batt_ev_175 已接入
已连接电池 batt_ev_029, 初始SOC: 42.0%, 最大功率: 80kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_195, 初始SOC: 38.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
已连接电池 batt_ev_213, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 66kWh，并创BMS。
智能体的动作为: [ 1.         -0.7294351  -0.         -0.5142939  -0.66536105 -0.47206554
 -0.91782653 -0.38158223 -0.         -0.         -1.        ]
初次设置charger_power=46.56。
功率需求计算已禁用，直接使用充电桩功率: 46.56 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=62.85261154174805，设置charger_power=61.71526908874512失败。
功率需求计算已禁用，直接使用充电桩功率: 62.85 kW。
已有历史设置self.charger_power=58.22203755378723，设置charger_power=66.53610467910767失败。
功率需求计算已禁用，直接使用充电桩功率: 58.22 kW。
已有历史设置self.charger_power=17.68863558769226，设置charger_power=28.32393229007721失败。
功率需求计算已禁用，直接使用充电桩功率: 17.69 kW。
已有历史设置self.charger_power=89.50119614601135，设置charger_power=91.78265333175659失败。
功率需求计算已禁用，直接使用充电桩功率: 89.50 kW。
初次设置charger_power=22.894933819770813。
功率需求计算已禁用，直接使用充电桩功率: 22.89 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=51.781994104385376，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 51.78 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_058 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 62.85261154174805, -12.762767117016704
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 58.22203755378723, -11.822488965054726
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 17.68863558769226, -3.5918306508797713
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 89.50119614601135, -18.173993014550355
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 51.781994104385376, -10.51478236779439
已在 set_all_batteries_before_solve 中设置 batt_ev_175 充电的有无功功率为 46.56, -9.454411239119231
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 22.894933819770813, -4.649014596746825
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 0.0, -0.0
SOC从 0.88 更新为 1.00。
SOC从 0.42 更新为 0.42。
SOC从 0.74 更新为 0.92。
SOC从 0.71 更新为 0.90。
SOC从 0.09 更新为 0.16。
SOC从 0.54 更新为 0.81。
SOC从 0.38 更新为 0.52。
SOC从 0.28 更新为 0.28。
SOC从 0.28 更新为 0.28。
SOC从 0.42 更新为 0.67。
已断开电池: batt_ev_175
时间步 56 执行前: 电池 batt_ev_175 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.16535332643397027, voltage=-0.22700307003564513, ctrl=-0.0, connection=13.52, completion=4.437869822485207, energy=6.373498624812134, transformer=0.
已连接电池 batt_ev_133, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
时间步 56 执行前: 排队电池 batt_ev_133 已接入
智能体的动作为: [ 1.         -0.72375715 -0.         -0.5251425  -0.6213533  -0.36371046
 -0.90602326 -0.45510942 -0.         -0.         -0.92967975]
初次设置charger_power=86.85085773468018。
功率需求计算已禁用，直接使用充电桩功率: 86.85 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=62.85261154174805，设置charger_power=29.120000000000005失败。
功率需求计算已禁用，直接使用充电桩功率: 62.85 kW。
已有历史设置self.charger_power=58.22203755378723，设置charger_power=29.439999999999998失败。
功率需求计算已禁用，直接使用充电桩功率: 58.22 kW。
已有历史设置self.charger_power=17.68863558769226，设置charger_power=21.822627782821655失败。
功率需求计算已禁用，直接使用充电桩功率: 17.69 kW。
已有历史设置self.charger_power=89.50119614601135，设置charger_power=65.83999999999997失败。
功率需求计算已禁用，直接使用充电桩功率: 89.50 kW。
已有历史设置self.charger_power=22.894933819770813，设置charger_power=27.306565046310425失败。
功率需求计算已禁用，直接使用充电桩功率: 22.89 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=51.781994104385376，设置charger_power=55.78078508377075失败。
功率需求计算已禁用，直接使用充电桩功率: 51.78 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_058 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_118 充电的有无功功率为 62.85261154174805, -12.762767117016704
已在 set_all_batteries_before_solve 中设置 batt_ev_199 充电的有无功功率为 58.22203755378723, -11.822488965054726
已在 set_all_batteries_before_solve 中设置 batt_ev_153 充电的有无功功率为 17.68863558769226, -3.5918306508797713
已在 set_all_batteries_before_solve 中设置 batt_ev_169 充电的有无功功率为 89.50119614601135, -18.173993014550355
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 51.781994104385376, -10.51478236779439
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 22.894933819770813, -4.649014596746825
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 86.85085773468018, -17.635818846518593
SOC从 0.18 更新为 0.44。
SOC从 0.42 更新为 0.42。
SOC从 0.92 更新为 1.00。
SOC从 0.90 更新为 1.00。
SOC从 0.16 更新为 0.22。
SOC从 0.81 更新为 1.00。
SOC从 0.52 更新为 0.66。
SOC从 0.28 更新为 0.28。
SOC从 0.28 更新为 0.28。
SOC从 0.67 更新为 0.91。
已断开电池: batt_ev_058
时间步 57: 电池 batt_ev_058 已离开，当前SOC: 28.0%，能量满足率: 0.0%
已断开电池: batt_ev_118
时间步 57 执行前: 电池 batt_ev_118 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_199
时间步 57 执行前: 电池 batt_ev_199 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_153
时间步 57: 电池 batt_ev_153 已离开，当前SOC: 22.4%，能量满足率: 21.3%
已断开电池: batt_ev_169
时间步 57 执行前: 电池 batt_ev_169 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.18348822478458654, voltage=-0.24598420638585194, ctrl=-0.0, connection=13.92, completion=4.482758620689655, energy=6.374978549386498, transformer=0.
已连接电池 batt_ev_145, 初始SOC: 52.0%, 最大功率: 80kW, 电池容量: 62kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_145 已接入
已连接电池 batt_ev_044, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 58kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_044 已接入
已连接电池 batt_ev_154, 初始SOC: 32.0%, 最大功率: 100kW, 电池容量: 95kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_154 已接入
已连接电池 batt_ev_179, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 40kWh，并创BMS。
时间步 57 执行前: 排队电池 batt_ev_179 已接入
已连接电池 batt_ev_246, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 74kWh，并创BMS。
智能体的动作为: [ 1.         -0.72953415 -0.         -0.5139338  -0.66613346 -0.4745535
 -0.9180573  -0.37983093 -0.         -0.         -1.        ]
已有历史设置self.charger_power=86.85085773468018，设置charger_power=87.54409790039062失败。
功率需求计算已禁用，直接使用充电桩功率: 86.85 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=41.114702224731445。
功率需求计算已禁用，直接使用充电桩功率: 41.11 kW。
初次设置charger_power=39.96800780296326。
功率需求计算已禁用，直接使用充电桩功率: 39.97 kW。
初次设置charger_power=47.45534956455231。
功率需求计算已禁用，直接使用充电桩功率: 47.46 kW。
初次设置charger_power=55.083439350128174。
功率需求计算已禁用，直接使用充电桩功率: 55.08 kW。
已有历史设置self.charger_power=22.894933819770813，设置charger_power=22.78985559940338失败。
功率需求计算已禁用，直接使用充电桩功率: 22.89 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=51.781994104385376，设置charger_power=18.439999999999998失败。
功率需求计算已禁用，直接使用充电桩功率: 51.78 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_059 充电的有无功功率为 51.781994104385376, -10.51478236779439
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 22.894933819770813, -4.649014596746825
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_133 充电的有无功功率为 86.85085773468018, -17.635818846518593
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 41.114702224731445, -8.348696366119878
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 39.96800780296326, -8.115850132679144
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 47.45534956455231, -9.636219722496463
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 55.083439350128174, -11.185169417551425
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 0.0, -0.0
SOC从 0.44 更新为 0.71。
SOC从 0.42 更新为 0.42。
SOC从 0.52 更新为 0.69。
SOC从 0.18 更新为 0.35。
SOC从 0.32 更新为 0.44。
SOC从 0.18 更新为 0.52。
SOC从 0.66 更新为 0.80。
SOC从 0.48 更新为 0.48。
SOC从 0.28 更新为 0.28。
SOC从 0.91 更新为 1.00。
已断开电池: batt_ev_059
时间步 58 执行前: 电池 batt_ev_059 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_133
时间步 58: 电池 batt_ev_133 已离开，当前SOC: 71.0%，能量满足率: 66.2%
奖励各项的值：powerloss=-0.19517531126745574, voltage=-0.25489165731429786, ctrl=-0.0, connection=14.08, completion=4.488636363636363, energy=6.3969611933651995, transformer=0.
已连接电池 batt_ev_184, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 103kWh，并创BMS。
时间步 58 执行前: 排队电池 batt_ev_184 已接入
已连接电池 batt_ev_066, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 76kWh，并创BMS。
时间步 58 执行前: 排队电池 batt_ev_066 已接入
智能体的动作为: [ 1.         -0.71871346 -0.         -0.52405083 -0.5842737  -0.29805446
 -0.8956349  -0.4978437  -0.         -0.         -0.8665081 ]
初次设置charger_power=86.24561548233032。
功率需求计算已禁用，直接使用充电桩功率: 86.25 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=41.114702224731445，设置charger_power=41.9240665435791失败。
功率需求计算已禁用，直接使用充电桩功率: 41.11 kW。
已有历史设置self.charger_power=39.96800780296326，设置charger_power=35.056421756744385失败。
功率需求计算已禁用，直接使用充电桩功率: 39.97 kW。
已有历史设置self.charger_power=47.45534956455231，设置charger_power=29.805445671081543失败。
功率需求计算已禁用，直接使用充电桩功率: 47.46 kW。
已有历史设置self.charger_power=55.083439350128174，设置charger_power=53.73809337615967失败。
功率需求计算已禁用，直接使用充电桩功率: 55.08 kW。
已有历史设置self.charger_power=22.894933819770813，设置charger_power=29.870622754096985失败。
功率需求计算已禁用，直接使用充电桩功率: 22.89 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=103.98097515106201。
功率需求计算已禁用，直接使用充电桩功率: 103.98 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 22.894933819770813, -4.649014596746825
已在 set_all_batteries_before_solve 中设置 batt_ev_213 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_145 充电的有无功功率为 41.114702224731445, -8.348696366119878
已在 set_all_batteries_before_solve 中设置 batt_ev_044 充电的有无功功率为 39.96800780296326, -8.115850132679144
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 47.45534956455231, -9.636219722496463
已在 set_all_batteries_before_solve 中设置 batt_ev_179 充电的有无功功率为 55.083439350128174, -11.185169417551425
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 86.24561548233032, -17.512919165397324
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 103.98097515106201, -21.114237545592314
SOC从 0.28 更新为 0.49。
SOC从 0.42 更新为 0.42。
SOC从 0.69 更新为 0.85。
SOC从 0.35 更新为 0.52。
SOC从 0.44 更新为 0.57。
SOC从 0.52 更新为 0.87。
SOC从 0.80 更新为 0.94。
SOC从 0.48 更新为 0.48。
SOC从 0.28 更新为 0.28。
SOC从 0.08 更新为 0.42。
已断开电池: batt_ev_213
时间步 59: 电池 batt_ev_213 已离开，当前SOC: 28.0%，能量满足率: 0.0%
已断开电池: batt_ev_145
时间步 59: 电池 batt_ev_145 已离开，当前SOC: 85.2%，能量满足率: 72.1%
已断开电池: batt_ev_044
时间步 59: 电池 batt_ev_044 已离开，当前SOC: 52.4%，能量满足率: 43.1%
已断开电池: batt_ev_179
时间步 59: 电池 batt_ev_179 已离开，当前SOC: 86.9%，能量满足率: 86.1%
奖励各项的值：powerloss=-0.20673104111050256, voltage=-0.2743632999746004, ctrl=-0.0, connection=14.4, completion=4.388888888888889, energy=6.366591281511758, transformer=0.
已连接电池 batt_ev_233, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 45kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_233 已接入
已连接电池 batt_ev_219, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 65kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_219 已接入
已连接电池 batt_ev_249, 初始SOC: 8.0%, 最大功率: 120kW, 电池容量: 100kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_249 已接入
已连接电池 batt_ev_032, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 82kWh，并创BMS。
时间步 59 执行前: 排队电池 batt_ev_032 已接入
智能体的动作为: [ 1.         -0.72950023 -0.         -0.5140563  -0.6658711  -0.47370616
 -0.9179777  -0.38042486 -0.         -0.         -1.        ]
已有历史设置self.charger_power=86.24561548233032，设置charger_power=87.54002809524536失败。
功率需求计算已禁用，直接使用充电桩功率: 86.25 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=30.843379497528076。
功率需求计算已禁用，直接使用充电桩功率: 30.84 kW。
初次设置charger_power=39.95226502418518。
功率需求计算已禁用，直接使用充电桩功率: 39.95 kW。
已有历史设置self.charger_power=47.45534956455231，设置charger_power=47.37061560153961失败。
功率需求计算已禁用，直接使用充电桩功率: 47.46 kW。
初次设置charger_power=110.15732288360596。
功率需求计算已禁用，直接使用充电桩功率: 110.16 kW。
已有历史设置self.charger_power=22.894933819770813，设置charger_power=10.159999999999997失败。
功率需求计算已禁用，直接使用充电桩功率: 22.89 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=103.98097515106201，设置charger_power=120.0失败。
功率需求计算已禁用，直接使用充电桩功率: 103.98 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_029 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_195 充电的有无功功率为 22.894933819770813, -4.649014596746825
已在 set_all_batteries_before_solve 中设置 batt_ev_154 充电的有无功功率为 47.45534956455231, -9.636219722496463
已在 set_all_batteries_before_solve 中设置 batt_ev_246 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_184 充电的有无功功率为 86.24561548233032, -17.512919165397324
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 103.98097515106201, -21.114237545592314
已在 set_all_batteries_before_solve 中设置 batt_ev_233 充电的有无功功率为 30.843379497528076, -6.263015330194355
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 39.95226502418518, -8.11265342510581
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 110.15732288360596, -22.368398443772556
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 0.0, -0.0
SOC从 0.49 更新为 0.70。
SOC从 0.42 更新为 0.42。
SOC从 0.22 更新为 0.39。
SOC从 0.18 更新为 0.33。
SOC从 0.57 更新为 0.69。
SOC从 0.08 更新为 0.36。
SOC从 0.94 更新为 1.00。
SOC从 0.48 更新为 0.48。
SOC从 0.48 更新为 0.48。
SOC从 0.42 更新为 0.76。
已断开电池: batt_ev_029
时间步 60: 电池 batt_ev_029 已离开，当前SOC: 42.0%，能量满足率: 0.0%
已断开电池: batt_ev_195
时间步 60 执行前: 电池 batt_ev_195 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_154
时间步 60: 电池 batt_ev_154 已离开，当前SOC: 69.5%，能量满足率: 56.7%
已断开电池: batt_ev_246
时间步 60: 电池 batt_ev_246 已离开，当前SOC: 48.0%，能量满足率: 0.0%
已断开电池: batt_ev_184
时间步 60: 电池 batt_ev_184 已离开，当前SOC: 69.9%，能量满足率: 59.8%
已断开电池: batt_ev_233
时间步 60: 电池 batt_ev_233 已离开，当前SOC: 39.1%，能量满足率: 22.5%
奖励各项的值：powerloss=-0.21519259087668444, voltage=-0.2857596010894081, ctrl=-0.0, connection=14.88, completion=4.301075268817204, energy=6.289763657578633, transformer=0.
已连接电池 batt_ev_060, 初始SOC: 56.99999999999999%, 最大功率: 100kW, 电池容量: 90kWh，并创BMS。
时间步 60 执行前: 排队电池 batt_ev_060 已接入
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
智能体的动作为: [ 1.         -0.72955585 -0.         -0.513861   -0.66629404 -0.4750744
 -0.9181106  -0.37947854 -0.         -0.         -1.        ]
初次设置charger_power=72.95558452606201。
功率需求计算已禁用，直接使用充电桩功率: 72.96 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=51.38610005378723。
功率需求计算已禁用，直接使用充电桩功率: 51.39 kW。
已有历史设置self.charger_power=39.95226502418518，设置charger_power=39.97764229774475失败。
功率需求计算已禁用，直接使用充电桩功率: 39.95 kW。
初次设置charger_power=28.504464626312256。
功率需求计算已禁用，直接使用充电桩功率: 28.50 kW。
已有历史设置self.charger_power=110.15732288360596，设置charger_power=110.17327308654785失败。
功率需求计算已禁用，直接使用充电桩功率: 110.16 kW。
初次设置charger_power=37.94785439968109。
功率需求计算已禁用，直接使用充电桩功率: 37.95 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=103.98097515106201，设置charger_power=71.75999999999999失败。
功率需求计算已禁用，直接使用充电桩功率: 103.98 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_066 充电的有无功功率为 103.98097515106201, -21.114237545592314
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 39.95226502418518, -8.11265342510581
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 110.15732288360596, -22.368398443772556
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_060 充电的有无功功率为 72.95558452606201, -14.814263279633028
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 51.38610005378723, -10.434392652126961
已在 set_all_batteries_before_solve 中设置 batt_ev_217 充电的有无功功率为 28.504464626312256, -5.788078409108316
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 37.94785439968109, -7.705640488333442
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 0.0, -0.0
SOC从 0.57 更新为 0.77。
SOC从 0.48 更新为 0.48。
SOC从 0.12 更新为 0.28。
SOC从 0.33 更新为 0.49。
SOC从 0.38 更新为 0.51。
SOC从 0.36 更新为 0.63。
SOC从 0.38 更新为 0.52。
SOC从 0.88 更新为 0.88。
SOC从 0.48 更新为 0.48。
SOC从 0.76 更新为 1.00。
已断开电池: batt_ev_066
时间步 61 执行前: 电池 batt_ev_066 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_060
时间步 61: 电池 batt_ev_060 已离开，当前SOC: 77.3%，能量满足率: 49.4%
已断开电池: batt_ev_217
时间步 61: 电池 batt_ev_217 已离开，当前SOC: 50.5%，能量满足率: 20.8%
奖励各项的值：powerloss=-0.21671034445175544, voltage=-0.292364348780918, ctrl=-0.0, connection=15.120000000000001, completion=4.285714285714286, energy=6.280020767524643, transformer=0.
已连接电池 batt_ev_073, 初始SOC: 48.0%, 最大功率: 120kW, 电池容量: 106kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_073 已接入
已连接电池 batt_ev_020, 初始SOC: 32.0%, 最大功率: 120kW, 电池容量: 99kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_020 已接入
已连接电池 batt_ev_208, 初始SOC: 38.0%, 最大功率: 100kW, 电池容量: 61kWh，并创BMS。
时间步 61 执行前: 排队电池 batt_ev_208 已接入
智能体的动作为: [ 1.         -0.7295552  -0.         -0.513859   -0.6662939  -0.47507423
 -0.918106   -0.37947035 -0.         -0.         -1.        ]
初次设置charger_power=87.54662275314331。
功率需求计算已禁用，直接使用充电桩功率: 87.55 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=51.38610005378723，设置charger_power=51.385897397994995失败。
功率需求计算已禁用，直接使用充电桩功率: 51.39 kW。
已有历史设置self.charger_power=39.95226502418518，设置charger_power=39.97763514518738失败。
功率需求计算已禁用，直接使用充电桩功率: 39.95 kW。
初次设置charger_power=57.00890779495239。
功率需求计算已禁用，直接使用充电桩功率: 57.01 kW。
已有历史设置self.charger_power=110.15732288360596，设置charger_power=110.17272233963013失败。
功率需求计算已禁用，直接使用充电桩功率: 110.16 kW。
已有历史设置self.charger_power=37.94785439968109，设置charger_power=37.94703483581543失败。
功率需求计算已禁用，直接使用充电桩功率: 37.95 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=100.0。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_219 充电的有无功功率为 39.95226502418518, -8.11265342510581
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 110.15732288360596, -22.368398443772556
已在 set_all_batteries_before_solve 中设置 batt_ev_032 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 51.38610005378723, -10.434392652126961
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 37.94785439968109, -7.705640488333442
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 87.54662275314331, -17.77709995928371
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 57.00890779495239, -11.57615246105047
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 100.0, -20.30586606340041
SOC从 0.48 更新为 0.69。
SOC从 0.48 更新为 0.48。
SOC从 0.28 更新为 0.45。
SOC从 0.49 更新为 0.64。
SOC从 0.32 更新为 0.46。
SOC从 0.63 更新为 0.91。
SOC从 0.52 更新为 0.65。
SOC从 0.88 更新为 0.88。
SOC从 0.48 更新为 0.48。
SOC从 0.38 更新为 0.79。
已断开电池: batt_ev_219
时间步 62: 电池 batt_ev_219 已离开，当前SOC: 64.1%，能量满足率: 72.0%
已断开电池: batt_ev_032
时间步 62: 电池 batt_ev_032 已离开，当前SOC: 48.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.2172346526918188, voltage=-0.29481243814701186, ctrl=-0.0, connection=15.280000000000001, completion=4.2408376963350785, energy=6.251980376886045, transformer=0.
已连接电池 batt_ev_091, 初始SOC: 22.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_091 已接入
时间步 62: 电池 batt_ev_176 已错过离开时间，无法接入
已连接电池 batt_ev_102, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 55kWh，并创BMS。
时间步 62 执行前: 排队电池 batt_ev_102 已接入
智能体的动作为: [ 1.         -0.7296005  -0.         -0.51388025 -0.6664217  -0.4750118
 -0.9182793  -0.37986475 -0.         -0.         -1.        ]
已有历史设置self.charger_power=87.54662275314331，设置charger_power=87.55205869674683失败。
功率需求计算已禁用，直接使用充电桩功率: 87.55 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=51.38610005378723，设置charger_power=51.38802528381348失败。
功率需求计算已禁用，直接使用充电桩功率: 51.39 kW。
初次设置charger_power=39.985302686691284。
功率需求计算已禁用，直接使用充电桩功率: 39.99 kW。
已有历史设置self.charger_power=57.00890779495239，设置charger_power=57.001415491104126失败。
功率需求计算已禁用，直接使用充电桩功率: 57.01 kW。
已有历史设置self.charger_power=110.15732288360596，设置charger_power=37.51999999999998失败。
功率需求计算已禁用，直接使用充电桩功率: 110.16 kW。
已有历史设置self.charger_power=37.94785439968109，设置charger_power=37.986475229263306失败。
功率需求计算已禁用，直接使用充电桩功率: 37.95 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=100.0，设置charger_power=51.28失败。
功率需求计算已禁用，直接使用充电桩功率: 100.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_249 充电的有无功功率为 110.15732288360596, -22.368398443772556
已在 set_all_batteries_before_solve 中设置 batt_ev_205 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_072 充电的有无功功率为 51.38610005378723, -10.434392652126961
已在 set_all_batteries_before_solve 中设置 batt_ev_124 充电的有无功功率为 37.94785439968109, -7.705640488333442
已在 set_all_batteries_before_solve 中设置 batt_ev_189 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 87.54662275314331, -17.77709995928371
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 57.00890779495239, -11.57615246105047
已在 set_all_batteries_before_solve 中设置 batt_ev_208 充电的有无功功率为 100.0, -20.30586606340041
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 39.985302686691284, -8.119362008604778
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 0.0, -0.0
SOC从 0.69 更新为 0.89。
SOC从 0.48 更新为 0.48。
SOC从 0.45 更新为 0.61。
SOC从 0.22 更新为 0.37。
SOC从 0.46 更新为 0.61。
SOC从 0.91 更新为 1.00。
SOC从 0.65 更新为 0.79。
SOC从 0.88 更新为 0.88。
SOC从 0.48 更新为 0.48。
SOC从 0.79 更新为 1.00。
已断开电池: batt_ev_249
时间步 63 执行前: 电池 batt_ev_249 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_205
时间步 63: 电池 batt_ev_205 已离开，当前SOC: 48.0%，能量满足率: 0.0%
已断开电池: batt_ev_072
时间步 63: 电池 batt_ev_072 已离开，当前SOC: 60.8%，能量满足率: 56.7%
已断开电池: batt_ev_124
时间步 63: 电池 batt_ev_124 已离开，当前SOC: 78.7%，能量满足率: 75.3%
已断开电池: batt_ev_189
时间步 63: 电池 batt_ev_189 已离开，当前SOC: 88.0%，能量满足率: 0.0%
已断开电池: batt_ev_208
时间步 63 执行前: 电池 batt_ev_208 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.2146241317435096, voltage=-0.3043557997968871, ctrl=-0.0, connection=15.76, completion=4.213197969543147, energy=6.230122447940304, transformer=0.
时间步 63: 电池 batt_ev_236 已错过离开时间，无法接入
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
已连接电池 batt_ev_243, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 54kWh，并创BMS。
智能体的动作为: [ 1.         -0.7295622  -0.         -0.5138609  -0.6663149  -0.4750665
 -0.9181322  -0.37952644 -0.         -0.         -1.        ]
已有历史设置self.charger_power=87.54662275314331，设置charger_power=45.360000000000014失败。
功率需求计算已禁用，直接使用充电桩功率: 87.55 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=51.386088132858276。
功率需求计算已禁用，直接使用充电桩功率: 51.39 kW。
已有历史设置self.charger_power=39.985302686691284，设置charger_power=39.978893995285034失败。
功率需求计算已禁用，直接使用充电桩功率: 39.99 kW。
已有历史设置self.charger_power=57.00890779495239，设置charger_power=57.00798153877258失败。
功率需求计算已禁用，直接使用充电桩功率: 57.01 kW。
初次设置charger_power=110.1758623123169。
功率需求计算已禁用，直接使用充电桩功率: 110.18 kW。
初次设置charger_power=22.771586179733276。
功率需求计算已禁用，直接使用充电桩功率: 22.77 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=60.0。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_073 充电的有无功功率为 87.54662275314331, -17.77709995928371
已在 set_all_batteries_before_solve 中设置 batt_ev_020 充电的有无功功率为 57.00890779495239, -11.57615246105047
已在 set_all_batteries_before_solve 中设置 batt_ev_091 充电的有无功功率为 39.985302686691284, -8.119362008604778
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_074 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 51.386088132858276, -10.434390231479094
已在 set_all_batteries_before_solve 中设置 batt_ev_012 充电的有无功功率为 110.1758623123169, -22.372163035335518
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 22.771586179733276, -4.623967790168438
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 60.0, -12.183519638040249
SOC从 0.89 更新为 1.00。
SOC从 0.48 更新为 0.48。
SOC从 0.28 更新为 0.44。
SOC从 0.37 更新为 0.52。
SOC从 0.61 更新为 0.75。
SOC从 0.48 更新为 0.76。
SOC从 0.22 更新为 0.33。
SOC从 0.38 更新为 0.38。
SOC从 0.48 更新为 0.48。
SOC从 0.12 更新为 0.40。
已断开电池: batt_ev_073
时间步 64 执行前: 电池 batt_ev_073 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_020
时间步 64: 电池 batt_ev_020 已离开，当前SOC: 75.2%，能量满足率: 72.0%
已断开电池: batt_ev_091
时间步 64: 电池 batt_ev_091 已离开，当前SOC: 51.9%，能量满足率: 39.3%
已断开电池: batt_ev_012
时间步 64 执行前: 电池 batt_ev_012 已充满 (SOC: 76.1%)，离开
奖励各项的值：powerloss=-0.21131799553850777, voltage=-0.3199713654683767, ctrl=-0.0, connection=16.080000000000002, completion=4.228855721393035, energy=6.26098916275324, transformer=0.
已连接电池 batt_ev_122, 初始SOC: 28.000000000000004%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [ 1.         -0.7290721  -0.         -0.51554793 -0.6625227  -0.46318197
 -0.9169937  -0.3878115  -0.         -0.         -1.        ]
初次设置charger_power=43.74432563781738。
功率需求计算已禁用，直接使用充电桩功率: 43.74 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=51.386088132858276，设置charger_power=51.55479311943054失败。
功率需求计算已禁用，直接使用充电桩功率: 51.39 kW。
已有历史设置self.charger_power=22.771586179733276，设置charger_power=23.268690705299377失败。
功率需求计算已禁用，直接使用充电桩功率: 22.77 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=60.0，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_102 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_074 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 51.386088132858276, -10.434390231479094
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 22.771586179733276, -4.623967790168438
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_122 充电的有无功功率为 43.74432563781738, -8.882664174352925
SOC从 0.28 更新为 0.55。
SOC从 0.48 更新为 0.48。
SOC从 0.44 更新为 0.61。
SOC从 0.33 更新为 0.43。
SOC从 0.38 更新为 0.38。
SOC从 0.48 更新为 0.48。
SOC从 0.40 更新为 0.68。
已断开电池: batt_ev_102
时间步 65: 电池 batt_ev_102 已离开，当前SOC: 48.0%，能量满足率: 0.0%
已断开电池: batt_ev_074
时间步 65: 电池 batt_ev_074 已离开，当前SOC: 48.0%，能量满足率: 0.0%
已断开电池: batt_ev_122
时间步 65: 电池 batt_ev_122 已离开，当前SOC: 54.7%，能量满足率: 38.1%
奖励各项的值：powerloss=-0.19790130458131855, voltage=-0.2869625619039584, ctrl=-0.0, connection=16.32, completion=4.166666666666667, energy=6.187601315702435, transformer=0.
已连接电池 batt_ev_139, 初始SOC: 12.0%, 最大功率: 80kW, 电池容量: 84kWh，并创BMS。
智能体的动作为: [ 0.14226818 -0.09238192 -0.         -0.28118214 -0.17745599 -0.
 -0.31842464 -1.         -0.66967267 -0.         -0.        ]
已有历史设置self.charger_power=51.386088132858276，设置charger_power=28.118214011192322失败。
功率需求计算已禁用，直接使用充电桩功率: 51.39 kW。
初次设置charger_power=14.196479320526123。
功率需求计算已禁用，直接使用充电桩功率: 14.20 kW。
已有历史设置self.charger_power=22.771586179733276，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 22.77 kW。
self.charger_power=0.0 改为 53.57381343841553。
功率需求计算已禁用，直接使用充电桩功率: 53.57 kW。
已有历史设置self.charger_power=60.0，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 60.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 51.386088132858276, -10.434390231479094
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 22.771586179733276, -4.623967790168438
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 53.57381343841553, -10.878626801860667
已在 set_all_batteries_before_solve 中设置 batt_ev_243 充电的有无功功率为 60.0, -12.183519638040249
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 14.196479320526123, -2.882718076544371
SOC从 0.61 更新为 0.77。
SOC从 0.12 更新为 0.16。
SOC从 0.43 更新为 0.54。
SOC从 0.38 更新为 0.57。
SOC从 0.68 更新为 0.95。
已断开电池: batt_ev_243
时间步 66 执行前: 电池 batt_ev_243 已充满 (SOC: 95.3%)，离开
奖励各项的值：powerloss=-0.20810860376608373, voltage=-0.1975088766434574, ctrl=-0.0, connection=16.4, completion=4.195121951219512, energy=6.206198382455106, transformer=0.
已连接电池 batt_ev_004, 初始SOC: 8.0%, 最大功率: 100kW, 电池容量: 91kWh，并创BMS。
已连接电池 batt_ev_019, 初始SOC: 52.0%, 最大功率: 60kW, 电池容量: 43kWh，并创BMS。
智能体的动作为: [ 0.6300372  -0.4180984  -0.         -0.3028907  -0.05955968 -0.
 -0.54866326 -1.         -0.64292735 -0.         -0.        ]
已有历史设置self.charger_power=51.386088132858276，设置charger_power=30.289068818092346失败。
功率需求计算已禁用，直接使用充电桩功率: 51.39 kW。
已有历史设置self.charger_power=14.196479320526123，设置charger_power=4.764774143695831失败。
功率需求计算已禁用，直接使用充电桩功率: 14.20 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=32.919795513153076。
功率需求计算已禁用，直接使用充电桩功率: 32.92 kW。
已有历史设置self.charger_power=22.771586179733276，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 22.77 kW。
已有历史设置self.charger_power=53.57381343841553，设置charger_power=51.43418788909912失败。
功率需求计算已禁用，直接使用充电桩功率: 53.57 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 51.386088132858276, -10.434390231479094
已在 set_all_batteries_before_solve 中设置 batt_ev_228 充电的有无功功率为 22.771586179733276, -4.623967790168438
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 53.57381343841553, -10.878626801860667
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 14.196479320526123, -2.882718076544371
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 32.919795513153076, -6.684649585246161
SOC从 0.77 更新为 0.94。
SOC从 0.16 更新为 0.20。
SOC从 0.08 更新为 0.08。
SOC从 0.52 更新为 0.71。
SOC从 0.54 更新为 0.65。
SOC从 0.57 更新为 0.76。
已断开电池: batt_ev_228
时间步 67: 电池 batt_ev_228 已离开，当前SOC: 64.9%，能量满足率: 56.5%
奖励各项的值：powerloss=-0.20242965124393558, voltage=-0.11694309106612844, ctrl=-0.0, connection=16.48, completion=4.174757281553398, energy=6.203500559588317, transformer=0.
智能体的动作为: [ 0.141788   -0.09240519 -0.         -0.28111577 -0.17744009 -0.
 -0.31830454 -1.         -0.6696827  -0.         -0.        ]
已有历史设置self.charger_power=51.386088132858276，设置charger_power=19.04000000000002失败。
功率需求计算已禁用，直接使用充电桩功率: 51.39 kW。
已有历史设置self.charger_power=14.196479320526123，设置charger_power=14.195207357406616失败。
功率需求计算已禁用，直接使用充电桩功率: 14.20 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=32.919795513153076，设置charger_power=19.0982723236084失败。
功率需求计算已禁用，直接使用充电桩功率: 32.92 kW。
已有历史设置self.charger_power=53.57381343841553，设置charger_power=53.57461452484131失败。
功率需求计算已禁用，直接使用充电桩功率: 53.57 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_061 充电的有无功功率为 51.386088132858276, -10.434390231479094
已在 set_all_batteries_before_solve 中设置 batt_ev_218 充电的有无功功率为 53.57381343841553, -10.878626801860667
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 14.196479320526123, -2.882718076544371
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 32.919795513153076, -6.684649585246161
SOC从 0.94 更新为 1.00。
SOC从 0.20 更新为 0.25。
SOC从 0.08 更新为 0.08。
SOC从 0.71 更新为 0.90。
SOC从 0.76 更新为 0.95。
已断开电池: batt_ev_061
时间步 68 执行前: 电池 batt_ev_061 已充满 (SOC: 100.0%)，离开
已断开电池: batt_ev_218
时间步 68 执行前: 电池 batt_ev_218 已充满 (SOC: 95.4%)，离开
奖励各项的值：powerloss=-0.19618347355112503, voltage=-0.09808065654773213, ctrl=-0.0, connection=16.64, completion=4.230769230769231, energy=6.240005361899969, transformer=0.
智能体的动作为: [ 0.13192594 -0.11438229 -0.         -0.17825715 -0.1922102  -0.
 -0.20898956 -1.         -0.7428197  -0.         -0.        ]
已有历史设置self.charger_power=14.196479320526123，设置charger_power=15.376815795898438失败。
功率需求计算已禁用，直接使用充电桩功率: 14.20 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=32.919795513153076，设置charger_power=12.539373636245728失败。
功率需求计算已禁用，直接使用充电桩功率: 32.92 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_139 充电的有无功功率为 14.196479320526123, -2.882718076544371
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_019 充电的有无功功率为 32.919795513153076, -6.684649585246161
SOC从 0.25 更新为 0.29。
SOC从 0.08 更新为 0.08。
SOC从 0.90 更新为 1.00。
已断开电池: batt_ev_139
时间步 69: 电池 batt_ev_139 已离开，当前SOC: 28.9%，能量满足率: 19.7%
已断开电池: batt_ev_019
时间步 69 执行前: 电池 batt_ev_019 已充满 (SOC: 100.0%)，离开
奖励各项的值：powerloss=-0.1911320766832431, voltage=-0.04683446000002034, ctrl=-0.0, connection=16.8, completion=4.238095238095238, energy=6.237556120305331, transformer=0.
已连接电池 batt_ev_177, 初始SOC: 38.0%, 最大功率: 80kW, 电池容量: 59kWh，并创BMS。
智能体的动作为: [ 0.03576565 -0.07117494 -0.         -0.12137741 -0.3445207  -0.
 -0.24070819 -0.8929705  -1.         -0.1638102  -0.        ]
初次设置charger_power=5.693995356559753。
功率需求计算已禁用，直接使用充电桩功率: 5.69 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 5.693995356559753, -1.1562150707592624
SOC从 0.38 更新为 0.40。
SOC从 0.08 更新为 0.08。
奖励各项的值：powerloss=-0.17799836129171898, voltage=-0.037222334914552846, ctrl=-0.0, connection=16.8, completion=4.238095238095238, energy=6.237556120305331, transformer=0.
已连接电池 batt_ev_202, 初始SOC: 48.0%, 最大功率: 100kW, 电池容量: 76kWh，并创BMS。
已连接电池 batt_ev_160, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [ 0.07425892 -0.29536647 -0.         -0.1275877  -0.47387022 -0.
 -0.36458212 -0.717381   -1.         -0.31602684 -0.        ]
self.charger_power=5.693995356559753 改为 23.62931728363037。
功率需求计算已禁用，直接使用充电桩功率: 23.63 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=18.961610198020935。
功率需求计算已禁用，直接使用充电桩功率: 18.96 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 23.62931728363037, -4.798137519309907
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 18.961610198020935, -3.8503191702742043
SOC从 0.40 更新为 0.50。
SOC从 0.48 更新为 0.48。
SOC从 0.08 更新为 0.08。
SOC从 0.18 更新为 0.30。
奖励各项的值：powerloss=-0.16288526125702887, voltage=-0.07426110585268653, ctrl=-0.0, connection=16.8, completion=4.238095238095238, energy=6.237556120305331, transformer=0.
智能体的动作为: [-0.00618356 -0.03739105 -0.         -0.12053005 -0.36036783 -0.
 -0.23157571 -0.89200807 -1.         -0.21043931 -0.        ]
已有历史设置self.charger_power=23.62931728363037，设置charger_power=2.991284132003784失败。
功率需求计算已禁用，直接使用充电桩功率: 23.63 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=18.961610198020935，设置charger_power=12.626358568668365失败。
功率需求计算已禁用，直接使用充电桩功率: 18.96 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 0.618356466293335, 0.2032439418051887
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 23.62931728363037, -4.798137519309907
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 18.961610198020935, -3.8503191702742043
SOC从 0.50 更新为 0.60。
SOC从 0.48 更新为 0.48。
SOC从 0.08 更新为 0.08。
SOC从 0.30 更新为 0.41。
奖励各项的值：powerloss=-0.14617691047990247, voltage=-0.12770729528488012, ctrl=-0.0, connection=16.8, completion=4.238095238095238, energy=6.237556120305331, transformer=0.
已连接电池 batt_ev_099, 初始SOC: 68.0%, 最大功率: 60kW, 电池容量: 67kWh，并创BMS。
已连接电池 batt_ev_100, 初始SOC: 18.0%, 最大功率: 80kW, 电池容量: 58kWh，并创BMS。
智能体的动作为: [-0.00813586 -0.0362835  -0.         -0.12054912 -0.36058396 -0.
 -0.23116453 -0.8913136  -1.         -0.21083833 -0.        ]
已有历史设置self.charger_power=23.62931728363037，设置charger_power=2.9026800394058228失败。
功率需求计算已禁用，直接使用充电桩功率: 23.63 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=71.3050889968872。
功率需求计算已禁用，直接使用充电桩功率: 71.31 kW。
已有历史设置self.charger_power=18.961610198020935，设置charger_power=12.650299966335297失败。
功率需求计算已禁用，直接使用充电桩功率: 18.96 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 0.8135855197906494, 0.26741262855886994
已在 set_all_batteries_before_solve 中设置 batt_ev_004 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_177 充电的有无功功率为 23.62931728363037, -4.798137519309907
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_160 充电的有无功功率为 18.961610198020935, -3.8503191702742043
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 71.3050889968872, -14.479115868096379
SOC从 0.60 更新为 0.70。
SOC从 0.48 更新为 0.48。
SOC从 0.08 更新为 0.08。
SOC从 0.18 更新为 0.49。
SOC从 0.41 更新为 0.53。
SOC从 0.68 更新为 0.68。
已断开电池: batt_ev_004
时间步 73: 电池 batt_ev_004 已离开，当前SOC: 8.0%，能量满足率: 0.0%
已断开电池: batt_ev_177
时间步 73: 电池 batt_ev_177 已离开，当前SOC: 70.5%，能量满足率: 54.1%
已断开电池: batt_ev_160
时间步 73: 电池 batt_ev_160 已离开，当前SOC: 52.7%，能量满足率: 43.4%
奖励各项的值：powerloss=-0.1245217888126393, voltage=-0.17958359683422076, ctrl=-0.0, connection=17.04, completion=4.178403755868544, energy=6.195454251819493, transformer=0.
智能体的动作为: [ 0.12904716 -0.1196719  -0.         -0.16251901 -0.19317265 -0.
 -0.19345479 -1.         -0.75251275 -0.         -0.        ]
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=71.3050889968872，设置charger_power=80.0失败。
功率需求计算已禁用，直接使用充电桩功率: 71.31 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -1.4, -0.4601577472504085
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_100 充电的有无功功率为 71.3050889968872, -14.479115868096379
SOC从 0.48 更新为 0.48。
SOC从 0.49 更新为 0.79。
SOC从 0.68 更新为 0.68。
已断开电池: batt_ev_100
时间步 74: 电池 batt_ev_100 已离开，当前SOC: 79.5%，能量满足率: 83.1%
奖励各项的值：powerloss=-0.11611799844543383, voltage=-0.21446593553412052, ctrl=-0.0, connection=17.12, completion=4.158878504672897, energy=6.2053282080945795, transformer=0.
智能体的动作为: [ 0.381961   -0.2750654  -0.         -0.16266753 -0.21129751 -0.
 -0.26900262 -0.9560577  -0.87649024 -0.         -0.        ]
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_202 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 0.0, -0.0
SOC从 0.48 更新为 0.48。
SOC从 0.68 更新为 0.68。
已断开电池: batt_ev_202
时间步 75: 电池 batt_ev_202 已离开，当前SOC: 48.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.10846452947487978, voltage=-0.24070245691444336, ctrl=-0.0, connection=17.2, completion=4.1395348837209305, energy=6.176466216429023, transformer=0.
智能体的动作为: [ 0.12331808 -0.337629   -0.         -0.12718369 -0.48772988 -0.
 -0.36044657 -0.68619907 -1.         -0.3072017  -0.        ]
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 0.0, -0.0
SOC从 0.68 更新为 0.68。
奖励各项的值：powerloss=-0.10822512144454058, voltage=-0.26955585132240056, ctrl=-0.0, connection=17.2, completion=4.1395348837209305, energy=6.176466216429023, transformer=0.
已连接电池 batt_ev_120, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 82kWh，并创BMS。
智能体的动作为: [ 0.12465429 -0.33802843 -0.         -0.12736641 -0.48791412 -0.
 -0.3606165  -0.68589145 -1.         -0.3071467  -0.        ]
初次设置charger_power=15.283969044685364。
功率需求计算已禁用，直接使用充电桩功率: 15.28 kW。
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_099 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 15.283969044685364, -3.103542283385389
SOC从 0.18 更新为 0.23。
SOC从 0.68 更新为 0.68。
已断开电池: batt_ev_099
时间步 77: 电池 batt_ev_099 已离开，当前SOC: 68.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.10938690289114282, voltage=-0.24849551054823005, ctrl=-0.0, connection=17.28, completion=4.12037037037037, energy=6.147871465427038, transformer=0.
智能体的动作为: [-0.03887427 -0.1493971  -0.         -0.14223196 -0.44959778 -0.
 -0.36144054 -0.7945276  -1.         -0.3439828  -0.        ]
已有历史设置self.charger_power=15.283969044685364，设置charger_power=17.067834734916687失败。
功率需求计算已禁用，直接使用充电桩功率: 15.28 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 3.8874268531799316, 1.2777354166857298
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 15.283969044685364, -3.103542283385389
SOC从 0.23 更新为 0.27。
奖励各项的值：powerloss=-0.11540556965074458, voltage=-0.2356931045492816, ctrl=-0.0, connection=17.28, completion=4.12037037037037, energy=6.147871465427038, transformer=0.
已连接电池 batt_ev_035, 初始SOC: 48.0%, 最大功率: 80kW, 电池容量: 77kWh，并创BMS。
智能体的动作为: [-0.03986228 -0.14748135 -0.         -0.14253873 -0.44936442 -0.
 -0.36135685 -0.79538864 -1.         -0.344299   -0.        ]
已有历史设置self.charger_power=15.283969044685364，设置charger_power=17.104647159576416失败。
功率需求计算已禁用，直接使用充电桩功率: 15.28 kW。
初次设置charger_power=80.0。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 3.986227512359619, 1.3102096229392872
已在 set_all_batteries_before_solve 中设置 batt_ev_120 充电的有无功功率为 15.283969044685364, -3.103542283385389
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 80.0, -16.244692850720327
SOC从 0.27 更新为 0.32。
SOC从 0.48 更新为 0.74。
已断开电池: batt_ev_120
时间步 79: 电池 batt_ev_120 已离开，当前SOC: 32.0%，能量满足率: 17.5%
奖励各项的值：powerloss=-0.13705216755219773, voltage=-0.3547004771705242, ctrl=-0.0, connection=17.36, completion=4.1013824884792625, energy=6.1275907269666, transformer=0.
已连接电池 batt_ev_151, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 86kWh，并创BMS。
智能体的动作为: [ 0.20636451 -0.21865574 -0.         -0.15091796 -0.1832899  -0.
 -0.2069185  -1.         -0.80555075 -0.         -0.        ]
初次设置charger_power=21.99478805065155。
功率需求计算已禁用，直接使用充电桩功率: 21.99 kW。
已有历史设置self.charger_power=80.0，设置charger_power=64.44406032562256失败。
功率需求计算已禁用，直接使用充电桩功率: 80.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -7.879999999999999, -2.590030748809442
已在 set_all_batteries_before_solve 中设置 batt_ev_035 充电的有无功功率为 80.0, -16.244692850720327
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 21.99478805065155, -4.466232202494102
SOC从 0.28 更新为 0.34。
SOC从 0.74 更新为 1.00。
已断开电池: batt_ev_035
时间步 80 执行前: 电池 batt_ev_035 已充满 (SOC: 99.9%)，离开
奖励各项的值：powerloss=-0.1527332073617468, voltage=-0.3954189678444009, ctrl=-0.0, connection=17.44, completion=4.128440366972478, energy=6.145354072255744, transformer=0.
智能体的动作为: [ 0.134696   -0.12536973 -0.         -0.16209018 -0.19278651 -0.
 -0.19433774 -1.         -0.7566378  -0.         -0.        ]
已有历史设置self.charger_power=21.99478805065155，设置charger_power=23.134381771087646失败。
功率需求计算已禁用，直接使用充电桩功率: 21.99 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_151 充电的有无功功率为 21.99478805065155, -4.466232202494102
SOC从 0.34 更新为 0.41。
已断开电池: batt_ev_151
时间步 81: 电池 batt_ev_151 已离开，当前SOC: 40.8%，能量满足率: 18.3%
奖励各项的值：powerloss=-0.16140020887540812, voltage=-0.3381581788378929, ctrl=-0.0, connection=17.52, completion=4.10958904109589, energy=6.125636667929996, transformer=0.
智能体的动作为: [-0.0527041  -0.13101447 -0.         -0.144984   -0.44731992 -0.
 -0.3563288  -0.7955464  -1.         -0.3432983  -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 5.27040958404541, 1.7322998580580702
奖励各项的值：powerloss=-0.1699881694748834, voltage=-0.2956807440217091, ctrl=-0.0, connection=17.52, completion=4.10958904109589, energy=6.125636667929996, transformer=0.
智能体的动作为: [ 0.12330341 -0.3363138  -0.         -0.12754159 -0.48723555 -0.
 -0.36110944 -0.687307   -1.         -0.30761322 -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -5.28, -1.7354520753443978
奖励各项的值：powerloss=-0.17814866684985153, voltage=-0.34229649483114466, ctrl=-0.0, connection=17.52, completion=4.10958904109589, energy=6.125636667929996, transformer=0.
已连接电池 batt_ev_056, 初始SOC: 62.0%, 最大功率: 80kW, 电池容量: 64kWh，并创BMS。
已连接电池 batt_ev_226, 初始SOC: 18.0%, 最大功率: 60kW, 电池容量: 46kWh，并创BMS。
智能体的动作为: [ 0.12326896 -0.336291   -0.         -0.12751341 -0.48715904 -0.
 -0.3611099  -0.6873236  -1.         -0.30754435 -0.        ]
初次设置charger_power=20.177459120750427。
功率需求计算已禁用，直接使用充电桩功率: 20.18 kW。
初次设置charger_power=28.888792991638184。
功率需求计算已禁用，直接使用充电桩功率: 28.89 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 28.888792991638184, -5.866119612215055
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 20.177459120750427, -4.097207824056952
SOC从 0.18 更新为 0.29。
SOC从 0.62 更新为 0.73。
奖励各项的值：powerloss=-0.18541504517116125, voltage=-0.34197631520648475, ctrl=-0.0, connection=17.52, completion=4.10958904109589, energy=6.125636667929996, transformer=0.
已连接电池 batt_ev_048, 初始SOC: 42.0%, 最大功率: 120kW, 电池容量: 93kWh，并创BMS。
智能体的动作为: [ 0.02776861 -0.06350021 -0.         -0.12114549 -0.34729746 -0.
 -0.23840274 -0.89259523 -1.         -0.17114832 -0.        ]
已有历史设置self.charger_power=20.177459120750427，设置charger_power=3.810012638568878失败。
功率需求计算已禁用，直接使用充电桩功率: 20.18 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已有历史设置self.charger_power=28.888792991638184，设置charger_power=19.072219133377075失败。
功率需求计算已禁用，直接使用充电桩功率: 28.89 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 28.888792991638184, -5.866119612215055
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 20.177459120750427, -4.097207824056952
已在 set_all_batteries_before_solve 中设置 batt_ev_048 充电的有无功功率为 0.0, -0.0
SOC从 0.29 更新为 0.40。
SOC从 0.42 更新为 0.42。
SOC从 0.73 更新为 0.85。
已断开电池: batt_ev_048
时间步 85: 电池 batt_ev_048 已离开，当前SOC: 42.0%，能量满足率: 0.0%
奖励各项的值：powerloss=-0.19095422182968003, voltage=-0.41267991233663315, ctrl=-0.0, connection=17.6, completion=4.090909090909091, energy=6.09779286489395, transformer=0.
已连接电池 batt_ev_234, 初始SOC: 56.99999999999999%, 最大功率: 60kW, 电池容量: 63kWh，并创BMS。
已连接电池 batt_ev_227, 初始SOC: 8.0%, 最大功率: 60kW, 电池容量: 47kWh，并创BMS。
智能体的动作为: [ 0.01609409 -0.05424188 -0.         -0.12072875 -0.35118508 -0.
 -0.23541388 -0.89231926 -1.         -0.18267497 -0.        ]
已有历史设置self.charger_power=20.177459120750427，设置charger_power=3.254513069987297失败。
功率需求计算已禁用，直接使用充电桩功率: 20.18 kW。
已有历史设置self.charger_power=28.888792991638184，设置charger_power=18.833110332489014失败。
功率需求计算已禁用，直接使用充电桩功率: 28.89 kW。
初次设置charger_power=53.53915572166443。
功率需求计算已禁用，直接使用充电桩功率: 53.54 kW。
初次设置charger_power=10.960498452186584。
功率需求计算已禁用，直接使用充电桩功率: 10.96 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_056 充电的有无功功率为 28.888792991638184, -5.866119612215055
已在 set_all_batteries_before_solve 中设置 batt_ev_226 充电的有无功功率为 20.177459120750427, -4.097207824056952
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 10.960498452186584, -2.2256241355820827
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 53.53915572166443, -10.871589252316554
SOC从 0.40 更新为 0.51。
SOC从 0.85 更新为 0.96。
SOC从 0.08 更新为 0.36。
SOC从 0.57 更新为 0.61。
已断开电池: batt_ev_056
时间步 86: 电池 batt_ev_056 已离开，当前SOC: 95.8%，能量满足率: 94.0%
已断开电池: batt_ev_226
时间步 86: 电池 batt_ev_226 已离开，当前SOC: 50.9%，能量满足率: 51.4%
奖励各项的值：powerloss=-0.19480514261741358, voltage=-0.3913070771022742, ctrl=-0.0, connection=17.76, completion=4.054054054054054, energy=6.108339376164654, transformer=0.
智能体的动作为: [ 0.12907898 -0.11968628 -0.         -0.16252172 -0.19317415 -0.
 -0.1934558  -1.         -0.7525422  -0.         -0.        ]
已有历史设置self.charger_power=53.53915572166443，设置charger_power=60.0失败。
功率需求计算已禁用，直接使用充电桩功率: 53.54 kW。
已有历史设置self.charger_power=10.960498452186584，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 10.96 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 10.960498452186584, -2.2256241355820827
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 53.53915572166443, -10.871589252316554
SOC从 0.36 更新为 0.65。
SOC从 0.61 更新为 0.66。
奖励各项的值：powerloss=-0.1899291318759332, voltage=-0.34478493354688, ctrl=-0.0, connection=17.76, completion=4.054054054054054, energy=6.108339376164654, transformer=0.
智能体的动作为: [ 0.4843819  -0.30213982 -0.         -0.16587205 -0.21585517 -0.
 -0.34129357 -0.9074635  -0.8422524  -0.         -0.        ]
已有历史设置self.charger_power=53.53915572166443，设置charger_power=54.44780945777893失败。
功率需求计算已禁用，直接使用充电桩功率: 53.54 kW。
已有历史设置self.charger_power=10.960498452186584，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 10.96 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 10.960498452186584, -2.2256241355820827
已在 set_all_batteries_before_solve 中设置 batt_ev_227 充电的有无功功率为 53.53915572166443, -10.871589252316554
SOC从 0.65 更新为 0.93。
SOC从 0.66 更新为 0.70。
已断开电池: batt_ev_227
时间步 88: 电池 batt_ev_227 已离开，当前SOC: 93.4%，能量满足率: 94.9%
奖励各项的值：powerloss=-0.18678471290058568, voltage=-0.3460831810572218, ctrl=-0.0, connection=17.84, completion=4.0358744394618835, energy=6.123500911258658, transformer=0.
智能体的动作为: [ 0.4851439  -0.30219653 -0.         -0.16592778 -0.2158951  -0.
 -0.34194654 -0.90671533 -0.8418786  -0.         -0.        ]
已有历史设置self.charger_power=10.960498452186584，设置charger_power=0.0失败。
功率需求计算已禁用，直接使用充电桩功率: 10.96 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 10.960498452186584, -2.2256241355820827
SOC从 0.70 更新为 0.74。
奖励各项的值：powerloss=-0.1856821012145548, voltage=-0.28153292997117996, ctrl=-0.0, connection=17.84, completion=4.0358744394618835, energy=6.123500911258658, transformer=0.
智能体的动作为: [-0.02310348 -0.17547844 -0.         -0.13841026 -0.45258567 -0.
 -0.36362946 -0.7842062  -1.         -0.34052286 -0.        ]
已有历史设置self.charger_power=10.960498452186584，设置charger_power=20.431371331214905失败。
功率需求计算已禁用，直接使用充电桩功率: 10.96 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 2.310347557067871, 0.7593745194470258
已在 set_all_batteries_before_solve 中设置 batt_ev_234 充电的有无功功率为 10.960498452186584, -2.2256241355820827
SOC从 0.74 更新为 0.79。
已断开电池: batt_ev_234
时间步 90: 电池 batt_ev_234 已离开，当前SOC: 78.7%，能量满足率: 53.0%
奖励各项的值：powerloss=-0.19970655455494585, voltage=-0.20458709382785933, ctrl=-0.0, connection=17.92, completion=4.017857142857143, energy=6.119842024074284, transformer=0.
智能体的动作为: [-0.02403814 -0.1739465  -0.         -0.138621   -0.4524085  -0.
 -0.36355323 -0.7849206  -1.         -0.34078404 -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 2.403813600540161, 0.7900953223103242
奖励各项的值：powerloss=-0.19634791316138706, voltage=-0.07714568844706449, ctrl=-0.0, connection=17.92, completion=4.017857142857143, energy=6.119842024074284, transformer=0.
智能体的动作为: [ 0.12421227 -0.33675393 -0.         -0.12771542 -0.48765647 -0.
 -0.36115175 -0.68697035 -1.         -0.3077912  -0.        ]
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -4.72, -1.5513889764442346
奖励各项的值：powerloss=-0.18976264482307298, voltage=-0.057570948366936214, ctrl=-0.0, connection=17.92, completion=4.017857142857143, energy=6.119842024074284, transformer=0.
已连接电池 batt_ev_238, 初始SOC: 48.0%, 最大功率: 60kW, 电池容量: 41kWh，并创BMS。
智能体的动作为: [ 0.12423813 -0.33686298 -0.         -0.12769064 -0.48768628 -0.
 -0.36110526 -0.6868771  -1.         -0.30775267 -0.        ]
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 0.0, -0.0
SOC从 0.48 更新为 0.48。
奖励各项的值：powerloss=-0.19103238347241372, voltage=-0.019079880069807764, ctrl=-0.0, connection=17.92, completion=4.017857142857143, energy=6.119842024074284, transformer=0.
智能体的动作为: [ 0.1232816  -0.3368678  -0.         -0.12742935 -0.48754537 -0.
 -0.36084062 -0.6868708  -1.         -0.30756018 -0.        ]
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 0.0, -0.0
SOC从 0.48 更新为 0.48。
奖励各项的值：powerloss=-0.17846435097416052, voltage=-0.015467292617590278, ctrl=-0.0, connection=17.92, completion=4.017857142857143, energy=6.119842024074284, transformer=0.
智能体的动作为: [ 0.12348104 -0.3371361  -0.         -0.12737845 -0.48759788 -0.
 -0.36075985 -0.6866503  -1.         -0.30742562 -0.        ]
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 0.0, -0.0
SOC从 0.48 更新为 0.48。
奖励各项的值：powerloss=-0.16154765845306868, voltage=-0.08386977622689251, ctrl=-0.0, connection=17.92, completion=4.017857142857143, energy=6.119842024074284, transformer=0.
已连接电池 batt_ev_025, 初始SOC: 12.0%, 最大功率: 60kW, 电池容量: 49kWh，并创BMS。
已连接电池 batt_ev_013, 初始SOC: 18.0%, 最大功率: 120kW, 电池容量: 89kWh，并创BMS。
已连接电池 batt_ev_117, 初始SOC: 52.0%, 最大功率: 120kW, 电池容量: 111kWh，并创BMS。
已连接电池 batt_ev_166, 初始SOC: 28.000000000000004%, 最大功率: 120kW, 电池容量: 114kWh，并创BMS。
智能体的动作为: [ 0.12377417 -0.33745044 -0.         -0.12738542 -0.48777246 -0.
 -0.3606857  -0.68639004 -1.         -0.307413   -0.        ]
self.charger_power=0.0 改为 0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
初次设置charger_power=15.286250710487366。
功率需求计算已禁用，直接使用充电桩功率: 15.29 kW。
初次设置charger_power=58.53269577026367。
功率需求计算已禁用，直接使用充电桩功率: 58.53 kW。
初次设置charger_power=120.0。
功率需求计算已禁用，直接使用充电桩功率: 120.00 kW。
初次设置charger_power=0.0。
功率需求计算已禁用，直接使用充电桩功率: 0.00 kW。
已在 set_all_batteries_before_solve 中设置 batt1 充电的有无功功率为 -0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_238 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_025 充电的有无功功率为 0.0, -0.0
已在 set_all_batteries_before_solve 中设置 batt_ev_013 充电的有无功功率为 15.286250710487366, -3.104005595387158
已在 set_all_batteries_before_solve 中设置 batt_ev_117 充电的有无功功率为 120.0, -24.367039276080497
已在 set_all_batteries_before_solve 中设置 batt_ev_166 充电的有无功功率为 58.53269577026367, -11.885570806407378
SOC从 0.48 更新为 0.48。
SOC从 0.18 更新为 0.22。
SOC从 0.28 更新为 0.41。
SOC从 0.52 更新为 0.79。
SOC从 0.12 更新为 0.12。
已断开电池: batt_ev_238
时间步 96: 电池 batt_ev_238 已离开，当前SOC: 48.0%，能量满足率: 0.0%
已断开电池: batt_ev_025
时间步 96: 电池 batt_ev_025 已离开，当前SOC: 12.0%，能量满足率: 0.0%
已断开电池: batt_ev_013
时间步 96: 电池 batt_ev_013 已离开，当前SOC: 22.3%，能量满足率: 5.4%
已断开电池: batt_ev_117
时间步 96: 电池 batt_ev_117 已离开，当前SOC: 79.0%，能量满足率: 58.8%
已断开电池: batt_ev_166
时间步 96: 电池 batt_ev_166 已离开，当前SOC: 40.8%，能量满足率: 18.3%
奖励各项的值：powerloss=-0.15302434889428332, voltage=-0.15604542867978966, ctrl=-1.0, connection=18.32, completion=3.930131004366812, energy=6.02222665606094, transformer=0.
调度记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250511_173442_13Bus_cbat_1000000\test_results_20250511_223056\schedule.csv
储能放电功率记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250511_173442_13Bus_cbat_1000000\test_results_20250511_223056\storage_schedule.csv
储能能量记录已导出到 D:\LENOVO\Documents\Python\ML\powergym\results_20250511_173442_13Bus_cbat_1000000\test_results_20250511_223056\storage_energy.csv
已生成GIF动画，包含96步
测试完成 - 总奖励: 2067.0506
测试结果保存在: D:\LENOVO\Documents\Python\ML\powergym\results_20250511_173442_13Bus_cbat_1000000\test_results_20250511_223056
运行时间: 17859.70秒

进程已结束，退出代码为 0
```