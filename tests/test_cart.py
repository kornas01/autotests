import pytest
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_add_product_to_cart_from_homepage(page):
    base_page = BasePage(page)
    base_page.go_to()

    products_count = base_page.get_products_count()
    assert products_count > 0, "Ошибка: на главной нет товаров"

    base_page.click_first_product()

    page.wait_for_timeout(2000)

    product_page = ProductPage(page)
    product_page.add_to_cart()

    print("Товар добавлен в корзину")


def test_add_multiple_quantity(page):
    base_page = BasePage(page)
    base_page.go_to()

    base_page.search_product("Nokia")

    page.wait_for_selector('.product-title a')

    page.locator('.product-title a').first.click()

    page.wait_for_timeout(2000)

    product_page = ProductPage(page)
    product_page.add_to_cart(quantity=3)

    page.wait_for_timeout(2000)

    message = product_page.get_success_message_text()
    assert "added" in message.lower(), f"Ошибка: не видно сообщения '{message}'"

    print("Добавлено 3 единицы товара")


def test_remove_from_cart(page):
    base_page = BasePage(page)
    base_page.go_to()
    base_page.click_first_product()

    page.wait_for_timeout(2000)

    product_page = ProductPage(page)
    product_page.add_to_cart()
    page.wait_for_timeout(10000)

    page.goto("https://demo.nopcommerce.com/cart")
    page.wait_for_timeout(3000)

    cart_page = CartPage(page)

    items_count = cart_page.get_items_count()
    print(f"Товаров в корзине: {items_count}")

    #if items_count == 0:
        #print("Корзина пустая - товар не добавился")
        #return

    cart_page.remove_item(0)
    page.wait_for_timeout(2000)

    print("Тест удаления выполнен")