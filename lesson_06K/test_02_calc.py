from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    # 1. Открываем страницу в Google Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

        # 2. В поле ввода по локатору #delay вводим значение 45
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        def click_button(text):
            button = driver.find_element(
                By.XPATH,
                f"//span[contains(@class, 'btn') and text()='{text}']"
            )
            button.click()

        # 3. Нажимаем на кнопки: 7, +, 8, =
        click_button("7")
        click_button("+")
        click_button("8")
        click_button("=")

        # 4. Проверяем, что в окне отобразится результат 15 через 45 секунд.
        wait = WebDriverWait(driver, 50)

        screen_locator = (By.CSS_SELECTOR, ".screen")

        wait.until(
            EC.text_to_be_present_in_element(screen_locator, "15")
        )

        final_text = driver.find_element(*screen_locator).text
        assert final_text == "15", (
            f"Ожидался результат 15, но получено: {final_text}"
        )

    finally:
        driver.quit()
