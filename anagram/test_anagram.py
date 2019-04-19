import pytest
from anagram.anagram import is_anagram


def test_is_anagram():
    assert is_anagram("кабан", "банка")
    assert is_anagram("мышка", "камыш")
    assert is_anagram("кукла", "кулак")
