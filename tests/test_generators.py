import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return (
        (
            "USD",
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
        ),
        ("USD", "Пустой кортеж", []),
        ("USD", "Пустой кортеж", []),
    )


@pytest.fixture
def card_number_value():
    return (1, 100000)


def test_filter_by_currency(transactions):
    for currency_code, expected_name, transactions_list in transactions:
        generator = filter_by_currency(transactions_list, currency_code)
        filtered_transactions = list(generator)
        if not transactions_list:
            # Проверяем, что для пустого списка результат пуст
            assert len(filtered_transactions) == 0
        else:
            # Проверяем все транзакции на соответствие валюте
            assert all(t["operationAmount"]["currency"]["name"] == expected_name for t in filtered_transactions)


def test_transaction_descriptions(transactions):
    for currency_code, expected_name, transactions_list in transactions:
        generator = transaction_descriptions(transactions_list)
        description = list(generator)
        if not transactions_list:
            assert len(description) == 0
        else:
            assert description[0] == transactions_list[0]["description"]


def test_card_number_generator(card_number_value):
    generator = card_number_generator(123456789, 200000000)
    card_number = next(generator)
    assert isinstance(card_number, str)
    assert (card_number == '0000 0001 2345 6789')
    assert (next(generator) == '0000 0001 2345 6790')
    generator = card_number_generator(-1, 1)
    try:
        next(generator)
    except StopIteration as e:
        assert e.value == "Некорректный номер"
