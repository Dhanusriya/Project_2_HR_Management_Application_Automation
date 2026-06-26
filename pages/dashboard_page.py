from selenium.webdriver.common.by import By
from utilities.waits import Waits

class DashboardPage():
    profile_menu =(By.CLASS_NAME, "oxd-userdropdown-tab")
    logout_button = (By.CLASS_NAME, "oxd-userdropdown-link")
    all_menus = (By.CSS_SELECTOR, "span.oxd-main-menu-item--name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = Waits(driver)

    def logout(self):
        self.wait.clickable(self.profile_menu).click()
        self.wait.clickable(self.logout_button).click()

    def get_all_menus(self):
        return self.wait.visible_all(self.all_menus)

    def open_menu(self, menu_name):
        menus = self.get_all_menus()
        for menu in menus:
            if menu.text.strip() == menu_name:
                self.driver.execute_script("arguments[0].scrollIntoView();", menu)
                menu.click()
                return True
        return False
