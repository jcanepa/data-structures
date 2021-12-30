# BinarySearchTree Scratchpad
# Julian Canepa
# Use this as a "scratchpad" to tinker with your binary search tree.

from bst import BinarySearchTree

def three_level_tree():
    """
         10
       /    \
      5      15
     / \    /  \
    2   7  12   17
    """
    bst = BinarySearchTree(10)
    bst.insert(BinarySearchTree(5))
    bst.insert(BinarySearchTree(15))
    bst.insert(BinarySearchTree(2))
    bst.insert(BinarySearchTree(7))
    bst.insert(BinarySearchTree(12))
    bst.insert(BinarySearchTree(17))
    return bst

# Example
bst = three_level_tree()
print('Pre order:', bst.keys('pre'))
print('In order:', bst.keys('in'))
print('Post order:', bst.keys('post'))