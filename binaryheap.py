class BinaryHeap():

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
        print self.heap_list
