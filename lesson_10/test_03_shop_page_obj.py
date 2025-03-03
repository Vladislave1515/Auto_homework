import pytest
import allure
from selenium import webdriver
from pages_test03.LoginPage import LoginPage
from pages_test03.ProductsPage import ProductsPage
from pages_test03.CartPage import CartPage
from pages_test03.Check_infoPage import CheckInfoPage
from pages_test03.Check_viewPage import CheckViewPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест на покупку товаров")
@allure.description(
    "Этот тест проверяет сценарий покупки товаров в интернет-магазине."
    )
@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
def test_purchase_flow(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    check_info_page = CheckInfoPage(driver)
    check_view_page = CheckViewPage(driver)

    with allure.step("Открыть страницу входа"):
        login_page.open()

    with allure.step("Выполнить вход под пользователем 'standard_user'"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        products_page.add_items_to_cart()

    with allure.step("Перейти в корзину"):
        cart_page.go_to_cart()

    with allure.step("Начать оформление заказа"):
        cart_page.checkout()

    with allure.step("Ввести личную информацию"):
        check_info_page.enter_information("Влад", "Рыбас", "12345")

    with allure.step("Получить и проверить итоговую сумму заказа"):
        check_view_page.get_total()
