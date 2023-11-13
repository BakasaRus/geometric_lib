import unittest, circle


class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_zero_radius_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_small_radius_area(self):
        res = circle.area(3)
        self.assertEqual(res, 28.274333882308138)

    def test_small_perimeter_perimeter(self):
        res = circle.perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_big_radius_area(self):
        res = circle.area(100000)
        self.assertEqual(res, 31415926535.89793)

    def test_big_radius_perimeter(self):
        res = circle.perimeter(100000)
        self.assertEqual(res, 628318.5307179586)

    def test_negative_radius_area(self):
        res = circle.area(-2)
        self.assertRaises(ArithmeticError, res)

    def test_negative_radius_perimeter(self):
        res = circle.perimeter(-2)
        self.assertRaises(ArithmeticError, res)
