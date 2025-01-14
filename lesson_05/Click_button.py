from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

add_element_button = driver.find_element(By.CSS_SELECTOR,
                                         "button[onclick='addElement()']")
for _ in range(5):
    add_element_button.click()

delete_buttons = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")

print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

sleep(3)
driver.quit()
