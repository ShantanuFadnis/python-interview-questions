import unittest
from gfg.josephus import josephus


class TestJosephus(unittest.TestCase):
    def test_josephus_1(self):
        a, b = 10, 3
        output = 4
        self.assertEqual(output, josephus(a, b))

    def test_josephus_2(self):
        a, b = 3, 2
        output = 3
        self.assertEqual(output, josephus(a, b))
