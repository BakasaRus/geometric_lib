import math
import unittest

def area(a):
    '''
    Takes a number a and returns the area of a square with side length a.
    Example: area(5) = 25
    '''
    return a * a

def perimeter(a):
    '''
    Takes a number a and returns the perimeter of a square with side length a.
    Example: perimeter(5) = 20
    '''
    return 4 * a

class TestSquareFunctions(unittest.TestCase):

    def test_area_positive_side(self):
        self.assertEqual(area(5), 25)

    def test_perimeter_positive_side(self):
        self.assertEqual(perimeter(5), 20)

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_area_large_side(self):
        self.assertEqual(area(100), 10000)
