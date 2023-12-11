import unittest
from circle import *


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertEqual(res, 3.141592653589793)

    def test_area_pi(self):
        res = area(1.0/(3.141592653589793**0.5))
        self.assertAlmostEqual(res, 1)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_one(self):
        res = perimeter(1)
        self.assertEqual(res, 2*3.141592653589793)

    def test_perimeter_pi(self):
        res = perimeter(1.0/(2*3.141592653589793))
        self.assertEqual(res, 1)

    def test_perimeter_type_error(self):
        self.assertRaises(TypeError, perimeter, "abc")

    def test_area_type_error(self):
        self.assertRaises(TypeError, area, [1, 2, 3])

    def test_perimeter_value_error(self):
        self.assertRaises(ValueError, perimeter, -1)

    def test_area_value_error(self):
        self.assertRaises(ValueError, area, -10)


if __name__ == "__main__":
    unittest.main()
