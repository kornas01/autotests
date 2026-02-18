from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_to_cart_button = page.locator('.add-to-cart-button').first

    def add_to_cart(self, quantity=1):
        if quantity > 1:
            # Находим поле с количеством и вводим нужное число
            quantity_input = self.page.locator('.qty-input')
            quantity_input.fill(str(quantity))

        self.add_to_cart_button.click()
        print(f"Нажали кнопку 'Add to cart' (количество: {quantity})")
    def get_product_name(self):
        try:
            # Просто ищем название товара в заголовке
            product_name = self.page.locator('.product-name h1').first
            return product_name.text_content()
        except:
            return "Неизвестный товар"
    def get_success_message_text(self):
        try:
            self.page.wait_for_selector('.bar-notification', timeout=10000)

            notification = self.page.locator('.bar-notification').first
            message = notification.text_content()

            return message
        except:
            # Если сообщение не появилось
            print("Сообщение не появилось")
            return ""
    def close_success_message(self):
        try:
            # Ищем кнопку "X" и нажимаем её
            close_button = self.page.locator('.bar-notification .close').first
            close_button.click()
            print("Закрыли сообщение")
        except:
            pass