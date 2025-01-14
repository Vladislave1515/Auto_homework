from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    wait = WebDriverWait(driver, 15)
    input_field = wait.until(EC.presence_of_element_located(
        (By.TAG_NAME, "input")))

    input_field.send_keys("1000")
    input_field.clear()
    input_field.send_keys("999")

finally:
    driver.quit()
