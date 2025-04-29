import logging


def setup_logger():
    """Настройка логирования для модуля utils_log."""
    logger = logging.getLogger("utils_log")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("logs/utils_log.log")
    file_handler.setLevel(logging.DEBUG)

    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)

    return logger


logger = setup_logger()


def log_example_usage():
    """Пример использования логирования в utils_log."""
    logger.info("Пример использования логирования в utils_log.")
    try:
        # Здесь может быть код, который может вызвать ошибку
        result = 10 / 0  # Пример ошибки
    except ZeroDivisionError:
        logger.error("Произошла ошибка деления на ноль.")
