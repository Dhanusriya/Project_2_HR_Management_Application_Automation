import pytest
from pages.login_page import LoginPage
from utilities.logger import logger

#--------------------------------------TC03 VALIDATE PRESENCE OF LOGIN FIELDS ------------------------------------------
@pytest.mark.smoke
def test_login_fields(driver):
    driver.get("https://opensource-demo.orangehrmlive.com")
    try:
        login = LoginPage(driver)
        assert login.is_username_displayed()
        logger.info("Username field is displayed")

        assert login.is_password_displayed()
        logger.info("Password field is displayed")

        assert login.username_enabled()
        logger.info("Username field is enabled")

        assert login.password_enabled()
        logger.info("Password field is enabled")

        logger.info("Username and Password fields are visible and enabled")
    except Exception as e:
        logger.error(f"TC03 - Login Fields Validation Failed: {e}")
        driver.save_screenshot("screenshots/tc03_login_fields_failure.png")
        raise