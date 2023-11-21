import math
import unittest

from triangle import area, perimeter

class TestTriangleFunctions(unittest.TestCase):

    def test_area_positive_sides(self):
        self.assertEqual(area(5, 4), 10)

    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(1, 2, 3), 6)

    def test_area_zero_base(self):
        self.assertEqual(area(0, 4), 0)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 2, 3), 5)

    def test_area_large_values(self):
        self.assertEqual(area(100, 50), 2500)

    def test_wrong_arguments(self):
        self.assertRaises(ValueError, perimeter, "word", "word", "word")

    def test_negative_numbers(self):
        self.assertRaises(ValueError, perimeter, -1, 1, 2)

    def test_wrong_arguments_area(self):
        self.assertRaises(ValueError, area, "abc", "q")

    def test_negative_numbers_area(self):
        self.assertRaises(ValueError, area, -1, 1)