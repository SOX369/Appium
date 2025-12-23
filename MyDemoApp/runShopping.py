import pytest
import os
import shutil

if __name__ == '__main__':
    # 1. 定义报告数据的临时目录 和 最终HTML报告的目录
    result_dir = './report'

    # 2. 每次运行前，清理旧的报告数据，防止历史数据干扰
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)

    # 3. 运行 Pytest
    # -vs: 输出详细信息
    # --alluredir: 指定 Allure 数据生成路径
    # 这里不需要加 - -clean - alluredir，上面手动清理了
    args = ['-vs', 'Appium/MyDemoApp/testcases/test_shopping.py', f'--alluredir={result_dir}']
    pytest.main(args)

    # 4. (可选) 本地调试时直接生成并打开报告
    # 注意：在 Jenkins 中通常由 Jenkins Allure 插件负责生成报告，
    # 这一步在 CI 环境下可以注释掉，或者保留也没关系
    # os.system(f'allure generate {result_dir} -o {report_dir} --clean')