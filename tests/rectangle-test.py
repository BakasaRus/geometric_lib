import unittest
from geometric_lib.rectangle import *


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_float(self):
        res = area(1.0/9.0, 3.0)
        self.assertEqual(res, 1.0/3.0)

    def test_perimeter_zero(self):
        res = perimeter(100, 0)
        self.assertEqual(res, 200)

    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_type_error(self):
        self.assertRaises(TypeError, perimeter, "abc", 1)

    def test_area_type_error(self):
        self.assertRaises(TypeError, area, [1, 2, 3], "aaa")

    def test_perimeter_value_error(self):
        self.assertRaises(ValueError, perimeter, -1, 1)

    def test_area_value_error(self):
        self.assertRaises(ValueError, area, -10, -5)


if __name__ == "__main__":
    unittest.main()