import unittest
from square import *


class SquareTestCase(unittest.TestCase):
    def test_square_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_negative_area(self):
        res = area(-15)
        self.assertEqual(res, 0)

    def test_square_little_area(self):
        res = area(7)
        self.assertEqual(res, 49)

    def test_square_large_area(self):
        res = area(700)
        self.assertEqual(res, 490000)

    def test_square_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_negative_perimeter(self):
        res = perimeter(-15)
        self.assertEqual(res, 0)

    def test_square_little_perimeter(self):
        res = perimeter(7)
        self.assertEqual(res, 28)

    def test_square_large_perimeter(self):
        res = perimeter(700)
        self.assertEqual(res, 2800)