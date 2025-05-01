import re
from collections import Counter


def search_transactions(transactions, search_string):
    """
    Функция для поиска транзакций по описанию. """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [
        transaction
        for transaction in transactions
        if pattern.search(transaction.get("description", ""))
    ]


def count_transaction_categories(transactions, categories):
    """
    Функция для подсчета количества транзакций по категориям.
    """
    category_count = Counter()
    for transaction in transactions:
        description = transaction.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1
    return dict(category_count)
