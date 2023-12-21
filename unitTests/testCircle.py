import unittest

from methods.circle import *

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0)
        expected = 0
        self.assertEqual(result, expected)

    def test_small_area(self):
        result = area(0.5)
        expected = 0.7853981633974483
        self.assertEqual(result, expected)

    def test_medium_area(self):
        result = area(7435)
        expected = 173664807.15613723
        self.assertEqual(result, expected)

    def test_large_area(self):
        result = area(1983476)
        expected = 12359581694878.38
        self.assertEqual(result, expected)

    def test_zero_perimeter(self):
        result = perimeter(0)
        expected = 0
        self.assertEqual(result, expected)

    def test_small_perimeter(self):
        result = perimeter(0.5)
        expected = 3.141592653589793
        self.assertEqual(result, expected)

    def test_medium_perimeter(self):
        result = perimeter(7435)
        expected = 46715.48275888022
        self.assertEqual(result, expected)

    def test_large_perimeter(self):
        result = perimeter(1983476)
        expected = 12462547.260343337
        self.assertEqual(result, expected)