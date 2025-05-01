import unittest
from AAALLL.src.masks_log import get_mask_account


class TestMasks(unittest.TestCase):

    def test_get_mask_account(self):
        self.assertEqual(get_mask_account("12345678901234567890"), "**7890")
        self.assertEqual(
            get_mask_account("1234567890123456789"),
            "Проверьте правильность введенного номера счета!",
        )
        self.assertEqual(
            get_mask_account("abcdefghabcdefgh"),
            "Проверьте правильность введенного номера счета!",
        )
        self.assertEqual(
            get_mask_account(""), "Проверьте правильность введенного номера счета!"
        )


if __name__ == "__main__":
    unittest.main()
