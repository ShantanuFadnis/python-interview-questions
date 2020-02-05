import unittest
from dcp.easy.ps2 import count_univals
from dcp.easy.ps2 import Node


class TestEasyPs2(unittest.TestCase):
    def test_count_univals_1(self):
        root = Node(2)
        output = 1
        self.assertEqual(output, count_univals(root))

    def test_count_univals_2(self):
        root = Node(2)
        root.left = Node(2)
        output = 2
        self.assertEqual(output, count_univals(root))

    def test_count_univals_3(self):
        root = Node(2)
        root.left = Node(0)
        output = 1
        self.assertEqual(output, count_univals(root))

    def test_count_univals_4(self):
        root = Node(2)
        root.right = Node(2)
        output = 2
        self.assertEqual(output, count_univals(root))

    def test_count_univals_5(self):
        root = Node(2)
        root.right = Node(4)
        output = 1
        self.assertEqual(output, count_univals(root))

    def test_count_univals_6(self):
        root = Node(2)
        root.left = Node(2)
        root.right = Node(2)
        output = 3
        self.assertEqual(output, count_univals(root))

    def test_count_univals_7(self):
        root = Node(2)
        root.left = Node(1)
        root.right = Node(4)
        output = 2
        self.assertEqual(output, count_univals(root))

    def test_count_univals_8(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(0)
        root.right.left = Node(1)
        root.right.left.left = Node(1)
        root.right.left.right = Node(1)
        root.right.right = Node(0)
        output = 5
        self.assertEqual(output, count_univals(root))

    def test_count_univals_9(self):
        root = Node(5)
        root.left = Node(3)
        root.left.left = Node(2)
        root.right = Node(9)
        output = 2
        self.assertEqual(output, count_univals(root))
