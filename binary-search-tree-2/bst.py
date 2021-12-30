# BinarySearchTree: A binary search tree that passes all tests in test_bst.py.
# @author Julian Canepa
# @date 6 Nov 2021

from typing import List

class BinarySearchTree:

    def __init__(self, key=None)-> None:
        """
        Set initial state of new binary search tree that is also a node.
        """
        self.key = key
        self.left = self.right = self.parent = None

    def insert(self, node) -> None:
        """
        Insert a new node into the tree, placed by sorted key.
        Less than to the left, greater values on right.
        """
        if node.key <= self.key:
            if self.left:
                return self.left.insert(node)
            else:
                self.left = node
                node.parent = self
        else:
            if self.right:
                return self.right.insert(node)
            else:
                self.right = node
                node.parent = self

    def search(self, key) -> 'BinarySearchTree':
        """
        Return a tree node object that matches a given key.
        Or, return none if nothing is found.
        """
        # found
        if key is self.key:
            return self

        # no match
        if self.is_leaf():
            return None

        # keep looking...
        if key <= self.key:
            return self.left.search(key)
        return self.right.search(key)

    def delete(self, key) -> 'BinarySearchTree':
        """
        Remove the tree node matching a given key,
        then return the root of the tree.
        """
        node = self.search(key)

        if node:
            return node._remove()
        return self._get_root()

    def keys(self, order_type='pre') -> list:
        return getattr(
            self,
            '_list_'+ order_type +'_order')([])

    def _remove(self) -> 'BinarySearchTree':
        """
        Remove the current node and reconcile its position
        in the tree with respect to other nodes.
        """
        if self.is_leaf():
            """
            Simple removal of the node only.
            Returns the parent node.
            """
            if not self.parent: return None
            self._set_parent_child_pointer_attr(None)
            return self._get_root()

        if self._has_single_child():
            """
            Only child is adopted by node's parent.
            Returns the orphaned child.
            """
            return self._connect_child_with_parent()

        if self._has_children():
            """
            Node has two children. Replace the current node with successor
            and return the root of tree.
            """
            successor = self._replace_with_and_return_successor()
            return successor._get_root()

    def _connect_child_with_parent(self) -> 'BinarySearchTree':
        """
        Connect parent node to the child, and vice versa.
        """
        child = self._get_single_child()
        child.parent = self.parent
        self._set_parent_child_pointer_attr(child)
        return child

    def _replace_with_and_return_successor(self) -> 'BinarySearchTree':
        """
        Replace the current node with the smallest value to the right,
        and return the successor's value.
        """
        successor = self.right.minimum()
        # self.left.maximum() can also be implemented with some refactoring of line 123-29

        # update references pointing to node being removed
        self.left.parent = successor
        self.right.parent = successor
        self._set_parent_child_pointer_attr(successor)

        # child left behind by successor is attached to grandparent
        child = None
        if successor._has_single_child():
            child = successor._get_single_child()
            successor._connect_child_with_parent()

        # update references of nodes successor leaves behind
        right = None if self.right is successor else self.right
        successor._set_parent_child_pointer_attr(child)

        # successor referencing nodes at new position
        successor.parent = self.parent
        successor.left = self.left
        successor.right = right

        return successor

    def _list_pre_order(self, list) -> list:
        """
        List all nodes in pre-order: Self -> L -> R.
        """
        list.append(self.key)

        if self.left:
            self.left._list_pre_order(list)

        if self.right:
            self.right._list_pre_order(list)

        return list

    def _list_in_order(self, list) -> list:
        """
        List all nodes in in-order: L -> Self -> R.
        """
        if self.left:
            self.left._list_in_order(list)

        list.append(self.key)

        if self.right:
            self.right._list_in_order(list)

        return list

    def _list_post_order(self, list) -> list:
        """
        List all nodes in post-order: L -> R -> Self.
        """
        if self.left:
            self.left._list_post_order(list)

        if self.right:
            self.right._list_post_order(list)

        list.append(self.key)

        return list

    # -------------------------
    # Helper methods
    # -------------------------

    def _is_root(self) -> bool:
        """
        Node is root.
        """
        return not self.parent

    def _is_left_child(self) -> bool:
        """
        Node is the left child of its parent.
        """
        return self.parent and (
            self.parent.left is self)

    def is_leaf(self) -> bool:
        """
        Node is a tree leaf.
        """
        return not (
           self.has_right_child() or self.has_left_child())

    def _has_a_child(self) -> bool:
        """
        Node has at least one child.
        """
        return self.has_right_child() or self.has_left_child()

    def _has_children(self) -> bool:
        """
        Node has two children.
        """
        return self.has_right_child() and self.has_left_child()

    def _has_single_child(self) -> bool:
        """
        Node has exactly one child.
        """
        return self._has_a_child() and (
            not self._has_children())

    def _get_root(self) -> 'BinarySearchTree':
        """
        Returns the root of this tree.
        """
        if self._is_root():
            return self
        return self.parent._get_root()

    def _get_single_child(self) -> 'BinarySearchTree':
        """
        Return a node's single child, if it exists.
        """
        if not self._has_single_child():
            return None
        if self.has_left_child():
            return self.left
        return self.right

    def _get_parent_child_reference_attr(self) -> str:
        """
        Get the attribute name (left or right) node is assigned to on parent.
        """
        return 'left' if self._is_left_child() else 'right'

    def maximum(self) -> 'BinarySearchTree':
        """
        Return node with maximum value in tree.
        """
        if self.is_leaf():
            return self
        return self.right.maximum()

    def minimum(self) -> 'BinarySearchTree':
        """
        Return node with minimum value in tree.
        """
        if self.is_leaf():
            return self
        return self.left.minimum()

    def has_left_child(self) -> bool:
        """
        Node has a left child.
        """
        return not self.left is None

    def has_right_child(self) -> bool:
        """
        Node has a right child.
        """
        return not self.right is None

    def _set_parent_attr(self, attr_name, attr_value):
        """
        Sets a given attribute of a node's parent to a given value.
        """
        setattr(
            self.parent,
            attr_name,
            attr_value)

    def _set_parent_child_pointer_attr(self, attr_value):
        """
        Sets attribute of node parent, if it exists.
        """
        if self.parent:
            self._set_parent_attr(
                self._get_parent_child_reference_attr(),
                attr_value)