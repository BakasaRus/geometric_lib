import math
import unittest

def area(a, h):
    '''
    Takes numbers a and h and returns the area of a triangle with side a and height h.
    Example: area(5, 4) = 10
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Takes numbers a, b, and c and returns the perimeter of a triangle with these sides.
    Example: perimeter(1, 2, 3) = 6
    '''
    return a + b + c


class TestTriangleFunctions(unittest.TestCase):

    def test_area_positive_sides(self):
        self.assertEqual(area(5, 4), 10)

    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(1, 2, 3), 6)

    def test_area_zero_base(self):
        self.assertEqual(area(0, 4), 0)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 2, 3), 5)

    def test_area_large_values(self):
        self.assertEqual(area(100, 50), 2500)