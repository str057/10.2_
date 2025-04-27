import os
import pytest
import requests
from unittest.mock import patch, Mock
from AAALLL.src.external_api import convert_currency  # Обновите путь к вашему модулю


def test_convert_currency_usd():
    transaction = {
        "operationAmount": {
            "amount": "100",  # amount должен быть строкой
            "currency": {"name": "USD", "code": "USD"},
        }
    }
    mock_response = {"rates": {"RUB": 75.0}}

    with patch("AAALLL.src.external_api.requests.get") as mock_get:
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_response)
        os.environ["API_KEY"] = "test_api_key"  # Установите переменную окружения

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
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_response)
        os.environ["API_KEY"] = "test_api_key"  # Установите переменную окружения

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
        os.environ["API_KEY"] = "test_api_key"  # Установите переменную окружения

        with pytest.raises(
            RuntimeError, match="Error fetching exchange rate: API error"
        ):
            convert_currency(transaction)


def test_convert_currency_invalid_currency():
    transaction = {
        "operationAmount": {
            "amount": "100",  # amount должен быть строкой
            "currency": {"name": "GBP", "code": "GBP"},  # Неподдерживаемая валюта
        }
    }

    result = convert_currency(transaction)
    assert (
        result == 100.0
    )  # Неподдерживаемая валюта, сумма должна остаться без изменений


def test_convert_currency_missing_amount():
    transaction = {"operationAmount": {"currency": {"name": "USD", "code": "USD"}}}

    with pytest.raises(
        ValueError, match="Transaction must contain 'amount' and 'currency' keys."
    ):
        convert_currency(transaction)


def test_convert_currency_missing_currency():
    transaction = {
        "operationAmount": {"amount": "100.00"}  # amount должен быть строкой
    }

    with pytest.raises(
        ValueError, match="Transaction must contain 'amount' and 'currency' keys."
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
