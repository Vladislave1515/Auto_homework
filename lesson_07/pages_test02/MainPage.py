from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_buttons(self, buttons):
        for button in buttons:
            self.driver.find_element(
                By.XPATH, f"//span[text()='{button}']").click()

    def wait_for_result(self, expected_result):
        WebDriverWait(self.driver, 47).until(
            EC.text_to_be_present_in_element((
                By.CLASS_NAME, "screen"), expected_result))

    def get_result(self, expected_result):
        result = self.driver.find_element(By.CLASS_NAME, "screen").text
        assert result == expected_result, f"Ожидаемый результат = {
            expected_result}, но получилось = {result}"
