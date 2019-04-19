import pytest
from sum_of_numbers.sum_of_numbers import find_sum


def test_find_sum():
    assert find_sum([1, 2, 3, 4, 11], 12)
