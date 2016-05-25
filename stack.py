class Stack():

    def __init__(self):
        self.bucket = []

    def push(self, item):
        self.bucket.append(item)

    def pop(self):
        if len(self.bucket) > 0:
            return self.bucket.pop()
        else:
            return None

    def is_empty(self):
        return len(self.bucket) == 0

    def size(self):
        return len(self.bucket)

    def peek(self):
        if len(self.bucket) > 0:
            return self.bucket[-1]
        else:
            return None
