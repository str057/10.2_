import unittest
from src.transaction_operation import filter_transactions_by_amount, summarize_transactions, group_transactions_by_description


class TestTransactionOperations(unittest.TestCase):

    def setUp(self):
        # Создаем тестовые данные
        self.transactions = [
            {"description": "Salary", "amount": 5000},
            {"description": "Groceries", "amount": 150},
            {"description": "Utilities", "amount": 200},
            {"description": "Salary", "amount": 3000},
            {"description": "Entertainment", "amount": 100},
        ]

    def test_filter_transactions_by_amount(self):
        # Тестируем фильтрацию транзакций
        filtered = filter_transactions_by_amount(self.transactions, 200)
        self.assertEqual(len(filtered), 4)  # Ожидаем 4 транзакции

    def test_summarize_transactions(self):
        # Тестируем суммирование транзакций
        summary = summarize_transactions(self.transactions)
        self.assertEqual(
            summary["total_amount"], 5000 + 150 + 200 + 3000 + 100
        )  # Ожидаем общую сумму
        self.assertEqual(summary["transaction_count"], 5)  # Ожидаем 5 транзакций

    def test_group_transactions_by_description(self):
        # Тестируем группировку транзакций
        grouped = group_transactions_by_description(self.transactions)
        self.assertEqual(len(grouped), 4)  # Ожидаем 4 уникальных описания
        self.assertIn("Salary", grouped)  # Проверяем, что 'Salary' в группировке
        self.assertEqual(len(grouped["Salary"]), 2)
