import sys
import os
import unittest
from unittest.mock import patch
import pandas as pd

# Добавьте путь к папке src в начало sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from finance_reader import (
    read_financial_operations_from_csv,
    read_financial_operations_from_excel,
)  # Импортируйте модуль


class TestFinanceOperations(unittest.TestCase):
    @patch("pandas.read_csv")
    def test_read_financial_operations_from_csv(self, mock_read_csv):
        # Настройка mock
        mock_data = pd.DataFrame(
            {
                "id": [650703],
                "state": ["EXECUTED"],
                "date": ["2023-09-05T11:30:32Z"],
                "amount": [16210],
                "currency_name": ["Sol"],
                "currency_code": ["PEN"],
                "from": ["Счет 58803664561298323391"],
                "to": ["Счет 39745660563456619397"],
                "description": ["Перевод организации"],
            }
        )
        mock_read_csv.return_value = mock_data

        result = read_financial_operations_from_csv("dummy_path.csv")
        expected = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

        self.assertEqual(result, expected)

    @patch("pandas.read_excel")
    def test_read_financial_operations_from_excel(self, mock_read_excel):
        # Настройка mock
        mock_data = pd.DataFrame(
            {
                "id": [650703],
                "state": ["EXECUTED"],
                "date": ["2023-09-05T11:30:32Z"],
                "amount": [16210],
                "currency_name": ["Sol"],
                "currency_code": ["PEN"],
                "from": ["Счет 58803664561298323391"],
                "to": ["Счет 39745660563456619397"],
                "description": ["Перевод организации"],
            }
        )
        mock_read_excel.return_value = mock_data

        result = read_financial_operations_from_excel("dummy_path.xlsx")
        expected = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
