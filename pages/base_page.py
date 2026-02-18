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
        self.product_boxes = page.locator('.product-item')

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

    def go_to_cart(self):
        """Перейти в корзину"""
        self.cart_link.click()

    def click_first_product(self):
        """Кликнуть на первый товар на главной"""
        #if self.product_boxes.count() > 0:
           # self.product_boxes.first.click()
           # return True
        #return False
        """Кликнуть на второй товар на главной, тк в первом товаре слишком много обязательных кнопок"""
        if self.product_boxes.count() > 1:
            self.product_boxes.nth(1).click()  # Индексация начинается с 0
            return True
        return False

    def get_products_count(self):
        """Получить количество товаров на главной"""
        return self.product_boxes.count()
