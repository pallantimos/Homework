import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def get_sum_transaction(transaction: dict) -> Any:
    """
    Возвращает amount транзакции в рублях
    """
    if transaction["operationAmount"]["currency"]["code"] == "USD":
        amount = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/\
        convert?to=RUB&from=USD&amount={amount}"

        payload = {}
        headers = {"apikey": os.getenv("API_KEY")}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = response.json()
        return response["result"]

    elif transaction["operationAmount"]["currency"]["code"] == "EUR":
        amount = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/\
        convert?to=RUB&from=EUR&amount={amount}"

        payload = {}
        headers = {"apikey": os.getenv("API_KEY")}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = response.json()
        return response["result"]

    return transaction["operationAmount"]["amount"]
