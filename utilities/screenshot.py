from datetime import datetime
import os

def take_screenshot(driver, test_name):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    return filename