import unittest
from geometric_lib.triangle import *


class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(8, 0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1, 2)
        self.assertEqual(res, 1)

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_one_two_three(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)

    def test_perimeter_equilateral(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_perimeter_type_error(self):
        self.assertRaises(TypeError, perimeter, 0, "1", "aaa")

    def test_area_type_error(self):
        self.assertRaises(TypeError, area, [1, 2], "0")

    def test_perimeter_value_error(self):
        self.assertRaises(ValueError, perimeter, -1, 1, 2)

    def test_area_value_error(self):
        self.assertRaises(ValueError, area, 5, -1)


if __name__ == "__main__":
    unittest.main()