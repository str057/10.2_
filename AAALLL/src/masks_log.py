import logging

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("masks.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер карты."""
    if card_number.isdigit() and len(card_number) == 16:
        masked_number = (
            f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        )
        logger.info(f"Замаскированный номер карты: {masked_number}")
        return masked_number
    else:
        logger.error("Ошибка: Неверный номер карты.")
        return "Проверьте правильность введенного номера карты!"


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счета."""
    if account_number.isdigit() and len(account_number) == 20:
        masked_number = f"**{account_number[-4:]}"
        return masked_number
    else:
        return "Проверьте правильность введенного номера счета!"
