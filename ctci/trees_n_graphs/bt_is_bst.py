"""Implement a function to check if a binary tree is a binary search tree."""

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def make_tree(arr):
    # print('making tree from: ', arr)
    if len(arr) == 1:
        n = Node(arr[0])
        return n
    root_ind = len(arr) // 2
    n = Node(arr[root_ind])
    n.left = make_tree(arr[:root_ind])
    n.right = make_tree(arr[root_ind + 1:]) if root_ind + 1 < len(arr) else None
    return n


def is_bst(root):
    return _is_bst(root)


def _is_bst(root, lower=None, upper=None):
    if root is None:
        return True
    # print('checking (root.value, lower, upper): ', root.value, lower, upper)
    if lower is None and upper is None:
        return _is_bst(root.left, None, root.value) and _is_bst(root.right, root.value, None)
    elif lower is None:
        return root.value < upper and _is_bst(root.left, None, root.value) and _is_bst(root.right, root.value, upper)
    elif upper is None:
        return root.value > lower and _is_bst(root.left, lower, root.value) and _is_bst(root.right, root.value, None)
    else:
        return lower < root.value < upper and _is_bst(root.left, lower, root.value) and _is_bst(root.right, root.value, upper)


arr = [1,2,3,5,6,9,12,13,16,20,23,27,34,39, 41]
t = make_tree(arr)
t.right.left.right.value = 28
print(is_bst(t))