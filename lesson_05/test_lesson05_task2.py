import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():

    driver = webdriver.Chrome()

    try:
        # Шаг 1: Открываем страницу
        start_url = "https://httpbin.qa-territory.online/forms/post"
        driver.get(start_url)

        # Шаг 2: Находим поле ввода с названием custname
        name_input = driver.find_element(By.NAME, "custname")

        # Шаг 3: Вводим в него имя
        name_input.send_keys("Алена")

        # Шаг 4: Находим кнопку Submit и нажимаем на неё
        submit_button = driver.find_element(
            By.XPATH,
            "//button[text()='Submit order']"
        )
        submit_button.click()

        time.sleep(2)

        # Шаг 5: Проверяем, что после нажатия URL изменился
        assert driver.current_url != start_url, (
            f"Ошибка: URL не изменился после отправки формы "
            f"и остался прежним: {driver.current_url}"
        )

    finally:

        driver.quit()
