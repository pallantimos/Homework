from unittest.mock import Mock
from src.external_api import get_sum_transaction
from src.utils import get_transactions
import pytest


@pytest.fixture
def transactions():
    return


def test_get_transactions():
    assert type(get_transactions("C:\\Users\\dondo\\PycharmProjects\\Homework\\data\\operations.json")) == list
    assert get_transactions("") == []
