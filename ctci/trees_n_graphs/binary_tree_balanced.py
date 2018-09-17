"""Implement a function to check if a binary tree is balanced. For this question, a balanced tree is a tree such that
the heights of the two subtrees of any node never differ by more than one."""


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


def is_tree_balanced(root):
    queue = [(root, 0)]
    ptr = 0
    depths = set()
    while ptr < len(queue):
        node, depth = queue[ptr]
        print("Checking node: ", node.value, depth)
        print("Depths so far: ", depths)
        if node.left is None and node.right is None:
            for d in depths:
                if abs(depth - d) > 1:
                    return False
            depths.add(depth)
        else:
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        ptr += 1
    return True


arr = [1,2,3,5,6,9,12,13,16,20,23,27,34,39, 41]
t = make_tree(arr)
# t.left.left = None
# t.left.right = None
print(is_tree_balanced(t))
