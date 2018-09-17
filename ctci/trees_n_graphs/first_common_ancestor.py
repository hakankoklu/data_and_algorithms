"""Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing
additional nodes in a data structure. This is not necessarily a BST."""

class Node:
    """ class with children and parent links"""

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


def make_tree(arr):
    if len(arr) == 1:
        n = Node(arr[0])
        return n
    root_ind = len(arr) // 2
    n = Node(arr[root_ind])
    left = make_tree(arr[:root_ind])
    left.parent = n
    n.left = left
    right = make_tree(arr[root_ind + 1:]) if root_ind + 1 < len(arr) else None
    if right:
        right.parent = n
        n.right = right
    return n

def get_depth(node):
    depth = 0
    while node.parent is not None:
        node = node.parent
        depth += 1
    return depth


def first_common_ancestor(node1, node2):
    """Follow parent link to find depth, get the deeper one to the same level, then go up together until
    you find the ancestor"""
    node1_depth = get_depth(node1)
    node2_depth = get_depth(node2)
    if node1_depth > node2_depth:
        for _ in range(node1_depth - node2_depth):
            node1 = node1.parent
    elif node2_depth > node1_depth:
        for _ in range(node2_depth - node1_depth):
            node2 = node2.parent
    while node1 != node2:
        node1 = node1.parent
        node2 = node2.parent
    return node1

arr = [1,2,3,5,6,9,12,13,16,20,23,27,34,39, 41]
t = make_tree(arr)
node1 = t.left.left.left
node2 = t.left.left.right
print(first_common_ancestor(node1, node2).value)