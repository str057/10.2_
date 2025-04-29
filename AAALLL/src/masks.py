import logging
from typing import Union

def setup_logger():
    """Настройка логирования для модуля masks."""
    logger = logging.getLogger('masks')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('logs/masks.log')
    file_handler.setLevel(logging.DEBUG)

    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)

    return logger

# Настройка логгера
logger = setup_logger()

def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу XXXX XX** **** XXXX"""
    if card_number.isdigit() and len(card_number) == 16:
        masked_number = (
            card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        )
        logger.info(f"Успешно замаскирован номер карты: {card_number} -> {masked_number}")
        return masked_number
    else:
        logger.error(f"Ошибка при замаскировке номера карты: {card_number}")
        return "Проверьте правильность введенного номера карты!"

def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счета и возвращает маску номера."""
    if account_number.isdigit() and len(account_number) == 20:
        masked_number = "**" + account_number[-4:]
        logger.info(f"Успешно замаскирован номер счета: {account_number} -> {masked_number}")
        return masked_number
    else:
        logger.error(f"Ошибка при замаскировке номера счета: {account_number}")
        return "Проверьте правильность введенного номера счета!"