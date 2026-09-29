from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    # Инициализируем драйвер браузера Chrome
    driver = webdriver.Chrome()

    try:
        # Устанавливаем базовый URL для удобства проверок
        base_url = "https://qa-territory.online"

        # 1. Открываем страницу
        driver.get(base_url)

        # 2. Находим и кликаем на ссылку "HTML Form" по тексту ссылки
        html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
        html_form_link.click()

        # 3. Проверяем, что URL изменился на /forms/post
        expected_form_url = f"{base_url}/forms/post"
        assert driver.current_url == expected_form_url, (
            f"Ожидался URL {expected_form_url}, "
            f"но текущий URL: {driver.current_url}"
        )

        # 4. Возвращаемся назад на главную страницу
        driver.back()

        # 5. Проверяем, что вернулись на исходный URL
        # Добавляем финальный слеш для корректной проверки
        expected_main_url = f"{base_url}/"
        assert driver.current_url == expected_main_url, (
            f"Ожидался возврат на {expected_main_url}, "
            f"но текущий URL: {driver.current_url}"
        )

    finally:
        # В любом случае закрываем браузер и освобождаем ресурсы
        driver.quit()
