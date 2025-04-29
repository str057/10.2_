import pytest
from AAALLL.masks import get_mask_account

@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        ("1234567890123456789", "Проверьте правильность введенного номера счета!"),
        ("123456789012345678901", "Проверьте правильность введенного номера счета!"),
        ("abcdefghabcdefgh", "Проверьте правильность введенного номера счета!"),
        ("", "Проверьте правильность введенного номера счета!"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected