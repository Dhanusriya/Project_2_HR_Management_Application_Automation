import time
from utilities.logger import logger
from pages.claim_page import ClaimPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

#--------------------------------TC10 INITIATE A CLAIM REQUEST ---------------------------------------------------------
def test_submit_claim(driver):
    driver.get("https://opensource-demo.orangehrmlive.com")

    login = LoginPage(driver)
    login.enter_username("Admin1")
    login.enter_password("testing123")
    login.click_login()

    dashboard = DashboardPage(driver)
    dashboard.open_menu("Claim")

    claim = ClaimPage(driver)
    claim.open_submit_claim()
    remarks = f"Claim_{int(time.time())}"

    try:
        claim.select_event()
        print("Event selected")
        claim.select_currency()
        print("Currency selected")

        claim.enter_remarks(remarks)

        logger.info("Claim details entered")

        claim.click_create()

        claim.wait.visibility(claim.my_claims_tab)

        logger.info("Claim created successfully")

    except Exception as e:
        logger.error(f"Claim creation failed: {e}")
        driver.save_screenshot("screenshots/tc10_creation_failure.png")
        raise

    try:
        claim.open_my_claims()
        assert claim.verify_claim_exists()
        logger.info("Claim found in My Claims table")

    except Exception as e:
        logger.error(f"Claim verification failed: {e}")
        driver.save_screenshot("screenshots/tc10_verification_failure.png")
        raise