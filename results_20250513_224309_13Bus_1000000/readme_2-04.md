

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
- EV_demand `D:\LENOVO\Documents\Python\ML\powergym\ev_demand\ev_demand-public_parking-general-250-A95.csv`
- EV_PF -0.98
- kWh round 2


```dss
!PV Shape
New Loadshape.PV_Daily npts=96 interval=0.25
~ mult=(File=D:\LENOVO\Documents\Python\ML\powergym\systems\1-day-900-s-Solar-2-Average-Pad-06.csv)
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

- model_path ``
- 测试命令参数 `--model_path  --env_name 13Bus --test_only true`


## Train Info

### Overview

运行时间、最后日志和奖励情况。

```text

```