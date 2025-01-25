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


def test_form_submission_flow(driver):
    wait = WebDriverWait(driver, 5)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    fields = {
        'first-name': "Иван",
        'last-name': "Петров",
        'address': "Ленина, 55-3",
        'zip-code': "",
        'city': "Москва",
        'country': "Россия",
        'e-mail': "test@skypro.com",
        'phone': "+7985899998787",
        'job-position': "QA",
        'company': "SkyPro"
    }

    for field, value in fields.items():
        driver.find_element(
            By.NAME, field).send_keys(value)

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[type="submit"]'))).click()

    assert "alert-danger" in driver.find_element(
        By.ID, "zip-code").get_attribute("class")

    for field in ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']:
        assert "success" in driver.find_element(
            By.ID, field).get_attribute("class")
