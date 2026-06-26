from selenium.webdriver.support.wait import WebDriverWait

from pages.admin_page import AdminPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.logger import logger

#------------------------------------TC06 VALIDATE NEWLY CREATED USER IN ADMIN USER LIST -------------------------------
def test_search_user(driver):
    driver.get("https://opensource-demo.orangehrmlive.com")
    try:
        login = LoginPage(driver)
        login.enter_username("admin")
        login.enter_password("admin123")
        login.click_login()
        logger.info("Login Successful")

        dashboard = DashboardPage(driver)
        dashboard.open_menu("Admin")
        logger.info("Navigated to Admin Module")

        with open("test_data/created_user.txt", "r") as file:
            username = file.read().strip()
        logger.info(f"Searching for User: {username}")

        admin = AdminPage(driver)
        admin.wait_for_admin_page()
        admin.search_user(username)

        assert admin.verify_user_exists(username)
        logger.info(f"User verified successfully: {username}")
    except Exception as e:
        logger.error(f"TC06 - Search User Validation Failed: {e}")
        driver.save_screenshot("screenshots/tc06_search_user_failure.png")
        raise