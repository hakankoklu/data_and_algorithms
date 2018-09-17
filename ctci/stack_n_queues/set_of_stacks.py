"""Imagine a literal stack of plates. If the stack gets too high, it might topple so we would like to start a
new stack after a threshold. Implement a data structure SetOfStacks that does this. It will be composed of several
stacks and should create a new stack once the previous exceeds capacity. Push and pop should behave as expected
from a single stack. Follow up: Implement a popAt function that performs a pop operation on a specific sub-stack.
"""


class SetOfStacks:

    def __init__(self, height):
        self.max_height = height
        self.stacks = [[]]

    def push(self, value):
        if len(self.stacks[-1]) == self.max_height:
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if len(self.stacks[-1]) > 0:
            result = self.stacks[-1].pop()
        else:
            raise ValueError("Stacks are empty!")
        if len(self.stacks[-1]) == 0 and len(self.stacks) != 1:
            self.stacks.pop()
        return result

    def pop_at(self, stack_no):
        if stack_no >=len(self.stacks) or len(self.stacks[stack_no]) == 0:
            raise ValueError("Stack does not exist or empty")
        if len(self.stacks[stack_no]) == 1 and len(self.stacks) != 1:
            return self.stacks.pop(stack_no).pop()
        return self.stacks[stack_no].pop()