from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "newButtonName"))
)
input_field.send_keys("SkyPro")

blue_button = driver.find_element(By.ID, "updatingButton")
blue_button.click()

print(blue_button.text)

driver.quit()
