import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    # AREA

    # res = 0
    def test_zero_area_0(self):
        self.assertRaises(ValueError, area, 10, 0)

    # small res
    def test_small_area_0(self):
        res = area(10, 11)
        self.assertEqual(res, 110)

    # big res
    def test_big_area_0(self):
        res = area(1009975434567, 12345678987654543)
        self.assertEqual(res, 12468832500581077694496787881)

    # float res
    def test_float_area_0(self):
        res = area(12345432.08, 1113321.67)
        self.assertEqual(res, 13744437060177.172)

    # incorrect
    def test_incorrect_area_0(self):
        self.assertRaises(ValueError, area, -123, 0)

    # PERIMETER

    # res = 0
    def test_zero_perimeter(self):
        self.assertRaises(ValueError, perimeter, 10, 0)

    # small res
    def test_small_perimeter_0(self):
        res = perimeter(10, 11)
        self.assertEqual(res, 42)

    # big res
    def test_big_perimeter_1(self):
        res = perimeter(1111111111111111111111, 98765456765434421222)
        self.assertEqual(res, 2419753135753091064666)

    # float res
    def test_float_perimeter_0(self):
        res = perimeter(12345432.08, 1113321.67)
        self.assertEqual(res, 26917507.5)

    # incorrect
    def test_incorrect_perimeter_0(self):
        self.assertRaises(ValueError, perimeter, -123, -5678)