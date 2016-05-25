class TreeNode():

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return not self.left_child == None

    def has_right_child(self):
        return not self.right_child == None

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return self.parent == None

    def is_leaf(self):
        return not self.has_any_children()

    def has_any_children(self):
        return self.left_child != None or self.right_child != None

    def has_both_children(self):
        return self.left_child != None and self.right_child != None

    def print_tree(self):
        if self.left_child != None:
            self.left_child.print_tree()
        print self.key
        if self.right_child != None:
            self.right_child.print_tree()

class BinarySearchTree():

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def put(self, key, value):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self._put(key, value, self.root)
        self.size += 1

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
        elif key > current_node.key:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)
        else:
            current_node.paylod = value

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if current_node == None:
            return None
        if key == current_node.key:
            return current_node
        elif key < current_node.key:
            if current_node.has_left_child():
                return self._get(key, current_node.left_child)
            else:
                return None
        else:
            if current_node.has_right_child():
                return self._get(key, current_node.right_child)
            else:
                return None

    def print_tree(self):
        if self.root:
            self.root.print_tree()
