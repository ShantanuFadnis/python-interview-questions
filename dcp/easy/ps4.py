"""
Given two singly linked lists that intersect at some point, find the intersecting node.
The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space

"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head


# Constant space solution pending!!
def get_intersect_node(l1, l2):
    data = set()
    while l1.head:
        data.add(l1.head.data)
        l1.head = l1.head.next
    while l2.head:
        if l2.head.data in data:
            return l2.head
        l2.head = l2.head.next
    return Node()
