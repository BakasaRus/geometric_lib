import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_zero_argument_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_zero_argument_perimeter(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_zero_arguments_area(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_rectangle_zero_arguments_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_rectangle_zero_argument_perimeter(self):
        self.assertRaises(ArithmeticError, rectangle.area, -3, 1)

    def test_rectangle_negative_argument_perimeter(self):
        self.assertRaises(ArithmeticError, rectangle.perimeter, -3, 1)

    def test_rectangle_incorrect_data_area(self):
        self.assertRaises(Exception, rectangle.area, "abc", "abc")

    def test_rectangle_incorrect_data_perimeter(self):
        self.assertRaises(Exception, rectangle.perimeter, "abc", "abc")
