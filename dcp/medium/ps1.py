"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

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

def create_tree(tree_list:list):
    node = Node(None)
    # -1 for empty node

    if len(tree_list) != 0:
        value = tree_list.pop(1)

        if value != "-1":
            node.left = create_tree(tree_list)
            node = Node(value)
            node.right = create_tree(tree_list)

    return node


def traverse(node):
    tree_list = []
    if node is None:
        tree_list.append("-1")
    else:
        tree_list.append(traverse(node.left))
        tree_list.append(traverse(node.val))
        tree_list.append(traverse(node.right))

    return tree_list

def serialize(node):
    my_list = traverse(node)
    my_string = ""
    for element in my_list:
        my_string = " ".join(str(element))

    return my_string

def deserialize(string:str):
    tree_list = string.split(' ')
    tree = create_tree(tree_list)

    return tree

if __name__ == '__main__':
    tree_list = [2, 5, 3, 9]
    my_tree = create_tree(tree_list)
    srt1 = serialize(my_tree)
    print(srt1)

