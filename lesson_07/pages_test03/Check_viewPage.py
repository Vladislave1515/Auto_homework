from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckViewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def get_total(self):
        total_element = self.wait.until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text
