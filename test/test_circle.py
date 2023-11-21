import math
import unittest

from circle import area, perimeter

class TestCircleFunctions(unittest.TestCase):

    def test_area_positive_radius(self):
        self.assertEqual(area(3), math.pi * 9)

    def test_perimeter_positive_radius(self):
        self.assertEqual(perimeter(3), math.pi * 6)

    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_wrong_arguments(self):
        self.assertRaises(ValueError, perimeter, "word")

    def test_negative_numbers(self):
        self.assertRaises(ValueError, perimeter, -1)

    def test_wrong_arguments_area(self):
        self.assertRaises(ValueError, area, "word")

    def test_negative_numbers_area(self):
        self.assertRaises(ValueError, area, -1)



