import math
import unittest

def area(a, b):
    '''
    Takes numbers a and b and returns the area of a rectangle with these sides.
    Example: area(5, 3) = 15
    '''
    return a * b

def perimeter(a, b):
    '''
    Takes numbers a and b and returns the perimeter of a rectangle with these sides.
    Example: perimeter(5, 3) = 16
    '''
    return a + b + a + b


class TestRectangleFunctions(unittest.TestCase):

    def test_area_positive_sides(self):
        self.assertEqual(area(5, 3), 15)

    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(5, 3), 16)

    def test_area_zero_sides(self):
        self.assertEqual(area(0, 4), 0)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 4), 8)

    def test_area_large_sides(self):
        self.assertEqual(area(100, 200), 20000)