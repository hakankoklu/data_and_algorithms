from queue import Queue

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

    def print_tree_in_order(self):
        if self.left_child != None:
            self.left_child.print_tree_in_order()
        if self.key != None:
            print self.key
        if self.right_child != None:
            self.right_child.print_tree_in_order()

    def print_tree_pre_order(self):
        if self.key != None:
            print self.key
        if self.left_child != None:
            self.left_child.print_tree_pre_order()
        if self.right_child != None:
            self.right_child.print_tree_pre_order()

    def print_tree_post_order(self):
        if self.left_child != None:
            self.left_child.print_tree_post_order()
        if self.right_child != None:
            self.right_child.print_tree_post_order()
        if self.key != None:
            print self.key

    def print_tree_level_order(self):
        q = Queue()
        q.enqueue(self)
        while not q.is_empty():
            current_node = q.dequeue()
            print current_node.get_root()
            if current_node.get_left_child():
                q.enqueue(current_node.get_left_child())
            if current_node.get_right_child():
                q.enqueue(current_node.get_right_child())

    def print_tree_zigzag_order(self):
        q_zigzag = []
        q_zigzag.append([self])
        direction = 1
        while len(q_zigzag) > 0:
            current_arr = q_zigzag.pop(0)
            if direction == 1:
                for i in current_arr:
                    print i.get_root()
            else:
                current_arr.reverse()
                for i in current_arr:
                    print i.get_root()
                current_arr.reverse()
            direction = -1*direction
            children = []
            for node in current_arr:
                if node.get_left_child():
                    children.append(node.get_left_child())
                if node.get_right_child():
                    children.append(node.get_right_child())
            if len(children) > 0:
                q_zigzag.append(children)

    def clean_tree(self):
        if self.key == -1:
            self.key=None
        if self.get_left_child() != None:
            self.get_left_child().clean_tree()
        if self.get_right_child() != None:
            self.get_right_child().clean_tree()
