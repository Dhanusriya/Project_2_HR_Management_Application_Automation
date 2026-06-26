from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage
from pages.login_page import LoginPage
from utilities.logger import logger
from datetime import datetime, timedelta

#----------------------------TC09 ASIGN LEAVE AND VERIFY ASSIGNMENT ----------------------------------------------------
def test_assign_leave(driver):
    try:
        driver.get("https://opensource-demo.orangehrmlive.com")

        #Login
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        logger.info("Login Successful")

        #Open leave module
        dashboard = DashboardPage(driver)
        dashboard.open_menu("Leave")

        logger.info("Leave menu opened successfully")

        #Open assign leave page
        leave = LeavePage(driver)
        leave.open_assign_leave_link()

        logger.info("Assign Leave page opened successfully")

        #verify navigation
        assert "assignLeave" in driver.current_url

        #Filling up form
        leave.enter_employee_name("Baron Marong")
        leave.select_leave_type()

        from_date = datetime.today().strftime("%Y-%m-%d")
        to_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

        leave.enter_from_date(from_date)
        leave.enter_to_date(to_date)

        logger.info("Dates entered successfully")

        #Verify assign button exists
        assert leave.is_assign_button_displayed()

        logger.info("Assign button displayed")

        #click on assign button
        leave.click_assign_button()
        logger.info("Assign button clicked")

    except Exception as e:
        logger.error(f"Failed: {str(e)}")

        #screenshot for debugging
        driver.save_screenshot("screenshots/tc09_failure.png")
        raise