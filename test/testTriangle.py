import unittest

from lib.triangle import *

class TriangleTestCase(unittest.TestCase):
    testDelta = 0.000000000001

    def test_one_area(self):
        res = area(1, 1)
        self.assertAlmostEqual(res, 0.5, delta=self.testDelta)

    def test_one_perimeter(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_small_area(self):
        res = area(0.00000000001, 0.00000000001)
        self.assertAlmostEqual(res, 4.9999999999999997e-23, delta=self.testDelta)

    def test_small_perimeter(self):
        res = perimeter(0.00000000001, 0.00000000001, 0.00000000001)
        self.assertAlmostEqual(res, 0.00000000003, delta=self.testDelta)

    def test_large_area(self):
        res = area(10000000000000, 10000000000000)
        self.assertAlmostEqual(res, 50000000000000000000000000.0, delta=self.testDelta)

    def test_large_perimeter(self):
        res = perimeter(10000000000000, 10000000000000, 10000000000000)
        self.assertAlmostEqual(res, 30000000000000, delta=self.testDelta)

    def test_larger_aprox_one_area(self):
        res = area(1.00000000001, 1.00000000001)
        self.assertAlmostEqual(res, 0.50000000001, delta=self.testDelta)

    def test_larger_aprox_one_perimeter(self):
        res = perimeter(1.00000000001, 1.00000000001, 1.00000000001)
        self.assertAlmostEqual(res, 3.00000000003, delta=self.testDelta)

    def test_smaller_aprox_one_area(self):
        res = area(0.999999999999, 0.999999999999)
        self.assertAlmostEqual(res, 0.499999999999, delta=self.testDelta)

    def test_smaller_aprox_one_perimeter(self):
        res = perimeter(0.999999999999, 0.999999999999, 0.999999999999)
        self.assertAlmostEqual(res, 2.999999999997, delta=self.testDelta)

    def test_zero_side_area(self):
        with self.assertRaises(ValueError):
            area(0, 0)

    def test_zero_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(0, 0, 0)

    def test_neg_side_area(self):
        with self.assertRaises(ValueError):
            area(-1, -1)

    def test_neg_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-1, -1, -1)

    def test_type_string_area(self):
        with self.assertRaises(TypeError):
            area("bad string", "bad string")

    def test_type_string_perim(self):
        with self.assertRaises(TypeError):
            perimeter("bad string", "bad string", "bad string")

    def test_type_tuple_area(self):
        with self.assertRaises(TypeError):
            area((1, 2), (1, 2))

    def test_type_tuple_perim(self):
        with self.assertRaises(TypeError):
            perimeter((1, 2), (1, 2), (1, 2))

    def test_type_array_area(self):
        with self.assertRaises(TypeError):
            area([1, 2], [1, 2])

    def test_type_array_perim(self):
        with self.assertRaises(TypeError):
            perimeter([1, 2], [1, 2], [1, 2])
