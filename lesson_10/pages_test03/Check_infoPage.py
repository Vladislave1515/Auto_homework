from selenium.webdriver.common.by import By


class CheckInfoPage:
    def __init__(self, driver):
        """
        Инициализирует объект класса CheckInfoPage.

        :param driver: WebDriver instance
        """
        self.driver = driver

    def enter_information(self, first_name: str,
                          last_name: str, postal_code: str) -> None:
        """
        Вводит информацию в поля формы и нажимает кнопку "Continue".

        :param first_name: Имя (str)
        :param last_name: Фамилия (str)
        :param postal_code: Почтовый индекс (str)
        :return: None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
