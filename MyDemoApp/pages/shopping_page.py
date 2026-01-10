import allure
from appium.webdriver.common.appiumby import AppiumBy
from MyDemoApp.base.base_page import BasePage


class ShoppingPage(BasePage):
    # --- 1. 变量名语义化 ---
    # 首页列表页元素
    sort_btn = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc=\"sort button\"]/android.widget.ImageView")
    price_asc_opt = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"Price - Ascending\"]")
    first_product = (AppiumBy.XPATH,"(//android.view.ViewGroup[@content-desc=\"store item\"])[1]/android.view.ViewGroup[1]/android.widget.ImageView")
    fourth_product = (AppiumBy.XPATH,"(//android.view.ViewGroup[@content-desc=\"store item\"])[4]/android.view.ViewGroup[1]/android.widget.ImageView")

    # 商品详情页元素
    counter_plus_btn = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc=\"counter plus button\"]/android.widget.ImageView")
    add_to_cart_btn = (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button")
    cart_badge_icon = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc=\"cart badge\"]/android.widget.ImageView")

    # 购物车页元素
    checkout_btn = (AppiumBy.ACCESSIBILITY_ID, "Proceed To Checkout button")

    # 地址输入页元素
    full_name_input = (AppiumBy.ACCESSIBILITY_ID, "Full Name* input field")
    address_input = (AppiumBy.ACCESSIBILITY_ID, "Address Line 1* input field")
    city_input = (AppiumBy.ACCESSIBILITY_ID, "City* input field")
    zip_input = (AppiumBy.ACCESSIBILITY_ID, "Zip Code* input field")
    country_input = (AppiumBy.ACCESSIBILITY_ID, "Country* input field")
    to_payment_btn = (AppiumBy.ACCESSIBILITY_ID, "To Payment button")

    # 支付页元素
    payment_screen_title = (AppiumBy.XPATH, '//android.widget.TextView[@text="Enter a payment method"]')

    pay_fullname_input = (AppiumBy.ACCESSIBILITY_ID, "Full Name* input field")
    card_number_input = (AppiumBy.ACCESSIBILITY_ID, "Card Number* input field")
    expire_date_input = (AppiumBy.ACCESSIBILITY_ID, "Expiration Date* input field")
    security_code_input = (AppiumBy.ACCESSIBILITY_ID, "Security Code* input field")
    review_order_btn = (AppiumBy.ACCESSIBILITY_ID, "Review Order button")

    # 确认订单页元素
    place_order_btn = (AppiumBy.ACCESSIBILITY_ID, "Place Order button")
    continue_shopping_btn = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"Continue Shopping\"]")

    """
    将上述所有动作写在一起的话，如果只想测试“加入购物车”功能，不想测试支付，那么这个函数就没法复用了。
    如果支付失败了，很难快速定位是哪一步（虽然报错会提示行号，但逻辑上不清晰）。
    建议：将大动作拆分为以下几个方法：
    add_item_to_cart(): 负责排序、选商品、加购。
    go_to_checkout(): 负责点击购物车、点击去结算。
    fill_address_info(): 负责填收货地址。
    submit_payment(): 负责填卡号、支付、下单。
    """
    @allure.step("步骤一：排序并加购商品")
    def add_items_to_cart(self, start_x, end_x, y):
        """步骤1: 排序、选品、加购"""
        print("点击排序按钮...")
        self.click(self.sort_btn)
        print("选择价格升序...")
        self.click(self.price_asc_opt)

        print("加购第一个商品...")
        self.click(self.first_product)
        self.click(self.counter_plus_btn)
        self.click(self.counter_plus_btn)  # 点两次
        self.click(self.add_to_cart_btn)

        print("执行滑动操作返回列表...")
        self.swipe_left(start_x, end_x, y)

        print("加购第四个商品...")
        self.click(self.fourth_product)
        self.click(self.counter_plus_btn)
        self.click(self.counter_plus_btn)  # 点两次
        self.click(self.add_to_cart_btn)

    @allure.step("步骤二：进行购物车并结算")
    def go_to_checkout(self):
        """步骤2: 进入购物车并去结算"""
        print("点击购物车图标...")
        self.click(self.cart_badge_icon)
        print("点击去结算...")
        self.click(self.checkout_btn)

    @allure.step("步骤三：填写收货地址-{full_name}")
    def fill_address_info(self, full_name, address, city, zip_code, country):
        """步骤3: 填写收货地址"""
        print("填写收货地址信息...")
        self.input(self.full_name_input, full_name)
        self.input(self.address_input, address)
        self.input(self.city_input, city)
        self.input(self.zip_input, zip_code)
        self.input(self.country_input, country)

        print("点击去支付...")
        self.click(self.to_payment_btn)

    @allure.step("填写支付信息并下单")
    def submit_payment(self, full_name, card_num, expiration_date, security_code):
        """步骤4: 填写支付信息并下单"""
        print("等待支付页面加载(锚点检查)...")
        self.find_element(self.payment_screen_title)

        print("填写支付信息...")
        self.input(self.pay_fullname_input, full_name)
        self.input(self.card_number_input, card_num)
        self.input(self.expire_date_input, expiration_date)
        self.input(self.security_code_input, security_code)

        print("点击预览订单...")
        self.click(self.review_order_btn)
        self.click(self.review_order_btn)  # 原脚本点了两次，保持一致

        print("点击下单...")
        self.click(self.place_order_btn)

    @allure.step("步骤四：获取购物测试最终页面结果")
    def get_shopping_result(self):
        return self.get_text(self.continue_shopping_btn)