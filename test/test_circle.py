import unittest
import circle
import math

class CircleTest(unittest.TestCase):
    def test_null_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_not_null_perimeter(self):
        res = circle.perimeter(23)
        self.assertEqual(res, 2 * math.pi * 23)

    def test_null_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_not_null_area(self):
        res = circle.area(12)
        self.assertEqual(res, math.pi * 144)

    def test_if_wrong_params(self):
        with self.assertRaises(Exception):
            res = circle.area([1])
