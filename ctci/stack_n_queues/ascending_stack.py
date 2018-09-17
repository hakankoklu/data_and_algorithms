"""Write a program to sort a stack in ascending order (biggest on top). You may use another stack to hold
items but no other data structure (array, etc.) The stack supports: push, pop, peek, isEmpty
"""

class Stack:

    def __init__(self, arr=None):
        if arr:
            self.stack = arr
        else:
            self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        return self.stack == []


def sort_ascending(stack):
    flip_stack = Stack()
    result_stack = Stack()
    while not stack.is_empty():
        current = stack.pop()
        if result_stack.is_empty() or result_stack.peek() <= current:
            result_stack.push(current)
        else:
            while not result_stack.is_empty() and result_stack.peek() > current:
                flip_stack.push(result_stack.pop())
            result_stack.push(current)
            while not flip_stack.is_empty():
                result_stack.push(flip_stack.pop())
    return result_stack
