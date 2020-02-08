import unittest
from dcp.easy.ps5 import get_rooms


class TestEastPs5(unittest.TestCase):
    def test_get_rooms(self):
        self.assertEqual(2, get_rooms([(30, 75), (0, 50), (60, 150)]))
        self.assertEqual(3, get_rooms([(0, 75), (0, 50), (0, 150)]))
        self.assertEqual(3, get_rooms([(0, 50), (30, 60), (60, 100)]))
        self.assertEqual(2, get_rooms([(0, 50), (30, 60), (61, 100)]))
        self.assertEqual(0, get_rooms([]))
        self.assertEqual(1, get_rooms([(10, 30)]))
        self.assertEqual(2, get_rooms([(30, 500), (50, 60), (70, 80)]))
