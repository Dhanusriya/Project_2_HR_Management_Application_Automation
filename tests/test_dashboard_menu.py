import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.logger import logger

@pytest.mark.regression
#--------------------TC04 VERIFY VISIBILITY AND CLICKABILITY OF MENU ITEMS AFTER LOGIN ---------------------------------
def test_dashboard_menu(driver):
    driver.get("https://opensource-demo.orangehrmlive.com")
    try:
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        dashboard = DashboardPage(driver)
        menus = dashboard.get_all_menus()
        for menu in menus:
            driver.execute_script("arguments[0].scrollIntoView();", menu)
            assert menu.is_displayed()
            assert menu.is_enabled()

            logger.info(f"Verified Dashboard Menu: {menu.text}")
    except Exception as e:
        logger.error(f"TC04 Failed: {e}")
        driver.save_screenshot("screenshots/tc04_dashboard_menu_failure.png")
        raise