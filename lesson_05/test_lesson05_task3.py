from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()

    try:
        # Шаг 1: Открываем страницу
        driver.get("https://httpbin.qa-territory.online/links/10")

        # Шаг 2: Находим все ссылки на странице по тегу <a>
        links = driver.find_elements(By.TAG_NAME, "a")

        # Шаг 3: Проверяем, что количество ссылок на странице равно 9
        assert len(links) == 9, (
            f"Ожидалось 9 ссылок, но найдено: {len(links)}"
        )

        # Шаг 4: Проверяем в цикле, что все ссылки отображаются на странице
        for index, link in enumerate(links):
            assert link.is_displayed(), (
                f"Ссылка с индексом {index} не отображается"
            )

        # Шаг 5: Проверяем, что текст первой ссылки содержит "1"
        first_link_text = links[0].text
        assert "1" in first_link_text, (
            f"Текст первой ссылки ('{first_link_text}') "
            f"не содержит '1'"
        )

    finally:

        driver.quit()
