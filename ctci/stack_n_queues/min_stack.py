"""Design a stack which has a function min in addition to push and pop, all should operate in O(1) time.
"""

class MinStack:

    def __init__(self):
        self.stack_min = None
        self.stack = []

    def push(self, num):
        self.stack_min = min(num, self.stack_min) if self.stack_min else num
        self.stack.append((num, self.stack_min))

    def pop(self):
        if self.stack:
            result = self.stack.pop()[0]
            self.stack_min = self.stack[-1][1] if self.stack else None
            return result
        else:
            raise ValueError("The stack is empty")

    def min(self):
        return self.stack_min
