import unittest
from circle import *

import math

class CircleTestCase(unittest.TestCase):
    # AREA
    delta = 0.000000001
    # res = 0
    def test_zero_area_0(self):
        self.assertRaises(ValueError, area, 0)

    # small res
    def test_small_area_0(self):
        res = area(10)
        self.assertAlmostEqual(res, 314.1592653589793, delta=self.delta)

    # big res
    def test_big_area_0(self):
        res = area(12345678987654543)
        self.assertAlmostEqual(res, 4.7882832510646796e+32, delta=self.delta)
    # float res
    def test_float_area_1(self):
        res = area(0.13452)
        self.assertAlmostEqual(res, 0.05684909952671613, delta=self.delta)
    # incorrect
    def test_incorrect_area_0(self):
        self.assertRaises(ValueError, area, -123)
    # invalid input
    def test_invalid_area(self):
        self.assertRaises(TypeError, area, (0, 2, 1))
    # PERIMETER
    # res = 0
    def test_zero_perimeter(self):
        self.assertRaises(ValueError, perimeter, 0)
    # small res
    def test_small_perimeter_0(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 62.83185307179586, delta=self.delta)
    # big res
    def test_big_perimeter_0(self):
        res = perimeter(12345678987654543)
        self.assertAlmostEqual(res, 7.757018882238678e+16, delta=self.delta)
    # float res
    def test_float_perimeter_1(self):
        res = perimeter(4.091)
        self.assertAlmostEqual(res, 25.704511091671687, delta=self.delta)
    # incorrect
    def test_incorrect_perimeter_0(self):
        self.assertRaises(ValueError, perimeter, -1245673)
    # invalid input
    def test_invalid_perimeter(self):
        self.assertRaises(TypeError, perimeter, "454")
