import pytest
from selenium import webdriver
from pages_test01.FormPage import FormPage
from pages_test01.SubmittedPage import SubmittedPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    submitted_page = SubmittedPage(driver)
    assert submitted_page.check_zip_code_error()
    assert submitted_page.check_fields_success()
