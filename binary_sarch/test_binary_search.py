import pytest
from binary_search.binary_search import binary_search


def test_binary_search():
    assert binary_search([9, 4, 2, 1, 5, 7, 6, 8], 8) == 7
    assert binary_search([9, 111, 245, 1, 75, 756, 6, 8111], 9) == 0
    assert binary_search([678, 4123, 255, 179, 523, 700, 612, 856], 700) == 5
