from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    #查找可见元素
    def find_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    #查找可点击元素
    def find_clickable(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    #点击操作
    def click(self,locator):
        return self.find_clickable(locator).click()

    #输入文本操作
    def input(self,locator,text):
        x=self.wait.until(EC.visibility_of_element_located(locator))
        x.clear()
        x.send_keys(text)

    #获取文本
    def get_text(self,locator):
        return self.find_element(locator).text

    #封装滑动操作
    def swipe_left(self, start_x=1273, end_x=52, y=1548):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()



