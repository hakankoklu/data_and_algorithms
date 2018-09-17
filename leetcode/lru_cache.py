"""LRU Cache"""


class ListNode:

    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0
        self.cache = {}
        self.least_recent = None
        self.most_recent = None

    def add(self, key, value):

        if self.current_size == 0:
            node = ListNode(key, value)
            self.least_recent = node
            self.most_recent = node
            self.cache[key] = node
            self.current_size += 1
        elif self.current_size < self.max_size:
            if key in self.cache:
                self.make_most_recent(key)
            else:
                node = ListNode(key, value)
                self.most_recent.prev = node
                node.next = self.most_recent
                self.most_recent = node
                self.cache[key] = node
                self.current_size += 1
        elif self.current_size == self.max_size:
            self.cache.pop(self.least_recent.key)
            self.least_recent.prev.next = None
            self.least_recent = self.least_recent.prev
            node = ListNode(key, value)
            self.most_recent.prev = node
            node.next = self.most_recent
            self.most_recent = node
            self.cache[key] = node

    def get(self, key):
        if key in self.cache:
            self.make_most_recent(key)
            return self.cache[key]
        return None

    def make_most_recent(self, key):
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.most_recent.prev = node
        node.next = self.most_recent
        node.prev = None
        self.most_recent = node


l = LRUCache(5)
print(l.most_recent, l.least_recent)
l.add(1, 11)
print(l.most_recent.key, l.least_recent.key)
l.add(2, 12)
print(l.most_recent.key, l.least_recent.key)
l.add(3, 13)
print(l.most_recent.key, l.least_recent.key)
l.add(4, 14)
print(l.most_recent.key, l.least_recent.key)
l.add(5, 15)
print(l.most_recent.key, l.least_recent.key)
l.get(2)
print(l.most_recent.key, l.least_recent.key)
l.add(6, 16)
print(l.most_recent.key, l.least_recent.key)
l.get(5)
print(l.most_recent.key, l.least_recent.key)
l.add(7, 17)
print(l.cache, l.most_recent.key, l.least_recent.key)
