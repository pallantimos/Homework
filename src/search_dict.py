import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция Принимает список операций и строку для поиска."""
    """Возвращает список операций где в описании есть переданная строка."""
    if not search:
        return data

    search = search.lower()

    new_data = [
        x
        for x in data
        if x
        and re.search(re.escape(search), x["description"].lower(), flags=re.I)
    ]

    return new_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """ "Функция принимает список операций и категории"""
    data_description = [
        d.get("description")
        for d in data
        if d.get("description") not in categories
    ]
    count_description = dict(Counter(data_description))

    return count_description
