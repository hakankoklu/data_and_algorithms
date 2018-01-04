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

# proposed solution:
# - every node is connected to every other node and there is only one path
# between two nodes
# - for every pair of nodes, find the path and compare with max
# - how to find the path between two nodes:
#  - every two node shares a parent or nth-grand-parent or they are direct descendant of each other
#  - from each node go up to root and find the first intersection 
#  - make the path by connecting them thru that

class TreeNode():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

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


def turn_tree_to_list(root):
    node_list = []
    to_look = []
    node_list.append(root)
    to_look.append(root)
    while len(to_look) != 0:
        current_node = to_look.pop(0)
        if current_node.left is not None:
            node_list.append(current_node.left)
            to_look.append(current_node.left)
        if current_node.right is not None:
            node_list.append(current_node.right)
            to_look.append(current_node.right)
    return node_list


def get_all_pairs(list_of_nodes):
    return make_pairs([], list_of_nodes)


def make_pairs(current_list, list_of_nodes):
    if len(list_of_nodes) == 1:
        return current_list
    current = list_of_nodes.pop(0)
    for node in list_of_nodes:
        current_list.append((current, node))
    return make_pairs(current_list, list_of_nodes)


def get_path_to_root(node):
    parent = node.parent
    nodes = [node]
    while parent is not None:
        nodes.append(parent)
        parent = parent.parent
    return nodes


def get_path(node1, node2):
    node1_root_path = get_path_to_root(node1)
    parent = node2
    node2_list = []
    while parent not in node1_root_path:
        node2_list.append(parent)
        parent = parent.parent
    node2_list.reverse()
    path = node1_root_path[:node1_root_path.index(parent) + 1]
    path.extend(node2_list)
    return path


def calculate_sum(node_list):
    return sum([node.key for node in node_list])


def get_max(root):
    node_list = turn_tree_to_list(root)
    all_pairs = get_all_pairs(node_list)
    all_paths = [get_path(*pair) for pair in all_pairs]
    return max([calculate_sum(path) for path in all_paths])

node_5 = TreeNode(-5)
node_3 = TreeNode(-3)
node5 = TreeNode(5)
node5.set_left_child(node_3)
node5.set_right_child(node_5)
node4 = TreeNode(4)
node2 = TreeNode(2)
node2.set_left_child(node5)
node2.set_right_child(node4)
node_1 = TreeNode(-1)
node3 = TreeNode(3)
node3.set_left_child(node2)
node3.set_right_child(node_1)