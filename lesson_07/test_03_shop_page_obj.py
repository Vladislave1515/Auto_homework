import pytest
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


def test_purchase_flow(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    check_info_page = CheckInfoPage(driver)
    check_view_page = CheckViewPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_items_to_cart()
    cart_page.go_to_cart()

    cart_page.checkout()
    check_info_page.enter_information("Влад", "Рыбас", "12345")
    check_view_page.get_total()
