from selenium import webdriver
from shop_pages import LoginPage, InventoryPage, CartPage, CheckoutPage


def test_saucedemo_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    total_price_text = ""

    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_item_to_cart("Sauce Labs Onesie")

        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form("Иван", "Иванов", "123456")

        total_price_text = checkout_page.get_total_price()

    finally:
        driver.quit()

    assert "$58.29" in total_price_text, (
        f"Ожидалась сумма $58.29, но на странице: '{total_price_text}'"
    )
