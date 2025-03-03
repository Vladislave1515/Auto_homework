from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        """
        Инициализирует объект класса ProductsPage.

        :param driver: WebDriver instance
        """
        self.driver = driver
        self.items = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

    def add_items_to_cart(self) -> None:
        """
        Добавляет товары из списка в корзину.

        :return: None
        """
        for item in self.items:
            self.driver.find_element(By.ID, item).click()
