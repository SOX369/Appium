import pytest
import os

if __name__ == '__main__':
    # 1. 定义报告数据的临时目录 和 最终HTML报告的目录
    result_dir = './report'

    # 2. 运行 Pytest
    # -vs: 输出详细信息
    # --alluredir: 指定 Allure 数据生成路径
    args = ['-vs', './testcases/test_login.py', f'--alluredir={result_dir}', '--clean-alluredir']
    pytest.main(args)
