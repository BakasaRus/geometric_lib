import unittest
import square

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