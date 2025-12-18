import time
import sys,os
# 将项目根目录添加到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from appium.webdriver.common.appiumby import AppiumBy
from Appium.Bilibili_test.base.base_page import BasePage

#处理手机桌面，从主桌面滑动找到 Bilibili 并进入
class LauncherPage(BasePage):
    # 元素定位 (Locator)
    # 注意：这里只定义“B站图标”，滑动逻辑不需要定位符
    icon_bilibili = (AppiumBy.ACCESSIBILITY_ID, "哔哩哔哩")

    def start_bilibili(self):
        """业务逻辑：滑动3次并点击B站"""
        print("正在桌面寻找B站应用...")
        # 调用 BasePage 封装好的滑动
        self.swipe_left(1184, 103, 1633)
        time.sleep(1)
        self.swipe_left(1180, 69, 1295)
        time.sleep(1)
        self.swipe_left(1161, 84, 1279)
        time.sleep(1)

        print("点击B站图标...")
        self.click(self.icon_bilibili)

        time.sleep(5)