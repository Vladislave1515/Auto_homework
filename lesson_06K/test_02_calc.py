from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

wait = WebDriverWait(driver, 5)

delay_input = wait.until(EC.presence_of_element_located((By.ID, "delay")))
delay_input.clear()
delay_input.send_keys("45")

wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='calculator']/div[2]/span[1]"))).click()
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='calculator']/div[2]/span[4]"))).click()
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='calculator']/div[2]/span[2]"))).click()
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='calculator']/div[2]/span[15]"))).click()

result = WebDriverWait(driver, 46).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

result = driver.find_element(By.CLASS_NAME, "screen").text
assert result == "15", f"Ожидаемый результат = 15, но получил = {result}"

driver.quit()
