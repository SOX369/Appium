import sys,os
# 将项目根目录添加到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from appium.webdriver.common.appiumby import AppiumBy
from Appium.Bilibili_test.base.base_page import BasePage

#专门处理登录相关的元素和逻辑。
class LoginPage(BasePage):
    # === 元素定位 ===
    btn_other_login = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"其他登录方式\"]")
    btn_change_acct = (AppiumBy.ID, "tv.danmaku.bili:id/btn_change_account")
    # 密码登录按钮 (注意：您脚本里这也是 btn_change_account，如果一样则复用)
    btn_pass_login = (AppiumBy.ID, "tv.danmaku.bili:id/btn_change_account")

    ipt_username = (
    AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText[1]")
    ipt_password = (
    AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText[2]")

    chk_agreement = (
    AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[4]")
    btn_login = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"登录\"]")

    # 断言用的元素
    txt_nickname = (AppiumBy.ID, "tv.danmaku.bili:id/nick_name")
    btn_mine = (AppiumBy.ID, "我的_按钮_ID_这里需要您补充或者滑动查找")

    # 注意：您原脚本最后有个滑动操作进入“我的”，我建议封装到这里

    def login_action(self, user, pwd):
        """业务逻辑：执行登录流程"""
        print("开始执行登录流程...")
        self.click(self.btn_other_login)
        self.click(self.btn_change_acct)
        self.click(self.btn_pass_login)

        self.input(self.ipt_username, user)
        self.input(self.ipt_password, pwd)

        self.click(self.chk_agreement)
        self.click(self.btn_login)

    def get_login_result(self):
        # 进入'我的'页面并获取昵称
        self.swipe_left(1192, 1192, 2757)  # 使用的 swipe/action 模拟点击坐标 (1192, 2757)，这通常是“我的”按钮的位置

        return self.get_text(self.txt_nickname)