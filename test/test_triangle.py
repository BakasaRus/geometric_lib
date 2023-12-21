import unittest
import math

import triangle

class TriangleAreaTestCase(unittest.TestCase):
    def test_simple(self):
        res = triangle.area(3, 4)
        self.assertEqual(res, 6)

    def test_zero_side(self):
        self.assertRaises(Exception, triangle.area, 0, 3)
    
    def test_zero_height(self):
        self.assertRaises(Exception, triangle.area, 3, 0)
    
    def test_negative_side(self):
        self.assertRaises(Exception, triangle.area, -3, 3)
    
    def test_negative_height(self):
        self.assertRaises(Exception, triangle.area, 3, -3)

    def test_string_side(self):
        self.assertRaises(Exception, triangle.area, "hello", 3)

    def test_bool_side(self):
        self.assertRaises(Exception, triangle.area, 3, True)

    def test_string_height(self):
        self.assertRaises(Exception, triangle.area, 3, "helo")

    def test_bool_height(self):
        self.assertRaises(Exception, triangle.area, 3, True)

class TrianglePerimeterTestCase(unittest.TestCase):
    def test_simple(self):
        res = triangle.area(3, 4)
        self.assertEqual(res, 6)

    def test_zero_side(self):
        self.assertRaises(Exception, triangle.perimeter, 0, 3)
    
    def test_zero_height(self):
        self.assertRaises(Exception, triangle.perimeter, 3, 0)
    
    def test_negative_side(self):
        self.assertRaises(Exception, triangle.perimeter, -3, 3)
    
    def test_negative_height(self):
        self.assertRaises(Exception, triangle.perimeter, 3, -3)

    def test_string_side(self):
        self.assertRaises(Exception, triangle.perimeter, "hello", 3)

    def test_bool_side(self):
        self.assertRaises(Exception, triangle.perimeter, 3, True)

    def test_string_height(self):
        self.assertRaises(Exception, triangle.perimeter, 3, "helo")

    def test_bool_height(self):
        self.assertRaises(Exception, triangle.perimeter, 3, True)

class TriangleMedianTestCase(unittest.TestCase):
    def test_simple(self):
        res = triangle.median(3, 4, 5)
        self.assertEqual(res, math.sqrt(2 * 25 + 2 * 16 - 9) / 2)
    
    def test_negative_first_side(self):
        self.assertRaises(Exception, triangle.median, -3, 4, 5)
    
    def test_negative_second_side(self):
        self.assertRaises(Exception, triangle.median, 3, -4, 5)
    
    def test_zero_first_side(self):
        self.assertRaises(Exception, triangle.median, 0, 4, 5)
    
    def test_zero_second_side(self):
        self.assertRaises(Exception, triangle.median, 3, 0, 5)

    def test_string_side(self):
        self.assertRaises(Exception, triangle.median, "hello", 1, 2)

    def test_bool_side(self):
        self.assertRaises(Exception, triangle.median, True, 1, 2)
