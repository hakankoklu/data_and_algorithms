"""You are given a binary tree in which each node contains a value. Design an algorithm to print all paths which
sum to a given value. The path does not need to start or end at the root or a leaf."""

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


def get_parent_map(root):
    stack = [root]
    parent_map = {}
    while stack:
        current = stack.pop()
        if current.left:
            parent_map[current.left] = current
            stack.append(current.left)
        if current.right:
            parent_map[current.right] = current
            stack.append(current.right)
    return parent_map


def get_path(node1, node2, parents):
    node1_root_path = get_root_path(node1, parents)
    node2_root_path = get_root_path(node2, parents)
    node1_root_path.reverse()
    node2_root_path.reverse()
    count = 0
    for n1, n2 in zip(node1_root_path, node2_root_path):
        if n1 != n2:
            break
        count += 1
    # check if direct ancestor
    if n1 == n2:
        if len(node1_root_path) > len(node2_root_path):
            path = node1_root_path[count - 1:]
        else:
            path = node2_root_path[count - 1:]
    else:
        path = node1_root_path[count:]
        path.reverse()
        node2_partial = node2_root_path[count - 1:]
        path.extend(node2_partial)
    return path


def get_path_sum(path):
    return sum([x.value for x in path])


def get_root_path(node, parents):
    path = [node]
    current = node
    while current in parents.keys():
        current = parents[current]
        path.append(current)
    return path


def get_all_nodes(tree):
    stack = [tree]
    nodes = []
    while stack:
        node = stack.pop()
        nodes.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return nodes


def get_sum_paths(tree, target):
    nodes = get_all_nodes(tree)
    parents = get_parent_map(tree)
    result = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            path = get_path(nodes[i], nodes[j], parents)
            if get_path_sum(path) == target:
                result.append(path)
    for node in nodes:
        if node.value == target:
            result.append([node])
    return result


arr = [1,2,3,5,6,9,12,13,16,20,23,27,34,39, 41]
t = make_tree(arr)
paths = get_sum_paths(t, 28)
for path in paths:
    print([x.value for x in path])