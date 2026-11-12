import allure
from selenium import webdriver
from shop_pages_allure import LoginPage, InventoryPage, CartPage, CheckoutPage


@allure.title("Оформление заказа в Swag Labs и проверка суммы ($58.29)")
@allure.description(
    "Тест выполняет вход, добавляет три товара в корзину, "
    "заполняет форму заказа и проверяет, что итоговая сумма $58.29."
)
@allure.feature("Интернет-магазин (Оформление заказа)")
@allure.severity(allure.severity_level.BLOCKER)
def test_saucedemo_shop() -> None:
    with allure.step("Запустить браузер Firefox и развернуть окно"):
        driver = webdriver.Firefox()
        driver.maximize_window()

    total_price_text = ""

    try:
        with allure.step("Открыть главную страницу магазина Swag Labs"):
            driver.get(("https://www.saucedemo.com/"))

        with allure.step("Авторизоваться под пользователем 'standard_user'"):
            login_page = LoginPage(driver)
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить 3 товара в корзину и перейти в неё"):
            inventory_page = InventoryPage(driver)
            inventory_page.add_item_to_cart("Sauce Labs Backpack")
            inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
            inventory_page.add_item_to_cart("Sauce Labs Onesie")
            inventory_page.go_to_cart()

        with allure.step("Перейти к оформлению заказа (Checkout)"):
            cart_page = CartPage(driver)
            cart_page.click_checkout()

        with allure.step("Заполнить форму доставки и получить итоговую сумму"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_checkout_form("Иван", "Иванов", "123456")
            total_price_text = checkout_page.get_total_price()

    finally:
        with allure.step("Закрыть браузер"):
            driver.quit()

    with allure.step("Проверить, что итоговая сумма заказа '$58.29'"):
        assert "$58.29" in total_price_text, (
            f"Ожидалась сумма $58.29, но на странице: '{total_price_text}'"
        )
