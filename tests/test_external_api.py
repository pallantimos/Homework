from src.external_api import get_sum_transaction
import pytest
from unittest.mock import patch
import os


@pytest.fixture
def transaction():
    return [
        {
            "id": 634356296,
            "state": "EXECUTED",
            "date": "2018-01-21T01:10:28.317704",
            "operationAmount": {"amount": "96900.90", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 33407225454123927865",
            "to": "Счет 79619011266276091215",
        },
        {
            "id": 34148726,
            "state": "EXECUTED",
            "date": "2018-11-23T23:52:36.999661",
            "operationAmount": {"amount": "79428.73", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 5355133159258236",
            "to": "Maestro 8045769817179061",
        },
        {
            "id": 692008409,
            "state": "CANCELED",
            "date": "2019-02-14T17:38:09.910336",
            "operationAmount": {"amount": "37044.95", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод организации",
            "from": "Visa Classic 4610247282706784",
            "to": "Счет 63229171188548882700",
        },
        ("", "Пустой кортеж", []),
    ]


def test_get_sum_transaction(transaction):
    assert get_sum_transaction(transaction[0]) == "96900.90"
    with patch("requests.request") as mock_get:
        mock_get.return_value.json.return_value = {"result": "100"}
        
        assert get_sum_transaction(transaction[1]) == "100"
        args, kwargs = mock_get.call_args
        assert args[0] == "GET"
        assert "convert?to=RUB&from=USD&amount=79428.73" in args[1]
        assert kwargs["headers"] == {"apikey": os.getenv("API_KEY")}
        assert kwargs["data"] == {}

        assert get_sum_transaction(transaction[2]) == "100"
        args, kwargs = mock_get.call_args
        assert args[0] == "GET"
        assert "convert?to=RUB&from=EUR&amount=37044.95" in args[1]
        assert kwargs["headers"] == {"apikey": os.getenv("API_KEY")}
        assert kwargs["data"] == {}