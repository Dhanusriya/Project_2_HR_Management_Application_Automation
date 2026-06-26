from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.waits import Waits

class MyInfoPage:

    menu_items = (By.CSS_SELECTOR, "a.orangehrm-tabs-item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = Waits(driver)

    def get_all_menu_items(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.menu_items))
        return self.driver.find_elements(*self.menu_items)