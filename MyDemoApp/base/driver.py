from appium import webdriver

import sys,os
# 将项目根目录添加到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Appium.MyDemoApp.utils.file_reader import load_yaml_data
from appium.options.common.base import AppiumOptions


def get_driver():
    caps = load_yaml_data("caps.yaml")
    options = AppiumOptions()
    options.load_capabilities(caps)

    # 启动驱动
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver
