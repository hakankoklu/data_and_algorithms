class BinaryHeap():
    """Class for a min-heap"""

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_up(self, index):
        if index/2 == 0:
            return
        else:
            if self.heap_list[index] < self.heap_list[index/2]:
                tmp = self.heap_list[index/2]
                self.heap_list[index/2] = self.heap_list[index]
                self.heap_list[index] = tmp
                self.perc_up(index/2)

    def print_heap(self):
        print(self.heap_list)

class MaxHeap:
    """Class for a max-heap, all implemented from CLRS"""

    def __init__(self):
        self.heap_list = [0]  # do not use the index 0 to make sure heap math holds
        self.current_size = 0

    def insert(self, item):
        self.current_size += 1
        if self.current_size > 1:
            self.heap_list.append(-999999)
            self.increase_key(self.current_size, item)
        else:
            self.heap_list.append(item)
        print(self.heap_list)

    def increase_key(self, ind, key):
        if self.heap_list[ind] > key:
            raise ValueError('New key is smaller!!')
        self.heap_list[ind] = key
        while ind > 1 and self.heap_list[ind // 2] < self.heap_list[ind]:
            tmp = self.heap_list[ind // 2]
            self.heap_list[ind // 2] = self.heap_list[ind]
            self.heap_list[ind] = tmp
            ind = ind // 2

    def max_heapify(self, ind):
        lind = 2 * ind
        rind = 2 * ind + 1
        largest = ind
        if lind <= self.current_size and self.heap_list[lind] > self.heap_list[largest]:
            largest = lind
        if rind <= self.current_size and self.heap_list[rind] > self.heap_list[largest]:
            largest = rind
        if largest != ind:
            tmp = self.heap_list[ind]
            self.heap_list[ind] = self.heap_list[largest]
            self.heap_list[largest] = tmp
            self.max_heapify(largest)

    def heapsort(self):
        for ind in range(self.current_size, 1, -1):
            tmp = self.heap_list[1]
            self.heap_list[1] = self.heap_list[self.current_size]
            self.heap_list[self.current_size] = tmp
            self.current_size -= 1
            self.max_heapify(1)


def build_max_heap(random_list):
    h = MaxHeap()
    h.heap_list = [0] + random_list
    h.current_size = len(random_list)
    for ind in range(h.current_size//2, 0, -1):
        h.max_heapify(ind)
    return h