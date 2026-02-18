from pages.login_page import LoginPage

def test_admin_login(page):
    login_page = LoginPage(page)
    login_page.go_to()

    login_page.login("admin@yourstore.com", "admin")
    page.wait_for_timeout(2000)

    assert login_page.is_logged_in()
    print("Успешный вход в админку")


def test_admin_wrong_password(page):
    login_page = LoginPage(page)
    login_page.go_to()

    login_page.login("admin@yourstore.com", "wrong_password")

    error_msg = page.locator('.message-error')
    assert error_msg.is_visible()
    assert "login was unsuccessful" in error_msg.text_content().lower()
    print("Неправильный пароль не пускает в админку")