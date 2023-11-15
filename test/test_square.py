import math
import unittest

from square import area, perimeter

class TestSquareFunctions(unittest.TestCase):

    def test_area_positive_side(self):
        self.assertEqual(area(5), 25)

    def test_perimeter_positive_side(self):
        self.assertEqual(perimeter(5), 20)

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_area_large_side(self):
        self.assertEqual(area(100), 10000)

    def test_wrong_arguments(self):
        self.assertRaises(ValueError, perimeter, "word")

    def test_negative_numbers(self):
        self.assertRaises(ValueError, perimeter, -1)

    def test_wrong_arguments_area(self):
        self.assertRaises(ValueError, area, "word")

    def test_negative_numbers_area(self):
        self.assertRaises(ValueError, area, -1)