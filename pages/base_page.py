class BasePage:

    def __init__(self, page):
        self.page = page
        self.search_box = page.locator('#small-searchterms')
        self.search_button = page.locator('button:has-text("Search")')
        self.product_title = page.locator('.product-title a')
        self.register_link = page.locator('a:has-text("Register")')
        self.login_link = page.locator('a:has-text("Log in")')
        self.cart_link = page.locator('a:has-text("Shopping cart")').first
        self.info_links = page.locator('.footer a')

    def go_to(self):
        self.page.goto('https://demo.nopcommerce.com/')

    def search_product(self, product_name):
        self.search_box.fill(product_name)
        self.search_button.click()

    def get_search_results_text(self):
        return self.product_title.first.text_content()

    def click_register(self):
        self.register_link.click()

    def click_login(self):
        self.login_link.click()

    def get_cart_count(self):
        try:
            cart_text = self.cart_link.text_content()
            print(f"Текст корзины: {cart_text}")  # для отладки

            import re
            numbers = re.findall(r'\d+', cart_text)
            if numbers:
                return int(numbers[0])
            return 0
        except:
            print("Не удалось получить количество товаров в корзине")
            return 0