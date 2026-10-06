from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_form():
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        # 1. Открываем страницу
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        # 2. Заполняем форму значениями
        def find_by_name(name):
            return driver.find_element(By.NAME, name)

        find_by_name("first-name").send_keys("Иван")
        find_by_name("last-name").send_keys("Петров")
        find_by_name("address").send_keys("Ленина, 55-3")
        find_by_name("e-mail").send_keys("test@skypro.com")
        find_by_name("phone").send_keys("+7985899998787")
        find_by_name("city").send_keys("Москва")
        find_by_name("country").send_keys("Россия")
        find_by_name("job-position").send_keys("QA")
        find_by_name("company").send_keys("SkyPro")

        # 3. Нажимаем кнопку Submit
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait = WebDriverWait(driver, 10)

        # 4. Проверяем, что поле Zip code подсвечено красным
        zip_field = wait.until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )
        assert "alert-danger" in zip_field.get_attribute(
            "class"
        ), "Поле Zip code должно быть подсвечено красным"

        # 5. Проверяем, что остальные поля подсвечены зеленым
        green_fields_ids = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]

        for field_id in green_fields_ids:
            field = driver.find_element(By.ID, field_id)
            assert "alert-success" in field.get_attribute(
                "class"
            ), f"Поле {field_id} должно быть подсвечено зеленым"

    finally:
        driver.quit()
