import unittest
import circle, rectangle, square, triangle


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


class SquareTestCase(unittest.TestCase):
    def test_square_zero_argument_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_square_negative_argument_area(self):
        self.assertRaises(ArithmeticError, square.area, -3)

    def test_square_zero_argument_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_square_negative_argument_perimeter(self):
        self.assertRaises(ArithmeticError, square.perimeter, -3)

    def test_square_incorrect_data_area(self):
        self.assertRaises(Exception, square.area, "abc")

    def test_square_incorrect_data_perimeter(self):
        self.assertRaises(Exception, square.perimeter, "abc")


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
