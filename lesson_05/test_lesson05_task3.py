from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    # Инициализируем драйвер браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 1. Открываем страницу
        driver.get("https://qa-territory.online")

        # 2. Находим все ссылки на странице по тегу <a>
        links = driver.find_elements(By.TAG_NAME, "a")

        # 3. Проверяем, что количество ссылок на странице равно 9
        assert len(links) == 9, (
            f"Ожидалось 9 ссылок, но найдено: {len(links)}"
        )

        # 4. Проверяем в цикле, что все ссылки отображаются на странице
        for index, link in enumerate(links):
            assert link.is_displayed(), (
                f"Ссылка с индексом {index} не отображается"
            )

        # 5. Проверяем, что текст первой ссылки содержит "1"
        first_link_text = links[0].text
        assert "1" in first_link_text, (
            f"Текст первой ссылки ('{first_link_text}') "
            f"не содержит '1'"
        )

    finally:
        # Гарантированно закрываем браузер после выполнения всех проверок
        driver.quit()
