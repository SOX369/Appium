from appium import webdriver
from appium.options.common.base import AppiumOptions

#封装驱动的配置和启动，对应设置测试设备options参数部分
def get_driver():
    """初始化并返回 Appium 驱动"""
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "A7QK023515000172",
        "appium:dontStopAppOnReset": True,
        "appium:noReset": True,
        # 注意：这里保持您原本的 honor launcher，因为您的脚本是从桌面开始滑动的
        "appium:appPackage": "com.hihonor.android.launcher",
        "appium:appActivity": "com.hihonor.android.launcher.unihome.UniHomeLauncher",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })

    # 保持appium 1.x URL 的格式
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    return driver