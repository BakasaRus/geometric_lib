import unittest
from circle import *


class CircleTestCase(unittest.TestCase):

    def test_circle_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_negative_area(self):
        res = area(-5)
        self.assertEqual(res, 0)

    def test_circle_little_area(self):
        res = area(5)
        self.assertEqual(res, 5 ** 2 * math.pi)


    def test_circle_large_area(self):
        res = area(700)
        self.assertEqual(res, 700 *700 * math.pi)


    def test_circle_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_negative_argument_perimeter(self):
        res = perimeter(-5)
        self.assertEqual(res, 0)

    def test_circle_little_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 2 * math.pi * 5)

    def test_circle_large_perimeter(self):
        res = perimeter(700)
        self.assertEqual(res, 2 * math.pi * 700)