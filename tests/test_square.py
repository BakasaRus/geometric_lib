import unittest
from square import *

class SquareTestCase(unittest.TestCase):
    # AREA

    # res = 0
    def test_zero_area_0(self):
        self.assertRaises(ValueError, area, 0)

    # small res
    def test_small_area_0(self):
        res = area(10)
        self.assertEqual(res, 100)

    # big res
    def test_big_area_1(self):
        res = area(1111111111111111111111)
        self.assertEqual(res, 1234567901234567901234320987654320987654321)

    # float res
    def test_float_area_0(self):
        res = area(12345432.08)
        self.assertEqual(res, 152409693241893.12)

    # incorrect
    def test_incorrect_area_0(self):
        self.assertRaises(ValueError, area, -5678976546789)

    # invalid input
    def test_invalid_area(self):
        self.assertRaises(TypeError, area, "*")

    # PERIMETER

    # res = 0
    def test_zero_perimeter(self):
        self.assertRaises(ValueError, perimeter, 0)

    # small res
    def test_small_perimeter_0(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    # big res
    def test_big_perimeter_0(self):
        res = perimeter(12345678987654543)
        self.assertEqual(res, 49382715950618172)

    # float res
    def test_float_perimeter_0(self):
        res = perimeter(12345432.08)
        self.assertEqual(res, 49381728.32)

    # incorrect
    def test_incorrect_perimeter_0(self):
        self.assertRaises(ValueError, perimeter, -123)

    # invalid input
    def test_invalid_perimeter(self):
        self.assertRaises(TypeError, perimeter, ("3"))