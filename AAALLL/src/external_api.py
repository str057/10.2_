import os
import requests
from typing import Dict


def convert_currency(transaction: Dict[str, float]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции, должен содержать ключи 'amount' и 'currency'.
    :return: Сумма транзакции в рублях. Если валюта не поддерживается, возвращает сумму без изменений.
    """
    amount = transaction.get("amount")
    currency = transaction.get("currency")

    if amount is None or currency is None:
        raise ValueError("Transaction must contain 'amount' and 'currency' keys.")

    if currency in ["USD", "EUR"]:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is not set.")

        url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
        headers = {"apikey": api_key}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            rate = response.json().get("rates", {}).get("RUB")
            if rate is not None:
                return amount * rate
            else:
                raise ValueError("Failed to retrieve exchange rate for RUB.")

        except requests.RequestException as e:
            raise RuntimeError(f"Error fetching exchange rate: {e}")

    return float(amount)
