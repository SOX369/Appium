@echo off
:: ==========================================
:: 自动化测试执行脚本 (Windows)
:: ==========================================

:: 1. 解决 Jenkins 控制台中文乱码 & Emoji 报错问题
set PYTHONIOENCODING=utf-8

:: 2. 切换到当前脚本所在的目录 (确保路径正确)
cd /d %~dp0

:: 3. 创建日志目录 (如果没有的话)
if not exist "logs" mkdir logs

echo [INFO] Start Automation Test...
echo [INFO] Current Dir: %cd%

:: 4. 调用 Python 运行测试
:: 使用你配置好的 Anaconda 绝对路径
:: 调用 run_all.py (或者 runLogin.py)
D:\Anaconda3\envs\DL\python.exe runLogin.py

:: 注意：这里不需要 exit 0，让 Python 的返回码决定构建成功还是失败
echo [INFO] Test Script Finished.