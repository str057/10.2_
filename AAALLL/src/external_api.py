import requests


def convert_currency(amount: float, rate: float) -> float:
    """Конвертирует сумму по заданному курсу."""
    if not isinstance(amount, (int, float)) or not isinstance(rate, (int, float)):
        raise TypeError("amount and rate must be numbers")
    return amount * rate


def long_function_name(arg1, arg2, arg3, arg4, arg5, arg6):
    """Пример функции с длинными аргументами."""
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6


def fetch_data(url: str):
    """Пример функции, использующей requests для получения данных."""
    response = requests.get(url)
    return response.json()


# Пример использования
if __name__ == "__main__":
    converted_amount = convert_currency(100, 1.2)
    print(f"Converted amount: {converted_amount}")

    # Пример использования функции fetch_data
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = fetch_data(url)
    print(data)
