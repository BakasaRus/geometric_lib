import unittest
from triangle import *


class TriangleTestCase(unittest.TestCase):
    def test_triangle_zero_area(self):
        res = area(7, 0)
        self.assertEqual(res, 0)

    def test_triangle_negative_area(self):
        res = area(-11, 222)
        self.assertEqual(res, 0)

    def test_triangle_double_negative_area(self):
        res = area(-11, -222)
        self.assertEqual(res, 0)

    def test_triangle_little_area(self):
        res = area(3, 2)
        self.assertEqual(res, 3)

    def test_triangle_large_area(self):
        res = area(700, 200)
        self.assertEqual(res, 700 * 100)

    def test_triangle_zero_perimeter(self):
        res = perimeter(0, 2, 4)
        self.assertEqual(res, 0)

    def test_triangle_negative_perimeter(self):
        res = perimeter(-11, -200, 90)
        self.assertEqual(res, 0)

    def test_triangle_little_perimeter(self):
        res = perimeter(1, 4, 7)
        self.assertEqual(res, 12)

    def test_triangle_large_perimeter(self):
        res = perimeter(600, 700, 800)
        self.assertEqual(res, 2100)