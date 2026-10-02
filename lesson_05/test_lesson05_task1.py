from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():

    driver = webdriver.Chrome()

    try:
        # Шаг 1: Открываем страницу
        driver.get("https://httpbin.qa-territory.online")

        # Шаг 2: Находим и кликаем на ссылку HTML Form
        html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
        html_form_link.click()

        # Шаг 3: Проверяем, что URL изменился на /forms/post
        expected_form_url = "https://httpbin.qa-territory.online/forms/post"
        assert driver.current_url == expected_form_url, (
            f"Ожидался URL {expected_form_url}, "
            f"но текущий URL: {driver.current_url}"
        )

        # Шаг 4: Вернулись назад на главную страницу
        driver.back()

        # Шаг 5: Проверяем, что вернулись на исходный URL
        expected_main_url = "https://httpbin.qa-territory.online/"
        assert driver.current_url == expected_main_url, (
            f"Ожидался возврат на {expected_main_url}, "
            f"но текущий URL: {driver.current_url}"
        )

    finally:

        driver.quit()
