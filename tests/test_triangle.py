import unittest
from triangle import *

class RectangleTestCase(unittest.TestCase):
    # AREA

    # res = 0
    def test_zero_area_0(self):
        self.assertRaises(ValueError, area, 10, 0)

    # small res
    def test_small_area_1(self):
        res = area(4, 209)
        self.assertEqual(res, 418)

    # big res
    def test_big_area_0(self):
        res = area(100997543456864665558, 1234567876543)
        self.assertEqual(res, 6.234416138080039e+31)

    # float res
    def test_float_area_0(self):
        res = area(12345432.08, 1113321.67)
        self.assertEqual(res, 6872218530088.586)

    # incorrect
    def test_incorrect_area_0(self):
        self.assertRaises(ValueError, area, -123, -5678)

    # PERIMETER

    # res = 0
    def test_zero_perimeter(self):
        self.assertRaises(ValueError, perimeter, 0, 0, 0)

    # small res
    def test_small_perimeter_0(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    # big res
    def test_big_perimeter_1(self):
        res = perimeter(3654312701234854312, 2283945438271783945, 4111101788889211101)
        self.assertEqual(res, 10049359928395849358)

    # float res
    def test_float_perimeter_0(self):
        res = perimeter(169702963701.273, 226270618268.364, 282838272835.455)
        self.assertEqual(res, 678811854805.092)

    # incorrect
    def test_incorrect_perimeter_0(self):
        self.assertRaises(ValueError, perimeter, 0, -5678, -8)

    #incrorrect triangle
    def test_incorrect_triangle_perimeter_0(self):
        self.assertRaises(ValueError, perimeter, 45, 32, 1000)