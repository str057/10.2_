from datetime import datetime
from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты в виде строки и
    возвращает маску номера по правилу XXXX XX** **** XXXX"""
    if card_number.isdigit() and len(card_number) == 16:
        masked_number = (
            card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        )
        return masked_number
    else:
        return "Проверьте правильность введенного номера карты!"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счета в виде строки и
    возвращает маску номера по правилу XXXX XXXX XXXX XXXX XX"""
    if account_number.isdigit() and len(account_number) == 20:
        masked_number = (
            "**" + account_number[-4:]
        )  # Маскируем все, кроме последних 4 цифр
        return masked_number
    else:
        return "Проверьте правильность введенного номера счета!"


def mask_account_card(input_string: str) -> str:
    """Функция принимает строку с типом карты или счета и номером,
    возвращает замаскированный номер."""
    parts = input_string.split()
    card_type = " ".join(parts[:-1])  # Все кроме последнего элемента
    number = parts[-1]  # Последний элемент - номер

    if (
        card_type.startswith("Visa")
        or card_type.startswith("MasterCard")
        or card_type.startswith("Maestro")
    ):
        return f"{card_type} {get_mask_card_number(number)}"
    elif card_type.startswith("Счет"):
        return f"{card_type} {get_mask_account(number)}"
    else:
        return "Неизвестный тип карты или счета!"


def get_date(date_string: str) -> str:
    """Функция принимает строку с датой в формате ISO и возвращает
    строку с датой в формате ДД.ММ.ГГГГ."""
    date_obj = datetime.fromisoformat(date_string)
    return date_obj.strftime("%d.%m.%Y")
