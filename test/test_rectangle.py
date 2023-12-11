import math
import unittest

import rectangle


class RectangleAreaTestCase(unittest.TestCase):
    def test_rectangle_zero_argument_area(self):
        res = rectangle.area(5, 0)
        self.assertEqual(res, 0)

    def test_rectangle_small_argument_area(self):
        res = rectangle.area(5, 7)
        self.assertEqual(res, 5 * 7)

    def test_rectangle_big_argument_area(self):
        res = rectangle.area(400, 240)
        self.assertEqual(res, 400 * 240)

    def test_rectangle_negative_argument_area(self):
        self.assertRaises(ValueError, rectangle.area, -5, 240)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_rectangle_zero_argument_perimeter(self):
        self.assertRaises(ValueError, rectangle.perimeter, -5, 0)

    def test_rectangle_small_argument_perimeter(self):
        res = rectangle.perimeter(5, 7)
        self.assertEqual(res, 2 * 5 + 2 * 7)

    def test_rectangle_big_argument_perimeter(self):
        res = rectangle.perimeter(400, 240)
        self.assertEqual(res, 2 * 400 + 2 * 240)

    def test_rectangle_negative_argument_perimeter(self):
        self.assertRaises(ValueError, rectangle.perimeter, -5, -7)
