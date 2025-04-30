import logging
from typing import Union

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler("masks.log")
file_handler.setLevel(logging.DEBUG)

# Определение формата логов
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу XXXX XX** **** XXXX"""
    if card_number.isdigit() and len(card_number) == 16:
        masked_number = (
            card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        )
        logger.info(f"Успешно замаскирован номер карты: {masked_number}")
        return masked_number
    else:
        logger.error("Ошибка: Неверный номер карты.")
        return "Проверьте правильность введенного номера карты!"


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счета."""
    if account_number.isdigit() and len(account_number) == 20:
        masked_number = f"**{account_number[-4:]}"
        logger.info(f"Замаскированный номер счета: {masked_number}")
        return masked_number
    else:
        logger.error("Ошибка: Неверный номер счета.")
        return "Проверьте правильность введенного номера счета!"  # Убедитесь, что это сообщение корректно


# Пример использования функций
if __name__ == "__main__":
    card = "1234567812345678"
    account = "12345678901234567890"

    print(get_mask_card_number(card))
    print(get_mask_account(account))
