import unittest
from src import rectangle

class RectangleTestcase(unittest.TestCase):
    def test_zero_mul_area(self):
        res = rectangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_zero_mul_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_calculation_area(self):
        res = rectangle.area(5, 6)
        self.assertEqual(res, 30)

    def test_calculation_perimeter(self):
        res = rectangle.perimeter(5, 6)
        self.assertEqual(res, 22)

    #def test_string_input_area(self):
    #    with self.assertRaises(TypeError):
    #        rectangle.area('5', '5')

    # def test_string_input_perimeter(self):
    #    with self.assertRaises(TypeError):
    #        rectangle.perimeter('10', '5')