import pytest
from AAALLL.src.processing import (
    filter_by_state,
    sort_by_date,
)  # Замените на правильный путь к вашему модулю


@pytest.fixture
def transactions():
    """Фикстура для предоставления тестовых данных о транзакциях."""
    return [
        {"id": 1, "date": "2023-01-01", "state": "EXECUTED"},
        {"id": 2, "date": "2023-01-02", "state": "CANCELED"},
        {"id": 3, "date": "2023-01-03", "state": "EXECUTED"},
        {"id": 4, "date": "2023-01-01", "state": "EXECUTED"},
        {"id": 5, "date": "2023-01-04", "state": "CANCELED"},
    ]


def test_filter_by_state(transactions):
    """Тестирование функции фильтрации по состоянию."""
    executed_transactions = filter_by_state(transactions, "EXECUTED")
    assert len(executed_transactions) == 3
    assert all(tx["state"] == "EXECUTED" for tx in executed_transactions)

    canceled_transactions = filter_by_state(transactions, "CANCELED")
    assert len(canceled_transactions) == 2
    assert all(tx["state"] == "CANCELED" for tx in canceled_transactions)

    # Проверка на отсутствие транзакций с несуществующим состоянием
    unknown_transactions = filter_by_state(transactions, "UNKNOWN")
    assert len(unknown_transactions) == 0


def test_sort_by_date_with_same_dates():
    """Тестирование сортировки при одинаковых датах."""
    transactions_with_same_dates = [
        {"id": 1, "date": "2023-01-01", "state": "EXECUTED"},
        {"id": 2, "date": "2023-01-01", "state": "CANCELED"},
    ]
    sorted_transactions = sort_by_date(transactions_with_same_dates, descending=True)
    assert [tx["id"] for tx in sorted_transactions] == [2, 1]  # Проверяем порядок по id


def test_sort_by_date_empty_list():
    """Тестирование сортировки пустого списка."""
    sorted_transactions = sort_by_date([], descending=True)
    assert sorted_transactions == []


def test_filter_by_state_empty_list():
    """Тестирование фильтрации пустого списка."""
    empty_transactions = []
    filtered_transactions = filter_by_state(empty_transactions, "EXECUTED")
    assert filtered_transactions == []


def test_sort_by_date_single_transaction():
    """Тестирование сортировки списка с одной транзакцией."""
    single_transaction = [{"id": 1, "date": "2023-01-01", "state": "EXECUTED"}]
    sorted_transactions = sort_by_date(single_transaction, descending=True)
    assert sorted_transactions == single_transaction
