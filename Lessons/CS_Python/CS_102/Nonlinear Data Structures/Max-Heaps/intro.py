class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

# HEAP HELPER METHODS
# DO NOT CHANGE!

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

# END OF HEAP HELPER METHODS

    def add(self, element):
        self.count += 1
        print("Adding: {0} to {1}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Heapifying up")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent < child:
                print("swapping {0} with {1}".format(parent, child))
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        print("Heap Restored {0}".format(self.heap_list))

    def retrieve_max(self):
        if self.count == 0:
            print("No items in heap")
            return None   
        max_val = self.heap_list[1]
        print("Removing: {0} from {1}".format(max_val, self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print("Last element moved to first: {0}".format(self.heap_list))    
        return max_val

# import random number generator
from random import randrange

# make an instance of MaxHeap
max_heap = MaxHeap()

# populate max_heap with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
    max_heap.add(el)