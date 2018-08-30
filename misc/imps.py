from misc.stack import Stack
from misc.queue import Queue
from misc.binarytree import BinaryTree

def par_checker(text):
    par_stack = Stack()
    chars = list(text)
    for let in chars:
        if let == '(':
            par_stack.push(1)
        elif let == ')':
            if par_stack.is_empty():
                return False
            else:
                par_stack.pop()
    return par_stack.is_empty()

def hot_potato(people, num):
    peep_queue = Queue(people)
    while peep_queue.size() > 1:
        for i in range(num):
            peep_queue.enqueue(peep_queue.dequeue())
        peep_queue.dequeue()
    return peep_queue.dequeue()

def parse_par_expression(expression):
    exp_list = list(expression)
    root_tree = BinaryTree('')
    par_stack = Stack()
    current_node = root_tree
    for let in exp_list:
        if let == '(':
            par_stack.push(current_node)
            current_node.insert_left_child(BinaryTree(''))
            current_node = current_node.get_left_child()
        elif let in '1234567890':
            current_node.set_root(let)
            current_node = par_stack.pop()
        elif let in '+-*/':
            current_node.set_root(let)
            current_node.insert_right_child(BinaryTree(''))
            par_stack.push(current_node)
            current_node = current_node.get_right_child()
        elif let == ')':
            if par_stack.is_empty():
                return root_tree
            else:
                current_node = par_stack.pop()
    return root_tree

def calculate_tree(thetree):
    key = thetree.get_root()
    if key in '1234567890':
        return int(thetree.get_root())
    else:
        if key == '+':
            return calculate_tree(thetree.get_left_child()) + calculate_tree(thetree.get_right_child())
        if key == '-':
            return calculate_tree(thetree.get_left_child()) - calculate_tree(thetree.get_right_child())
        if key == '*':
            return calculate_tree(thetree.get_left_child()) * calculate_tree(thetree.get_right_child())
        if key == '/':
            return calculate_tree(thetree.get_left_child()) / calculate_tree(thetree.get_right_child())
