import pytest
from max_node_in_stack.max_node_in_stack import Stack


def test_get_max_item():
    a = Stack()
    a.push(1)
    a.push(12)
    a.push(3)
    a.push(5)
    a.push(56)
    a.push(1)
    a.push(8)
    a.push(11)
    a.push(9)
    assert a.get_max_item() == 56
