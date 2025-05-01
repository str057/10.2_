import logging
import os

# Создаем папку для логов, если она не существует
os.makedirs("logs", exist_ok=True)


def setup_utils_logger():
    """Настройка логирования для модуля utils."""
    # Создаем логгер
    utils_logger = logging.getLogger("utils")
    utils_logger.setLevel(logging.DEBUG)  # Уровень логирования не ниже DEBUG

    # Создаем обработчик для записи логов в файл
    file_handler = logging.FileHandler("logs/utils.log")
    file_handler.setLevel(logging.DEBUG)  # Уровень обработчика

    # Создаем форматтер для логов
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)  # Устанавливаем форматтер для обработчика

    # Добавляем обработчик к логгеру
    utils_logger.addHandler(file_handler)

    return utils_logger
