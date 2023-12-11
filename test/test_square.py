import math
import unittest

import square


class SquareAreaTestCase(unittest.TestCase):
    def test_square_zero_argument_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_square_small_argument_area(self):
        res = square.area(5)
        self.assertEqual(res, 5 * 5)

    def test_square_big_argument_area(self):
        res = square.area(400)
        self.assertEqual(res, 400 * 400)

    def test_square_negative_argument_area(self):
        self.assertRaises(ValueError, square.area, -5)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_square_zero_argument_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_square_small_argument_perimeter(self):
        res = square.perimeter(5)
        self.assertEqual(res, 4 * 5)

    def test_square_big_argument_perimeter(self):
        res = square.perimeter(400)
        self.assertEqual(res, 4 * 400)

    def test_square_negative_argument_perimeter(self):
        self.assertRaises(ValueError, square.perimeter, -5)

