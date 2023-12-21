import unittest
from lib.triangle import *


class TriangleTestCase(unittest.TestCase):
    def test_triangle_zero_area(self):
        res = area(7, 0)
        self.assertEqual(res, 0)

    def test_triangle_negative_area(self):
        with self.assertRaises(ValueError):
            area(-11, 222)

    def test_triangle_double_negative_area(self):
        with self.assertRaises(ValueError):
            area(-11, -222)

    def test_triangle_little_area(self):
        res = area(3, 2)
        self.assertEqual(res, 3)

    def test_triangle_large_area(self):
        res = area(700, 200)
        self.assertEqual(res, 700 * 100)

    def test_triangle_zero_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(0, 2, 4)
    def test_triangle_unright_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(1, 17, 5)
    def test_triangle_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-11, -200, 90)

    def test_triangle_little_perimeter(self):
        res = perimeter(1, 7, 7)
        self.assertEqual(res, 15)

    def test_triangle_large_perimeter(self):
        res = perimeter(600, 700, 800)
        self.assertEqual(res, 2100)