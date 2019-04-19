import pytest
from bubble_sort.bubble_sort import bubble_sort


def test_buble_sort():
    assert bubble_sort([4, 1, 6, 9, 2, 3, 5, 8, 7]) == [1, 2, 3, 4,
                                                        5, 6, 7, 8, 9]
