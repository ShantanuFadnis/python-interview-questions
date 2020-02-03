import unittest
from dcp.easy.ps1 import find_sum


class TestEasyPs1(unittest.TestCase):
    def test_find_sum_8(self):
        my_list = [8, 5, 3, 2, 6, 4, 19]
        k = 8
        self.assertEqual(True, find_sum(my_list, k))

    def test_find_sum_10(self):
        my_list = [8, 5, 3, 2, 6, 4, 19]
        k = 10
        self.assertEqual(True, find_sum(my_list, k))

    def test_find_sum_13(self):
        my_list = [8, 5, 3, 2, 6, 4, 19]
        k = 13
        self.assertEqual(True, find_sum(my_list, k))

    def test_find_sum_43(self):
        my_list = [8, 5, 3, 2, 6, 4, 19]
        k = 43
        self.assertEqual(False, find_sum(my_list, k))

    def test_find_sum_1(self):
        my_list = [8, 5, 3, 2, 6, 4, 19]
        k = 1
        self.assertEqual(False, find_sum(my_list, k))

    def test_find_sum_0(self):
        my_list = [8, 5, 3, 2, 6, 4, 19]
        k = 0
        self.assertEqual(False, find_sum(my_list, k))
