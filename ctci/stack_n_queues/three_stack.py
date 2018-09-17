"""Describe how you could use a single array to implement three stacks"""

class ThreeStack:

    def __init__(self, size):
        size = max(10, size)
        self.container = [None] * size
        self.top_next = 0
        self.bottom_next = len(self.container) - 1
        self.mid_next = size // 3
        self.mid_start = self.mid_next

    def push(self, num, stack_no):
        """stack_no 1, 2, 3 refers to top, bottom and mid respectively"""
        if not 1 <= stack_no <= 3:
            raise ValueError("I can only serve to stacks 1,2 or 3")
        if stack_no == 1:
            if not self.container[self.top_next]:
                print("push normally")
                self.container[self.top_next] = num
                self.top_next += 1
            elif self.mid_next <= self.bottom_next:
                print("need to move the middle")
                to_shift = max(1, (self.bottom_next - self.mid_next) // 3)
                self._move_middle(to_shift)
                self.container[self.top_next] = num
                self.top_next += 1
            else:
                ValueError("Stacks are full")
        elif stack_no == 2:
            if not self.container[self.bottom_next]:
                print("push normally")
                self.container[self.bottom_next] = num
                self.bottom_next -= 1
            elif self.top_next < self.mid_start:
                print("need to move the middle")
                to_shift = max(1, (self.mid_start - self.top_next) // 2)
                self._move_middle(-1 * to_shift)
                self.container[self.bottom_next] = num
                self.bottom_next -= 1
            else:
                ValueError("Stacks are full")
        elif stack_no == 3:
            if not self.container[self.mid_next]:
                print("push normally")
                self.container[self.mid_next] = num
                self.mid_next += 1
            elif self.top_next < self.mid_start:
                print("need to move the middle")
                to_shift = max(1, (self.mid_start - self.top_next) // 2)
                self._move_middle(-1 * to_shift)
                self.container[self.mid_next] = num
                self.mid_next += 1
            else:
                ValueError("Stacks are full")

    def pop(self, stack_no):
        if not 1 <= stack_no <= 3:
            raise ValueError("I can only serve to stacks 1,2 or 3")
        else:
            result = None
            if stack_no == 1 and self.top_next > 0:
                self.top_next -= 1
                result = self.container[self.top_next]
                self.container[self.top_next] = None
            elif stack_no == 2 and self.bottom_next < len(self.container) - 1:
                self.bottom_next += 1
                result = self.container[self.bottom_next]
                self.container[self.bottom_next] = None
            elif stack_no == 3 and self.mid_next > self.mid_start:
                self.mid_next -= 1
                result = self.container[self.mid_next]
                self.container[self.mid_next] = None
            return result

    def _move_middle(self, to_shift):
        print(f"Moving middle {to_shift} amount")
        if to_shift > 0:
            for i in range(self.mid_next - 1, self.mid_start - 1, -1):
                self.container[i + to_shift] = self.container[i]
            for i in range(to_shift):
                self.container[self.mid_start + i] = None
            self.mid_start += to_shift
            self.mid_next += to_shift
        else:
            to_shift *= -1
            for i in range(self.mid_start, self.mid_next):
                self.container[i - to_shift] = self.container[i]
            for i in range(to_shift):
                self.container[self.mid_next - 1 - i] = None
            self.mid_start -= to_shift
            self.mid_next -= to_shift
