import unittest
from lib.circle import *


class CircleTestCase(unittest.TestCase):
    def test_circle_zero_argument_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_small_argument_area(self):
        res = area(7)
        self.assertEqual(res, 7 ** 2 * math.pi)

    def test_circle_big_argument_area(self):
        res = area(600)
        self.assertEqual(res, 600 ** 2 * math.pi)

    def test_circle_negative_argument_area(self):
        res = area(-10)
        self.assertEqual(res, 0)

    def test_circle_zero_argument_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_small_argument_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 2 * math.pi * 5)

    def test_circle_big_argument_perimeter(self):
        res = perimeter(600)
        self.assertEqual(res, 2 * math.pi * 600)

    def test_circle_negative_argument_perimeter(self):
        res = perimeter(-10)
        self.assertEqual(res, 0)

    def test_circle_incorrect_data_area(self):
        res = area("abc")
        self.assertEqual(res, None)

    def test_circle_incorrect_data_perimeter(self):
        res = perimeter("abc")
        self.assertEqual(res, None)