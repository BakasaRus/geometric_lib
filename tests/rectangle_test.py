import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    # AREA

    # res = 0
    def test_zero_area_0(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_zero_area_1(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    # small res
    def test_small_area_0(self):
        res = area(10, 11)
        self.assertEqual(res, 110)
    
    def test_small_area_1(self):
        res = area(4, 209)
        self.assertEqual(res, 836)

    # big res
    def test_big_area_0(self):
        res = area(1009975434567, 12345678987654543)
        self.assertEqual(res, 12468832500581077694496787881)
    
    def test_big_area_1(self):
        res = area(1111111111111111111111, 98765456765434421222)
        self.assertEqual(res, 109739396406038245802211248282581618397642)

    # float res
    def test_float_area_0(self):
        res = area(12345432.08, 1113321.67)
        self.assertEqual(res, 13744437060177.172)
    
    def test_float_area_1(self):
        res = area(0.134, 4.09)
        self.assertEqual(res, 0.54806)

    # PERIMETER

    # res = 0
    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    # small res
    def test_small_perimeter_0(self):
        res = perimeter(10, 11)
        self.assertEqual(res, 42)
    
    def test_small_perimeter_1(self):
        res = perimeter(4, 209)
        self.assertEqual(res, 426)

    # big res
    def test_big_perimeter_0(self):
        res = perimeter(1009975434567, 12345678987654543)
        self.assertEqual(res, 24693377926178220)
    
    def test_big_perimeter_1(self):
        res = perimeter(1111111111111111111111, 98765456765434421222)
        self.assertEqual(res, 2419753135753091064666)

    # float res
    def test_float_perimeter_0(self):
        res = perimeter(12345432.08, 1113321.67)
        self.assertEqual(res, 26917507.5)
    
    def test_float_perimeter_1(self):
        res = perimeter(0.134, 4.09)
        self.assertEqual(res, 8.448)