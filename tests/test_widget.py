import pytest
from src.widget import mask_account_card, get_date

# Параметризация для карт и счетов
@pytest.mark.parametrize("input_str, expected", [
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
    ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
    ("Invalid 123", "Некорректный счет"),
    ("Visa Platinum 123", "Некорректный номер"),
    ("", 'Пустой ввод')
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected

# Тесты для даты
@pytest.mark.parametrize("input_date, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2025-12-31T00:00:00.000000", "31.12.2025"),
    ("invalid-date", "Некорректная дата"),
])
def test_get_date(input_date, expected):
    assert get_date(input_date) == expected