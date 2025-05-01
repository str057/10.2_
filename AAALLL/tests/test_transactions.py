import pytest
from transactions import search_transactions, count_transaction_categories

# Пример данных для тестирования
sample_transactions = [
    {
        "description": "Открытие вклада",
        "status": "EXECUTED",
        "date": "2019-12-08",
        "currency": "RUB",
    },
    {
        "description": "Перевод с карты на карту",
        "status": "EXECUTED",
        "date": "2019-11-12",
        "currency": "USD",
    },
    {
        "description": "Перевод организации",
        "status": "CANCELED",
        "date": "2018-07-18",
        "currency": "RUB",
    },
    {
        "description": "Перевод со счета на счет",
        "status": "PENDING",
        "date": "2018-06-03",
        "currency": "EUR",
    },
]


def test_search_transactions():
    # Тест поиска транзакций по описанию
    result = search_transactions(sample_transactions, "вклада")
    assert len(result) == 1
    assert result[0]["description"] == "Открытие вклада"

    result = search_transactions(sample_transactions, "перевод")
    assert len(result) == 3

    result = search_transactions(sample_transactions, "несуществующее слово")
    assert len(result) == 0


def test_count_transaction_categories():
    # Тест подсчета транзакций по категориям
    categories = ["вклада", "перевод", "организации"]
    result = count_transaction_categories(sample_transactions, categories)

    assert result["вклада"] == 1
    assert result["перевод"] == 3  # Изменено с 2 на 3


# Запуск тестов
if __name__ == "__main__":
    pytest.main()
