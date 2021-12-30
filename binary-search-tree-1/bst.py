# BinarySearchTree: A binary search tree that passes all tests in test_bst.py.
# @author Julian Canepa
# @date 31 October 2021

class BinarySearchTree:

    def __init__(self, key=None) -> None:
        """
        Set initial state of new binary search tree that is also a node.
        """
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, node):
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
        # Found!
        if key is self.key:
            return self

        # No match
        if self.is_leaf():
            return None

        # Keep looking...
        if key <= self.key:
            return self.left.search(key)
        return self.right.search(key)

    def delete(self, key):
        """
        Remove the tree node matching a given key.
        """
        node = self.search(key)

        if node:
            return node._remove()
        return self.get_root()

    def _remove(self) -> None:
        """
        Remove the current node and reconcile its position
        in the tree with respect to other nodes.
        """
        if self.is_leaf():
            """
            No children - simple removal of the node only.
            Returns the parent node.
            """
            if self.parent:
                setattr(
                    self.parent,
                    self._get_parent_child_reference_attr(),
                    None)
            return self.parent

        if self.has_single_child():
            """
            Only child is adopted by node's parent.
            Returns the orphaned child.
            """
            return self._replace_and_return_orphan()

        if self.has_children():
            """
            Node has two children, deturmine a replacement for the current node by a successor.
            Return the successor.
            """
            return self._replace_and_return_successor()

    def _replace_and_return_orphan(self) -> None:
        """
        Connect the parent node to the child, and vice versa.
        """
        orphan = self.get_single_child()
        orphan.parent = self.parent

        if self.parent:
            setattr(
                self.parent,
                self._get_parent_child_reference_attr(),
                orphan)
        return orphan

    def _replace_and_return_successor(self):
        """
        Replace the current node with the smallest value to the right,
        and return the successor's value.
        """
        successor = self.right._get_min()
        # successor = self.left._get_max()

        setattr(
            successor.parent,
            successor._get_parent_child_reference_attr(),
            None
        )
        successor.parent = self.parent
        successor.right = self.right
        successor.left = self.left

        return successor

    # -------------------------
    # "Private" helper methods
    # -------------------------

    def is_root(self):
        return not self.parent

    def is_left_child(self):
        return self.parent and self.parent.left is self

    def is_right_child(self):
        return self.parent and self.parent.right is self

    def is_leaf(self):
        return not (self.right or self.left)

    def has_a_child(self):
        return self.right or self.left

    def has_children(self):
        return self.right and self.left

    def has_single_child(self):
        return self.has_a_child() and not self.has_children()

    def get_root(self):
        if self.is_root():
            return self
        return self.parent.get_root()

    def get_single_child(self):
        if not self.has_single_child():
            return None
        if self.left:
            return self.left
        return self.right

    def _get_parent_child_reference_attr(self):
        if self.is_root():
            return None
        return 'left' if self.is_left_child() else 'right'

    def _get_max(self):
        if self.is_leaf():
            return self
        return self.right._get_max()

    def _get_min(self):
        if self.is_leaf():
            return self
        return self.left._get_min()
