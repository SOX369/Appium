import pytest
import sys,os
# 将项目根目录添加到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Appium.Bilibili_test.base.driver import get_driver
from Appium.Bilibili_test.pages.launcher_page import LauncherPage
from Appium.Bilibili_test.pages.login_page import LoginPage

#编写登录测试逻辑，这里只负责调用，不负责实现
class TestLogin:
    def setup_class(self):
        # 1. 获取驱动
        self.driver = get_driver()
        # 2. 初始化页面对象
        self.launcher = LauncherPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    def test_bilibili_login(self):
        # 步骤1：从桌面进入B站
        self.launcher.start_bilibili()

        # 步骤2：执行登录操作
        self.login_page.login_action("18338655681", "3.1415926535")

        # 步骤3：获取结果并断言
        # 注意：这里假设 login_action 后通过坐标点击进入了“我的”页面
        nickname = self.login_page.get_login_result()

        if nickname == "亦訫予平":
            print(" 登录成功！")
        else:
            print("❌ 登录失败！")

        assert nickname == "亦訫予平"


if __name__ == '__main__':
    pytest.main(["-vs", "test_login.py"])