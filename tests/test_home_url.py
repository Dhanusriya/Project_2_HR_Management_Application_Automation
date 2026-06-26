import pytest
from pages.login_page import LoginPage
from utilities.logger import logger

#-------------------------------TC02 VERIFY HOME PAGE URL IS ACCESSIBLE ------------------------------------------------
@pytest.mark.smoke
def test_home_url(driver):
    driver.get("https://opensource-demo.orangehrmlive.com")
    try:
        login = LoginPage(driver)
        assert "auth/login" in driver.current_url
        logger.info("Verified Home URL")

        assert (login.is_login_page_displayed())
        logger.info("Login page displayed successfully")

        logger.info("Home URL Loaded Successfully")
    except Exception as e:
        logger.error(f"TC01 - Home URL Validation Failed: {e}")
        driver.save_screenshot("screenshots/tc01_home_url_failure.png")
        raise