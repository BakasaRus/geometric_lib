import unittest
import circle

class CircleTestCase(unittest.TestCase):
    def test_circle_radius_area(self):
        res = circle.area(100000)
        self.assertEqual(res, 31415926535.89793)

    def test_circle_zero_radius_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_circle_zero_radius_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_negative_radius_area(self):
        self.assertRaises(ArithmeticError, circle.area, -2)

    def test_circle_negative_radius_perimeter(self):
        self.assertRaises(ArithmeticError, circle.perimeter, -2)

    def test_circle_incorrect_data_area(self):
        self.assertRaises(Exception, circle.area, "abc")

    def test_circle_incorrect_data_perimeter(self):
        self.assertRaises(Exception, circle.perimeter, "abc")
