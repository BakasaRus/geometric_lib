import unittest
from src import square

class SquareTestcase(unittest.TestCase):
    def test_zero_mul_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_zero_mul_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_calculation_area(self):
        res = square.area(4)
        self.assertEqual(res, 16)

    def test_calculation_perimeter(self):
        res = square.perimeter(4)
        self.assertEqual(res, 16)

    #def test_string_input_area(self):
    #    with self.assertRaises(TypeError):
    #        square.area('5')

    #def test_string_input_perimeter(self):
    #    with self.assertRaises(TypeError):
    #        square.perimeter('10')