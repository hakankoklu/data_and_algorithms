"""Design an ID allocator which can allocate and de-allocate from a range of 1-1,000,000"""


class IDAllocator:

    def __init__(self, size):

        self.free_ids = set()
        self.used_ids = set()
        self.last_id = -1
        self.size = size

    def get_id(self):
        if self.free_ids:
            self.last_id = id = self.free_ids.pop()
            self.used_ids.add(id)
            return id
        id = (self.last_id + 1) % self.size
        if id in self.used_ids:
            raise ValueError("No id available")
        else:
            self.last_id = id
            self.used_ids.add(id)
            return id

    def release_id(self, some_id):
        if some_id in self.used_ids:
            self.used_ids.remove(some_id)
            self.free_ids.add(some_id)


if __name__ == '__main__':
    ia = IDAllocator(4)
    ids = []
    ids.append(ia.get_id())
    ids.append(ia.get_id())
    ia.release_id(1)
    ids.append(ia.get_id())
    ia.release_id(2)
    ids.append(ia.get_id())
    ids.append(ia.get_id())
    ids.append(ia.get_id())
    ids.append(ia.get_id())