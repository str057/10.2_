from unittest.mock import mock_open, patch
import os
import pytest
import requests
from AAALLL.src.utils import read_json_file  # Убедитесь, что путь к модулю правильный
from AAALLL.src.external_api import (
    convert_currency,
)  # Замените на правильный путь к вашему модулю


# Тесты для функции чтения JSON-файла
def test_read_json_file_valid():
    mock_data = '[{"amount": 100, "currency": "USD"}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json_file("dummy_path")
        assert result == [{"amount": 100, "currency": "USD"}]


def test_read_json_file_empty():
    mock_data = "[]"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json_file("dummy_path")
        assert result == []


def test_read_json_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_json_file("dummy_path")
        assert result == []


def test_read_json_file_invalid_json():
    mock_data = "invalid json"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json_file("dummy_path")
        assert result == []


# Тесты для функции конвертации валюты
def test_convert_currency_usd():
    transaction = {
        "operationAmount": {
            "amount": "100",  # amount должен быть строкой
            "currency": {"name": "USD", "code": "USD"},
        }
    }
    mock_response = {"rates": {"RUB": 75.0}}

    with patch("AAALLL.src.external_api.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        os.environ["API_KEY"] = "test_api_key"

        result = convert_currency(transaction)
        assert result == 7500.0  # 100 * 75.0


def test_convert_currency_eur():
    transaction = {
        "operationAmount": {
            "amount": "100",  # amount должен быть строкой
            "currency": {"name": "EUR", "code": "EUR"},
        }
    }
    mock_response = {"rates": {"RUB": 85.0}}

    with patch("AAALLL.src.external_api.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        os.environ["API_KEY"] = "test_api_key"

        result = convert_currency(transaction)
        assert result == 8500.0  # 100 * 85.0


def test_convert_currency_invalid_api():
    transaction = {
        "operationAmount": {
            "amount": "100",  # amount должен быть строкой
            "currency": {"name": "USD", "code": "USD"},
        }
    }

    with patch("AAALLL.src.external_api.requests.get") as mock_get:
        mock_get.side_effect = requests.RequestException("API error")
        os.environ["API_KEY"] = "test_api_key"

        with pytest.raises(
            RuntimeError, match="Error fetching exchange rate: API error"
        ):
            convert_currency(transaction)


def test_convert_currency_missing_api_key():
    transaction = {
        "operationAmount": {
            "amount": "100",  # amount должен быть строкой
            "currency": {"name": "USD", "code": "USD"},
        }
    }
    del os.environ["API_KEY"]  # Удаляем переменную окружения API_KEY

    with pytest.raises(ValueError, match="API_KEY environment variable is not set."):
        convert_currency(transaction)


def test_convert_currency_invalid_currency():
    transaction = {
        "operationAmount": {
            "amount": "100",  # amount должен быть строкой
            "currency": {"name": "GBP", "code": "GBP"},  # Неподдерживаемая валюта
        }
    }

    result = convert_currency(transaction)
    assert result == 100.0  # Сумма должна остаться без изменений
