"""Implement a MyQueue class which implements a queue using two stacks."""

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


class MyQueue:

    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, value):
        if self.enqueue_stack.is_empty():
            self._flip_stacks()
        self.enqueue_stack.push(value)

    def dequeue(self):
        if self.dequeue_stack.is_empty():
            self._flip_stacks()
        if self.dequeue_stack.is_empty():
            raise ValueError("The queue is empty")
        return self.dequeue_stack.pop()

    def _flip_stacks(self):
        if self.enqueue_stack.is_empty() and not self.dequeue_stack.is_empty():
            while not self.dequeue_stack.is_empty():
                self.enqueue_stack.push(self.dequeue_stack.pop())
        elif not self.enqueue_stack.is_empty() and self.dequeue_stack.is_empty():
            while not self.enqueue_stack.is_empty():
                self.dequeue_stack.push(self.enqueue_stack.pop())