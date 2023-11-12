import unittest
from circle import *

import math

class RectangleTestCase(unittest.TestCase):
    # AREA

    # res = 0
    def test_zero_area_0(self):
        res = area(0)
        self.assertEqual(res, 0)

    # small res
    def test_small_area_0(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)
    
    def test_small_area_1(self):
        res = area(209)
        self.assertEqual(res, 137227.90870145577)

    # big res
    def test_big_area_0(self):
        res = area(12345678987654543)
        self.assertEqual(res, 4.7882832510646796e+32)
    
    def test_big_area_1(self):
        res = area(1111111111111111111111)
        self.assertEqual(res, 3.8785094488762877e+42)

    # float res
    def test_float_area_0(self):
        res = area(12345432.08)
        self.assertEqual(res, 478809172624605.4)
    
    def test_float_area_1(self):
        res = area(0.13452)
        self.assertEqual(res, 0.05684909952671613)

    # PERIMETER

    # res = 0
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    # small res
    def test_small_perimeter_0(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)
    
    def test_small_perimeter_1(self):
        res = perimeter(209)
        self.assertEqual(res, 1313.1857292005336)

    # big res
    def test_big_perimeter_0(self):
        res = perimeter(12345678987654543)
        self.assertEqual(res, 7.757018882238678e+16)
    
    def test_big_perimeter_1(self):
        res = perimeter(98765456765434421222)
        self.assertEqual(res, 6.205616668054581e+20)

    # float res
    def test_float_perimeter_0(self):
        res = perimeter(12345432.08)
        self.assertEqual(res, 77568637.45583951)
    
    def test_float_perimeter_1(self):
        res = perimeter(4.091)
        self.assertEqual(res, 25.704511091671687)