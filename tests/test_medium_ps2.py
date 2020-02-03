import unittest
from dcp.medium.ps2 import cons, car, cdr


class TestMediumPs2(unittest.TestCase):
    def test_car(self):
        func = cons(10, 20)
        self.assertEqual(10, car(func))

    def test_cdr(self):
        func = cons(8, 19)
        self.assertEqual(19, cdr(func))
