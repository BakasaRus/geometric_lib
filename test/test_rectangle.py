import math
import unittest

from rectangle import area, perimeter

class TestRectangleFunctions(unittest.TestCase):

    def test_area_positive_sides(self):
        self.assertEqual(area(5, 3), 15)

    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(5, 3), 16)

    def test_area_zero_sides(self):
        self.assertEqual(area(0, 4), 0)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 4), 8)

    def test_area_large_sides(self):
        self.assertEqual(area(100, 200), 20000)

    def test_wrong_arguments(self):
        self.assertRaises(ValueError, perimeter, "word", "word")

    def test_negative_numbers(self):
        self.assertRaises(ValueError, perimeter, -1, 1)

    def test_wrong_arguments_area(self):
        self.assertRaises(ValueError, area, "word", "word")

    def test_negative_numbers_area(self):
        self.assertRaises(ValueError, area, -1, 1)
