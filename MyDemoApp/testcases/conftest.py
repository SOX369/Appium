import allure
import pytest
import sys
import os
import time

 # 向上找4层，定位到 .../FPGA_test (根目录)，这样才能找到 "Appium" 这个文件夹
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from Appium.MyDemoApp.base.driver import get_driver

@pytest.fixture(scope="class")
def driver(request):
    print("\n[Fixture] 正在启动 Appium Driver...")
    driver_instance = get_driver()

    # 在测试类上创建一个叫 driver 的属性，把驱动放进去(request.cls.xxx 中的 xxx 只是一个自定义的变量名，写成 request.cls.xxx，就要用 self.xxx 取。)
    if request.cls:
        request.cls.driver = driver_instance

    yield driver_instance

    print("\n[Fixture] 正在关闭 Driver...")
    driver_instance.quit()


# ----------------- 新增：日志配置钩子 -----------------
# 这个钩子会在 pytest 启动配置阶段运行
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # 1. 定义日志目录 (这里默认是在您运行 pytest 命令的当前目录下创建 logs)
    # 如果您想指定绝对路径，可以将 log_dir 修改为您想要的绝对路径
    log_dir = "./logs"

    # 2. 如果目录不存在，自动创建，避免报错
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 3. 生成时间戳文件名，例如: test_run_2026-01-10_18-30-00.log
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_file_name = f"test_run_{now}.log"

    # 4. 修改 pytest 的配置，覆盖 pytest.ini 中的 log_file 设置
    # 这样生成的日志就会带上时间戳，且不会相互覆盖
    config.option.log_file = os.path.join(log_dir, log_file_name)


# ----------------- 新增：失败自动截图钩子 -----------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例的执行结果
    """
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()

    # 如果是 "call" 阶段（即执行测试用例的阶段）且结果是 "failed"
    if rep.when == "call" and rep.failed:
        # 从 item 中获取 driver 实例 (因为我们在 fixture 里把 driver 挂到了 request.cls 上)
        # item.cls 是测试类，getattr 安全地获取 driver 属性
        driver = getattr(item.cls, "driver", None)

        if driver:
            print(f"\n[Allure] 检测到用例失败: {item.name}，正在截图...")
            # 截图并通过 allure.attach 添加到报告中
            allure.attach(
                driver.get_screenshot_as_png(),
                name="失败截图_Fail_Screenshot",
                attachment_type=allure.attachment_type.PNG
            )


