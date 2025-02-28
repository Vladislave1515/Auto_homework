from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckViewPage:
    def __init__(self, driver):
        """
        Инициализирует объект класса CheckViewPage.

        :param driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def get_total(self) -> float:
        """
        Получает итоговую сумму из элемента на странице и проверяет
        ее на соответствие ожидаемой сумме.

        :return: Итоговая сумма (float)
        """
        total_element = self.wait.until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )
        total = total_element.text
        expected_total = "Total: $58.29"
        assert total == expected_total, (
            f"Ожидаемая сумма: {expected_total}, получилось: {total}"
        )
        return float(total.split("$")[1])
