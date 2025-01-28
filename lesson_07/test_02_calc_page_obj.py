import pytest
from selenium import webdriver
from pages_test02.MainPage import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_flow(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.set_delay(45)
    main_page.click_buttons(["7", "+", "8", "="])
    main_page.wait_for_result("47")
    main_page.get_result("15")
