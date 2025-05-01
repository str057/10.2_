import pandas as pd
from typing import List, Dict


def read_financial_operations_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV файла.

    :param file_path: Путь к CSV файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_csv(file_path, sep=";")
    transactions = df.to_dict(orient="records")
    return transactions


def read_financial_operations_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel файла.

    :param file_path: Путь к Excel файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_excel(file_path)
    transactions = df.to_dict(orient="records")
    return transactions


# Укажите путь к файлу Excel
file_path_excel = r"C:\Users\R\PycharmProjects\10.2_new\AAALLL\transactions_excel.xlsx"

# Пример вызова функции для чтения Excel файла
transactions_from_excel = read_financial_operations_from_excel(file_path_excel)

# Выводим результат
print(transactions_from_excel)
