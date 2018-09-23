""""""


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


def serialize_tree(root):
    stack = [root]
    arr = []
    while stack:
        node = stack.pop()
        if node:
            arr.append(str(node.value))
            stack.append(node.right)
            stack.append(node.left)
        else:
            arr.append('N')
    return ' '.join(arr)


def deserialize(s):
    return _deserialize(s.split())


def _deserialize(arr):
    if len(arr) == 0:
        return None
    root_value = arr.pop(0)
    if root_value == 'N':
        return None
    root = Node(root_value)
    root.left = _deserialize(arr)
    root.right = _deserialize(arr)
    return root


if __name__ == '__main__':
    arr = [1, 2, 3, 5, 6, 9, 12, 13, 16, 20, 23, 27, 34, 39, 41]
    t = make_tree(arr)
    s = serialize_tree(t)
    print(s)
    tt = deserialize(s)
    print(tt.value)
