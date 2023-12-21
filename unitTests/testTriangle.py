import unittest

from methods.triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0, 0)
        expected = 0
        self.assertEqual(result, expected)

    def test_small_area(self):
        result = area(0.5, 3)
        expected = 0.75
        self.assertEqual(result, expected)

    def test_medium_area(self):
        result = area(7435, 2871)
        expected = 10672942.5
        self.assertEqual(result, expected)

    def test_large_area(self):
        result = area(1983476, 8937442)
        expected = 8863600854196
        self.assertEqual(result, expected)

    def test_zero_perimeter(self):
        result = perimeter(0, 0, 0)
        expected = 0
        self.assertEqual(result, expected)

    def test_small_perimeter(self):
        result = perimeter(0.5, 3, 7)
        expected = 10.5
        self.assertEqual(result, expected)

    def test_medium_perimeter(self):
        result = perimeter(7435, 2871, 9483)
        expected = 19789
        self.assertEqual(result, expected)

    def test_large_perimeter(self):
        result = perimeter(1983476, 8937442, 9314582)
        expected = 20235500
        self.assertEqual(result, expected)