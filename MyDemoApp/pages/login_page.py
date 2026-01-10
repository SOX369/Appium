import allure
from appium.webdriver.common.appiumby import AppiumBy

import sys,os
# 将项目根目录添加到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from Appium.MyDemoApp.base.base_page import BasePage


class LoginPage(BasePage):
    menu_icon = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc=\"open menu\"]/android.widget.ImageView")
    menu_login_item = (AppiumBy.ACCESSIBILITY_ID, "menu item log in")
    username_input = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    password_input = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
    login_btn = (AppiumBy.ACCESSIBILITY_ID, "Login button")

    # 登录成功后的标志元素
    product_title = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"Products\"]")

    # [删除] 既然报错位置不固定，不再死板地定义 error_msg 的位置
    # error_msg = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='generic-error-message']/android.widget.TextView")

    # 退出登录相关元素
    menu_logout_item = (AppiumBy.ACCESSIBILITY_ID, "menu item log out")
    confirm_dialog_btn = (AppiumBy.ID, "android:id/button1")
    logout_success_ok_btn = (AppiumBy.ID, "android:id/button1")

    @allure.step("执行登录操作：用户名={usr}")
    def login_action(self, usr, pwd):
        """执行登录操作：点击菜单 -> 输入 -> 点击登录"""
        self.click(self.menu_icon)
        self.click(self.menu_login_item)
        self.input(self.username_input, usr)
        self.input(self.password_input, pwd)
        self.click(self.login_btn)

    @allure.step("断言正确后，需执行退出登录操作(便于后续进行多组登录用例测试)")
    def logout_action(self):
        """执行退出登录操作"""
        print("   >>> 执行退出登录清理操作...")
        self.click(self.menu_icon)
        self.click(self.menu_logout_item)
        self.click(self.confirm_dialog_btn)
        self.click(self.logout_success_ok_btn)
        print("   >>> 退出登录完成，回到初始状态。")

    def get_login_success_text(self):
        """获取登录成功的标题 (Products)"""
        return self.get_text(self.product_title)

    def is_error_message_exist(self, text_content):
        """
        [重构] 核心修改：直接查找页面上是否存在包含指定文字的元素不再依赖固定的 XPath，解决 '用户名为空' 报错位置不同的问题
        """
        # 使用 Android 原生定位：找 text 属性等于预期的元素
        try:
            locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text_content}")')
            element = self.find_element(locator)
            return element.text
        except:
            return "未找到报错信息"