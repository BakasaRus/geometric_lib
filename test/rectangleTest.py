import unittest
from lib.rectangle import *


class RectangleTestCase(unittest.TestCase):
    def test_rectangle_zero_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_rectangle_negative_area(self):
        with self.assertRaises(ValueError):
            area(-1, 12)

    def test_rectangle_double_negative_area(self):
        with self.assertRaises(ValueError):
            area(-12, -13)

    def test_rectangle_little_area(self):
        res = area(2, 3)
        self.assertEqual(res, 2 * 3)

    def test_rectangle_large_area(self):
        res = area(1000, 200)
        self.assertEqual(res, 1000 * 200)

    def test_rectangle_zero_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(23, 0)

    def test_rectangle_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-11, 223)

    def test_rectangle_little_perimeter(self):
        res = perimeter(2, 3)
        self.assertEqual(res, (2+3)*2)

    def test_rectangle_large_perimeter(self):
        res = perimeter(1000, 200)
        self.assertEqual(res, (1000+200)*2)