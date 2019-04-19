import pytest
from depth_of_three.depth_of_three import Node, max_depth


def test_depth_of_three():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    assert max_depth(root) == 3
