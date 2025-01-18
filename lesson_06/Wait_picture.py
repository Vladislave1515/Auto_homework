from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
        )

    wait = WebDriverWait(driver, 20)
    third_image = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img:nth-of-type(3)"))
    )

    third_image_src = third_image.get_attribute("src")
    print(third_image_src)

finally:
    driver.quit()
