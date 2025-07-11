import csv
import pandas


def get_from_csv(csv_path: str) -> list:
    with open(csv_path) as file:
        list_csv = []
        reader = csv.DictReader(file, delimiter=";")
        next(reader)
        for row in reader:
            list_csv.append(row)

    return list_csv


def get_from_excel(excel_path: str) -> list:
    reader = pandas.read_excel(excel_path)
    list_excel = reader.to_dict(orient="records")

    return list_excel
