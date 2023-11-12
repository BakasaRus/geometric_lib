import unittest
from lib.square import *


class SquareTestCase(unittest.TestCase):
    def test_square_zero_argument_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_small_argument_area(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_square_big_argument_area(self):
        res = area(600)
        self.assertEqual(res, 360000)

    def test_square_negative_argument_area(self):
        res = area(-10)
        self.assertEqual(res, 0)

    def test_square_zero_argument_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_small_argument_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_square_big_argument_perimeter(self):
        res = perimeter(600)
        self.assertEqual(res, 2400)

    def test_square_negative_argument_perimeter(self):
        res = perimeter(-10)
        self.assertEqual(res, 0)