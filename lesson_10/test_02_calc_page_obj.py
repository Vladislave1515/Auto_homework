import pytest
import allure
from selenium import webdriver
from pages_test02.MainPage import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест на работу калькулятора")
@allure.description("Этот тест проверяет работу калькулятора.")
@allure.feature("Работа калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_flow(driver):
    main_page = MainPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        main_page.open()

    with allure.step("Установить задержку в 2 секунды"):
        main_page.set_delay(2)

    with allure.step("Нажать кнопки на калькуляторе: 7, +, 8, ="):
        main_page.click_buttons(["7", "+", "8", "="])

    with allure.step("Ожидать результата 15"):
        main_page.wait_for_result("15")

    with allure.step("Получить и проверить результат 15"):
        main_page.get_result("15")
