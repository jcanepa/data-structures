# Queue: A queue.
# Your implementation should pass the tests in test_queue.py.
# Julian Canepa

from llist import sllist

class Queue:
    def __init__(self):
        self.items = 0
        self.data = sllist()

    def enqueue(self, item):
        self.data.append(item)
        self.items += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError()

        self.items -= 1
        return self.data.popleft()

    def is_empty(self):
        return self.items == 0

    def size(self):
        return self.items