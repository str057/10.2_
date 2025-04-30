import logging
import re
import pytest


# Logging configuration
def init_logging(log_level: str = "DEBUG"):
    logging.basicConfig(
        level=log_level, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)


# Function to mask sensitive data
def mask_sensitive_data(data: str) -> str:
    patterns = [
        r"\d{3}-\d{2}-\d{4}",  # Social Security numbers
        r"\d{4}-\d{4}-\d{4}-\d{4}",  # Credit card numbers
    ]
    for pattern in patterns:
        data = re.sub(pattern, "******", data)
    return data


# Example function that may raise an error
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# Unit tests
def test_mask_sensitive_data():
    assert mask_sensitive_data("My SSN is 123-45-6789") == "My SSN is ******"
    assert (
        mask_sensitive_data("My credit card is 1234-5678-9012-3456")
        == "My credit card is ******"
    )


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_divide():
    assert divide(10, 2) == 5.0


if __name__ == "__main__":
    logger = init_logging()
    logger.info("Starting the application")

    # Example usage
    try:
        result = divide(10, 0)
    except ValueError as e:
        logger.error(f"Error occurred: {e}")

    # Run tests
    pytest.main()
