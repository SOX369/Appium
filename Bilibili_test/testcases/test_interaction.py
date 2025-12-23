import pytest
import sys,os
# 将项目根目录添加到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Appium.Bilibili_test.base.driver import get_driver
from Appium.Bilibili_test.pages.launcher_page import LauncherPage
from Appium.Bilibili_test.pages.video_page import VideoPage

#编写点赞收藏测试逻辑
class TestInteraction:
    def setup_class(self):
        self.driver = get_driver()
        self.launcher = LauncherPage(self.driver)
        self.video_page = VideoPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    def test_video_interaction(self):
        # 步骤1：进入B站
        self.launcher.start_bilibili()

        # 步骤2：搜索视频
        self.video_page.search_video("appium")

        # 步骤3：交互（点赞、收藏、评论、弹幕）
        self.video_page.interact_with_video("感谢教学，受益匪浅！", "受益匪浅！！")

        print("点赞、收藏、评论业务功能测试成功！")


if __name__ == '__main__':
    pytest.main(["-vs", "test_interaction.py"])