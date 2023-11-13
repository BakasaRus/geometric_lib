import math
import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(10)
        self.assertEqual(res, 100 * math.pi)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 20 * math.pi)

    def test_wrong_arguments(self):
        res = perimeter("abc")
        self.assertEqual(res, ValueError)

    def test_negative_numbers(self):
        res = perimeter(-1)
        self.assertEqual(res, ValueError)

    def test_none_argument(self):
        res = perimeter(None)
        self.assertEqual(res, ValueError)
