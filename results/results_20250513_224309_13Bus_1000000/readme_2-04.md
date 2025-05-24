

## Case Pre-definition

- 算例 04 连续->离散 发现之前的后处理映射存在问题没考虑离散，相当于一直设置为最大功率的情况，这是修改后重新训练的。
- BMS enable charger_power <= 10 可重设
- not cbat
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

- model_path `D:\LENOVO\Documents\Python\ML\dssgym\results\results_20250513_224309_13Bus_1000000\model\ppo_model.zip`
- 测试命令参数 `--model_path D:\LENOVO\Documents\Python\ML\dssgym\results\results_20250513_224309_13Bus_1000000\model\ppo_model.zip --env_name 13Bus --test_only true`


## Train Info

### Overview

运行时间、最后日志和奖励情况。

```text
-----------------------------------------
| rollout/                |             |
|    ep_len_mean          | 96          |
|    ep_rew_mean          | 2.04e+03    |
| time/                   |             |
|    fps                  | 31          |
|    iterations           | 489         |
|    time_elapsed         | 32197       |
|    total_timesteps      | 1001472     |
| train/                  |             |
|    approx_kl            | 0.008997658 |
|    clip_fraction        | 0.0757      |
|    clip_range           | 0.2         |
|    entropy_loss         | -26.1       |
|    explained_variance   | 1           |
|    learning_rate        | 0.0003      |
|    loss                 | 10.3        |
|    n_updates            | 4880        |
|    policy_gradient_loss | -0.0263     |
|    value_loss           | 17.9        |
-----------------------------------------

训练过程奖励统计:
  最小奖励: 1626.2761
  最大奖励: 2073.6339
  平均奖励: 1826.6251
  奖励标准差: 105.4046
警告: 检测到非常大的奖励值(>1000)，这可能导致训练不稳定。建议考虑奖励缩放。
奖励数据已成功导出到: D:\LENOVO\Documents\Python\ML\dssgym\results\results_20250513_224309_13Bus_1000000\rewards_in_training.csv
模型已保存至 D:\LENOVO\Documents\Python\ML\dssgym\results\results_20250513_224309_13Bus_1000000\model\ppo_model
奖励函数权重已保存至 D:\LENOVO\Documents\Python\ML\dssgym\results\results_20250513_224309_13Bus_1000000\reward_weights.csv.
```