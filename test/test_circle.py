import math
import unittest

import circle


class CircleAreaTestCase(unittest.TestCase):
    def test_circle_zero_argument_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_circle_small_argument_area(self):
        res = circle.area(5)
        self.assertEqual(res, 5 * 5 * math.pi)

    def test_circle_big_argument_area(self):
        res = circle.area(400)
        self.assertEqual(res, 400 * 400 * math.pi)

    def test_circle_negative_argument_area(self):
        self.assertRaises(ValueError, circle.area, -5)


class CirclePerimeterTestCase(unittest.TestCase):
    def test_circle_zero_argument_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_small_argument_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 2 * 5 * math.pi)

    def test_circle_big_argument_perimeter(self):
        res = circle.perimeter(400)
        self.assertEqual(res, 2 * 400 * math.pi)

    def test_circle_negative_argument_perimeter(self):
        self.assertRaises(ValueError, circle.area, -5)

