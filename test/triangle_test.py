import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    def test_triangle_zero_argument_area(self):
        res = triangle.area(5, 0)
        self.assertEqual(res, 0)

    def test_triangle_negative_argument_area(self):
        self.assertRaises(ArithmeticError, triangle.area, -3, 1)

    def test_triangle_zero_argument_perimeter(self):
        res = triangle.perimeter(5, 0, 6)
        self.assertEqual(res, 0)

    def test_triangle_negative_argument_perimeter(self):
        self.assertRaises(ArithmeticError, triangle.perimeter, -3, 2, 1)

    def test_triangle_incorrect_data_area(self):
        self.assertRaises(Exception, triangle.area, "abc", "abc")

    def test_triangle_incorrect_data_perimeter(self):
        self.assertRaises(Exception, triangle.perimeter, "abc", "abc", "abc")
