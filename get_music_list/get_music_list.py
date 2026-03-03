from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

# --- 配置部分 ---
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "A7QK023515000172",
    "appium:appPackage": "com.tinghai.music",
    "appium:appActivity": "com.tinghai.music.MainActivity",
    "appium:dontStopAppOnReset": True,
    "appium:noReset": True,
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

# 初始化 Driver
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# 这一步是你录制的点击操作，用于进入列表（保留你的逻辑）
# 注意：instance(35) 这种定位比较脆弱，如果运行报错，请手动点进收藏列表再运行代码
try:
    el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                              value="new UiSelector().className(\"android.view.View\").instance(35)")
    el7.click()
    time.sleep(2)  # 等待页面跳转
except:
    print("点击操作跳过或失败，假设当前已在歌曲列表页面...")


# --- 定义滑动函数 (基于你录制的代码封装) ---
def swipe_up():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # 坐标从 (547, 2258) 滑动到 (582, 979)，模拟向上拖动
    actions.w3c_actions.pointer_action.move_to_location(547, 2000)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.move_to_location(547, 800)  # 稍微调整终点，保证滑动更垂直
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    print("执行了一次上滑操作...")
    time.sleep(1.5)  # 等待列表惯性滚动停止


# --- 核心抓取逻辑 ---
all_songs = set()  # 使用集合自动去重
output_file = "music_list.txt"
max_no_new_data_count = 0  # 计数器，用于判断是否到底

print("开始抓取任务...")

with open(output_file, "w", encoding="utf-8") as f:
    # 循环抓取，最多尝试滑动100次（防止死循环）
    for i in range(100):
        print(f"正在扫描第 {i + 1} 页...")

        # 获取屏幕上所有的 TextView (包含歌名、时间、其他标签)
        # 对应你截图中 Source 里的 android.widget.TextView
        elements = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")

        new_data_found = False

        for el in elements:
            try:
                text = el.text
                if not text:
                    continue

                # --- 过滤逻辑 (关键步骤) ---
                # 1. 排除包含冒号的短文本 (如 3:21, 4:16)，这是时间
                if ":" in text and len(text) < 6:
                    continue
                # 2. 排除一些已知的非歌名关键词 (根据需要添加)
                if text in ["添加", "播放", "下载", "我的", "歌单", "分类", "首页", "收藏", "媒体库", "喜欢", "添加日期", "339 首歌曲"]:
                    continue
                # 3. 排除纯数字
                if text.isdigit():
                    continue

                # 如果这个歌名之前没存过，就写入文件
                if text not in all_songs:
                    all_songs.add(text)
                    f.write(text + "\n")
                    f.flush()  # 实时保存
                    print(f"  [+] 捕获歌曲: {text}")
                    new_data_found = True
            except Exception:
                continue

        # 判断是否到底部
        if not new_data_found:
            max_no_new_data_count += 1
            print(f"当前页面无新数据 ({max_no_new_data_count}/3)")
        else:
            max_no_new_data_count = 0  # 只要发现新数据，计数器归零

        # 连续 3 次滑动都没有新数据，说明到底了
        if max_no_new_data_count >= 3:
            print("=== 似乎已到达列表底部，停止抓取 ===")
            break

        # 执行滑动
        swipe_up()

print(f"抓取完成！共记录 {len(all_songs)} 首歌曲。")
driver.quit()