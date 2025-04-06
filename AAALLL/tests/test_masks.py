import pytest
from AAALLL.src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("123456781234567", "Проверьте правильность введенного номера карты!"),
        ("12345678123456789", "Проверьте правильность введенного номера карты!"),
        ("abcdefghabcdefgh", "Проверьте правильность введенного номера карты!"),
        ("", "Проверьте правильность введенного номера карты!"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        ("1234567890123456789", "Проверьте правильность введенного номера карты!"),
        ("123456789012345678901", "Проверьте правильность введенного номера карты!"),
        ("abcdefghabcdefgh", "Проверьте правильность введенного номера карты!"),
        ("", "Проверьте правильность введенного номера карты!"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
