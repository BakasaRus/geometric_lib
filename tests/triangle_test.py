import unittest
from src import triangle

class TriangleTestcase(unittest.TestCase):
    def test_zero_mul_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_zero_mul_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_calculation_area(self):
        res = triangle.area(8, 6)
        self.assertEqual(res, 24)

    def test_calculation_perimeter(self):
        res = triangle.perimeter(5, 6, 8)
        self.assertEqual(res, 19)

    #def test_string_input_area(self):
    #    with self.assertRaises(TypeError):
    #        triangle.area('5', '3')

    #def test_string_input_perimeter(self):
    #    with self.assertRaises(TypeError):
    #        triangle.perimeter('10', '7', '8')