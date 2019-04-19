class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def reverse(self, node, previous_value=None):
        if node.next is not None:
            self.reverse(node.next, previous_value=node)
        node.next = previous_value
