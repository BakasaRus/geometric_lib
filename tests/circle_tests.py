import math
import unittest
import circle


class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_zero_radius_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_area_1(self):
        res = circle.area(1)
        self.assertEqual(res, math.pi)

    def test_area_2(self):
        radius = 1_000_000_000
        res = circle.area(radius)
        self.assertEqual(res, math.pi * radius * radius)


if __name__ == "__main__":
    unittest.main()
