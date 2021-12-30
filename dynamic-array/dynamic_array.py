'''
DynamicArray: An array that grows to accommodate new elements.
Implementation must pass all tests in test_dynamic_array.py.
Julian Canepa
'''

import numpy as np

class DynamicArray:

    def __init__(self):
        self.capacity = 10
        self.length = 0
        self.next_index = 0
        # Underlaying data structure is numpy.ndarray
        self.data = np.empty(
            shape=(self.capacity,),
            dtype=object)

    def __len__(self):
        return self.length

    def __str__(self):
        return self.data

    def __getitem__(self, index):
        if index not in range(self.capacity):
            raise IndexError(
                'index '+ str(index) +
                ' is out of bounds for array with size ' +
                str(self.capacity))
        return self.data[index]

    def __str__(self):
        array = []
        for item in self.data:
            array.append(str(item))
        return str(array)

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.capacity == self.length

    def append(self, value):
        if self.is_full():
            self.resize_array()
        self.data[self.next_index] = value
        self.update_state_after_element_added()

    def clear(self):
        self.data = np.empty(
            shape=(self.capacity,),
            dtype=object)
        self.length = 0
        self.next_index = 0

    def pop(self):
        if self.is_empty():
            raise IndexError(
                'cannot remove element from array with no length')
        last_element = self.data[self.get_last_index()]
        self.delete(self.get_last_index())
        return last_element

    def delete(self, index):
        if index not in range(self.capacity - 1) or self.is_empty():
            raise IndexError(
                'index '+ str(index) +
                ' is out of bounds for array with length ' +
                str(self.length))
        self.data[index] = None
        self.shift_elements_left(index)
        self.update_state_after_element_removed()

    def insert(self, index, value):
        if index not in range(self.capacity - 1):
            raise IndexError(
                'index '+ str(index) +
                ' is out of bounds for array with size ' +
                str(self.capacity))
        if self.is_full():
            self.resize_array()
        self.shift_elements_right(index)
        self.data[index] = value
        self.update_state_after_element_added()

    def max(self):
        if self.is_empty():
            return None
        max = 0
        for i in range(self.length):
            if self.data[i] > max:
                max = self.data[i]
        return max

    def min(self):
        if self.is_empty():
            return None
        min = self.data[self.get_last_index()]
        for i in range(self.length):
            if self.data[i] < min:
                min = self.data[i]
        return min

    def sum(self):
        if self.is_empty():
            return None
        sum = 0
        for i in range(self.length):
            sum += self.data[i]
        return sum

    def linear_search(self, value):
        for i in range(self.length):
            if self.data[i] == value:
                return i
        return None

    def binary_search(self, value):
        left = 0
        right = self.get_last_index()
        return self.binary_search_recursive(
            value,
            left,
            right)

    """
    # Class helper methods
    """

    def binary_search_recursive(self, value, left, right):
        if (left > right):
            return None

        middle_index = (left + right) // 2
        middle_value = self.data[middle_index]

        if middle_value == value:
            return middle_index

        if value < middle_value:
            return self.binary_search_recursive(value, left, middle_index - 1)

        return self.binary_search_recursive(value, middle_index + 1, right)

    def resize_array(self):
        self.capacity *= 2

        new_array = np.empty(
            shape=(self.capacity,),
            dtype=object)

        for i in range(self.length):
            new_array[i] = self.data[i]

        self.data = new_array

    def shift_elements_left(self, start):
        index = start
        for el in self.data[start + 1:self.get_last_index() + 1]:
            self.data[index] = el
            index += 1

            if index == self.get_last_index():
                self.data[self.get_last_index()] = None

    def shift_elements_right(self, start):
        next = self.data[start]
        for i in range(start, self.length):
            # retain the next element
            after = self.data[i + 1]
            # replace the next index
            self.data[i + 1] = next
            # update next (value that was just overwritten)
            next = after

    def get_last_index(self):
        return self.length - 1

    def update_state_after_element_removed(self):
        self.length -= 1
        self.next_index -= 1

    def update_state_after_element_added(self):
        self.length += 1
        self.next_index += 1
