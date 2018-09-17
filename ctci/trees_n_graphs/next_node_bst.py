"""Write an algorithm to find the next node of a given node on a binary search tree . You may assume that each node
has a link to its parent.
"""


class TreeNode:

    def __init__(self, value, parent=None , left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class BST:

    def __init__(self, root=None):
        self.root = root

    def next_node(self, node):
        # it has a right subtree
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current
        # it is a left node without a right subtree
        elif node.parent.left == node:
            return node.parent
        # it is a right node without a right subtree
        else:
            current = node.parent
            while current.parent is not None and current.parent.left != current:
                current = current.parent
            if current == self.root:
                return None
            return current.parent

# n5 = TreeNode(5)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n6 = TreeNode(6)
# n7 = TreeNode(7)
# n8 = TreeNode(8)
# n10 = TreeNode(10)
# n5.left = n3;n5.right = n8;n3.parent = n5;n8.parent = n5
# n3.left = n2;n3.right = n4;n2.parent = n3;n4.parent = n3
# n8.left = n6;n8.right = n10; n6.parent = n8; n10.parent = n8
# n6.right = n7;n7.parent = n6