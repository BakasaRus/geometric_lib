import math

import unittest

def area(r):
    '''Принимает число r, возвращает площадь круга радиусом r'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r, возвращает длину окружности радиусом r'''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    testDelta = 0.000000000001

    def test_zero_rad_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_rad_perim(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_small_rad_area(self):
        res = area(0.0001)
        self.assertAlmostEqual(res, 3.141592653589793e-08, delta=self.testDelta)

    def test_small_rad_perim(self):
        res = perimeter(0.0001)
        self.assertAlmostEqual(res, 0.0006283185307179586, delta=self.testDelta)

    def test_large_rad_area(self):
        res = area(10000000000000)
        self.assertAlmostEqual(res, 3.141592653589793e+26, delta=self.testDelta)

    def test_large_rad_perim(self):
        res = perimeter(10000000000000)
        self.assertAlmostEqual(res, 62831853071795.86, delta=self.testDelta)

    def test_one_rad_area(self):
        res = area(1)
        self.assertAlmostEqual(res, 3.141592653589793, delta=self.testDelta)

    def test_one_rad_perim(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 6.283185307179586, delta=self.testDelta)

    def test_larger_aprox_one_rad_area(self):
        res = area(1.00000000001)
        self.assertAlmostEqual(res, 3.141592653652625, delta=self.testDelta)

    def test_larger_aprox_one_rad_perim(self):
        res = perimeter(1.00000000001)
        self.assertAlmostEqual(res, 6.283185307242418, delta=self.testDelta)

    def test_smaller_prox_one_rad_area(self):
        res = area(0.999999999999)
        self.assertAlmostEqual(res, 3.14159265358351, delta=self.testDelta)

    def test_smaller_prox_one_rad_perim(self):
        res = perimeter(0.999999999999)
        self.assertAlmostEqual(res, 6.283185307173303, delta=self.testDelta)

