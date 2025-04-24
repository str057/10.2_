from typing import Dict
from typing import List


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей с данными о банковских операциях.
    :param state: Значение для фильтрации по ключу 'state'.
    :return: Новый список словарей, содержащий только те, у которых ключ 'state' соответствует указанному значению.
    """
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате.

    :param transactions: Список словарей с данными о банковских операциях.
    :param descending: Параметр, определяющий порядок сортировки (по умолчанию - убывание).
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(
        transactions,
        key=lambda x: (x["date"], -x["id"] if descending else x["id"]),
        reverse=not descending,
    )
