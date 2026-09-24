import pytest
from string_utils import StringUtils

utils = StringUtils()


# ПОЗИТИВНЫЕ СЦЕНАРИИ

def test_capitalize_positive_standard():
    """Позитивный сценарий: 'Тест' — не пустая строка."""
    assert utils.capitalize("Тест") == "Тест"


def test_trim_positive_numbers_string():
    """Позитивный сценарий: '123' — числа как строка."""
    assert utils.trim("   123") == "123"


def test_contains_positive_spaces_string():
    """Позитивный сценарий: строка с пробелами."""
    assert utils.contains("04 апреля 2023", "апреля") is True


# НЕГАТИВНЫЕ СЦЕНАРИИ

def test_capitalize_negative_empty():
    """Негативный сценарий: Пустая строка — ''."""
    assert utils.capitalize("") == ""


def test_trim_negative_whitespace():
    """Негативный сценарий: Строка с пробелом — ' '."""
    assert utils.trim(" ") == ""


def test_delete_symbol_negative_empty_list():
    """Негативный сценарий: Пустой список — []."""
    assert utils.delete_symbol([], "a") == []


def test_capitalize_negative_none():
    """Негативный сценарий: Передача None."""
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ ДЛЯ ПОЛНОГО ПОКРЫТИЯ


def test_capitalize_basic():
    """Базовый тест для capitalize."""
    assert utils.capitalize("skypro") == "Skypro"


def test_trim_basic():
    """Базовый тест для trim."""
    assert utils.trim("   skypro") == "skypro"


def test_contains_basic_true():
    """Базовый тест для contains (True)."""
    assert utils.contains("SkyPro", "S") is True


def test_contains_basic_false():
    """Базовый тест для contains (False)."""
    assert utils.contains("SkyPro", "U") is False


def test_delete_symbol_basic():
    """Базовый тест для delete_symbol."""
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
