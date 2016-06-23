#
#       3
#      / \
#     2   -1
#    / \
#   5  4
#  / \
# -3  -5
# Path: from one node to any other node 5 - 2 (7),   5 - 2 - 4 (11), 4 - 2 - 3 (9)

# Not valid path 5 2 4 3

# Goal: find the maximum sum path for binary tree with integers on each node

# paths = [[5,2], [5,2,3], [5,2,4], [5,2,3,-1]]
# to_look = []
# pop = [-1, [5,2,3,-1]]

import itertools

class BinaryTree():

    def __init__(self, root):
        self.root = root

class TreeNode():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def get_key(self):
        return self.key

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_parent(self):
        return self.parent

    def set_left_child(self, ll):
        self.left = ll
        ll.set_parent(self)

    def set_right_child(self, rr):
        self.right = rr
        rr.set_parent(self)

    def set_parent(self, pp):
        self.parent = pp

    def get_connections(self):
        return [self.left, self.right, self.parent]

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.left is None and self.right is None

def check_path(node_list):
    current = node_list[0]
    for node in node_list[1:]:
        if current.get_left_child() == node:
            current = node
        elif current.get_right_child() == node:
            current = node
        elif current.get_parent() == node:
            current = node
        else:
            return False
    return True

def calculate_sum(node_list):
    running_sum = 0
    for node in node_list:
        running_sum += node.get_key()
    return running_sum

def turn_tree_to_list(binary_tree):
    node_list = []
    to_look = []
    root = binary_tree.root
    node_list.append(root)
    to_look.append(root)
    while len(to_look) != 0:
        current_node = to_look.pop(0)
        if current_node.get_left_child() is not None:
            node_list.append(current_node.get_left_child())
            to_look.append(current_node.get_left_child())
        if current_node.get_right_child() is not None:
            node_list.append(current_node.get_right_child())
            to_look.append(current_node.get_right_child())
    return node_list

def check_all_paths(node_list):
    all_paths = []
    if len(node_list) == 1:
        return node_list[0].get_key()
    max_sum = node_list[0].get_key() + node_list[1].get_key()
    for i in range(2,len(node_list)+1):
        all_paths.extend(itertools.permutations(node_list, i))
    for path in all_paths:
        if check_path(path):
            temp_sum = calculate_sum(path)
            if temp_sum > max_sum:
                max_sum == temp_sum
    return max_sum

def make_paths_bfs(node):
    paths = []
    quu = []
    temp_nodes = node.get_connections()
    for temp_node in temp_nodes:
        if temp_node is not None:
            paths.append([node, temp_node])
            quu.append([temp_node, [node, temp_node]])
    while len(quu) > 0:
        temp = quu.pop(0)
        temp_nodes = temp[0].get_connections()
        for temp_node in temp_nodes:
            if temp_node is not None and temp_node != temp[1][-2]:
                new_path = []
                new_path.extend(temp[1])
                new_path.append(temp_node)
                paths.append(new_path)
                quu.append([temp_node, new_path])
    return paths

node5 = TreeNode(5)
node4 = TreeNode(4)
node_1 = TreeNode(-1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node3.set_left_child(node2)
node3.set_right_child(node_1)
node2.set_left_child(node5)
node2.set_right_child(node4)

thetree = BinaryTree(node3)
node_list = turn_tree_to_list(thetree)
all_paths = []
for node in node_list:
    paths = make_paths_bfs(node)
    all_paths.extend(paths)

maxx = 0
for path in all_paths:
    bb = calculate_sum(path)
    maxx = max(maxx, bb)
print maxx

# onsite: find the local minima in an array of distinct integers in log(n) time
