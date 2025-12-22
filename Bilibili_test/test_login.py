# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# --- 新增的导入：用于智能等待,等待元素加载完成后再执行操作，避免因网络或设备卡顿导致的元素找不到问题 ---
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:automationName": "UiAutomator2",
	"appium:deviceName": "Magic5 Pro",
	"appium:appPackage": "com.hihonor.android.launcher",
	"appium:appActivity": "com.hihonor.android.launcher.unihome.UniHomeLauncher",
	"appium:dontStopAppOnReset": True,
	"appium:noReset": True,
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

wait=WebDriverWait(driver,10)

print("主界面向左滑动一步...")
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1184, 1633)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(103, 1633)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(1)

print("主界面向左滑动两步...")
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1180, 1295)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(69, 1279)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(1)

print("主界面向左滑动三步...")
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1161, 1279)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(84, 1295)
actions.w3c_actions.pointer_action.release()
actions.perform()

print("点击B站图表，进入app...")
x1=wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"哔哩哔哩"))).click()

print("点击弹出登录界面的其他登录方式...")
x2=wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.TextView[@text=\"其他登录方式\"]"))).click()

print("点击其他登录...")
x3=wait.until(EC.element_to_be_clickable((AppiumBy.ID,"tv.danmaku.bili:id/btn_change_account"))).click()

print("点击密码登录按钮..")
x4=wait.until(EC.element_to_be_clickable((AppiumBy.ID,"tv.danmaku.bili:id/btn_change_account"))).click()

print("输入账号...")
x5=wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,"//androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText[1]"))).send_keys("18338655681")

print("输入密码...")
x6=wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,"//androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText[2]"))).send_keys("3.1415926535")

print("点击同意协议选项...")
x7=wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[4]"))).click()

print("点击登录按钮...")
x8=wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.TextView[@text=\"登录\"]"))).click()

print("登录成功后点击主界面 我的 按钮...")
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1192, 2757)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

print("通过 我的 界面中用户名进行断言")

x9=wait.until(EC.visibility_of_element_located((AppiumBy.ID,"tv.danmaku.bili:id/nick_name"))).text

if x9=="亦訫予平":
    print("登录成功！")
    assert x9=="亦訫予平"
else:
    print("登录失败！")


driver.quit()