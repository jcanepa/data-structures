# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_max_heap

import unittest
import time
import random
from max_heap import MaxHeap


class TestMaxHeap(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A MaxHeap exists.
        """
        try:
            MaxHeap()
        except NameError:
            self.fail("Could not instantiate MaxHeap.")

    """
    A heap stores its data in an array, such as a Python list.
    """

    def test_internal_data(self):
        """
        A MaxHeap uses an array (a dynamic array / Python list) to store its data.
        """
        h = MaxHeap()
        self.assertEqual(list, type(h._data))
        self.assertEqual(0, len(h._data))

    """
    Size is the number of items in the heap.
    """

    def test_size_initial(self):
        """
        The _size() of a new heap is 0.
        """
        h = MaxHeap()
        self.assertEqual(0, h._size())

    def test_size_data(self):
        """
        The _size() of a heap is equal to the number of values in its list.
        """
        h = MaxHeap()
        h._data.append('fake')
        self.assertEqual(1, h._size())
        h._data.append('fake')
        self.assertEqual(2, h._size())
        h._data.pop()
        self.assertEqual(1, h._size())

    """
    Emptiness. A warm-up. Good to know, and a handy abstraction that you might
    use elsewhere.
    """

    def test_empty_initial(self):
        """
        A new heap is empty.
        Hint: _size is a convenient abstraction, and helps avoid repetitive code.
        """
        h = MaxHeap()
        self.assertTrue(h._is_empty())

    def test_not_empty(self):
        """
        A heap is not empty if there are items in its data list.
        """
        h = MaxHeap()
        h._data.append('fake')
        self.assertFalse(h._is_empty())
        h._data.append('fake')
        self.assertFalse(h._is_empty())

    def test_empty(self):
        """
        A heap with no items in its data list is empty.
        """
        h = MaxHeap()
        h._data.append('fake')
        h._data.append('fake')
        h._data = []
        self.assertTrue(h._is_empty())

    """
    Last index. The index of the last element in the heap.
    Later, when deleting from a heap, the first step in the deletion algorithm
    moves the last element to the root position. So this will be handy.
    """

    def test_last_index_initial(self):
        """
        The 'last index' of an empty heap happens to be -1.
        Hint: Easy to calculate if you know its size.
        """
        h = MaxHeap()
        self.assertEqual(-1, h._last_index())

    def test_last_index_one(self):
        """
        The last index of a heap with one element is 0.
        Hint: Easy, if you know how to determine the last index of a list.
        """
        h = MaxHeap()
        h._data.append('fake')
        self.assertEqual(0, h._last_index())

    def test_last_index_two(self):
        """
        The last index of a heap with two elements is 1.
        """
        h = MaxHeap()
        h._data.append('fake')
        h._data.append('fake')
        self.assertEqual(1, h._last_index())

    def test_last_index_42(self):
        """
        The last index of a heap with forty-two elements is 41.
        """
        h = MaxHeap()
        for _ in range(42):
            h._data.append('fake')
        self.assertEqual(41, h._last_index())

    """
    Value at an index. It's handy to grab a value at a particular index, so lets
    encapsulate this work into a method.
    """

    def test_value_at_zero(self):
        """
        The value at index 0 is the value of the 0th item in the heap's data list.
        """
        h = MaxHeap()
        value = fake_value()
        h._data.append(value)
        self.assertEqual(value, h._value_at(0))

    def test_value_at(self):
        """
        The value at index i is the value of the i'th item in the heap's data list.
        """
        h = MaxHeap()
        value = fake_value()
        h._data.append(value)
        self.assertEqual(value, h._value_at(0))
        value = fake_value()
        h._data.append(value)
        self.assertEqual(value, h._value_at(1))
        for i in range(2, 9):
            value = fake_value()
            h._data.append(value)
            self.assertEqual(value, h._value_at(i))

    def test_value_at_invalid_index(self):
        """
        _value_at raises an IndexError when the index is out of bounds.
        """
        h = MaxHeap()
        self.assertRaises(IndexError, h._value_at, 0)
        h._data.append('fake')
        self.assertRaises(IndexError, h._value_at, 1)
        self.assertRaises(IndexError, h._value_at, 2)

    """
    Indexes of left child, right child, and parent.
    A heap stores values linearly in a list, but it's really a tree. The root is
    at 0, and its left child is at index 1, and its right child is at index 2.
    The element at index 1 has a left child at index 3, and a right at index 4.
    The element at index 2 has a left child at index 5, and a right at index 6.
    What's the formula for this?
    Hint: Draw it out.
    """

    def test_left_child_index(self):
        """
        An element at index i has a left child at index ____.
        Hint: Know how the heap works. Look up and study the concept.
        """
        h = MaxHeap()
        # This method just calculates the index. It doesn't care about the data.
        self.assertEqual(1, h._left_child_index(0))
        self.assertEqual(3, h._left_child_index(1))
        self.assertEqual(5, h._left_child_index(2))
        self.assertEqual(7, h._left_child_index(3))
        self.assertEqual(8675309, h._left_child_index(4337654))

    def test_right_child_index(self):
        """
        An element at index i has a right child at index ____.
        Hint: Know how the heap works. Look up and study the concept.
        """
        h = MaxHeap()
        # This method just calculates the index. It doesn't care about the data.
        self.assertEqual(2, h._right_child_index(0))
        self.assertEqual(4, h._right_child_index(1))
        self.assertEqual(6, h._right_child_index(2))
        self.assertEqual(8, h._right_child_index(3))
        self.assertEqual(5446, h._right_child_index(2722))

    def test_parent_index(self):
        """
        An element at index i has a parent at index ___.
        Hints: Work this out instead of looking it up. Draw it.
               And, use integer division for natural flooring.
               Watch your order of operations.
        """
        h = MaxHeap()
        # This first one is nonsense, but is here for completeness.
        self.assertEqual(-1, h._parent_index(0))
        # The root's left child is at 1, so its parent is at index 0.
        self.assertEqual(0, h._parent_index(1))
        # The root's right child is at 2, so its parent is at index 0.
        self.assertEqual(0, h._parent_index(2))
        self.assertEqual(1, h._parent_index(3))
        self.assertEqual(1, h._parent_index(4))
        self.assertEqual(2, h._parent_index(5))
        self.assertEqual(2, h._parent_index(6))
        self.assertEqual(3, h._parent_index(7))
        self.assertEqual(4337654, h._parent_index(8675309))
        self.assertEqual(2722, h._parent_index(5446))

    """
    Left child, right child, and parent _values_.
    Now that we know that calculating the left, right and parent indexes given
    any element's index, retrieving the values there is easy.
    Hint: Use your previous abstractions. Don't repeat yourself.
    """

    def test_parent(self):
        """
        Given an index i, the parent is the value at the 'parent index' of i.
        Hint: The phrase above is nearly identical to the code, if you use your
              abstractions.
        """
        h = MaxHeap()
        fake_root = fake_value()
        fake_left_child = fake_value()
        fake_right_child = fake_value()
        fake_left_left_child = fake_value()
        fake_left_right_child = fake_value()
        h._data.append(fake_root)
        h._data.append(fake_left_child)
        h._data.append(fake_right_child)
        h._data.append(fake_left_left_child)
        h._data.append(fake_left_right_child)
        self.assertEqual(fake_root, h._parent(1))
        self.assertEqual(fake_root, h._parent(2))
        self.assertEqual(fake_left_child, h._parent(3))
        self.assertEqual(fake_left_child, h._parent(4))

    def test_parent_invalid(self):
        """
        Retrieving the parent value for an index without a parent is invalid.
        """
        h = MaxHeap()
        self.assertRaises(IndexError, h._parent, 0)
        self.assertRaises(IndexError, h._parent, 1)
        self.assertRaises(IndexError, h._parent, 2)
        h._data.append('fake')
        try:
            h._parent(1)
            h._parent(2)
        except IndexError:
            self.fail("Could not retrieve parent properly.")
        for i in range(3, 9):
            self.assertRaises(IndexError, h._parent, i)

    def test_left_child_none(self):
        """
        If the 'left child index' of an element at index i exceeds the bounds of
        the data list, just return None.
        Hint: Draw both a 5-element array and tree. What is the value of the left
              child of the third (index 2) element? And the fourth? And the fifth?
        """
        h = MaxHeap()
        h._data.append('fake')
        h._data.append('fake')
        h._data.append('fake')
        self.assertIsNone(h._left_child(1))
        self.assertIsNone(h._left_child(2))
        h._data.append('fake')
        h._data.append('fake')
        self.assertIsNone(h._left_child(2))
        self.assertIsNone(h._left_child(3))
        self.assertIsNone(h._left_child(4))

    def test_left_child(self):
        """
        Given an index i, the left child is the value at the 'left child index'
        of i.
        Hint: The phrase above is nearly identical to the code, if you use your
              abstractions.
        """
        h = MaxHeap()
        fake_root = fake_value()
        fake_left_child = fake_value()
        fake_right_child = fake_value()
        fake_left_left_child = fake_value()
        fake_left_right_child = fake_value()
        h._data.append(fake_root)
        h._data.append(fake_left_child)
        h._data.append(fake_right_child)
        h._data.append(fake_left_left_child)
        h._data.append(fake_left_right_child)
        self.assertEqual(fake_left_child, h._left_child(0))
        self.assertEqual(fake_left_left_child, h._left_child(1))
        self.assertIsNone(h._left_child(2))
        self.assertIsNone(h._left_child(3))
        self.assertIsNone(h._left_child(4))

    def test_right_child_none(self):
        """
        If the 'right child index' of an element at index i exceeds the bounds of
        the data list, just return None.
        Hint: Draw both a 5-element array and tree. What is the value of the right
              child of the third (index 2) element? And the fourth? And the fifth?
        """
        h = MaxHeap()
        h._data.append('fake')
        h._data.append('fake')
        h._data.append('fake')
        self.assertIsNone(h._right_child(2))
        h._data.append('fake')
        h._data.append('fake')
        self.assertIsNone(h._right_child(2))
        self.assertIsNone(h._right_child(3))
        self.assertIsNone(h._right_child(4))

    def test_right_child(self):
        """
        Given an index i, the right child is the value at the 'right child index'
        of i.
        Hint: The phrase above is nearly identical to the code, if you use your
              abstractions.
        """
        h = MaxHeap()
        fake_root = fake_value()
        fake_left_child = fake_value()
        fake_right_child = fake_value()
        fake_left_left_child = fake_value()
        fake_left_right_child = fake_value()
        h._data.append(fake_root)
        h._data.append(fake_left_child)
        h._data.append(fake_right_child)
        h._data.append(fake_left_left_child)
        h._data.append(fake_left_right_child)
        self.assertEqual(fake_right_child, h._right_child(0))
        self.assertEqual(fake_left_right_child, h._right_child(1))
        self.assertIsNone(h._right_child(2))
        self.assertIsNone(h._right_child(3))
        self.assertIsNone(h._right_child(4))

    """
    Left child and right child presence. These will be handy later.
    """

    def test_has_left_child(self):
        """
        True when an element's left child isn't None. Otherwise False.
        """
        h = MaxHeap()
        fake_root = fake_value()
        fake_left_child = fake_value()
        fake_right_child = fake_value()
        fake_left_left_child = fake_value()
        fake_left_right_child = fake_value()
        h._data.append(fake_root)
        h._data.append(fake_left_child)
        h._data.append(fake_right_child)
        h._data.append(fake_left_left_child)
        h._data.append(fake_left_right_child)
        self.assertTrue(h._has_left_child(0))
        self.assertTrue(h._has_left_child(1))
        self.assertFalse(h._has_left_child(2))
        self.assertFalse(h._has_left_child(3))
        self.assertFalse(h._has_left_child(4))

    def test_has_right_child(self):
        """
        True when an element's right child isn't None. Otherwise False.
        """
        h = MaxHeap()
        fake_root = fake_value()
        fake_left_child = fake_value()
        fake_right_child = fake_value()
        fake_left_left_child = fake_value()
        h._data.append(fake_root)
        h._data.append(fake_left_child)
        h._data.append(fake_right_child)
        h._data.append(fake_left_left_child)
        self.assertTrue(h._has_right_child(0))
        self.assertFalse(h._has_right_child(1))
        self.assertFalse(h._has_right_child(2))
        self.assertFalse(h._has_right_child(3))
        self.assertFalse(h._has_right_child(4))

    """
    Index of the greater child.
    When we remove the root of a MaxHeap, we move the last element in the data
    list to the root position. Then, the new root gets 'pushed down' its left
    branch or its right branch. Which branch? The branch that is 'led' by the child
    with the greater value. Remember, a binary heap is not a bst: the rule is
    only that both children must be smaller than their parent.
    Therefore, it's handy to be able to determine the index of the larger child.
    """

    def test_greater_child_index_one(self):
        """
        The 'greater child index' of an element without children is None.
        """
        h = MaxHeap()
        h._data.append('fake')
        self.assertIsNone(h._greater_child_index(0))

    def test_greater_child_index_left_only(self):
        """
        The 'greater child index' of an element with just a left child (no right
        child) returns the index of that left child.
        """
        h = MaxHeap()
        h._data.append('fake')
        h._data.append('fake')
        self.assertEqual(1, h._greater_child_index(0))

    def test_greater_child_index_left(self):
        """
        The 'greater child index' of an element with a left and right child, is
        the index of the left child when it has a value greater than or equal to
        the right child.
        """
        h = MaxHeap()
        h._data.append(10)
        h._data.append(5)
        h._data.append(1)
        self.assertEqual(1, h._greater_child_index(0))

    def test_greater_child_index_right(self):
        """
        The 'greater child index' of an element with a left and right child, is
        the index of the right child when it has a larger value than the left child.
        Hint: Refine your logic. What are the possible states? No children, a
              left but no right, or a left and a right.
        """
        h = MaxHeap()
        h._data.append(10)
        h._data.append(1)
        h._data.append(5)
        self.assertEqual(2, h._greater_child_index(0))

    """
    The max-heap property. Obey.
    A MaxHeap has one rule that makes it a MaxHeap: An item in the tree has a
    value that is greater than (or equal to) both its left and right children.
    We care about this 'locally', meaning, given an index i, we verify that the
    value at i is greater than its left child value and its right child value.
    This is not recursive! Checking the whole tree is not the job of this method.
    It only checks the max-heap property at a given index, by checking the value
    at that index and the values of the immediate children at that index.
    """

    def test_heap_property_one(self):
        """
        A heap with one element obeys the max-heap property.
        """
        h = MaxHeap()
        h._data.append('fake')
        self.assertTrue(h._obeys_heap_property_at_index(0))

    def test_heap_property_two_violate(self):
        """
        A heap with two elements, with a parent value less than its left child's
        value violates the max-heap property.
        """
        h = MaxHeap()
        h._data.append(5)
        h._data.append(10)
        # Index 0 (root / value 5) has a child with a value 10, so it violates.
        self.assertFalse(h._obeys_heap_property_at_index(0))
        # No children at 1, so it obeys here:
        self.assertTrue(h._obeys_heap_property_at_index(1))

    def test_heap_property_two_obey(self):
        """
        A heap with two elements, with a parent value greater than its left
        child's value obeys the max-heap property.
        """
        h = MaxHeap()
        h._data.append(10)
        h._data.append(5)
        self.assertTrue(h._obeys_heap_property_at_index(0))
        self.assertTrue(h._obeys_heap_property_at_index(1))

    def test_heap_property_three_violate(self):
        """
        A heap with three elements, with a parent value less than its right
        child's value or its left child's value violates the max-heap property.
        Hint: Refine your logic. What are the possible states? No children,
        a left child, or both a left and right child.
        """
        h = MaxHeap()
        h._data.append(10)
        h._data.append(5)
        h._data.append(42)
        self.assertFalse(h._obeys_heap_property_at_index(0))
        self.assertTrue(h._obeys_heap_property_at_index(1))
        self.assertTrue(h._obeys_heap_property_at_index(2))
        h._data = []
        h._data.append(10)
        h._data.append(42)
        h._data.append(5)
        self.assertFalse(h._obeys_heap_property_at_index(0))
        self.assertTrue(h._obeys_heap_property_at_index(1))
        self.assertTrue(h._obeys_heap_property_at_index(2))

    def test_heap_property_three_obey(self):
        """
        A heap with three elements, with a parent value greater than its left
        child's value and its right child's value obeys the max-heap property.
        Hint: Refine your logic. What are the possible states? No children,
        a left child, or both a left and right child.
        """
        h = MaxHeap()
        h._data.append(10)
        h._data.append(5)
        h._data.append(1)
        self.assertTrue(h._obeys_heap_property_at_index(0))
        self.assertTrue(h._obeys_heap_property_at_index(1))
        self.assertTrue(h._obeys_heap_property_at_index(2))
        h._data = []
        h._data.append(10)
        h._data.append(1)
        h._data.append(5)
        self.assertTrue(h._obeys_heap_property_at_index(0))
        self.assertTrue(h._obeys_heap_property_at_index(1))
        self.assertTrue(h._obeys_heap_property_at_index(2))

    """
    Swap. Given the indexes of two items, swap their positions in the data list.
    This swaps their position in the conceptual tree. We'll only ever use it to
    swap a child with its parent, or vice-versa. But, this method shouldn't care.
    """

    def test_swap(self):
        """
        Given an index a and an index b, swapping a with b moves b's value to a
        and a's value to b.
        Hint: A classic algorithm. Three lines.
        """
        h = MaxHeap()
        h._data.append(10)
        h._data.append(5)
        h._data.append(1)
        h._swap(0, 1)
        self.assertEqual(5, h._data[0])
        self.assertEqual(10, h._data[1])
        h._swap(0, 2)
        self.assertEqual(1, h._data[0])
        self.assertEqual(5, h._data[2])
        # We'll never swap siblings, but let's make sure swap is simple.
        h._swap(1, 2)
        self.assertEqual(5, h._data[1])
        self.assertEqual(10, h._data[2])

    """
    Sift down. An important heap algorithm.
    When we remove an element from the heap, we always remove the root. We then
    take the last element in the heap and make it the new root. But that new
    root's value will most definitely be smaller than it's childrens' values.
    And we don't want to violate the max-heap property. We rectify this by
    'sifting' or 'pushing' down the new root until it is in a location where it
    is greater than its two children.
    But, what direction do we push the node down: the left or the right?
    The algorithm for a max-heap is that we push down the branch owned by the
    larger child.
    """

    def test_sift_down_one(self):
        """
        Sifting down the root of a single-element heap is easy.
        Hint: Be naive for now.
        """
        h = MaxHeap()
        h._data.append(1)
        h._sift_down(0)
        self.assertEqual(1, h._data[0])

    def test_sift_down_two_stable(self):
        """
        Sifting down an element in a two-element heap, when the element is larger
        than its child, is easy.
        Hint: Be naive for now.
        """
        h = MaxHeap()
        h._data.append(5)
        h._data.append(1)
        # Sifting down the root of this tree doesn't change anything.
        h._sift_down(0)
        self.assertEqual(5, h._data[0])
        self.assertEqual(1, h._data[1])
        # Sifting down the last element of this tree doesn't change anything, either.
        h._sift_down(1)
        self.assertEqual(5, h._data[0])
        self.assertEqual(1, h._data[1])

    def test_sift_down_three_stable(self):
        """
        Sifting down an element in a three-element heap, when the element is larger
        than its children, is easy.
        Hint: Be naive for now.
        """
        h = MaxHeap()
        h._data.append(10)
        h._data.append(5)
        h._data.append(1)
        # Sifting down the root of this tree doesn't change anything.
        h._sift_down(0)
        self.assertEqual(10, h._data[0])
        self.assertEqual(5, h._data[1])
        self.assertEqual(1, h._data[2])
        # Sifting down the second element of this tree doesn't change anything.
        h._sift_down(1)
        self.assertEqual(10, h._data[0])
        self.assertEqual(5, h._data[1])
        self.assertEqual(1, h._data[2])
        # Sifting down the third element of this tree doesn't change anything.
        h._sift_down(2)
        self.assertEqual(10, h._data[0])
        self.assertEqual(5, h._data[1])
        self.assertEqual(1, h._data[2])

    def test_sift_down_two_unstable(self):
        """
        Sifting down an element in a two-element heap, when the element is smaller
        than its child swaps the element with its child.
        Hint: A little more genuine now. Use your abstractions!
        Hint 2: If it obeys the heap property at that index, there's no work to do.
        """
        h = MaxHeap()
        h._data.append(1)
        h._data.append(5)
        # Sifting down the root of this tree swaps it with its child.
        h._sift_down(0)
        self.assertEqual(5, h._data[0])
        self.assertEqual(1, h._data[1])

    def test_sift_down_three_unstable_right(self):
        """
        Sifting down an element in a three-element heap, swaps it with the larger
        of its two children.
        Hint: Review your handy helper methods. And use them.
        """
        h = MaxHeap()
        h._data.append(1)
        h._data.append(5)
        h._data.append(10)
        # Sifting down the root of this tree swaps it with its right child.
        h._sift_down(0)
        self.assertEqual(10, h._data[0])
        self.assertEqual(5, h._data[1])
        self.assertEqual(1, h._data[2])

    # But, in a larger heap, an element may need to be sifted down further than
    # one level. Time to be recursive.

    def test_sift_down_left(self):
        """
        Sifting down an element swaps it with the larger of its two children,
        and continues to sift down that element in its new position and its new
        children, until it is in a position where it obeys the heap property.
        Hint: This might only require one more line of code, if expressed recursively.
        """
        h = MaxHeap()
        h._data.append(2)
        h._data.append(10)
        h._data.append(9)
        h._data.append(5)
        h._data.append(4)
        h._data.append(7)
        h._data.append(6)
        h._data.append(1)
        h._sift_down(0)
        self.assertEqual(10, h._data[0])
        self.assertEqual(5, h._data[1])
        self.assertEqual(9, h._data[2])
        self.assertEqual(2, h._data[3])
        self.assertEqual(4, h._data[4])
        self.assertEqual(7, h._data[5])
        self.assertEqual(6, h._data[6])
        self.assertEqual(1, h._data[7])

    def test_sift_down(self):
        """
        Sifting down an element swaps it with the larger of its two children,
        and continues to sift down that element in its new position and its new
        children, until it is in a position where it obeys the heap property.
        Hint: This might only require one more line of code, if expressed recursively.
        """
        h = MaxHeap()
        h._data.append(2)
        h._data.append(9)
        h._data.append(10)
        h._data.append(5)
        h._data.append(4)
        h._data.append(7)
        h._data.append(6)
        h._data.append(1)
        h._sift_down(0)
        self.assertEqual(10, h._data[0])
        self.assertEqual(9, h._data[1])
        self.assertEqual(7, h._data[2])
        self.assertEqual(5, h._data[3])
        self.assertEqual(4, h._data[4])
        self.assertEqual(2, h._data[5])
        self.assertEqual(6, h._data[6])
        self.assertEqual(1, h._data[7])

    """
    Sift up. The second important heap algorithm.
    When we add a new element to a heap, we always add it as the last element
    in the list. Conceptually, we're adding elements to a tree from the top down,
    and left to right, one level of the tree at a time. Adding a new element to
    a heap adds a new leaf node to the tree. But, that leaf node's value might
    be greater than its parent, which violates the heap property.
    We rectify this by 'sifting up' the new element until it is in a location
    where it is less than its parent.
    """

    def test_sift_up_one(self):
        """
        Sifting up the root is easy.
        Hint: Be naive for now.
        """
        h = MaxHeap()
        h._data.append(1)
        h._sift_up(0)
        self.assertEqual(1, h._data[0])

    def test_sift_up_two_stable(self):
        """
        Sifting up an element in a two-element heap, when the element is smaller
        than its parent, is easy.
        Hint: Be naive for now.
        """
        h = MaxHeap()
        h._data.append(5)
        h._data.append(1)
        # Sifting up the root of this tree doesn't change anything.
        h._sift_up(0)
        self.assertEqual(5, h._data[0])
        self.assertEqual(1, h._data[1])
        # Sifting up the last element of this tree doesn't change anything, either.
        h._sift_up(1)
        self.assertEqual(5, h._data[0])
        self.assertEqual(1, h._data[1])

    def test_sift_up_three_stable(self):
        """
        Sifting up an element in a three-element heap, when the element is smaller
        than its parent, is easy.
        Hint: Be naive for now.
        """
        h = MaxHeap()
        h._data.append(10)
        h._data.append(5)
        h._data.append(1)
        # Sifting up the root of this tree doesn't change anything.
        h._sift_up(0)
        self.assertEqual(10, h._data[0])
        self.assertEqual(5, h._data[1])
        self.assertEqual(1, h._data[2])
        # Sifting up the left leaf of this tree doesn't change anything.
        h._sift_up(1)
        self.assertEqual(10, h._data[0])
        self.assertEqual(5, h._data[1])
        self.assertEqual(1, h._data[2])
        # Sifting up the right leaft of this tree doesn't change anything.
        h._sift_up(2)
        self.assertEqual(10, h._data[0])
        self.assertEqual(5, h._data[1])
        self.assertEqual(1, h._data[2])

    def test_sift_up_two_unstable(self):
        """
        Sifting up an element in a two-element heap, when the element is larger
        than its parent swaps the element with its parent.
        Hint: A little more genuine now. Refine your logic. Use your abstractions.
        """
        h = MaxHeap()
        h._data.append(1)
        h._data.append(5)
        # Sifting up the leaf of this tree swaps it with its parent.
        h._sift_up(1)
        self.assertEqual(5, h._data[0])
        self.assertEqual(1, h._data[1])

    def test_sift_up_three_unstable_left(self):
        """
        Sifting up an element in a three-element heap, when the element is
        larger than its parent, swaps it with its parent.
        """
        h = MaxHeap()
        h._data.append(1)
        h._data.append(10)
        h._data.append(5)
        # Sifting up the left leaf of this tree swaps it with its parent.
        h._sift_up(1)
        self.assertEqual(10, h._data[0])
        self.assertEqual(1, h._data[1])
        self.assertEqual(5, h._data[2])

    def test_sift_up_three_unstable_right(self):
        """
        Sifting up an element in a three-element heap, when the leaf is
        greater than its parent, swaps it with its parent.
        Hint: Refine your logic.
        """
        h = MaxHeap()
        h._data.append(1)
        h._data.append(5)
        h._data.append(10)
        # Sifting up the right leaf of this tree swaps it with its parent.
        h._sift_up(2)
        self.assertEqual(10, h._data[0])
        self.assertEqual(5, h._data[1])
        self.assertEqual(1, h._data[2])

    # But, in a larger heap, an element may need to be sifted up further than
    # one level. Time to be recursive.

    def test_sift_up_to_root(self):
        """
        Sifting up an element swaps it with its parent when appropriate, and
        continues to sift up that element from its new position, until it either
        becomes the root or its parent's value is larger than its value.
        Hint: Think of the stopping condition first.
        """
        h = MaxHeap()
        h._data.append(10)
        h._data.append(9)
        h._data.append(8)
        h._data.append(7)
        h._data.append(6)
        h._data.append(5)
        h._data.append(4)
        h._data.append(3)
        h._data.append(2)
        h._data.append(1)
        h._data.append(42)
        h._sift_up(10)
        self.assertEqual(42, h._data[0])
        self.assertEqual(10, h._data[1])
        self.assertEqual(8, h._data[2])
        self.assertEqual(7, h._data[3])
        self.assertEqual(9, h._data[4])
        self.assertEqual(5, h._data[5])
        self.assertEqual(4, h._data[6])
        self.assertEqual(3, h._data[7])
        self.assertEqual(2, h._data[8])
        self.assertEqual(1, h._data[9])
        self.assertEqual(6, h._data[10])

    def test_sift_up(self):
        """
        Sifting up an element swaps it with its parent when appropriate, and
        continues to sift up that element from its new position, until it either
        becomes the root or its parent's value is larger than its value.
        """
        h = MaxHeap()
        h._data.append(600)
        h._data.append(500)
        h._data.append(8)
        h._data.append(7)
        h._data.append(6)
        h._data.append(5)
        h._data.append(4)
        h._data.append(3)
        h._data.append(2)
        h._data.append(1)
        h._data.append(42)
        h._sift_up(10)
        self.assertEqual(600, h._data[0])
        self.assertEqual(500, h._data[1])
        self.assertEqual(8, h._data[2])
        self.assertEqual(7, h._data[3])
        self.assertEqual(42, h._data[4])
        self.assertEqual(5, h._data[5])
        self.assertEqual(4, h._data[6])
        self.assertEqual(3, h._data[7])
        self.assertEqual(2, h._data[8])
        self.assertEqual(1, h._data[9])
        self.assertEqual(6, h._data[10])

    """
    Inserting a value. It's easy now.
    Adding a value to a heap appends a new element to the end of its data list,
    which is also conceptually adding a new leaf node. After adding the new
    leaf node, the heap must 'sift up' the new leaf in case it has a value larger
    than its parent.
    Hint: Two steps. Add the new value, and sift up. That's it.
    """

    def test_insert_empty(self):
        """
        An empty MaxHeap stores a new value as the root. No algorithms necessary.
        """
        h = MaxHeap()
        h.insert(10)
        self.assertEqual(10, h._data[0])

    def test_insert_smaller_one(self):
        """
        An inserted value that is smaller than the root becomes the left child.
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(5)
        self.assertEqual(10, h._data[0])
        self.assertEqual(5, h._data[1])

    def test_insert_larger_one(self):
        """
        An inserted value that is larger than the root becomes the root, and the
        root becomes the left child.
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(15)
        self.assertEqual(15, h._data[0])
        self.assertEqual(10, h._data[1])

    def test_insert_smaller_two(self):
        """
        An inserted value that is smaller than the root of a two-element MaxHeap
        becomes the right child.
          10           10
         /      =>    /  \
        5            5    1
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(5)
        h.insert(1)
        self.assertEqual(10, h._data[0])
        self.assertEqual(5, h._data[1])
        self.assertEqual(1, h._data[2])

    def test_insert_larger_two(self):
        """
        An inserted value that is larger than the root becomes the new root, and
        the old root becomes the last element in the tree.
          10           15
         /      =>    /  \
        5            5    10
        Hint: Remember, insertion is just two steps. Append the new leaf to the
        end, and sift that new leaf up.
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(5)
        h.insert(15)
        self.assertEqual(15, h._data[0])
        self.assertEqual(5, h._data[1])
        self.assertEqual(10, h._data[2])

    def test_insert_stable(self):
        """
        An inserted value that is smaller than its parent will remain in the new
        leaf position.
          10            10
         /  \   =>    /    \
        8    4       8      4
                    / \    / \
                   3   4  1   2
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(8)
        h.insert(4)
        h.insert(3)
        h.insert(4)
        h.insert(1)
        h.insert(2)
        self.assertEqual(10, h._data[0])
        self.assertEqual(8, h._data[1])
        self.assertEqual(4, h._data[2])
        self.assertEqual(3, h._data[3])
        self.assertEqual(4, h._data[4])
        self.assertEqual(1, h._data[5])
        self.assertEqual(2, h._data[6])

    def test_insert_unstable_three(self):
        """
        An inserted value that is larger than its parent should sift up until
        the heap property is obeyed.
          10            10
         /  \   =>    /    \
        8    4       9      4
                    /
                   8
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(8)
        h.insert(4)
        h.insert(9)
        self.assertEqual(10, h._data[0])
        self.assertEqual(9, h._data[1])
        self.assertEqual(4, h._data[2])
        self.assertEqual(8, h._data[3])

    def test_insert_unstable_root_three(self):
        """
        An inserted value that is larger than its parent should sift up until
        the heap property is obeyed.
          10            15
         /  \   =>    /    \
        8    4       10      4
                    /
                   8
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(8)
        h.insert(4)
        h.insert(15)
        self.assertEqual(15, h._data[0])
        self.assertEqual(10, h._data[1])
        self.assertEqual(4, h._data[2])
        self.assertEqual(8, h._data[3])

    def test_insert_unstable_four(self):
        """
        An inserted value that is larger than its parent should sift up until
        the heap property is obeyed.
            10              10
           /  \   =>      /    \
          8    4         9      4
         /              / \
        1              1   8
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(8)
        h.insert(4)
        h.insert(1)
        h.insert(9)
        self.assertEqual(10, h._data[0])
        self.assertEqual(9, h._data[1])
        self.assertEqual(4, h._data[2])
        self.assertEqual(1, h._data[3])
        self.assertEqual(8, h._data[4])

    def test_insert_unstable_root_five(self):
        """
        An inserted value that is larger than its parent should sift up until
        the heap property is obeyed.
             10              15
           /    \   =>     /    \
          8      4        8      10
         / \             / \    /
        1   3           1   3  4
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(8)
        h.insert(4)
        h.insert(1)
        h.insert(3)
        h.insert(15)
        self.assertEqual(15, h._data[0])
        self.assertEqual(8, h._data[1])
        self.assertEqual(10, h._data[2])
        self.assertEqual(1, h._data[3])
        self.assertEqual(3, h._data[4])
        self.assertEqual(4, h._data[5])

    def test_insert_unstable_six(self):
        """
        An inserted value that is larger than its parent should sift up until
        the heap property is obeyed.
             10               10
           /    \   =>      /    \
          8      4         8      9
         / \    /         / \    / \
        1   3  2         1   3  2   4
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(8)
        h.insert(4)
        h.insert(1)
        h.insert(3)
        h.insert(2)
        h.insert(9)
        self.assertEqual(10, h._data[0])
        self.assertEqual(8, h._data[1])
        self.assertEqual(9, h._data[2])
        self.assertEqual(1, h._data[3])
        self.assertEqual(3, h._data[4])
        self.assertEqual(2, h._data[5])
        self.assertEqual(4, h._data[6])

    def test_insert_omg(self):
        """
        Lots of inserts should result in the MaxHeap obeying the max-heap
        property at every node in the tree.
        """
        h = MaxHeap()
        for _ in range(100):
            h.insert(random.randint(1, 1000))
        for i in reversed(range(len(h._data))):
            if (i - 1) // 2 < 0:
                break
            self.assertTrue(h._data[i] <= h._data[(i - 1) // 2])

    """
    Deleting a value. Straightforward, but with a couple base cases.
    Deleting a value from a heap removes and returns the rot node. Then, it
    replaces the old root with the last element in its data list, which is,
    conceptually, moving the last leaf node to the root position. After placing
    the new root node, the heap must 'sift down' the new root, since it is
    smaller than its children. The sifting-down continues until the node being
    sifted-down is in a position that obeys the heap property.
    Hint: Two simple cases, then the more dramatic one.
    Hint 2: Don't forget to return the root.
    """

    def test_delete_empty(self):
        """
        Deleting from an empty MaxHeap returns None.
        """
        h = MaxHeap()
        self.assertIsNone(h.delete())

    def test_delete_one(self):
        """
        Deleting when there is only one element removes that element
        and returns it.
        """
        h = MaxHeap()
        h.insert(10)
        self.assertEqual(10, h.delete())
        self.assertEqual(0, len(h._data))

    def test_delete_two(self):
        """
        Deleting when there are two elements in the heap removes the root element
        and returns it, leaving the other element in its place as the new root.
        Hint: There's a version of the pop method that takes an argument.
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(5)
        self.assertEqual(10, h.delete())
        self.assertEqual(1, len(h._data))
        self.assertEqual(5, h.delete())
        self.assertEqual(0, len(h._data))

    def test_delete_larger_left_three(self):
        """
        Deleting when there are three elements in the heap removes the root element
        and returns it, leaving the larger of the two children as the new root.
          10            5
         /  \    =>    /
        5    1        1
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(5)
        h.insert(1)
        self.assertEqual(10, h.delete())
        self.assertEqual(2, len(h._data))
        self.assertEqual(5, h._data[0])
        self.assertEqual(1, h._data[1])

    def test_delete_larger_right_three(self):
        """
        Deleting when there are three elements in the heap removes the root element
        and returns it, leaving the larger of the two children as the new root.
          10            5
         /  \    =>    /
        1    5        1
        Hint: Two base cases, and one case that requires the algorithm.
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(1)
        h.insert(5)
        self.assertEqual(10, h.delete())
        self.assertEqual(2, len(h._data))
        self.assertEqual(5, h._data[0])
        self.assertEqual(1, h._data[1])

    def test_delete_larger_left_four(self):
        """
        Deleting when there are four elements in the heap removes the root element
        and returns it, leaving the larger of the two children as the new root.
            10            8
           /  \    =>    /  \
          8    5        2    5
         /
        2
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(8)
        h.insert(5)
        h.insert(2)
        self.assertEqual(10, h.delete())
        self.assertEqual(3, len(h._data))
        self.assertEqual(8, h._data[0])
        self.assertEqual(2, h._data[1])
        self.assertEqual(5, h._data[2])

    def test_delete_larger_right_four(self):
        """
        Deleting when there are four elements in the heap removes the root element
        and returns it, leaving the larger of the two children as the new root.
            10            8
           /  \    =>    /  \
          5    8        5    2
         /
        2
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(5)
        h.insert(8)
        h.insert(2)
        self.assertEqual(10, h.delete())
        self.assertEqual(3, len(h._data))
        self.assertEqual(8, h._data[0])
        self.assertEqual(5, h._data[1])
        self.assertEqual(2, h._data[2])

    def test_delete_larger_left_five(self):
        """
        Deleting when there are five elements in the heap removes the root element
        and returns it, leaving the larger of the two children as the new root.
        The leaf that was made the new root sifts down only as far as it needs to,
        to obey the heap property.
            10            8
           /  \    =>    /  \
          8    5        4    5
         / \           /
        2   4         2
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(8)
        h.insert(5)
        h.insert(2)
        h.insert(4)
        self.assertEqual(10, h.delete())
        self.assertEqual(4, len(h._data))
        self.assertEqual(8, h._data[0])
        self.assertEqual(4, h._data[1])
        self.assertEqual(5, h._data[2])
        self.assertEqual(2, h._data[3])

    def test_delete_larger_left_five_root(self):
        """
        Deleting when there are five elements in the heap removes the root element
        and returns it, leaving the larger of the two children as the new root.
        The leaf that was made the new root sifts down as far as it needs to,
        to obey the heap property.
            10            8
           /  \    =>    /  \
          8    5        2    5
         / \           /
        2   1         1
        """
        h = MaxHeap()
        h.insert(10)
        h.insert(8)
        h.insert(5)
        h.insert(2)
        h.insert(1)
        self.assertEqual(10, h.delete())
        self.assertEqual(4, len(h._data))
        self.assertEqual(8, h._data[0])
        self.assertEqual(2, h._data[1])
        self.assertEqual(5, h._data[2])
        self.assertEqual(1, h._data[3])

    def test_delete_omg(self):
        """
        Lots of deletions should result in the MaxHeap obeying the max-heap
        property at every node in the tree, and the root always being the largest
        value in the tree.
        """
        h = MaxHeap()
        for _ in range(100):
            h.insert(random.randint(1, 1000))
        previous_root = h._data[0] + 1 # Seed a value larger than anything in the heap.
        while len(h._data) > 0:
            latest_root = h.delete()
            self.assertTrue(previous_root >= latest_root)
            for i in reversed(range(len(h._data))):
                if (i - 1) // 2 < 0:
                    break
                self.assertTrue(h._data[i] <= h._data[(i - 1) // 2])
            previous_root = latest_root


#                                                 .''.
#                     .''.      .        *''*    :_\/_:     .
#                    :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
#                .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
#               :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
#               : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
#                '..'  ':::'     * /\ *     .'/.\'.   '
#                    *            *..*         :
#
#                                              Art by Joan Stark

def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
