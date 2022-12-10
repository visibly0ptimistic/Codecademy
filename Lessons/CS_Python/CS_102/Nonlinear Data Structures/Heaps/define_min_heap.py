# Define MinHeap below...
class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

# Make an instance of MinHeap
heap = MinHeap()
# Print out the internal list
print(heap.heap_list)