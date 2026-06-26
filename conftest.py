import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.logger import logger

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.passed:
            logger.info(f"{item.name} passed")
        elif report.failed:
            logger.info(f"{item.name} failed")