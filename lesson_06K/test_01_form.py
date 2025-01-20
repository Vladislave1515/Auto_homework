from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input.form-control[name='first-name']"))).send_keys(
    "Иван")
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input.form-control[name='last-name']"))).send_keys(
    "Петров")
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input.form-control[name='address']"))).send_keys(
    "Ленина, 55-3")
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input.form-control[name='e-mail']"))).send_keys(
    "test@skypro.com")
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input.form-control[name='phone']"))).send_keys(
    "+798589998787")
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input.form-control[name='zip-code']"))).send_keys(
    "")
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input.form-control[name='city']"))).send_keys(
    "Москва")
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input.form-control[name='country']"))).send_keys(
    "Россия")
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input.form-control[name='job-position']"))).send_keys(
    "QA")
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input.form-control[name='company']"))).send_keys(
    "SkyPro")

wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))).click()

zip_code_field = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#zip-code.alert-danger")))
background_color = zip_code_field.value_of_css_property("background-color")
assert "rgba(248, 215, 218" in background_color

fields_to_check = ["first-name", "last-name", "address", "e-mail", "phone",
                   "city", "country", "job-position", "company"]
for field_name in fields_to_check:
    field = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, f"div.alert.py-2.alert-success[id='{field_name}']")))
    background_color = field.value_of_css_property("background-color")
    assert background_color == "rgba(209, 231, 221, 1)"

driver.quit()
