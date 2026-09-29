from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    # Инициализируем драйвер браузера Chrome
    driver = webdriver.Chrome()

    try:
        # Задаем исходный URL формы
        start_url = "https://qa-territory.online"
        driver.get(start_url)

        # 1. Находим поле ввода по атрибуту name="custname"
        name_input = driver.find_element(By.NAME, "custname")

        # 2. Вводим имя в поле
        name_input.send_keys("Ваше Имя")

        # 3. Находим кнопку Submit с помощью XPath по тексту и кликаем
        # Используем встроенную функцию text()
        submit_xpath = "//button[text()='Submit order']"
        submit_button = driver.find_element(By.XPATH, submit_xpath)
        submit_button.click()

        # 4. Проверяем, что после нажатия текущий URL изменился
        current_url = driver.current_url
        assert current_url != start_url, (
            f"Ошибка: URL не изменился после отправки формы "
            f"и остался: {current_url}"
        )

    finally:
        # Гарантированно закрываем браузер после выполнения теста
        driver.quit()
