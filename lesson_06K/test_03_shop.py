import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_purchase_flow(driver):
    wait = WebDriverWait(driver, 5)

    driver.get("https://www.saucedemo.com/")
    wait.until(EC.presence_of_element_located(
        (By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    items = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for item in items:
        wait.until(EC.element_to_be_clickable((By.ID, item))).click()

    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Влад")
    driver.find_element(By.ID, "last-name").send_keys("Рыбас")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    total_element = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "summary_total_label")))
    total = total_element.text

    driver.quit()

    assert total == "Total: $58.29", f"Ожидаемая сумма: $58,29, получилось {
        total
        }"
