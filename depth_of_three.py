def get_tree_height(root):
    if root is None:
        return -1
    return max(get_tree_height(root.left), get_tree_height(root.right)) + 1
