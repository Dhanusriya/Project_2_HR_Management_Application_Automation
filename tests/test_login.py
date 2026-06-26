import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.logger import logger
from utilities.excel_reader import get_login_data

@pytest.mark.login
@pytest.mark.smoke
@pytest.mark.parametrize("username,password,expected", get_login_data())

#---------------------------TC01 VALIDATE LOGIN FUNCTIONALITY USING MULTIPLE SETS OF CREDENTIALS------------------------
def test_login(driver, username, password, expected):
    driver.get("https://opensource-demo.orangehrmlive.com")
    try:
        login = LoginPage(driver)
        logger.info(f"Executing Login Test: {username}")
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        if expected == "Pass":
            WebDriverWait(driver, 15).until(lambda d: "dashboard" in driver.current_url)
            logger.info("Login Successful")
            dashboard = DashboardPage(driver)

            dashboard.logout()
            logger.info("Logout Successful")

        else:
            assert "Invalid" in login.get_invalid_message()
            logger.info("Invalid Login Verified")
    except Exception as e:
        logger.error(f"Login Test Failed: {e}")
        driver.save_screenshot("screenshots/login_test_failure.png")
        raise