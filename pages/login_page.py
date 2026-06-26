from selenium.webdriver.common.by import By
from utilities.waits import Waits


class LoginPage:
    username_box = (By.NAME, "username")
    password_box = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    error_message = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")
    login_title = (By.XPATH, "//h5[text()='Login']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = Waits(driver)

    def enter_username(self, username):
        self.wait.visibility(self.username_box).send_keys(username)

    def enter_password(self, password):
        self.wait.visibility(self.password_box).clear()
        self.wait.visibility(self.password_box).send_keys(password)

    def click_login(self):
        self.wait.clickable(self.login_button).click()

    def get_invalid_message(self):
        return self.wait.visibility(self.error_message).text

    def is_login_page_displayed(self):
        return self.wait.visibility(self.login_title).is_displayed()

    def is_username_displayed(self):
        return self.wait.visibility(self.username_box).is_displayed()

    def is_password_displayed(self):
        return self.wait.visibility(self.password_box).is_displayed()

    def username_enabled(self):
        return self.wait.visibility(self.username_box).is_enabled()

    def password_enabled(self):
        return self.wait.visibility(self.password_box).is_enabled()