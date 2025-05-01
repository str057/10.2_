import unittest
from AAALLL.src.external_api import convert_currency


class TestExternalAPI(unittest.TestCase):

    def test_convert_currency_usd(self):
        self.assertAlmostEqual(convert_currency(100, 1.2), 120.0)

    def test_convert_currency_eur(self):
        self.assertAlmostEqual(convert_currency(50, 0.85), 42.5)

    def test_convert_currency_invalid_currency(self):
        with self.assertRaises(TypeError):
            convert_currency(100, "invalid_rate")  # Пример вызова с неправильным типом


if __name__ == "__main__":
    unittest.main()
