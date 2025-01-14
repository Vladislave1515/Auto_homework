from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

try:
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    wait = WebDriverWait(driver, 10)
    close_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal-footer .close-button")))

    close_button.click()

finally:
    driver.quit()
