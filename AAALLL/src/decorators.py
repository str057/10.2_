import logging
import functools
import sys


def setup_logging(filename=None):
    """Настройка логирования. Если filename указан, логи будут записываться в файл."""
    if filename:
        logging.basicConfig(
            level=logging.INFO,
            filename=filename,
            filemode="a",
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
    else:
        logging.basicConfig(
            level=logging.INFO,
            stream=sys.stdout,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )


def log(filename=None):
    """Декоратор для логирования вызовов функций.

    Этот декоратор оборачивает функцию и добавляет логирование её вызовов.
    Если функция выполняется успешно, в лог записывается сообщение о её успешном выполнении.
    Если возникает исключение, в лог записывается сообщение об ошибке, включая информацию о входных данных.

    Параметры:
    filename (str, optional): Имя файла, в который будут записываться логи.
                               Если не указано, логи будут выводиться в консоль.

    Возвращает:
    function: Обернутая функция с добавленным логированием.
    """
    setup_logging(filename)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logging.error(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator


@log()  # Вызываем декоратор без параметров, чтобы логировать в консоль
def add(a: int, b: int) -> int:
    return a + b


@log()  # Вызываем декоратор без параметров, чтобы логировать в консоль
def divide(a: int, b: int) -> float:
    return a / b
