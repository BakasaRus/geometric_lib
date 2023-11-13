import unittest
from lib.triangle import *


class TriangleTestCase(unittest.TestCase):
    def test_triangle_zero_argument_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_triangle_small_argument_area(self):
        res = area(5, 8)
        self.assertEqual(res, 20)

    def test_triangle_big_argument_area(self):
        res = area(600, 250)
        self.assertEqual(res, 300 * 250)

    def test_triangle_negative_argument_area(self):
        res = area(-10, 250)
        self.assertEqual(res, 0)

    def test_triangle_zero_argument_perimeter(self):
        res = perimeter(5, 0, 6)
        self.assertEqual(res, 0)

    def test_triangle_small_argument_perimeter(self):
        res = perimeter(5, 7, 4)
        self.assertEqual(res, 16)

    def test_triangle_big_argument_perimeter(self):
        res = perimeter(600, 250, 470)
        self.assertEqual(res, 1320)

    def test_triangle_negative_argument_perimeter(self):
        res = perimeter(-10, -250, 10)
        self.assertEqual(res, 0)

    def test_triangle_incorrect_data_area(self):
        res = area("abc")
        self.assertEqual(res, None)

    def test_triangle_incorrect_data_perimeter(self):
        res = perimeter("abc")
        self.assertEqual(res, None)