"""You have two very large binary trees, T1 with millions of nodes and T2 with hundreds of nodes. Create an algorithm
to to decide if T2 is a subtree of T1. T2 is a subtree of T1 if there exists a node n in T1 such that the subtree
of n is identical to T2. If you cut off the tree at node n, the two trees would be identical."""

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def equals(self, other):
        return self.value == other.value


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


def subtree(t1, t2):
    