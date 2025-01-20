from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver, 5)

username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
username.send_keys("standard_user")
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']"))).click()
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']"))).click()

cart = driver.find_element(By.ID, "shopping_cart_container")
cart.click()

checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
checkout_button.click()

first_name = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
first_name.send_keys("Влад")
last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Рыбас")
postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("12345")

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

total_element = wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, "summary_total_label")))
total = total_element.text

driver.quit()

assert total == "Total: $58.29", f"Ожидаемая сумма: $58,29, получилось {total}"
