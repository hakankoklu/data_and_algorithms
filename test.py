from binarytree import BinaryTree
from stack import Stack

def serialize(some_tree):
    result = []
    result.append(some_tree.get_root())
    if some_tree.get_left_child() == None:
        result.append(-1)
    else:
        result.extend(serialize(some_tree.get_left_child()))
    if some_tree.get_right_child() == None:
        result.append(-1)
    else:
        result.extend(serialize(some_tree.get_right_child()))
    return result

def deserialize(some_list):
    par_stack = Stack()
    count = 0
    result = BinaryTree(some_list[count])
    par_stack.push(result)
    count += 1
    while not par_stack.is_empty():
        if par_stack.peek().left_child == None:
            par_stack.peek().left_child = BinaryTree(some_list[count])
            if some_list[count] != -1:
                par_stack.push(par_stack.peek().left_child)
            count += 1
        elif par_stack.peek().right_child == None:
            par_stack.peek().right_child = BinaryTree(some_list[count])
            if some_list[count] != -1:
                par_stack.push(par_stack.peek().right_child)
            count += 1
        else:
            par_stack.pop()
    return result

aa = BinaryTree(1)
aa.insert_left_child(2)
aa.insert_right_child(3)
aa.get_right_child().insert_left_child(4)
aa.get_right_child().insert_right_child(5)
print 'original'
aa.print_tree()
ss = serialize(aa)
print 'serialized'
print ss
bb = deserialize(ss)
bb.clean_tree()
print 'deserialized'
bb.print_tree()
