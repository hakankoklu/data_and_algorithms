"""Element present in a tree"""


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


def isPresent(root, val):
    if root.value == val:
        return 1
    elif val < root.value:
        if root.left is None:
            return 0
        return isPresent(root.left, val)
    else:
        if root.right is None:
            return 0
        return isPresent(root.right, val)


if __name__ == '__main__':
    arr = [1, 2, 3, 5, 6, 9, 12, 13, 16, 20, 23, 27, 34, 39, 41]
    t = make_tree(arr)
    print(isPresent(t, 5))
    print(isPresent(t, 40))
    print(isPresent(t, 34))
