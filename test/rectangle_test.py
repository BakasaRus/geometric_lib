from lib.rectangle import *
import unittest


class RectangleTestCase(unittest.TestCase):
    def test_rectangle_zero_argument_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_rectangle_negative_argument_area(self):
        res = area(-10, 250)
        self.assertEqual(res, 0)

    def test_rectangle_zero_argument_perimeter(self):
        res = perimeter(5, 0)
        self.assertEqual(res, 0)

    def test_rectangle_negative_argument_perimeter(self):
        res = perimeter(-10, 250)
        self.assertEqual(res, 0)

    def test_rectangle_incorrect_data_area(self):
        with self.assertRaises(Exception):
            res = area("abc", "abc")

    def test_rectangle_incorrect_data_perimeter(self):
        with self.assertRaises(Exception):
            res = perimeter("abc", "abc")
