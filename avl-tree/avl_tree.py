# AVLTree: A Self-balancing Binary Search Tree
# Implementation passes all tests in test_avl_tree.py.
# @author jcanepa

class AVLTree:

    def __init__(self, key=None) -> None:
        self.key = key
        self.parent = self.right = self.left = None
        self.balance_factor = self.height = 0 # collectively referred to as "node meta"

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
                return node.rebalance()
                # self._update_node_meta()
                # return self
        else:
            if self.right:
                return self.right.insert(node)
            else:
                self.right = node
                node.parent = self
                return node.rebalance()
                # self._update_node_meta()
                # return self

    # Do not modify these helper functions, they are included for your convenience.
    def _is_left_child(self):
            return self.parent.left is self

    def _is_right_child(self):
            return self.parent.right is self

    def _is_root_node(self):
            return self.parent is None

    def is_leaf(self):
            return not (self.has_left_child() \
                or self.has_right_child())

    def has_left_child(self):
        return not self.left is None

    def has_right_child(self):
        return not self.right is None

    def has_left_child_only(self):
        return not self.left is None \
            and self.right is None

    def has_right_child_only(self):
        return not self.right is None \
            and self.left is None
    # Thanks for not modify helper functions included for your convenience.

    def _height(self, node):
        '''
        A method that works for AVLTree nodes and None.
        '''
        return self.height if node else -1 # should this be -1? That way leaves have a height of 0

    def _calculate_height(self):
        '''
        Get the height of the current node.
        The height of a node is the number of edges from its position to a leaf
        '''
        return 1 + max(
            self._height(self.left),
            self._height(self.right))

    def _calculate_balance_factor(self):
        '''
        The balance factor of a node equals:
        the height of its left subtree - the height of its right subtree
        '''
        return \
            (self.left._calculate_height() if self.has_left_child() else 0) - \
            (self.right._calculate_height() if self.has_right_child() else 0)

    def _set_height_and_balance_factor(self):
        '''
        Update node height & balance factor based on the height of its children.
        '''
        self.height = self._calculate_height()
        self.balance_factor = self._calculate_balance_factor()

    # def _update_node_meta(self) -> int:
    #     self._set_height_and_balance_factor()
    #     is_left_heavy = self.balance_factor >= 2
    #     is_right_heavy = self.balance_factor <= -2
    #     if is_left_heavy or is_right_heavy:
    #         if is_left_heavy:
    #             self._rotate_right()
    #         else:
    #             if self.has_right_child() and self.right.balance_factor > 0:
    #                 self.right._rotate_right()
    #                 self.right._set_height_and_balance_factor()
    #                 self._update_node_meta()
    #             self._rotate_left()

    #         self._set_height_and_balance_factor()
    #     if self.parent:
    #         return self.parent._update_node_meta()
    #     return self

    def is_imbalanced(self):
        return self.balance_factor > 1 \
            or self.balance_factor < -1

    def is_left_heavy(self):
        return self.balance_factor > 1

    def rebalance(self):
        self._set_height_and_balance_factor()

        if self.is_imbalanced():
            if self.is_left_heavy():
            #     if self.has_left_child() and self.left.balance_factor < 0:
            #         self.left._rotate_left()
                self._rotate_right()
            else:
                if self.has_right_child() and self.right.balance_factor > 0:
                    self.right._rotate_right()
                self._rotate_left()

        return self.parent.rebalance() \
            if self.parent else self

    '''
    Jill's notes on rebalancing if it's needed:
    After inserting a new node, this is how we update everyone's balance factor, all the way up the chain
    updateBalanceFactor(self)
    if self's balance factor is 2 or -2, rebalance(self)
    otherwise if you're a right child, subtract one from your parent's balance factor
    otherwise if you're a left child ..
    if parent's balance factor it not 0, call the method again sending in your parent
    '''
    def _rotate_left(self):
        root = self.right
        self.right = None
        self.left = None
        if root.has_left_child():
            self.right = root.left
        root.left = self
        root.parent = self.parent
        self.parent = root

    def _rotate_right(self):
        root = self.left
        self.right = None
        self.left = None
        if root.has_right_child():
            self.lef = root.right
        root.right = self
        root.parent = self.parent
        self.parent = root