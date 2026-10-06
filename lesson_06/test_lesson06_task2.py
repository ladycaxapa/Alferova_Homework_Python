from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    USER_1_LOGIN = "451ruling@uberip.com"
    USER_1_PASSWORD = "RLm3z!CDy-8XfvF"

    USER_2_LOGIN = "e2ee75f2a820@uberip.com"
    USER_2_PASSWORD = "j.-5U!5Kr3uy5AE"

    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    # Авторизуемся под Пользователем 1
    driver.get("https://gitflic.ru/auth/login")
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@placeholder='Почта']")
        )).send_keys(USER_1_LOGIN)
    driver.find_element(
        By.XPATH, "//input[@placeholder='Пароль']").send_keys(USER_1_PASSWORD)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[text()='Войти' or @value='Войти']")
        )).click()

    wait.until(EC.url_changes("https://gitflic.ru/auth/login"))
    cookies_user1 = driver.get_cookies()
    driver.delete_all_cookies()

    # Авторизуемся под Пользователем 2
    driver.get("https://gitflic.ru/auth/login")
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@placeholder='Почта']")
        )).send_keys(USER_2_LOGIN)
    driver.find_element(
        By.XPATH, "//input[@placeholder='Пароль']").send_keys(USER_2_PASSWORD)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[text()='Войти' or @value='Войти']")
        )).click()

    wait.until(EC.url_changes("https://gitflic.ru/auth/login"))
    cookies_user2 = driver.get_cookies()
    driver.delete_all_cookies()

    # 1. Откройте страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/auth/login")

    # 2. Установите cookie пользователя 1
    for cookie in cookies_user1:
        driver.add_cookie(cookie)

    # 3. Обновите страницу
    driver.refresh()

    # 4. Перейдите на страницу пользователя 1
    driver.get("https://gitflic.ru/user/451ruling")

    # 5. Сохраните текущий URL
    url_user1 = driver.current_url

    # 6. Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()

    # 7. Установите cookie пользователя 2
    driver.get("https://gitflic.ru/auth/login")
    for cookie in cookies_user2:
        driver.add_cookie(cookie)

    # 8. Обновите страницу
    driver.refresh()

    # 9. Перейдите на страницу пользователя 2
    driver.get("https://gitflic.ru/user/e2ee75f2a820")

    # 10. Сохраните текущий URL
    url_user2 = driver.current_url

    # 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются
    assert url_user1 != url_user2, \
        f"ОШИБКА: URL пользователей одинаковые! ({url_user1})"

    print(f"\nURL Пользователя 1: {url_user1}")
    print(f"URL Пользователя 2: {url_user2}")

    driver.quit()
