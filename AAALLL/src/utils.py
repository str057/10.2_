import json
import logging
import os
from typing import List, Dict, Any


def setup_logger():
    """Настройка логирования для модуля utils."""
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("utils")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("logs/utils.log")
    file_handler.setLevel(logging.DEBUG)

    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)

    return logger


logger = setup_logger()


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными о транзакциях или пустой список, если файл пустой,
             содержит не список или не найден.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно прочитан файл: {file_path}")
                return data
            else:
                logger.warning(f"Файл {file_path} не содержит список.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
