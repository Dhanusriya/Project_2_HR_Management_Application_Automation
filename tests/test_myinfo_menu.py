from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.myinfo_page import MyInfoPage
from utilities.logger import logger

#-----------------------------------------------TC08 VALIDATE MENU ITEMS UNDER 'MY INFO' -------------------------------
def test_myinfo_menu(driver):
    driver.get("https://opensource-demo.orangehrmlive.com")
    try:
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        logger.info("Login Successful")

        dashboard = DashboardPage(driver)
        dashboard.open_menu("My Info")
        logger.info("Navigated to My Info module")

        myinfo = MyInfoPage(driver)

        for item in myinfo.get_all_menu_items():
            assert item.is_displayed()
            assert item.is_enabled()
        logger.info("All My Info menu items are visible and enabled")

        expected_menus = [
            "Personal Details",
            "Contact Details",
            "Emergency Contacts",
            "Dependents",
            "Immigration",
            "Job",
            "Salary",
            "Report-to",
            "Qualifications",
            "Memberships"
        ]

        menus = myinfo.get_all_menu_items()
        menu_names = [menu.text.strip() for menu in menus]
        print("Menu names:", menu_names)

        for menu in expected_menus:
            menu_elements = myinfo.get_all_menu_items()

            for element in menu_elements:

                if element.text.strip() == menu:
                    print("Clicking:", menu)
                    element.click()
                    break
            logger.info(f"Verified menu: {menu}")
    except Exception as e:
        logger.error(f"TC08 - My Info Menu Validation Failed: {e}")
        driver.save_screenshot("screenshots/tc08_myinfo_menu_failure.png")
        raise