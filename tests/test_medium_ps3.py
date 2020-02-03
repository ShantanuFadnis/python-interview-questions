import unittest
from dcp.medium.ps3 import num_ways


class TestMediumPs3(unittest.TestCase):
    def test_num_ways_123(self):
        message = '123'
        output = 3
        self.assertEqual(output, num_ways(message))

    def test_num_ways_111(self):
        message = '111'
        output = 3
        self.assertEqual(output, num_ways(message))

    def test_num_ways_001(self):
        message = '001'
        output = 0
        self.assertEqual(output, num_ways(message))

    def test_num_ways_12123(self):
        message = '12123'
        output = 8
        self.assertEqual(output, num_ways(message))
