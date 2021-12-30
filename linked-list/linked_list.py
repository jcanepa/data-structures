# A doubly-linked circular list using recursion that passes all tests.
# @author Julian Canepa

from typing import Optional


class LinkedList:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = self
        self.prev = self

    # node has no value
    def is_sentinel(self) -> bool:
        return self.value == None

    # list has no other nodes
    def is_empty(self) -> bool:
        return self == self.next and self == self.prev

    # node is last in the list
    def is_last(self) -> bool:
        return self.next.is_sentinel()

    # returns the "tail of the list"
    def last(self) -> 'LinkedList':
        if self.is_sentinel():
            return self.prev
        return self.next.last()

    # returns the sentinel "head" of the list
    def first(self) -> 'LinkedList':
        return self.last().next

    # sentinels can insert a node at the end of the list
    def append(self, node:'LinkedList') -> None:
        if self.is_sentinel():
            node.next = self
            node.prev = self.last()
            node.next.prev = node
            node.prev.next = node

    # a node deletes itself
    def delete(self) -> None:
        self.prev.next = self.next
        self.next.prev = self.prev

    # a node can insert a new node between itself and its next node
    def insert(self, node:'LinkedList') -> None:
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node

    # returns the nth node in the list, where n=0 is the sentinel
    def at(self, n:int, index=0) -> Optional['LinkedList']:
        # nth node found
        if n == index:
            return self

        # nth node not found
        if self.is_last():
            return

        return self.next.at(n, index + 1)

    # search list for a given value and return the node, or None if not found
    def search(self, value:object) -> Optional['LinkedList']:
        if self.value == value:
            return self

        if self.is_last():
            return

        return self.next.search(value)

    # insert node in order with respect to element value
    def insert_in_order(self, node:'LinkedList') -> None:
        if self.is_last():
            return self.insert(node)

        if self.next.value <= node.value:
            return self.next.insert_in_order(node)

        self.insert(node)
