import unittest
from dcp.easy.ps4 import Node, LinkedList, get_intersect_node


class TestEasyPs4(unittest.TestCase):
    def test_get_intersect_node_1(self):
        n1 = Node(2)
        n2 = Node(4)
        n3 = Node(6)
        n4 = Node(1)
        n5 = Node(3)

        list1 = LinkedList(n1)
        n1.next = n2
        n2.next = n3

        list2 = LinkedList(n4)
        n4.next = n5
        n5.next = n3

        self.assertEqual(6, get_intersect_node(list1, list2).data)

    def test_get_intersect_node_2(self):
        n1 = Node(2)
        n2 = Node(4)
        n3 = Node(6)
        n4 = Node(1)
        n5 = Node(3)
        n6 = Node(5)

        list1 = LinkedList(n1)
        n1.next = n2
        n2.next = n3

        list2 = LinkedList(n4)
        n4.next = n5
        n5.next = n6

        self.assertEqual(None, get_intersect_node(list1, list2).data)
