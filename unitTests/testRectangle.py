import unittest

from methods.rectangle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0, 0)
        expected = 0
        self.assertEqual(result, expected)

    def test_small_area(self):
        result = area(0.5, 3)
        expected = 1.5
        self.assertEqual(result, expected)

    def test_medium_area(self):
        result = area(7435, 2871)
        expected = 21345885
        self.assertEqual(result, expected)

    def test_large_area(self):
        result = area(1983476, 8937442)
        expected = 17727201708392
        self.assertEqual(result, expected)

    def test_zero_perimeter(self):
        result = perimeter(0, 0)
        expected = 0
        self.assertEqual(result, expected)

    def test_small_perimeter(self):
        result = perimeter(0.5, 3)
        expected = 7
        self.assertEqual(result, expected)

    def test_medium_perimeter(self):
        result = perimeter(7435, 2871)
        expected = 20612
        self.assertEqual(result, expected)

    def test_large_perimeter(self):
        result = perimeter(1983476, 8937442)
        expected = 21841836
        self.assertEqual(result, expected)