class RegisterPage:

    def __init__(self, page):
        self.page = page

        self.gender_male = page.locator('#gender-male')
        self.gender_female = page.locator('#gender-female')

        self.first_name = page.locator('#FirstName')
        self.last_name = page.locator('#LastName')
        self.email = page.locator('#Email')
        self.password = page.locator('#Password')
        self.confirm_password = page.locator('#ConfirmPassword')

        self.register_button = page.locator('#register-button')

        self.result_message = page.locator('.result')

    def go_to(self):
        self.page.goto('https://demo.nopcommerce.com/register')

    def register_user(self, first_name, last_name, email, password):
        self.gender_female.click()

        # Заполняем поля
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.email.fill(email)
        self.password.fill(password)
        self.confirm_password.fill(password)

        self.register_button.click()

    def get_success_message(self):
        if self.result_message.is_visible():
            return self.result_message.text_content()
        return ""