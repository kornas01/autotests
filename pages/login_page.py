class LoginPage:

    def __init__(self, page):
        self.page = page
        self.email_input = page.locator('#Email')
        self.password_input = page.locator('#Password')
        self.login_button = page.locator('button:has-text("Log in")')
        self.logout_link = page.locator('a:has-text("Logout")')

    def go_to(self):
        self.page.goto('https://admin-demo.nopcommerce.com/')

    def login(self, email, password):
        self.email_input.clear()
        self.email_input.fill(email)

        self.password_input.clear()
        self.password_input.fill(password)

        self.login_button.click()

    def is_logged_in(self):
        return self.logout_link.is_visible()