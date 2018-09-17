"""Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a
binary search tree with minimal height.
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print(self.value)
        if self.right:
            self.right.print_in_order()

    def print_bfs(self, level=0):
        q = [(level, self, 'root')]
        ptr = 0
        while ptr < len(q):
            current_level, current_node, current_type = q[ptr]
            print(current_level, current_node.value, current_type)
            ptr += 1
            if current_node.left:
                q.append((current_level + 1, current_node.left, 'left'))
            if current_node.right:
                q.append((current_level + 1, current_node.right, 'right'))


def make_tree(arr):
    print('making tree from: ', arr)
    if len(arr) == 1:
        n = Node(arr[0])
        return n
    root_ind = len(arr) // 2
    n = Node(arr[root_ind])
    n.left = make_tree(arr[:root_ind])
    n.right = make_tree(arr[root_ind + 1:]) if root_ind + 1 < len(arr) else None
    return n

arr = [1,2,3,5,6,9,12,13,16,20,23,27,34,39, 41]
print('arr_len: ', len(arr))
t = make_tree(arr)
t.print_bfs()