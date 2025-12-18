import pytest
import allure
from Appium.MyDemoApp.pages.login_page import LoginPage
from Appium.MyDemoApp.utils.file_reader import load_yaml_data

@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("用户登录模块")           #一级分类
@pytest.mark.usefixtures("driver")      # 使用装饰器，自动应用 conftest 中的 driver fixture
class TestLogin:
    @allure.story("登录功能点测试")         #二级分类

    @allure.title("测试系统登录功能")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("该测试用例 测试是使用等价类划分用例（有效类、无效类信息）来验证登录功能是否正确")

    @pytest.mark.parametrize("case_info", load_yaml_data("login_data.yaml"))        # 读取 yaml 数据进行参数化
    def test_login_scenarios(self, case_info):
        # 1. 实例化 Page 对象，去测试类里找一个叫 driver 的属性
        login_page = LoginPage(self.driver)

        # 2. 解析数据
        case_name = case_info['case_name']
        username = case_info['username']
        password = case_info['password']
        expected = case_info['expected']
        is_positive = case_info['is_positive']

        print(f"\n🚀 正在执行用例: {case_name}")
        print(f"   输入: 用户名={username}, 密码={password}")
        print(f"   预期结果: {expected}")

        # 3. 执行登录动作(内部已经有 @allure.step 了，报告会自动嵌套)
        login_page.login_action(username, password)

        # 4. 根据正向/反向用例，选择不同的断言逻辑
        if is_positive:
            with allure.step("正向用例断言"):
                actual = login_page.get_login_success_text()
                assert actual == expected , f"断言失败！期望是：{expected} ，但是实际却是：{actual}"
                login_page.logout_action()
        else:
            with allure.step("反向用例断言"):
                actual_text = login_page.is_error_message_exist(expected)
                assert actual_text == expected , f"断言失败！未在页面中找到预取报错：{expected}"

if __name__ == '__main__':
    pytest.main(["-vs", __file__])

