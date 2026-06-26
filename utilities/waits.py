from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Waits:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 20)

    def visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def visible_all(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
