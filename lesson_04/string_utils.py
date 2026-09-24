class StringUtils:
    """Класс с полезными утилитами для обработки и анализа строк."""

    def capitalize(self, string: str) -> str:
        """Сделать первую букву заглавной."""
        return string.capitalize()

    def trim(self, string: str) -> str:
        """Удалить пробелы в начале."""
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def contains(self, string: str, symbol: str) -> bool:
        """Проверить, содержит ли строка символ."""
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass

        return res

    def delete_symbol(self, string: str, symbol: str) -> str:
        """Удалить подстроки из переданной строки."""
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string
