import unittest
from AAALLL.src.external_api import convert_currency, long_function_name


class TestExternalAPI(unittest.TestCase):

    def test_convert_currency(self):
        # Тестирование конвертации валюты
        self.assertAlmostEqual(convert_currency(100, 1.2), 120.0)
        self.assertAlmostEqual(convert_currency(50, 0.5), 25.0)
        self.assertAlmostEqual(convert_currency(0, 1.5), 0.0)
        self.assertAlmostEqual(convert_currency(100, 0), 0.0)

    def test_long_function_name(self):
        # Тестирование функции с длинными аргументами
        result = long_function_name("arg1", "arg2", "arg3", "arg4", "arg5", "arg6")
        self.assertEqual(result, "arg1arg2arg3arg4arg5arg6")


if __name__ == "__main__":
    unittest.main()
