import pytest
from list_revers.list_revers import Node


def test_reverse():
    node0 = Node(0)
    node1 = Node(7)
    node0.next = node1
    node2 = Node(14)
    node1.next = node2
    node3 = Node(21)
    node2.next = node3
    node4 = Node(28)
    node3.next = node4
    node5 = Node(35)
    node4.next = node5
    node6 = Node(42)
    node5.next = node6
    node7 = Node(49)
    node6.next = node7
    node8 = Node(56)
    node7.next = node8
    node9 = Node(63)
    node8.next = node9
    node0.reverse(node0)
    assert node9.next == node8
    assert node8.next == node7
    assert node7.next == node6
    assert node6.next == node5
    assert node5.next == node4
    assert node4.next == node3
    assert node3.next == node2
    assert node2.next == node1
