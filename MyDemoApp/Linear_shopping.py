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

# --- 引入显式等待模块 ---
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:automationName": "UiAutomator2",
	"appium:deviceName": "Magic5 Pro",
	"appium:appPackage": "com.saucelabs.mydemoapp.rn",
	"appium:appActivity": "com.saucelabs.mydemoapp.rn.MainActivity",
	"appium:dontStopAppOnReset": True,
	"appium:noReset": True,
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# 初始化等待对象
wait = WebDriverWait(driver, 10)

print("点击排序按钮...")
x1 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc=\"sort button\"]/android.widget.ImageView")))
x1.click()

print("选择价格升序 (Price - Ascending)...")
x2 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text=\"Price - Ascending\"]")))
x2.click()

print("点击第一个商品...")
x3 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc=\"store item\"])[1]/android.view.ViewGroup[1]/android.widget.ImageView")))
x3.click()

print("点击加号按钮 (增加数量)...")
x4 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc=\"counter plus button\"]/android.widget.ImageView")))
x4.click()
x4.click()

print("点击加入购物车...")
x5 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Add To Cart button")))
x5.click()

print("执行滑动操作...")
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1273, 1548)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(52, 1548)
actions.w3c_actions.pointer_action.release()
actions.perform()

print("点击第四个商品...")
x6 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc=\"store item\"])[4]/android.view.ViewGroup[1]/android.widget.ImageView")))
x6.click()

print("点击加号按钮 (增加数量)...")
x7 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc=\"counter plus button\"]/android.widget.ImageView")))
x7.click()
x7.click()

print("点击加入购物车...")
x8 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Add To Cart button")))
x8.click()

print("点击购物车图标...")
x9 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc=\"cart badge\"]/android.widget.ImageView")))
x9.click()

print("点击去结算 (Proceed To Checkout)...")
x10 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Proceed To Checkout button")))
x10.click()

# 填写地址信息 (改为先 Click 后 SendKeys)
print("输入姓名...")
x11 = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Full Name* input field")))
x11.send_keys("zhang san")

print("输入地址...")
x12 = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Address Line 1* input field")))
x12.send_keys("dsabkjcgsafvcjhafvq")

print("输入城市...")
x13 = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "City* input field")))
x13.send_keys("china")

print("输入邮编...")
x14 = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Zip Code* input field")))
x14.send_keys("464400")

print("输入国家...")
x15 = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Country* input field")))
x15.send_keys("china")

print("点击去支付 (To Payment)...")
x16 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "To Payment button")))
x16.click()

# 重点思路--------等待一个“支付页独有”的元素出现（比如“卡号 Card Number”），然后再回头去找“Full Name”--------
wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Enter a payment method"]')))

print("输入支付姓名...")
x17 = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Full Name* input field")))
x17.send_keys("li si")

print("输入卡号...")
x18 = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Card Number* input field")))
x18.send_keys("1234567890")

print("输入过期日期...")
x19 = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Expiration Date* input field")))
x19.send_keys("0725")

print("输入安全码...")
x20 = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Security Code* input field")))
x20.send_keys("999")

print("点击预览订单 (Review Order)...")
x21 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Review Order button")))
x21.click()
x21.click()

print("点击下单 (Place Order)...")
x22 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Place Order button")))
x22.click()

print("进行断言...")
x23 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text=\"Continue Shopping\"]"))).text
if x23=="Continue Shopping":
    print("购物流程用例测试成功！")
else:
    print("购物流程用例测试失败！")

    assert x23=="Continue Shopping"

x23 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text=\"Continue Shopping\"]")))
x23.click()


driver.quit()
