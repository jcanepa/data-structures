# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_bst

import unittest
import time
from bst import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A BinarySearchTree exists.
        """
        try:
            BinarySearchTree()
        except NameError:
            self.fail("Could not instantiate BinarySearchTree.")

    def test_initial_attributes(self):
        """
        A BST is a recursive structure. When we refer to an object that "is a BST,"
        we are referring to a root node of a binary search tree.
        Every node has a left child, right child, and a key.
        A new BST has a left, right, key, and parent that are each None.
        Hint: Define an initializer.
        """
        bst = BinarySearchTree()
        self.assertIsNone(bst.left)
        self.assertIsNone(bst.right)
        self.assertIsNone(bst.key)
        self.assertIsNone(bst.parent)

    def test_instatiate_with_key(self):
        """
        A BST (node) can be instantiated with an initial key.
        When one isn't provided, the key is None.
        Hint: Use Python's 'default arguments' feature.
        """
        bst = BinarySearchTree()
        self.assertIsNone(bst.key)
        bst = BinarySearchTree(42)
        self.assertEqual(42, bst.key)

    # """
    # Cute, single-level trees. (Depth of zero.)
    # """

    def test_insert_single_smaller(self):
        """
        Inserting a node into a single-level tree appends the new node as the
        left child, when the new node key is less than the parent's key.
        (A new node whose key is <= parent key becomes the left child.)
        """
        bst = BinarySearchTree(5)
        child = BinarySearchTree(1)
        bst.insert(child)
        self.assertEqual(child, bst.left)

    def test_parent_child_relationship(self):
        """
        Inserting a node into a single-level tree appends makes the new node
        a child of its parent node
        """
        bst = BinarySearchTree(5)
        child = BinarySearchTree(1)
        bst.insert(child)
        self.assertEqual(bst, child.parent)

    def test_insert_single_equal(self):
        """
        Inserting a node into a single-level tree appends the new node as the
        left child, when the new node value is equal to the the parent's key.
        (A new node whose key is <= parent key becomes the left child.)
        """
        bst = BinarySearchTree(5)
        child = BinarySearchTree(5)
        bst.insert(child)
        self.assertEqual(child, bst.left)
        self.assertEqual(bst, child.parent)

    def test_insert_single_greater(self):
        """
        Inserting a node into a single-level tree appends the new node as the
        right child, when the new node key is greater than the parent's key.
        (A new node whose key is > parent key becomes the right child.)
        """
        bst = BinarySearchTree(5)
        child = BinarySearchTree(7)
        bst.insert(child)
        self.assertEqual(child, bst.right)
        self.assertEqual(bst, child.parent)

    def test_search_single_none(self):
        """
        Searching a single-level tree for a key that doesn't exist returns None.
        """
        bst = BinarySearchTree(5)
        self.assertIsNone(bst.search(-999))

    def test_search_single_one(self):
        """
        Searching a single-level tree for a key that does exist returns that node / tree.
        """
        bst = BinarySearchTree(5)
        self.assertEqual(bst, bst.search(5))

    def test_delete_single_nonexistent(self):
        """
        Deleting a node with a key that does not exist returns the root node of
        the single-level tree.
        """
        bst = BinarySearchTree(5)
        self.assertEqual(bst, bst.delete(-999))

    def test_delete_single(self):
        """
        Deleting the node of a single-level tree returns the node's parent.
        """
        bst = BinarySearchTree(5)
        self.assertIsNone(bst.delete(5))

    # """
    # Toddler, two-level trees. (Depth of one.)
    # # """

    def test_insert_two_smaller_left(self):
        """
        Inserting a node with a key that is less than the left child's key appends
        the new node as the left child's left child.
          5             5
         / \    =>     / \
        3   7         3   7
                     /
                    1
        Hint: Nest your logic. Delegate with recursion.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        child = BinarySearchTree(1)
        bst.insert(left)
        bst.insert(right)
        bst.insert(child)
        self.assertEqual(child, bst.left.left)
        self.assertEqual(left, child.parent)

    def test_insert_two_greater_left(self):
        """
        Inserting a node with a key that is greater than the left child's key
        (and less than the parent/root) appends the new node as the left child's
        right child.
          5             5
         / \    =>     / \
        3   7         3   7
                       \
                        4
        Hint: If this test immediately passes, you are on a happy path.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        child = BinarySearchTree(4)
        bst.insert(left)
        bst.insert(right)
        bst.insert(child)
        self.assertEqual(child, bst.left.right)
        self.assertEqual(left, child.parent)

    def test_insert_two_greater_right(self):
        """
        Inserting a node with a key that is greater than the right child's key
        appends the new node as the right child's right child.
          5             5
         / \    =>     / \
        3   7         3   7
                           \
                            9
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        child = BinarySearchTree(9)
        bst.insert(left)
        bst.insert(right)
        bst.insert(child)
        self.assertEqual(child, bst.right.right)
        self.assertEqual(right, child.parent)

    def test_insert_two_smaller_right(self):
        """
        Inserting a node with a key that is less than the right child's key
        (and greater than the parent/root) appends the new node as the right
        child's left child.
          5             5
         / \    =>     / \
        3   7         3   7
                         /
                        6
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        child = BinarySearchTree(6)
        bst.insert(left)
        bst.insert(right)
        bst.insert(child)
        self.assertEqual(child, bst.right.left)
        self.assertEqual(right, child.parent)

    def test_search_two_basics(self):
        """
        Searching a two-level tree for a key that doesn't exist returns None.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertIsNone(bst.search(-999))

    def test_search_two_root(self):
        """
        Searching a two-level tree for a key that exists in the root returns
        the root.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertEqual(bst, bst.search(5))

    def test_search_two_left(self):
        """
        Searching a two-level tree for a key that exists in the left subtree
        returns that left node / subtree.
        Hint: Try a brutish, 'naive' approach.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertEqual(left, bst.search(3))

    def test_search_two_right(self):
        """
        Searching a two-level tree for a key that exists in the right subtree
        returns that right node / subtree.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertEqual(right, bst.search(7))

    def test_delete_two_nonexistent(self):
        """
        Deleting a node with a key that does not exist does not modify the tree
        and returns the root node of the tree.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertEqual(bst, bst.delete(-999))
        self.assertEqual(5, bst.key)
        self.assertEqual(3, bst.left.key)
        self.assertEqual(7, bst.right.key)

    def test_delete_two_left_leaf(self):
        """
        Deleting the left child of a two-level tree removes the left child and returns the root node.
          5            5
         / \     =>     \
        3   7            7
        Hint: Consult the BST rules. Time to improve your `delete` method... a little.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertEqual(bst, bst.delete(3))
        self.assertIsNone(bst.left)
        self.assertEqual(5, bst.key)
        self.assertEqual(7, bst.right.key)

    def test_delete_two_right_leaf(self):
        """
        Deleting the right child of a two-level tree removes the right child and
        returns the root node.
          5            5
         / \     =>   /
        3   7        3
        Hint: Small changes to `delete`, lest you overthink it.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertEqual(bst, bst.delete(7))
        self.assertIsNone(bst.right)
        self.assertEqual(5, bst.key)
        self.assertEqual(3, bst.left.key)

    def test_delete_two_root_with_left(self):
        """
        Deleting the root of a two-level tree that has only a left child makes
        the left child the new root, and `delete` returns it.
          5
         /     =>  3
        3
        Hint: Small steps of a little nested logic.
        """
        bst = BinarySearchTree(5)
        initial_left_child = BinarySearchTree(3)
        bst.insert(initial_left_child)
        bst = bst.delete(5)
        self.assertEqual(initial_left_child, bst)
        self.assertEqual(3, bst.key)
        self.assertTrue(bst.is_leaf())
        self.assertIsNone(bst.parent)

    def test_delete_two_root_with_right(self):
        """
        Deleting the root of a two-level tree that has only a right child makes
        the right child the new root, and `delete` returns it.
        5
         \     =>  7
          7
        """
        bst = BinarySearchTree(5)
        initial_right_child = BinarySearchTree(7)
        bst.insert(initial_right_child)
        bst = bst.delete(5)
        self.assertEqual(initial_right_child, bst)
        self.assertEqual(7, bst.key)
        self.assertTrue(bst.is_leaf())
        self.assertIsNone(bst.parent)

    def test_delete_two_root(self):
        """
        Deleting the root of a two-level tree promotes the right child to be the
        new root, and `delete` returns it.
          5            7
         / \     =>   /
        3   7        3
        Hint: Consult the bst deletion rules... but be direct for now.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        initial_right_child = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(initial_right_child)
        bst = bst.delete(5)
        self.assertEqual(initial_right_child, bst)
        self.assertEqual(3, bst.left.key)
        self.assertIsNone(bst.right)

def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
