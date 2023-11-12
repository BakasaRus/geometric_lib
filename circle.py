import math
import unittest

def area(r):
    '''
    Takes a number r and returns the area of a circle with radius r.
    Example: area(3) = pi * 9
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Takes a number r and returns the circumference of a circle with radius r.
    Example: perimeter(3) = pi * 6
    '''
    return 2 * math.pi * r

class TestCircleFunctions(unittest.TestCase):

    def test_area_positive_radius(self):
        self.assertEqual(area(3), math.pi * 9)

    def test_area_positive_radius(self):
        self.assertEqual(area(4), math.pi * 4)

    def test_perimeter_positive_radius(self):
        self.assertEqual(perimeter(3), math.pi * 6)

    def test_perimeter_positive_radius(self):
        self.assertEqual(perimeter(2), math.pi * 4)

    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)
