import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:
    """Page Object для страницы авторизации интернет-магазина Swag Labs."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует экземпляр страницы авторизации.

        :param driver: Экземпляр веб-драйвера Selenium (WebDriver).
        :return: None
        """
        self.driver = driver
        self._username_field = (By.CSS_SELECTOR, "#user-name")
        self._password_field = (By.CSS_SELECTOR, "#password")
        self._login_button = (By.CSS_SELECTOR, "#login-button")

    @allure.step("Авторизоваться под пользователем '{username}'")
    def login(self, username: str, password: str) -> None:
        """
        Вводит логин, пароль и нажимает кнопку входа.

        :param username: Имя пользователя для входа (str).
        :param password: Пароль пользователя (str).
        :return: None
        """
        self.driver.find_element(*self._username_field).send_keys(username)
        self.driver.find_element(*self._password_field).send_keys(password)
        self.driver.find_element(*self._login_button).click()


class InventoryPage:
    """Page Object для страницы каталога товаров."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует экземпляр страницы каталога.

        :param driver: Экземпляр веб-драйвера Selenium (WebDriver).
        :return: None
        """
        self.driver = driver
        self._cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_item_to_cart(self, item_name: str) -> None:
        """
        Находит кнопку добавления товара по его названию и нажимает её.

        :param item_name: Название товара из каталога (str).
        :return: None
        """
        button_id = f"add-to-cart-{item_name.lower().replace(' ', '-')}"
        self.driver.find_element(By.ID, button_id).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """
        Нажимает на иконку корзины для перехода на страницу заказа.

        :return: None
        """
        self.driver.find_element(*self._cart_button).click()


class CartPage:
    """Page Object для страницы корзины товаров."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует экземпляр страницы корзины.

        :param driver: Экземпляр веб-драйвера Selenium (WebDriver).
        :return: None
        """
        self.driver = driver
        self._checkout_button = (By.CSS_SELECTOR, "#checkout")

    @allure.step("Нажать кнопку 'Checkout' для оформления заказа")
    def click_checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа в корзине.

        :return: None
        """
        self.driver.find_element(*self._checkout_button).click()


class CheckoutPage:
    """Page Object для страницы оформления заказа и проверки итоговой суммы."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует экземпляр страницы оформления заказа.

        :param driver: Экземпляр веб-драйвера Selenium (WebDriver).
        :return: None
        """
        self.driver = driver
        self._first_name_field = (By.CSS_SELECTOR, "#first-name")
        self._last_name_field = (By.CSS_SELECTOR, "#last-name")
        self._postal_code_field = (By.CSS_SELECTOR, "#postal-code")
        self._continue_button = (By.CSS_SELECTOR, "#continue")
        self._total_label = (By.CSS_SELECTOR, ".summary_total_label")

    @allure.step(
        "Заполнить форму: {first_name} {last_name}, индекс {postal_code}"
    )
    def fill_checkout_form(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """
        Заполняет поля имени, фамилии, почтового индекса и нажимает 'Continue'.

        :param first_name: Имя покупателя (str).
        :param last_name: Фамилия покупателя (str).
        :param postal_code: Почтовый индекс (str).
        :return: None
        """
        self.driver.find_element(*self._first_name_field).send_keys(first_name)
        self.driver.find_element(*self._last_name_field).send_keys(last_name)
        self.driver.find_element(*self._postal_code_field).send_keys(
            postal_code
        )
        self.driver.find_element(*self._continue_button).click()

    @allure.step("Получить текст итоговой суммы заказа")
    def get_total_price(self) -> str:
        """
        Считывает и возвращает текст с итоговой стоимостью заказа.

        :return: Строка с итоговой суммой заказа (str).
        """
        return self.driver.find_element(*self._total_label).text
