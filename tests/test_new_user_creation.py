import time
from conftest import driver
from pages.admin_page import AdminPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.logger import logger
from selenium.webdriver.support.ui import WebDriverWait

#----------------------------TC05 CREATE NEW USER AND VALIDATE LOGIN ---------------------------------------------------
def test_new_user_creation(driver):
    driver.get("https://opensource-demo.orangehrmlive.com")
    try:
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        logger.info("Login Successful")

        dashboard = DashboardPage(driver)
        dashboard.open_menu("Admin")
        logger.info("Navigated to Admin Module")

        admin = AdminPage(driver)
        admin.click_add_button()
        logger.info("Clicked Add User button")

        username = f"d{int(time.time())}"
        password = "test@123"

        admin.select_user_role_admin()
        logger.info("User Role selected")

        admin.enter_employee_name("john")
        logger.info("Employee selected")

        admin.select_status_enabled()
        logger.info("Status selected")

        admin.enter_username(username)
        admin.enter_password(password)
        admin.enter_confirm_password(password)
        admin.click_save_button()
        logger.info("Clicked Save button")

        WebDriverWait(driver, 10).until(lambda d: "viewSystemUsers" in d.current_url)

        with open("test_data/created_user.txt", "w") as file:
            file.write(username)

        logger.info(f"User created successfully: {username}")
    except Exception as e:
        logger.error(f"TC05 - New User Creation Failed: {e}")
        driver.save_screenshot("screenshots/tc05_new_user_creation_failure.png")
        raise