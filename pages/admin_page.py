from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilities.waits import Waits

class AdminPage:
    add_button = (By.XPATH, "//button[normalize-space()='Add']")
    save_button = (By.XPATH, "//button[@type='submit']")
    username = (By.XPATH, "(//input[contains(@class,'oxd-input')])[2]")
    password = (By.XPATH, "(//input[@type='password'])[1]")
    confirm_password = (By.XPATH, "(//input[@type='password'])[2]")
    employee_name = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    employee_option = (By.XPATH, "//div[@role='option']//span")
    user_role_dropdown = (
        By.XPATH,
        "//label[normalize-space()='User Role']/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text')]",
    )
    status_dropdown = (
        By.XPATH,
        "//label[normalize-space()='Status']/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text')]",
    )
    admin_role_option = (By.XPATH, "//div[@role='option']//span[normalize-space()='Admin']")
    enabled_status_option = (By.XPATH, "//div[@role='option']//span[normalize-space()='Enabled']")

    search_username = (By.XPATH, "//label[text()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    result_table = (By.XPATH, "//div[@class='oxd-table-body']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = Waits(driver)

    def click_add_button(self):
        self.wait.clickable(self.add_button).click()

    def enter_username(self, username):
        self.wait.visibility(self.username).send_keys(username)

    def enter_password(self, password):
        self.wait.visibility(self.password).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.wait.visibility(self.confirm_password).send_keys(confirm_password)

    def enter_employee_name(self, employee_name):
        field = self.wait.visibility(self.employee_name)
        field.clear()
        field.send_keys(employee_name)

        try:
            self.wait.clickable(self.employee_option).click()
        except Exception:
            field.send_keys(Keys.ARROW_DOWN)
            field.send_keys(Keys.ENTER)

    def select_user_role_admin(self):
        self.wait.clickable(self.user_role_dropdown).click()
        self.wait.clickable(self.admin_role_option).click()

    def select_status_enabled(self):
        self.wait.clickable(self.status_dropdown).click()
        self.wait.clickable(self.enabled_status_option).click()

    def click_save_button(self):
        self.wait.clickable(self.save_button).click()

    def search_user(self, username):
        field = self.wait.visibility(self.search_username)
        field.clear()
        field.send_keys(username)
        self.wait.clickable(self.search_button).click()

        # Wait until the results table is refreshed
        self.wait.visibility(self.result_table)

    def verify_user_exists(self, username):
        table = self.wait.visibility(self.result_table)

        print("TABLE CONTENT:")
        print(table.text)

        return username in table.text

    def wait_for_admin_page(self):
        self.wait.clickable(self.add_button)