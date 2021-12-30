# BinarySearchTree Scratchpad
# Julian Canepa

from bst import BinarySearchTree


#          5             7
#         / \     =>    / \
#        3   7         4   7
#       / \           /
#      1    4        1
# Deleting the root of a three-level tree promotes the right child to be the
# new root, and `delete` returns it.

bst = BinarySearchTree(5)
initial_left_child = BinarySearchTree(3)
_ = BinarySearchTree(1)
__ = BinarySearchTree(4)
___ = BinarySearchTree(7)
____ = BinarySearchTree(9)

bst.insert(initial_left_child)
bst.insert(_)
bst.insert(__)
bst.insert(___)
bst.insert(____)

s = bst.get_root()
while s.right:
    print(s.key)
    print('left:', s.left)
    print('right:', s.right)
    print('leaf?', s.is_leaf())
    s = s.right

print(bst.get_root()._get_min().key)
print(bst.get_root()._get_max().key)

# bst = bst.delete(3)
# print('bst key:', initial_left_child)

# print(bst.___leaf())
# print('____ should be none:', bst.parent)
