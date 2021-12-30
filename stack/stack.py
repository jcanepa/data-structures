# A stack data structure that passes all tests in stack.py.
# @author Julian Canepa

class Stack:
    def __init__(self):
        self._items = []

    # the stack is empty
    def is_empty(self) -> bool:
        return not bool(self._items)

    # remove the top item and return it
    def pop(self) -> 'object':
        if self.is_empty():
            raise IndexError('pop from empty stack')
        return self._items.pop()

    # return the top item
    def peek(self) -> 'object':
        return self._items[-1]

    # add an item to the stack
    def push(self, item:object):
        self._items.append(item)