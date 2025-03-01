from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        """
        Инициализирует объект класса CartPage.

        :param driver: WebDriver instance
        """
        self.driver = driver

    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.

        :return: None
        """
        self.driver.find_element(By.ID, "shopping_cart_container").click()

    def checkout(self) -> None:
        """
        Нажимает кнопку для начала процесса оформления заказа.

        :return: None
        """
        self.driver.find_element(By.ID, "checkout").click()
