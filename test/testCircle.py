import unittest

from lib.circle import *

class CircleTestCase(unittest.TestCase):
    testDelta = 0.000000000001

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

    def test_zero_rad_area(self):
        with self.assertRaises(ValueError):
            area(0)

    def test_zero_rad_perim(self):
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_neg_rad_area(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_neg_rad_perim(self):
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_type_string_area(self):
        with self.assertRaises(TypeError):
            area("bad string")

    def test_type_string_perim(self):
        with self.assertRaises(TypeError):
            perimeter("bad string")

    def test_type_tuple_area(self):
        with self.assertRaises(TypeError):
            area((1, 2))

    def test_type_tuple_perim(self):
        with self.assertRaises(TypeError):
            perimeter((1, 2))

    def test_type_array_area(self):
        with self.assertRaises(TypeError):
            area([1, 2])

    def test_type_array_perim(self):
        with self.assertRaises(TypeError):
            perimeter([1, 2])
