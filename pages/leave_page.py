from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from utilities.waits import Waits


class LeavePage:
    assign_leave_tab = (By.XPATH, "//a[text()='Assign Leave']")
    employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
    employee_option = (By.XPATH, "//div[@role='option']")
    leave_type_dropdown = (By.XPATH, "//label[text()='Leave Type']/following::div[contains(@class,'oxd-select-text')][1]")
    leave_type_option = (By.XPATH, "(//div[@role='option'])[1]")
    from_date = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
    to_date = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
    assign_button = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = Waits(driver)

    def open_assign_leave_link(self):
        self.wait.clickable(self.assign_leave_tab).click()

    def enter_employee_name(self, name):
        field = self.wait.visibility(self.employee_name)
        field.clear()
        field.send_keys(name)
        try:
            self.wait.clickable(self.employee_option).click()
        except Exception:
            field.send_keys(Keys.ARROW_DOWN)
            field.send_keys(Keys.ENTER)

    def select_leave_type(self):
        self.wait.clickable(self.leave_type_dropdown).click()
        self.wait.clickable(self.leave_type_option).click()

    def enter_from_date(self, date):
        field = self.wait.visibility(self.from_date)
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(str(date))

    def enter_to_date(self, date):
        field = self.wait.visibility(self.to_date)
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(str(date))

    def click_assign_button(self):
        self.wait.clickable(self.assign_button).click()

    def is_assign_button_displayed(self):
        return self.wait.visibility(self.assign_button).is_displayed()