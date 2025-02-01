from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
