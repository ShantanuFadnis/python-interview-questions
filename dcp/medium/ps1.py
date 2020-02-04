"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and\
deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def create_tree(self, tree_list: list):
        node = Node(None)
        # -1 for empty node

        if len(tree_list) != 0:
            value = tree_list.pop(1)

            if value != "-1":
                node.left = self.create_tree(tree_list)
                node = Node(value)
                node.right = self.create_tree(tree_list)

        return node

    def traverse(self, node):
        tree_list = []
        if node is None:
            tree_list.append("-1")
        else:
            tree_list.append(self.traverse(node.left))
            tree_list.append(self.traverse(node.val))
            tree_list.append(self.traverse(node.right))

        return tree_list

    def serialize(self, node):
        my_list = self.traverse(node)
        my_string = ""
        for element in my_list:
            my_string = " ".join(str(element))

        return my_string

    def deserialize(self, string:str):
        tree_list = string.split(' ')
        tree = self.create_tree(tree_list)
        return tree
