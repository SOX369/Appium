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

:: === 【关键修复 2】捕获 Python 错误 ===
:: 如果 Python 执行出错 (退出码不为0)，则让 Jenkins 任务也失败
if %errorlevel% neq 0 (
    echo [ERROR] Python script failed!
    exit /b %errorlevel%
)

echo [INFO] Test Script Finished.