import unittest

from methods.square import *

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0)
        expected = 0
        self.assertEqual(result, expected)

    def test_small_area(self):
        result = area(0.5)
        expected = 0.25
        self.assertEqual(result, expected)

    def test_medium_area(self):
        result = area(7435)
        expected = 55279225
        self.assertEqual(result, expected)

    def test_large_area(self):
        result = area(1983476)
        expected = 3934177042576
        self.assertEqual(result, expected)

    def test_zero_perimeter(self):
        result = perimeter(0)
        expected = 0
        self.assertEqual(result, expected)

    def test_small_perimeter(self):
        result = perimeter(0.5)
        expected = 2
        self.assertEqual(result, expected)

    def test_medium_perimeter(self):
        result = perimeter(7435)
        expected = 29740
        self.assertEqual(result, expected)

    def test_large_perimeter(self):
        result = perimeter(1983476)
        expected = 7933904
        self.assertEqual(result, expected)