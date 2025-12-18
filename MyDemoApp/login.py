# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

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
	"appium:deviceName": "A7QK023515000172",
	"appium:dontStopAppOnReset": True,
	"appium:noReset": True,
	"appium:appPackage": "com.saucelabs.mydemoapp.rn",
	"appium:appActivity": "com.saucelabs.mydemoapp.rn.MainActivity",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

wait=WebDriverWait(driver,5)

print("点击打开菜单选择...")
x1=driver.find_element(by=AppiumBy.XPATH,value="//android.view.ViewGroup[@content-desc=\"open menu\"]/android.widget.ImageView")
x1.click()

print("点击列表中的 Log In 按钮...")
x2=wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"menu item log in")))
x2.click()

print("输入用户名...")
x3=wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,"Username input field")))
x3.send_keys("bob@example.com")

print("输入密码...")
x3=wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,"Password input field")))
x3.send_keys("10203040")

print("点击 Login 按钮...")
x4=wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"Login button")))
x4.click()


print("进行断言...")
x5=wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,"//android.widget.TextView[@text=\"Products\"]"))).text

if x5=="Products":
    print("登录成功！")
else:
    print("登录失败！")

    assert x5=="Products"

print("退出登录，进行下一轮测试用例验证...")
x6=wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc=\"open menu\"]/android.widget.ImageView")))
x6.click()

x7=wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"menu item log out")))
x7.click()

x8=wait.until(EC.element_to_be_clickable((AppiumBy.ID,"android:id/button1")))
x8.click()

x9=wait.until(EC.element_to_be_clickable((AppiumBy.ID,"android:id/button1")))
x9.click()
print("成功退出登录！！")

driver.quit()

