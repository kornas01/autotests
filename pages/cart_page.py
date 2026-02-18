from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.cart_items = page.locator('.cart-item-row')
        self.remove_buttons = page.locator('.remove-btn')

    def remove_item(self, item_index=0):
        try:
            if self.remove_buttons.count() > item_index:
                self.remove_buttons.nth(item_index).click()
                self.page.wait_for_timeout(1000)
                print("Товар удален")
                return True
            else:
                print("Кнопка удаления не найдена")
                return False
        except Exception as e:
            print(f"Ошибка при удалении товара: {e}")
            return False

    def get_items_count(self):
        return self.cart_items.count()

    def is_cart_empty(self):
        if self.cart_items.count() == 0:
            return True

        empty_cart = self.page.locator('.order-summary-content')
        if empty_cart.count() > 0:
            text = empty_cart.text_content()
            return "Your Shopping Cart is empty" in text
        return False