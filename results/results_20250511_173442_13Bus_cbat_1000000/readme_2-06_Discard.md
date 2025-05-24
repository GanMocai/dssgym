

## Case Pre-definition

- 算例 06 关闭BMS，关闭容量基值（提供基于EV最大功率的标幺值）——但是EVBMS的代码逻辑出现问题，不可重设了，作废。
- BMS enable charger_power <= 10 可重设
- cbat
- s 1
- num_steps 1,000,000
- station_bus 680
- charger_num 10
- charger_kW \[120\] * 10
- transformer_kVA': 800
- EV_demand `D:\LENOVO\Documents\Python\ML\dssgym\ev_demand\ev_demand-public_parking-general-250-A95.csv`
- EV_PF -0.98
- kWh round 2


```dss
!PV Shape
New Loadshape.PV_Daily npts=96 interval=0.25
~ mult=(File=D:\LENOVO\Documents\Python\ML\dssgym\systems\1-day-900-s-Solar-2-Average-Pad-06.csv)
~ Action=Normalize

!ADD PV DEFINITIONS. Initialize with 0 kw. Checked by o3-mini
New Load.PV1 Bus1=680.1.2.3  Phases=3 Conn=Delta Model=6 kV=4.16 kW=-80.0 kvar=0.0 daily=PV_Daily

!BATTERY DEFINITIONS. Initialize with 0 kw
New Generator.batt1 bus1=680 kV=4.16 kW=0.0 pf=0.95 conn=Delta Model=1
```

```csv
name,max_kw,pf,max_kwh,initial_kwh
batt1,100,0.95,200,40
```

## Path

- model_path `D:\LENOVO\Documents\Python\ML\dssgym\results\results_20250511_121502_13Bus_cbat_s2_1000000\model\ppo_model.zip`
- 测试命令参数 `--model_path D:\LENOVO\Documents\Python\ML\dssgym\results\results_20250511_121502_13Bus_cbat_s2_1000000\model\ppo_model.zip --env_name 13Bus_cbat --test_only true`
  - 额外操作，在circuit中调整BMS和功率基值设置。

## Train Info

### Overview

运行时间、最后日志和奖励情况。

```text
运行时间: 17859.70秒
------------------------------------------
| rollout/                |              |
|    ep_len_mean          | 96           |
|    ep_rew_mean          | 1.65e+03     |
| time/                   |              |
|    fps                  | 56           |
|    iterations           | 489          |
|    time_elapsed         | 17767        |
|    total_timesteps      | 1001472      |
| train/                  |              |
|    approx_kl            | 0.0068638464 |
|    clip_fraction        | 0.0363       |
|    clip_range           | 0.2          |
|    entropy_loss         | -15.2        |
|    explained_variance   | 0.98         |
|    learning_rate        | 0.0003       |
|    loss                 | 1.34e+03     |
|    n_updates            | 4880         |
|    policy_gradient_loss | -0.00952     |
|    std                  | 0.967        |
|    value_loss           | 3.32e+03     |
------------------------------------------

训练过程奖励统计:
  最小奖励: -28930.5285
  最大奖励: 2261.8306
  平均奖励: 1539.0047
  奖励标准差: 2477.4346
警告: 检测到非常大的奖励值(>1000)，这可能导致训练不稳定。建议考虑奖励缩放。
奖励数据已成功导出到: D:\LENOVO\Documents\Python\ML\dssgym\results\results_20250511_173442_13Bus_cbat_1000000\rewards_in_training.csv
模型已保存至 D:\LENOVO\Documents\Python\ML\dssgym\results\results_20250511_173442_13Bus_cbat_1000000\model\ppo_model
奖励函数权重已保存至 D:\LENOVO\Documents\Python\ML\dssgym\results\results_20250511_173442_13Bus_cbat_1000000\reward_weights.csv.
```