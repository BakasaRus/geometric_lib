from lib.circle import *
import unittest

class CircleTestCase(unittest.TestCase):
    def test_circle_zero_argument_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_negative_argument_area(self):
        res = area(-10)
        self.assertEqual(res, 0)

    def test_circle_zero_argument_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_negative_argument_perimeter(self):
        res = perimeter(-10)
        self.assertEqual(res, 0)

    def test_circle_incorrect_data_area(self):
        with self.assertRaises(Exception):
            res = area("abc")

    def test_circle_incorrect_data_perimeter(self):
        with self.assertRaises(Exception):
            res = perimeter("abc")