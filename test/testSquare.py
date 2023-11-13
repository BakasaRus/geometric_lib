import unittest

from lib.square import *

class SquareTestCase(unittest.TestCase):
    testDelta = 0.000000000001

    def test_one_side_area(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_one_side_perimeter(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_small_side_area(self):
        res = area(0.00000000001)
        self.assertAlmostEqual(res, 9.999999999999999e-23, delta=self.testDelta)

    def test_small_side_perimeter(self):
        res = perimeter(0.00000000001)
        self.assertAlmostEqual(res, 4e-11, delta=self.testDelta)

    def test_large_side_area(self):
        res = area(10000000000000)
        self.assertEqual(res, 100000000000000000000000000)

    def test_large_side_perimeter(self):
        res = perimeter(10000000000000)
        self.assertEqual(res, 40000000000000)

    def test_larger_aprox_one_side_area(self):
        res = area(1.00000000001)
        self.assertAlmostEqual(res, 1.00000000002, delta=self.testDelta)

    def test_larger_aprox_one_side_perimeter(self):
        res = perimeter(1.00000000001)
        self.assertAlmostEqual(res, 4.00000000004, delta=self.testDelta)

    def test_smaller_aprox_one_side_area(self):
        res = area(0.999999999999)
        self.assertAlmostEqual(res, 0.999999999998, delta=self.testDelta)

    def test_smaller_aprox_one_side_perimeter(self):
        res = perimeter(0.999999999999)
        self.assertAlmostEqual(res, 3.999999999996, delta=self.testDelta)

    def test_zero_side_area(self):
        with self.assertRaises(ValueError):
            area(0)

    def test_zero_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_neg_side_area(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_neg_side_perimeter(self):
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


