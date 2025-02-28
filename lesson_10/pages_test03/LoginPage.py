from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        """
        Инициализирует объект класса LoginPage.

        :param driver: WebDriver instance
        """
        self.driver = driver

    def open(self) -> None:
        """
        Открывает страницу входа на веб-сайт.

        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход, заполняя поля имени пользователя и пароля,
        и нажимает кнопку "Login".

        :param username: Имя пользователя (str)
        :param password: Пароль (str)
        :return: None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
