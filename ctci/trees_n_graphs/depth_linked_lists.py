"""Given a binary tree, design an algorithm which creates a linked list of all the nodes at each
depth (if you have a tree with depth D, you’ll have D linked lists)."""


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def print_list(self):
        print(self.value)
        if self.next:
            self.next.print_list()


class LinkedList:

    def __init__(self, head):
        self.head = head


def make_tree(arr):
    if len(arr) == 1:
        n = Node(arr[0])
        return n
    root_ind = len(arr) // 2
    n = Node(arr[root_ind])
    n.left = make_tree(arr[:root_ind])
    n.right = make_tree(arr[root_ind + 1:]) if root_ind + 1 < len(arr) else None
    return n


def make_lists(root):
    q = [(root, 0)]
    ptr = 0
    while ptr < len(q):
        current_node, level = q[ptr]
        ptr += 1
        if current_node.left:
            q.append((current_node.left, level + 1))
        if current_node.right:
            q.append((current_node.right, level + 1))
    current_level = None
    current_list_node = None
    current_list = None
    lists = []
    for current_node, level in q:
        if level != current_level:
            if current_list:
                lists.append(current_list)
            current_list_node = ListNode(current_node.value)
            current_list = LinkedList(current_list_node)
            current_level = level
        else:
            current_list_node.next = ListNode(current_node.value)
            current_list_node = current_list_node.next
    lists.append(current_list)
    return lists

arr = [1,2,3,5,6,9,12,13,16,20,23,27,34,39, 41]
t = make_tree(arr)
ll = make_lists(t)
print(ll)
count = 0
for l in ll:
    print('List no: ', count)
    count += 1
    l.head.print_list()