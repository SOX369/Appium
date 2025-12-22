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

import time

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

# 初始化一个智能等待期，最多等待10s
wait=WebDriverWait(driver,10)

print("主界面向左滑动第一步...")
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1085, 1656)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(105, 1641)
actions.w3c_actions.pointer_action.release()
actions.perform()

print("主界面向左滑动第二步...")
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1066, 1626)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(131, 1634)
actions.w3c_actions.pointer_action.release()
actions.perform()

print("主界面向左滑动第三步...")
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1051, 1262)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(30, 1281)
actions.w3c_actions.pointer_action.release()
actions.perform()

print("点击哔哩哔哩 app按钮...")
x1=wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"哔哩哔哩"))).click()

time.sleep(5)

print("点击主页上方搜索栏...")
x2=wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"搜索栏，按钮"))).click()
print("输入搜索文本”appium“，查询相关视频...")
x3=wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,"搜索查询"))).send_keys("appium")
print("点击搜索按钮，进行查询...")
x4=wait.until(EC.element_to_be_clickable((AppiumBy.ID,"tv.danmaku.bili:id/action_search"))).click()
print("点击搜索结果中的第一个视频...")
x5=wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.GridView[@resource-id=\"tv.danmaku.bili:id/recycler_view\"]/android.view.ViewGroup[1]"))).click()
print("对该视频点赞...")
x6=wait.until(EC.element_to_be_clickable((AppiumBy.ID,"tv.danmaku.bili:id/like_icon"))).click()
print("收藏视频...")
x7=wait.until(EC.element_to_be_clickable((AppiumBy.ID,"tv.danmaku.bili:id/favorite_icon"))).click()
print("点击进入评论区...")
x8=wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.TextView[@resource-id=\"tv.danmaku.bili:id/tab_title\" and @text=\"评论\"]"))).click()
print("点击底部的评论文本框...")
x9=wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"文本栏"))).click()
print("输入评论文本...")
x10=wait.until(EC.visibility_of_element_located((AppiumBy.ID,"tv.danmaku.bili:id/edit"))).send_keys("感谢教学，收益匪浅！")
print("点击发布评论按钮...")
x11=wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.TextView[@text=\"发布\"]"))).click()
print("点击右侧弹幕文本框...")
x12=wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//androidx.compose.ui.platform.ComposeView[@resource-id=\"tv.danmaku.bili:id/danmaku_input_parent\"]/android.view.View"))).click()
print("输入弹幕文本...")
x13=wait.until(EC.visibility_of_element_located((AppiumBy.ID,"tv.danmaku.bili:id/player_input_edit"))).send_keys("受益匪浅！！")
print("点击发布弹幕按钮...")
x14=wait.until(EC.element_to_be_clickable((AppiumBy.ID,"tv.danmaku.bili:id/player_input_send"))).click()

print("点赞、收藏、评论业务功能测试成功！")

driver.quit()