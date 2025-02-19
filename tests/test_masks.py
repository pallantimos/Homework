import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_numbers():
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        (1234567890123456, "1234 56** **** 3456"),
        ("123", "Некорректная длина номера карты"),
    ]

@pytest.fixture
def account_numbers():
    return [
        ("64686473678894779589", "**9589"),
        ("123", "Некорректная длина номера карты"),
        (64686473678894779589, "**9589")
    ]


def test_get_mask_card_number(card_numbers):
    for number, expected in card_numbers:
        assert get_mask_card_number(number) == expected


def test_get_mask_account(account_numbers):
    for number, expected in account_numbers:
        assert get_mask_account(number) == expected

def test_empty_input():
    assert get_mask_card_number("") == "Некорректная длина номера карты"
    assert get_mask_account("") == "Некорректная длина номера карты"