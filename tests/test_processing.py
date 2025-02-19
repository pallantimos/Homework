import pytest
from src.processing import filter_by_state, sort_by_date

# Фикстура для тестовых данных
@pytest.fixture
def sample_transactions():
    return [
        {"state": "EXECUTED", "date": "2024-03-11T12:00:00"},
        {"state": "PENDING", "date": "2024-03-10T10:00:00"},
        {"state": "EXECUTED", "date": "2024-03-09T08:00:00"},
        {"state": "CANCELED", "date": "2024-03-08T06:00:00"},
    ]

# Тест фильтрации по статусу
@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("PENDING", 1),
    ("UNKNOWN", 0),
])
def test_filter_by_state(sample_transactions, state, expected_count):
    filtered = filter_by_state(sample_transactions, state)
    assert len(filtered) == expected_count

# Тест сортировки по дате
def test_sort_by_date(sample_transactions):
    sorted_decreasing = sort_by_date(sample_transactions, "decreasing")
    assert sorted_decreasing[0]["date"] == "2024-03-11T12:00:00"

    sorted_increasing = sort_by_date(sample_transactions, "increasing")
    assert sorted_increasing[0]["date"] == "2024-03-08T06:00:00"