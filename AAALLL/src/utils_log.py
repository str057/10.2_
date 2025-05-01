import logging

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("utils.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def mask_account_number(account_number: str) -> str:
    """Возвращает замаскированный номер счета."""
    if account_number.isdigit() and len(account_number) == 20:
        masked_number = f"**{account_number[-4:]}"
        logger.info(f"Замаскированный номер счета: {masked_number}")
        return masked_number
    else:
        logger.error("Ошибка: Неверный номер счета.")
        return "Проверьте правильность введенного номера счета!"
