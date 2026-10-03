from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.delete_all_cookies()
    driver.refresh()

    # 2. Найдите и нажмите на кнопку "Start"
    wait = WebDriverWait(driver, 15)
    start_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#start button")))
    start_btn.click()

    # 3. Дождитесь появления текста "Hello World!"
    wait.until(
        EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
    )

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("task1_page.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    hello_element = driver.find_element(By.ID, "finish")
    assert hello_element.text == "Hello World!", \
        f"Текст не совпадает: {hello_element.text}"

    driver.quit()
