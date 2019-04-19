class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_depth(root):
    if root is None:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print(max_depth(root))
