import allure
import pytest

import sys,os
# 将项目根目录添加到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
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