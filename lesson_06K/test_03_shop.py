from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_checkout():
    # 1. Открываем сайт магазина в Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()

    total_text = ""

    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)

        # 2. Авторизуемся как пользователь standard_user
        wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys(
            "standard_user"
        )
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 3. Добавляем в корзину товары
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

        # 4. Переходим в корзину
        driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()

        # 5. Нажимаем Checkout
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        ).click()

        # 6. Заполняем форму своими данными
        wait.until(
            EC.presence_of_element_located(
                (By.ID, "first-name")
            )
        ).send_keys("Алена")
        driver.find_element(
            By.ID, "last-name"
        ).send_keys("Алфёрова")
        driver.find_element(
            By.ID, "postal-code"
        ).send_keys("627350")

        # 7. Нажимаем кнопку Continue
        driver.find_element(By.ID, "continue").click()

        # 8. Прочитываем со страницы итоговую стоимость (Total)
        total_element = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_text = total_element.text  # Текст "Total: $58.29"

    finally:
        driver.quit()

    # 10. Проверяем, что итоговая сумма равна $58.29
    assert "Total: $58.29" in total_text, (
        f"Ожидалась сумма $58.29, но на странице: '{total_text}'"
    )
