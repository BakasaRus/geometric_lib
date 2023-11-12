import unittest
from triangle import *

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
        self.assertEqual(res, 55)
    
    def test_small_area_1(self):
        res = area(4, 209)
        self.assertEqual(res, 418)

    # big res
    def test_big_area_0(self):
        res = area(100997543456864665558, 1234567876543)
        self.assertEqual(res, 6.234416138080039e+31)
    
    def test_big_area_1(self):
        res = area(1111111111111111111111, 98765456765434421226)
        self.assertEqual(res, 5.486969820301912e+40)

    # float res
    def test_float_area_0(self):
        res = area(12345432.08, 1113321.67)
        self.assertEqual(res, 6872218530088.586)
    
    def test_float_area_1(self):
        res = area(0.134, 4.09)
        self.assertEqual(res, 0.27403)

    # PERIMETER

    # res = 0
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    # small res
    def test_small_perimeter_0(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_small_perimeter_1(self):
        res = perimeter(45, 34, 65)
        self.assertEqual(res, 144)

    # big res
    def test_big_perimeter_0(self):
        res = perimeter(1009975434567, 1009975434500, 1009975414557)
        self.assertEqual(res, 3029926283624)
    
    def test_big_perimeter_1(self):
        res = perimeter(3654312701234854312, 2283945438271783945, 4111101788889211101)
        self.assertEqual(res, 10049359928395849358)

    # float res
    def test_float_perimeter_0(self):
        res = perimeter(12345432.08, 1113321.67, 5676543456.54)
        self.assertEqual(res, 5690002210.29)
    
    def test_float_perimeter_1(self):
        res = perimeter(3.134, 4.09, 5.86)
        self.assertEqual(res, 13.084)