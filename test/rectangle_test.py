import unittest
from lib.rectangle import *


class RectangleTestCase(unittest.TestCase):
    def test_rectangle_zero_argument_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_rectangle_small_argument_area(self):
        res = area(5, 7)
        self.assertEqual(res, 5 * 7)

    def test_rectangle_big_argument_area(self):
        res = area(600, 250)
        self.assertEqual(res, 600 * 250)

    def test_rectangle_negative_argument_area(self):
        res = area(-10, 250)
        self.assertEqual(res, 0)

    def test_rectangle_zero_argument_perimeter(self):
        res = perimeter(5, 0)
        self.assertEqual(res, 0)

    def test_rectangle_small_argument_perimeter(self):
        res = perimeter(5, 7)
        self.assertEqual(res, 5 * 2 + 7 * 2)

    def test_rectangle_big_argument_perimeter(self):
        res = perimeter(600, 250)
        self.assertEqual(res, 600 * 2 + 250 * 2)

    def test_rectangle_negative_argument_perimeter(self):
        res = perimeter(-10, 250)
        self.assertEqual(res, 0)

    def test_rectangle_incorrect_data_area(self):
        res = area("abc")
        self.assertEqual(res, None)

    def test_rectangle_incorrect_data_perimeter(self):
        res = perimeter("abc")
        self.assertEqual(res, None)