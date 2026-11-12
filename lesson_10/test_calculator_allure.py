import allure
from selenium import webdriver
from calculator_page_allure import CalculatorPage


@allure.title("Медленный калькулятор: 7 + 8 = 15 (задержка 45 сек.)")
@allure.description(
    "Тест открывает калькулятор, задает задержку 45 сек., "
    "выполняет сложение 7 + 8 и проверяет результат на экране."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator() -> None:
    with allure.step("Запустить браузер Chrome и развернуть окно"):
        driver = webdriver.Chrome()
        driver.maximize_window()

    try:
        with allure.step("Открыть страницу медленного калькулятора"):
            driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/"
                "slow-calculator.html"
            )

        calc_page = CalculatorPage(driver)

        with allure.step("Установить задержку вычисления 45 секунд"):
            calc_page.set_delay("45")

        with allure.step("Нажать кнопки для вычисления: 7 + 8 ="):
            calc_page.click_button("7")
            calc_page.click_button("+")
            calc_page.click_button("8")
            calc_page.click_button("=")

        with allure.step("Ожидать результат '15' и проверить его"):
            result = calc_page.get_result_with_wait("15", timeout=50)
            assert result == "15", (
                f"Ожидался '15', но на экране: '{result}'"
            )

    finally:
        with allure.step("Закрыть браузер"):
            driver.quit()
