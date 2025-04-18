import logging
import functools
import sys

# Настройка логирования
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


def log(func):
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


@log
def add(a: int, b: int) -> int:
    return a + b


@log
def divide(a: int, b: int) -> float:
    return a / b
