import pytest
import allure

import sys,os
# 将项目根目录添加到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from Appium.MyDemoApp.pages.shopping_page import ShoppingPage

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("商品购物模块")               #一级分类
@pytest.mark.usefixtures("driver")
class TestShopping:
    @allure.story("购物下单全流程")             #二级分类
    @allure.title("测试用户从加购到支付成功的完整路径")
    @allure.description("该测试用例测试的是 MyDemoApp 中添加购物车、填写地址信息、结算账单的完整购物流程")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shopping_flow(self):
        # 1. 初始化页面对象 (使用 self.driver)
        shopping_page = ShoppingPage(self.driver)

        # 2. 加购商品（下面的方法调用都会在报告里显示为单独的 Step）
        shopping_page.add_items_to_cart(start_x=1273, end_x=52, y=1548)

        # 3. 去结算
        shopping_page.go_to_checkout()

        # 4. 填写地址
        shopping_page.fill_address_info(
            full_name="zhang san",
            address="dsabkjcgsafvcjhafvq",
            city="china",
            zip_code="464400",
            country="china"
        )

        # 5. 支付下单
        shopping_page.submit_payment(
            full_name="li si",
            card_num="1234567890",
            expiration_date="0725",
            security_code="999"
        )

        # 6. 断言，可以在 assert 后面加上自定义报错信息，这样报告更易读
        with allure.step("最终结果断言"):
            result = shopping_page.get_shopping_result()
            # 逗号后面的文字，只有在断言失败时才会显示在报告中
            assert result == "Continue Shopping", f"断言失败！预期是 'Continue Shopping'，但实际获取到的是: {result}"


if __name__ == '__main__':
    pytest.main(["-vs", __file__])
