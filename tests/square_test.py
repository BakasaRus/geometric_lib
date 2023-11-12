import unittest
from square import *

class RectangleTestCase(unittest.TestCase):
    # AREA

    # res = 0
    def test_zero_area_0(self):
        res = area(0)
        self.assertEqual(res, 0)

    # small res
    def test_small_area_0(self):
        res = area(10)
        self.assertEqual(res, 100)
    
    def test_small_area_1(self):
        res = area(209)
        self.assertEqual(res, 43681)

    # big res
    def test_big_area_0(self):
        res = area(12345678987654543)
        self.assertEqual(res, 152415789666214901691804308538849)
    
    def test_big_area_1(self):
        res = area(1111111111111111111111)
        self.assertEqual(res, 1234567901234567901234320987654320987654321)

    # float res
    def test_float_area_0(self):
        res = area(12345432.08)
        self.assertEqual(res, 152409693241893.12)
    
    def test_float_area_1(self):
        res = area(0.13452)
        self.assertEqual(res, 0.0180956304)

    # PERIMETER

    # res = 0
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    # small res
    def test_small_perimeter_0(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
    
    def test_small_perimeter_1(self):
        res = perimeter(209)
        self.assertEqual(res, 836)

    # big res
    def test_big_perimeter_0(self):
        res = perimeter(12345678987654543)
        self.assertEqual(res, 49382715950618172)
    
    def test_big_perimeter_1(self):
        res = perimeter(98765456765434421222)
        self.assertEqual(res, 395061827061737684888)

    # float res
    def test_float_perimeter_0(self):
        res = perimeter(12345432.08)
        self.assertEqual(res, 49381728.32)
    
    def test_float_perimeter_1(self):
        res = perimeter(4.091)
        self.assertEqual(res, 16.364)