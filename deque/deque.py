# Deque: A deque.
# Your implementation should pass the tests in test_deque.py.
# Julian Canepa

from llist import dllist

class Deque:
    def __init__(self):
        self.items = 0
        self.data = dllist()

    def enqueue_left(self, item):
        self.data.appendleft(item)
        self.items += 1

    def enqueue_right(self, item):
        self.data.appendright(item)
        self.items += 1

    def dequeue_left(self):
        if self.is_empty():
            raise ValueError()
        self.items -= 1
        return self.data.popleft()

    def dequeue_right(self):
        if self.is_empty():
            raise ValueError()
        self.items -= 1
        return self.data.popright()

    def size(self):
        return self.items

    def is_empty(self):
        return self.items == 0