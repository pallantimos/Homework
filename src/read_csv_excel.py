import csv
import pandas
import json


def get_from_csv(csv_path: str) -> list:
    """Функция читает csv файл по указанному пути"""
    """Возвращает считанный файл в виде списка словарей"""

    try:
        with open(csv_path, encoding="utf-8") as file:
            list_csv = []
            reader = csv.DictReader(file, delimiter=";")
            next(reader)
            for row in reader:
                list_csv.append(row)
    except FileNotFoundError:
        print("Указан неправильный путь")
        return []

    return list_csv


def get_from_excel(excel_path: str) -> list:
    """Функция читает excel файл по указанному пути"""
    """Возвращает считанный файл в виде списка словарей"""
    try:
        reader = pandas.read_excel(excel_path)
        list_excel = reader.to_dict(orient="records")
    except FileNotFoundError:
        print("Указан неправильный путь")
        return []

    return list_excel


with open("data/test.json", "w") as file:
    json.dump(get_from_csv("data/transactions.csv"), file)
