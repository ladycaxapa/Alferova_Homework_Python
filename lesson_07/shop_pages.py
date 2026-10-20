from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self._username_field = (By.CSS_SELECTOR, "#user-name")
        self._password_field = (By.CSS_SELECTOR, "#password")
        self._login_button = (By.CSS_SELECTOR, "#login-button")

    def login(self, username, password):
        self.driver.find_element(*self._username_field).send_keys(username)
        self.driver.find_element(*self._password_field).send_keys(password)
        self.driver.find_element(*self._login_button).click()


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self._cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_item_to_cart(self, item_name: str):
        button_id = f"add-to-cart-{item_name.lower().replace(' ', '-')}"
        self.driver.find_element(By.ID, button_id).click()

    def go_to_cart(self):
        self.driver.find_element(*self._cart_button).click()


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self._checkout_button = (By.CSS_SELECTOR, "#checkout")

    def click_checkout(self):
        self.driver.find_element(*self._checkout_button).click()


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self._first_name_field = (By.CSS_SELECTOR, "#first-name")
        self._last_name_field = (By.CSS_SELECTOR, "#last-name")
        self._postal_code_field = (By.CSS_SELECTOR, "#postal-code")
        self._continue_button = (By.CSS_SELECTOR, "#continue")
        self._total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_checkout_form(
        self, first_name: str, last_name: str, postal_code: str
    ):
        self.driver.find_element(*self._first_name_field).send_keys(first_name)
        self.driver.find_element(*self._last_name_field).send_keys(last_name)
        self.driver.find_element(*self._postal_code_field).send_keys(
            postal_code
        )
        self.driver.find_element(*self._continue_button).click()

    def get_total_price(self) -> str:
        return self.driver.find_element(*self._total_label).text
