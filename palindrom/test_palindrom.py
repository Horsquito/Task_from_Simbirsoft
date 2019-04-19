import pytest
from palindrom.palindrom import is_palindrom


def test_is_palindrom():
    assert is_palindrom('мадам')
    assert is_palindrom('потоп')
    assert is_palindrom('заказ')
