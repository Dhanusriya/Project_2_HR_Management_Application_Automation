from selenium.webdriver.common.by import By

from utilities.waits import Waits


class ForgotPasswordPage:
    forgot_password_link = (By.CLASS_NAME, "orangehrm-login-forgot")
    username_field = (By.NAME, "username")
    reset_button = (By.XPATH, "//button[@type='submit']")
    success_message = (
        By.XPATH,
        "//h6[text()='Reset Password link sent successfully']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = Waits(driver)

    def click_forgot_password(self):
        self.wait.clickable(self.forgot_password_link).click()

    def enter_username(self, username):
        self.wait.visibility(self.username_field).send_keys(username)

    def click_reset_password_button(self):
        self.wait.clickable(self.reset_button).click()

    def get_success_message(self):
        return self.wait.visibility(self.success_message).text