import pytest
import allure
from selenium import webdriver
from pages_test01.FormPage import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест на отправку формы")
@allure.description("Этот тест проверяет процесс отправки формы.")
@allure.feature("Отправка формы")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(driver):
    form_page = FormPage(driver)

    with allure.step("Открыть страницу формы"):
        form_page.open()

    with allure.step("Заполнить форму"):
        form_page.fill_form()

    with allure.step("Отправить форму"):
        form_page.submit_form()

    with allure.step("Проверить отправку формы"):
        form_page.check_form_submission()
