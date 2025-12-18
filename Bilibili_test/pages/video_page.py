import sys,os
# 将项目根目录添加到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from appium.webdriver.common.appiumby import AppiumBy
from Appium.Bilibili_test.base.base_page import BasePage

#处理视频互动，点赞、收藏、评论
class VideoPage(BasePage):
    # === 元素定位 ===
    bar_search = (AppiumBy.ACCESSIBILITY_ID, "搜索栏，按钮")
    ipt_search = (AppiumBy.ACCESSIBILITY_ID, "搜索查询")
    btn_search_action = (AppiumBy.ID, "tv.danmaku.bili:id/action_search")

    # 搜索结果第一个视频
    item_first_video = (AppiumBy.XPATH,"//android.widget.GridView[@resource-id=\"tv.danmaku.bili:id/recycler_view\"]/android.view.ViewGroup[1]")

    icon_like = (AppiumBy.ID, "tv.danmaku.bili:id/like_icon")
    icon_fav = (AppiumBy.ID, "tv.danmaku.bili:id/favorite_icon")

    tab_comment = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"tv.danmaku.bili:id/tab_title\" and @text=\"评论\"]")
    bar_comment_input = (AppiumBy.ACCESSIBILITY_ID, "文本栏")
    ipt_comment_edit = (AppiumBy.ID, "tv.danmaku.bili:id/edit")
    btn_publish_comment = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"发布\"]")

    bar_danmu = (AppiumBy.XPATH,"//androidx.compose.ui.platform.ComposeView[@resource-id=\"tv.danmaku.bili:id/danmaku_input_parent\"]/android.view.View")
    ipt_danmu = (AppiumBy.ID, "tv.danmaku.bili:id/player_input_edit")
    btn_send_danmu = (AppiumBy.ID, "tv.danmaku.bili:id/player_input_send")

    def search_video(self, keyword):
        self.click(self.bar_search)
        self.input(self.ipt_search, keyword)
        self.click(self.btn_search_action)
        self.click(self.item_first_video)

    def interact_with_video(self, comment_text, danmu_text):
        print("点赞...")
        self.click(self.icon_like)
        print("收藏...")
        self.click(self.icon_fav)

        print("发布评论...")
        self.click(self.tab_comment)
        self.click(self.bar_comment_input)
        self.input(self.ipt_comment_edit, comment_text)
        self.click(self.btn_publish_comment)

        print("发送弹幕...")
        self.click(self.bar_danmu)
        self.input(self.ipt_danmu, danmu_text)
        self.click(self.btn_send_danmu)