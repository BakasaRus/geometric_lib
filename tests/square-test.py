import unittest
from geometric_lib.square import *


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_sqrt_two(self):
        res = area(2**0.5)
        self.assertAlmostEqual(res, 2)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_ten(self):
        res = perimeter(10)
        self.assertEqual(res, 40)


if __name__ == "__main__":
    unittest.main()