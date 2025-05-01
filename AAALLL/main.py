from src.finance_reader import (
    read_financial_operations_from_csv,
    read_financial_operations_from_excel,
)


if __name__ == "__main__":
    print(read_financial_operations_from_csv("./transactions.csv"))
    print(read_financial_operations_from_excel("./transactions_excel.xlsx"))


import json
import csv
import pandas as pd
from transactions import search_transactions  # Функция поиска по описанию
from datetime import datetime  # Импортируем datetime один раз в начале файла


def load_transactions_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_transactions_from_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def load_transactions_from_xlsx(file_path):
    return pd.read_excel(file_path).to_dict(orient="records")


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    if choice == "1":
        transactions = load_transactions_from_json("transactions.json")
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        transactions = load_transactions_from_csv("transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        transactions = load_transactions_from_xlsx("transactions.xlsx")
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор.")
        return

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    status = (
        input(
            "Введите статус, по которому необходимо выполнить фильтрацию. \n"
            "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\n"
        )
        .strip()
        .upper()
    )
    while status not in valid_statuses:
        print(f'Статус операции "{status}" недоступен.')
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию. \n"
                "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\n"
            )
            .strip()
            .upper()
        )

    filtered_transactions = [
        t for t in transactions if t.get("status", "").upper() == status
    ]
    print(f"Операции отфильтрованы по статусу: {status}.")

    sort_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_choice == "да":
        order = (
            input("Отсортировать по возрастанию или по убыванию? \n").strip().lower()
        )

        def parse_date(t):
            date_str = t.get("date", "")
            try:
                return datetime.strptime(date_str, "%d.%m.%Y")
            except Exception:
                try:
                    return datetime.strptime(date_str, "%Y-%m-%d")
                except Exception:
                    return datetime.min

        if order == "по возрастанию":
            filtered_transactions.sort(key=parse_date)
        elif order == "по убыванию":
            filtered_transactions.sort(key=parse_date, reverse=True)
        else:
            print("Некорректный порядок сортировки. Продолжаем без сортировки.")

    currency_filter = (
        input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    )
    if currency_filter == "да":
        filtered_transactions = [
            t for t in filtered_transactions if t.get("currency", "").upper() == "RUB"
        ]

    description_filter = (
        input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
        )
        .strip()
        .lower()
    )

    if description_filter == "да":
        search_string = input("Введите слово для поиска: ")
        filtered_transactions = search_transactions(
            filtered_transactions, search_string
        )

    print("Распечатываю итоговый список транзакций...")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")

    for t in filtered_transactions:
        date = t.get("date")
        description = t.get("description", "")

        try:
            date_out = datetime.strptime(date, "%Y-%m-%d").strftime("%d.%m.%Y")
        except Exception:
            try:
                date_out = datetime.strptime(date, "%d.%m.%Y").strftime("%d.%m.%Y")
            except Exception:
                date_out = date

        amount = t.get("amount", "")
        currency = t.get("currency", "")

        print(f"{date_out} {description}\n")
        if "from_account" in t and "to_account" in t:
            print(f"{t.get('from_account')} -> {t.get('to_account')}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
