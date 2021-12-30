# MaxHeap: A binary 'max' heap.
# @author Julian Canepa

class MaxHeap:
    def __init__(self) -> None:
        self._data = []

    def _size(self) -> int:
        return len(self._data)

    def _is_empty(self) -> bool:
        return self._size() == 0

    def _last_index(self):
        return self._size() - 1

    def _value_at(self, index):
        return self._data[index]

    def _left_child_index(self, index) -> int:
        return (index * 2) + 1

    def _right_child_index(self, index) -> int:
        return (index * 2) + 2

    def _parent_index(self, index) -> int:
        return (index - 1) // 2

    def _parent(self, index):
        return self._data[
            self._parent_index(index)]

    def _left_child(self, index):
        if self._index_is_out_of_bounds(
            self._left_child_index(index)):
            return None

        return self._data[
            self._left_child_index(index)]

    def _right_child(self, index):
        if self._index_is_out_of_bounds(
            self._right_child_index(index)):
            return None

        return self._data[
            self._right_child_index(index)]

    def _return_single_child(self, index):
        if self._has_left_child(index):
            return self._left_child(index)

        return self._right_child(index)

    def _index_is_out_of_bounds(self, index) -> bool:
        return (index < 0) \
            or (index >= len(self._data))

    def _has_left_child(self, index) -> bool:
        return not self._left_child(index) is None

    def _has_right_child(self, index) -> bool:
        return not self._right_child(index) is None

    def _greater_child_index(self, index) -> int:
        """
        Return the index of the nodes child with the highest priority.
        """
        if not self._has_left_child(index):
            return None

        if not self._has_right_child(index):
            return self._left_child_index(index)

        # both children are set, compare their values and return the largest
        left = self._left_child_index(index)
        right = self._right_child_index(index)

        return left if \
            self._data[left] > self._data[right] \
            else right

    def _obeys_heap_property_at_index(self, index) -> bool:
        """
        Is faithful to the binary heap order property that says for (max) binary heaps,
        for every node x with parent p, the key in p is larger than or equal to the key in x
        """
        if self._index_is_out_of_bounds(index):
            return False

        if self._has_left_child(index) and \
            self._data[index] < self._data[
                self._greater_child_index(index)]:
            return False

        return True

    def _swap(self, index_a, index_b) -> None:
        """
        Switch two elements in an array.
        """
        self._data[index_a], self._data[index_b] = \
            self._data[index_b], self._data[index_a]

    def _sift_down(self, index):
        """
        aka "percolate down", "bubble down"
        Element swaps down levels in the tree until it is less than both children.
        Continues until it obeys the heap property.
        """
        if self._obeys_heap_property_at_index(index):
            return None

        if not self._has_left_child(index):
            return None

        greatest_child_index = self._greater_child_index(index)
        self._swap(index, greatest_child_index)
        return self._sift_down(greatest_child_index)

    def _sift_up(self, index):
        """
        aka "percolate", "bubble up"
        Element percolates up the tree as far as needed to maintain
        the heap order property.
        """
        if self._obeys_heap_property_at_index(
            self._parent_index(index)):
            return None

        if index == 0:
            return None

        self._swap(index, self._parent_index(index))
        return self._sift_up(
            self._parent_index(index))

    def insert(self, value):
        """
        Add a new element to the end of the list, then percolating up as needed.
        """
        self._data.append(value)
        self._sift_up(self._last_index())

    def delete(self, index=0):
        """
        Delete the root node by replacing it with the last node,
        bubbling down the new root as needed. Return deleted node.
        """
        if self._is_empty() or \
            self._index_is_out_of_bounds(index):
            return None

        deleted = self._data[0]
        self._data[0] = self._data[
            self._last_index()]
        self._data.pop(
            self._last_index())

        if not self._obeys_heap_property_at_index(0):
            self._sift_down(0)

        return deleted