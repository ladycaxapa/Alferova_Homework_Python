import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для главной страницы калькулятора с задержкой вычислений."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует экземпляр страницы калькулятора.

        :param driver: Экземпляр веб-драйвера Selenium (WebDriver).
        :return: None
        """
        self.driver = driver
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._screen = (By.CSS_SELECTOR, ".screen")

    @allure.step("Установить задержку вычисления: {seconds} сек.")
    def set_delay(self, seconds: str) -> None:
        """
        Ожидает появления поля задержки, очищает его и вводит новое значение.

        :param seconds: Время задержки в секундах в виде строки (str).
        :return: None
        """
        delay_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._delay_input)
        )
        delay_field.clear()
        delay_field.send_keys(seconds)

    @allure.step("Нажать на кнопку '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """
        Находит кнопку калькулятора по её текстовому значению и кликает по ней.

        :param button_text: Текст или символ на кнопке калькулятора (str).
        :return: None
        """
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    @allure.step(
        "Ожидать результат '{expected_text}' (таймаут: {timeout} сек.)"
    )
    def get_result_with_wait(self, expected_text: str, timeout: int) -> str:
        """
        Ожидает появления ожидаемого текста и возвращает его.

        :param expected_text: Ожидаемый текст результата на экране (str).
        :param timeout: Максимальное время ожидания в секундах (int).
        :return: Текст, отображаемый на экране калькулятора (str).
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._screen, expected_text)
        )
        return self.driver.find_element(*self._screen).text
