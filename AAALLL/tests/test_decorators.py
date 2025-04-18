import logging
import pytest
from ..src.decorators import add, divide


def test_add(caplog):
    with caplog.at_level(logging.INFO):
        result = add(1, 2)
    assert result == 3
    assert "add ok" in caplog.text


def test_divide(caplog):
    with caplog.at_level(logging.INFO):
        result = divide(4, 2)
    assert result == 2.0
    assert "divide ok" in caplog.text


def test_divide_by_zero(caplog):
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ZeroDivisionError):
            divide(1, 0)
    assert "divide error: division by zero" in caplog.text
