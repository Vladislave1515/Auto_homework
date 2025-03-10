from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        """
        Инициализирует объект класса FormPage.

        :param driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    def open(self) -> None:
        """
        Открывает веб-страницу.

        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )

    def fill_form(self) -> None:
        """
        Заполняет форму значениями из словаря fields.

        :return: None
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    def submit_form(self) -> None:
        """
        Нажимает кнопку отправки формы.

        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]'))).click()

    def get_field_class(self, field_id: str) -> str:
        """
        Возвращает значение атрибута "class" для указанного элемента.

        :param field_id: ID элемента
        :return: значение атрибута "class"
        """
        element = self.wait.until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        return element

    def check_zip_code_error(self) -> bool:
        """
        Проверяет, есть ли ошибка в поле "zip-code".

        :return: True, если ошибка есть, иначе False
        """
        return "alert-danger" in self.get_field_class("zip-code")

    def check_fields_success(self) -> bool:
        """
        Проверяет, что все поля формы успешно заполнены.

        :return: True, если все поля заполнены успешно, иначе False
        """
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    def check_form_submission(self) -> None:
        """
        Проверяет, что форма отправлена успешно и все поля заполнены корректно.

        :return: None
        """
        assert self.check_zip_code_error()
        assert self.check_fields_success()
