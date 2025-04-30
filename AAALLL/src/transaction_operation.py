from typing import List, Dict


def filter_transactions_by_amount(
    transactions: List[Dict], min_amount: float = 0
) -> List[Dict]:
    """
    Фильтрует транзакции по минимальной сумме.

    :param transactions: Список транзакций.
    :param min_amount: Минимальная сумма для фильтрации.
    :return: Список транзакций, сумма которых больше или равна min_amount.
    """
    return [
        transaction
        for transaction in transactions
        if transaction["amount"] >= min_amount
    ]


def summarize_transactions(transactions: List[Dict]) -> Dict[str, float]:
    """
    Подсчитывает общую сумму и количество транзакций.

    :param transactions: Список транзакций.
    :return: Словарь с общей суммой и количеством транзакций.
    """
    total_amount = sum(transaction["amount"] for transaction in transactions)
    transaction_count = len(transactions)
    return {"total_amount": total_amount, "transaction_count": transaction_count}


def group_transactions_by_description(
    transactions: List[Dict],
) -> Dict[str, List[Dict]]:
    """
    Группирует транзакции по описанию.

    :param transactions: Список транзакций.
    :return: Словарь, где ключи - описания, а значения - списки транзакций с этим описанием.
    """
    grouped: Dict[str, List[Dict]] = {}
    for transaction in transactions:
        description = transaction["description"]
        if description not in grouped:
            grouped[description] = []
        grouped[description].append(transaction)
    return grouped
