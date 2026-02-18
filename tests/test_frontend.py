import pytest
import random
import string
from pages.base_page import BasePage
from pages.register_page import RegisterPage


def test_homepage_title(page):
    base_page = BasePage(page)
    base_page.go_to()

    assert "nopCommerce" in page.title()
    print("Заголовок главной страницы правильный")


def test_search_product(page):
    base_page = BasePage(page)
    base_page.go_to()

    base_page.search_product("Nokia")
    page.wait_for_selector('.product-title a')

    result_text = base_page.get_search_results_text()
    assert "Nokia" in result_text
    print(f"Нашли товар: {result_text}")


def test_navigation_links(page):
    base_page = BasePage(page)
    base_page.go_to()

    base_page.click_register()
    assert "register" in page.url
    print("Ссылка на регистрацию работает")

    page.go_back()

    base_page.click_login()
    assert "login" in page.url
    print("Ссылка на авторизацию работает")


def test_cart_is_empty_at_start(page):
    base_page = BasePage(page)
    base_page.go_to()

    page.wait_for_timeout(2000)

    cart_count = base_page.get_cart_count()
    print(f"Количество товаров в корзине: {cart_count}")

    assert cart_count == 0, f"Корзина не пустая: {cart_count} товаров"
    print("Корзина пустая")


def test_footer_has_links(page):
    base_page = BasePage(page)
    base_page.go_to()

    links_count = base_page.info_links.count()
    assert links_count > 10
    print(f"В подвале {links_count} ссылок")


def test_successful_registration(page):
    register_page = RegisterPage(page)
    register_page.go_to()

    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    email = f"{random_string}@test.com"

    register_page.register_user(
        first_name="Nastya",
        last_name="Testova",
        email=email,
        password="qwerty123!"
    )

    page.wait_for_timeout(2000)

    success_message = register_page.get_success_message()
    assert "completed" in success_message.lower()
    print(f"Пользователь {email} успешно зарегистрирован")
