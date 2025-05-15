cd ..
REM 恒功率改为完全受桩侧控制，临时过渡，有待后续训练
::D:/LENOVO/anaconda3/envs/ML/python.exe D:/LENOVO/Documents/Python/ML/powergym/ppo_agent.py --model_path D:\LENOVO\Documents\Python\ML\powergym\results_20250501_021615_13Bus_cbat_1000000_01\model\ppo_model.zip --env_name 13Bus_cbat --test_only true
::D:/LENOVO/anaconda3/envs/ML/python.exe D:/LENOVO/Documents/Python/ML/powergym/ppo_agent.py --model_path D:\LENOVO\Documents\Python\ML\powergym\results_20250502_005245_13Bus_cbat_s2_1000000_02\model\ppo_model.zip --env_name 13Bus_cbat_s2 --test_only true
::D:/LENOVO/anaconda3/envs/ML/python.exe D:/LENOVO/Documents/Python/ML/powergym/ppo_agent.py --model_path D:\LENOVO\Documents\Python\ML\powergym\results_20250502_125646_13Bus_1000000_03\model\ppo_model.zip --env_name 13Bus --test_only true

REM 改为真正的容量，临时过渡，有待后续训练
D:/LENOVO/anaconda3/envs/ML/python.exe D:/LENOVO/Documents/Python/ML/powergym/ppo_agent.py --model_path D:\LENOVO\Documents\Python\ML\powergym\results_20250503_091058_13Bus_cbat_1000000_04\model\ppo_model.zip --env_name 13Bus_cbat --test_only true
D:/LENOVO/anaconda3/envs/ML/python.exe D:/LENOVO/Documents/Python/ML/powergym/ppo_agent.py --model_path D:\LENOVO\Documents\Python\ML\powergym\results_20250503_124337_13Bus_cbat_s2_1000000_05\model\ppo_model.zip --env_name 13Bus_cbat_s2 --test_only true
D:/LENOVO/anaconda3/envs/ML/python.exe D:/LENOVO/Documents/Python/ML/powergym/ppo_agent.py --model_path D:\LENOVO\Documents\Python\ML\powergym\results_20250503_165005_13Bus_1000000_06\model\ppo_model.zip --env_name 13Bus --test_only true
D:/LENOVO/anaconda3/envs/ML/python.exe D:/LENOVO/Documents/Python/ML/powergym/ppo_agent.py --model_path D:\LENOVO\Documents\Python\ML\powergym\results_20250504_012306_13Bus_cbat_1000000_07\model\ppo_model.zip --env_name 13Bus_cbat --test_only true
D:/LENOVO/anaconda3/envs/ML/python.exe D:/LENOVO/Documents/Python/ML/powergym/ppo_agent.py --model_path D:\LENOVO\Documents\Python\ML\powergym\results_20250504_055308_13Bus_cbat_1000000_08\model\ppo_model.zip --env_name 13Bus_cbat --test_only true

REM 不可行，基于根目录的相对路径powergym.powergym无法被识别为模块 ModuleNotFoundError: No module named 'powergym.powergym'
pause