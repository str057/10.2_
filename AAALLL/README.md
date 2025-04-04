# Project Bank

Этот проект предоставляет набор функций для работы с банковскими данными, такими как маскировка номеров карт и счетов, форматирование дат, фильтрация и сортировка данных о транзакциях.

## Описание

Проект состоит из следующих функций:

-   `def get_mask_card_number(card_number: Union[str]) -> Union[str]`: Маскирует номер карты, показывая только первые 6 и последние 4 цифры.
-   `def get_mask_account(account_number: Union[str]) -> Union[str]:`: Маскирует номер счета, показывая только последние 4 цифры.
-   `def mask_account_card(input_string: str) -> str`: Обрабатывает информацию о карте или счете клиента и маскирует номер.
-   `def get_date(date_string: str) -> str:`: Преобразует дату в формат 'ДД.ММ.ГГГГ'.
-   `def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]`: Фильтрует список словарей по значению ключа 'state'.
-   `def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]`: Сортирует список словарей по дате.

## Установка

Для установки и запуска проекта необходимо выполнить следующие шаги:

1.  **Клонируйте репозиторий:**

    ```
    git clone https://github.com/str057/re_10_1.git
    ```

2.  **Перейдите в папку проекта:**

    ```
    AAALLL
    ```

3.  **Установите зависимости с помощью Poetry:**

    ```
    poetry install
    ```

## Использование

Примеры использования функций:

~~~
from src.widget import get_mask_card_number, get_mask_account, mask_account_card, get_date, filter_by_state, sort_by_date
from typing import Dict, List

Маскировка номера карты
card_number = "6831982470375048"
masked_card = get_mask_card_number(card_number)
print(f"Masked card number: {masked_card}") # Output: 6831 98** **** 5048

Маскировка номера счета
account_number = "12345678901234567890"
masked_account = get_mask_account(account_number)
print(f"Masked account number: {masked_account}") # Output: **7890

Маскировка информации о карте/счете
bank_details = "Visa Classic 6831982470375048"
masked_details = mask_account_card(bank_details)
print(f"Masked details: {masked_details}") # Output: Visa Classic 6831 98** **** 5048

Преобразование даты
date_string = "2023-10-26T00:00:00"
formatted_date = get_date(date_string)
print(f"Formatted date: {formatted_date}") # Output: 26.10.2023

Пример данных для фильтрации и сортировки
transactions: List[Dict] = [
{"id": 1, "date": "2023-10-27T10:00:00", "state": "EXECUTED", "amount": 100},
{"id": 2, "date": "2023-10-26T12:00:00", "state": "CANCELED", "amount": 50},
{"id": 3, "date": "2023-10-28T14:00:00", "state": "EXECUTED", "amount": 200},
]

Фильтрация по статусу
executed_transactions = filter_by_state(transactions, state="EXECUTED")
print(f"Executed transactions: {executed_transactions}")

Сортировка по дате
sorted_transactions = sort_by_date(transactions)
print(f"Sorted transactions: {sorted_transactions}")

~~~

## Зависимости

Проект использует следующие зависимости:

*   Python 3.12.4
*   Poetry (для управления зависимостями)


## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE).

# Тестирование проекта

Этот проект включает в себя набор тестов, написанных с использованием
библиотеки [pytest](https://docs.pytest.org/en/stable/). Тесты помогают обеспечить 
корректность работы функций и модулей проекта.

## Структура тестов

Тесты организованы в папке `tests/`, где каждый файл соответствует модулю в проекте. Например:

## Описание тестов
Тесты для маскирования номера карты
Функция get_mask_card_number тестируется на различных входных данных, включая корректные и некорректные номера карт.

Тесты для фильтрации транзакций
Функция filter_by_state тестируется на различных состояниях транзакций, чтобы убедиться, что она правильно фильтрует
данные.

Тесты для сортировки транзакций
Функция sort_by_date тестируется на различных сценариях, включая сортировку по одинаковым датам и пустым спискам.

Тесты для виджетов
Функции mask_account_card и get_date тестируются на корректность маскирования и форматирования даты.