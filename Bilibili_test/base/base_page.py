from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

#所有页面的基类。封装最通用的 find, click, input 以及常用的 swipe 操作
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # 统一使用 10秒 智能等待
        self.wait = WebDriverWait(self.driver, 10)

    def find_ele(self, locator):
        """通用查找元素方法，带智能等待"""
        # locator 格式为 (AppiumBy.ID, "value")
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator):
        """查找可点击元素"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        """封装点击操作"""
        self.find_clickable(locator).click()

    def input(self, locator, text):
        """封装输入操作"""
        ele = self.wait.until(EC.visibility_of_element_located(locator))
        ele.clear()
        ele.send_keys(text)

    def get_text(self, locator):
        """获取文本"""
        return self.find_ele(locator).text

    def swipe_left(self, start_x=1184, end_x=103, y=1633):
        """封装左滑操作 (基于您脚本中的 W3C ActionChains)"""
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()