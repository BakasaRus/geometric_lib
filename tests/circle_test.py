import unittest
from src import circle

class CircleTestcase(unittest.TestCase):
    def test_zero_mul_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_zero_mul_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_calculation_area(self):
        res = round(circle.area(7), 5)
        self.assertEqual(res, 153.93804)

    def test_calculation_perimeter(self):
        res = round(circle.perimeter(4), 5)
        self.assertEqual(res, 25.13274)

    #def test_string_input_area(self):
    #    with self.assertRaises(TypeError):
    #        circle.area('2')

    #def test_string_input_perimeter(self):
    #    with self.assertRaises(TypeError):
    #        circle.perimeter('4')