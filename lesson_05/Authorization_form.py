from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

try:
    driver.get("http://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located(
        (By.ID, "username")))

    username_field.send_keys("tomsmith")

    password_field = wait.until(EC.presence_of_element_located(
        (By.ID, "password")))

    password_field.send_keys("SuperSecretPassword!")

    login_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.radius")))
    login_button.click()

finally:
    driver.quit()
