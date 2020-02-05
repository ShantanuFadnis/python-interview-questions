"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_univals(root):
    total_count, is_unival = helper(root)
    return total_count


def helper(root):
    if root is None:
        return 0, True
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    is_unival = True
    if not is_left_unival or not is_right_unival:
        is_unival = False
    if root.left is not None and root.left.val != root.val:
        is_unival = False
    if root.right is not None and root.right.val != root.val:
        is_unival = False
    if is_unival:
        return left_count + right_count + 1, True
    else:
        return left_count + right_count, False
