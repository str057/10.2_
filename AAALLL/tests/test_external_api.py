from unittest.mock import patch
import os
import pytest
import requests
from AAALLL.src.external_api import convert_currency  # Замените на правильный путь к вашему модулю


def test_convert_currency_usd():
    transaction = {"amount": 100, "currency": "USD"}
    mock_response = {"rates": {"RUB": 75.0}}

    with patch("AAALLL.src.external_api.requests.get") as mock_get:  # Обновите путь здесь
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        os.environ["API_KEY"] = "test_api_key"  # Установите переменную окружения

        result = convert_currency(transaction)
        assert result == 7500.0  # 100 * 75.0


def test_convert_currency_eur():
    transaction = {"amount": 100, "currency": "EUR"}
    mock_response = {"rates": {"RUB": 85.0}}

    with patch("AAALLL.src.external_api.requests.get") as mock_get:  # Обновите путь здесь
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        os.environ["API_KEY"] = "test_api_key"  # Установите переменную окружения

        result = convert_currency(transaction)
        assert result == 8500.0  # 100 * 85.0


def test_convert_currency_invalid_api():
    transaction = {"amount": 100, "currency": "USD"}

    with patch("AAALLL.src.external_api.requests.get") as mock_get:  # Обновите путь здесь
        mock_get.side_effect = requests.RequestException("API error")
        os.environ["API_KEY"] = "test_api_key"  # Установите переменную окружения

        with pytest.raises(RuntimeError, match="Error fetching exchange rate: API error"):
            convert_currency(transaction)
