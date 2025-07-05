import json
from typing import Any


def get_transactions(json_path: str) -> list:
    """
    Читает и возвращает содержимое JSON-файла.
    В случае ошибки пути или некорректного JSON возвращает пустой словарь.
    """

    try:
        with open(json_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Указан неправильный путь")

    return []
