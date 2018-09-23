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

    def put(self, key, value):

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
        if node == self.most_recent:
            return
        elif node == self.least_recent:
            node.prev.next = node.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.most_recent.prev = node
        node.next = self.most_recent
        node.prev = None
        self.most_recent = node


if __name__ == '__main__':
    aa = ["LRUCache","put","put","get","put","get","put","get","get","get"]
    bb = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    c = LRUCache(2)
    for b in bb:
        if len(b) == 1:
            c.get(*b)
        else:
            c.put(*b)
