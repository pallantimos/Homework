import random


def filter_by_currency(dict_list: list, currency: str):
    """ "Функция фильтрует список словарей, где валюта = USD"""
    if not dict_list:
        return "Пустой кортеж"

    for i in dict_list:
        if i["operationAmount"]["currency"]["name"] == "USD":
            yield i


def transaction_descriptions(dict_list: list):
    """ "Функция возвращает description из списка словарей"""
    for i in dict_list:
        yield i["description"]


def card_number_generator(start: int, end: int):
    """ "Функция генерирует случайный номер карты"""
    if end > 9999999999999999 or start > 9999999999999999 or start < 1 or end < 1 or start > end:
        return "Некорректный номер"
    while True:
        random_number = random.randint(start, end)
        formatted = f"{random_number:016d}"
        yield f"{formatted[:4]} {formatted[4:8]}" f" {formatted[8:12]} {formatted[12:]}"
