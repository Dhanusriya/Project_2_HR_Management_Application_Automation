from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.waits import Waits

class ClaimPage:
    submit_claim_tab = (By.XPATH, "//a[normalize-space()='Submit Claim']")
    my_claims_tab = (By.XPATH, "//a[normalize-space()='My Claims']")
    event_dropdown = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]")
    accommodation_option = (By.XPATH, "//span[text()='Accommodation']")
    currency_dropdown = (By.XPATH,
        "//label[contains(text(),'Currency')]/ancestor::div[contains(@class,'oxd-grid-item')]//div[contains(@class,'oxd-select-text')]")
    indian_rupee_option = (By.XPATH,"//div[@role='option']//span[contains(.,'Indian Rupee')]")
    remarks_text_area = (By.XPATH, "//textarea")
    create_button = (By.XPATH, "//button[@type='submit']")
    claims_table = (By.XPATH, "//div[contains(@class,'oxd-table-body')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = Waits(driver)

    def open_submit_claim(self):
        self.wait.clickable(self.submit_claim_tab).click()

    def select_event(self):
        self.wait.clickable(self.event_dropdown).click()

        accommodation = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@role='option']//span[text()='Accommodation']")))
        accommodation.click()

    def select_currency(self):
        self.wait.clickable(self.currency_dropdown).click()

        try:
            self.wait.clickable(self.indian_rupee_option).click()
        except Exception as e:
            print("ERROR:", e)

    def enter_remarks(self, remarks):
        self.wait.visibility(self.remarks_text_area).send_keys(remarks)

    def click_create(self):
        self.wait.clickable(self.create_button).click()

    def open_my_claims(self):
        self.wait.clickable(self.my_claims_tab).click()

    def verify_claim_exists(self):
        table = self.wait.visibility(self.claims_table)
        return "Accommodation" in table.text