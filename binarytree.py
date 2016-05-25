class BinaryTree():

    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def insert_left_child(self, new_node):
        new_left_child = BinaryTree(new_node)
        if self.left_child:
            new_left_child.left_child = self.left_child
            self.left_child = new_left_child
        else:
            self.left_child = new_left_child

    def insert_right_child(self, new_node):
        new_right_child = BinaryTree(new_node)
        if self.right_child:
            new_right_child.right_child = self.right_child
            self.right_child = new_right_child
        else:
            self.right_child = new_right_child

    def get_root(self):
        return self.key

    def set_root(self, new_key):
        self.key = new_key

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def print_tree(self):
        if self.left_child != None:
            self.left_child.print_tree()
        if self.key != None:
            print self.key
        if self.right_child != None:
            self.right_child.print_tree()

    def clean_tree(self):
        if self.key == -1:
            self.key=None
        if self.get_left_child() != None:
            self.get_left_child().clean_tree()
        if self.get_right_child() != None:
            self.get_right_child().clean_tree()
