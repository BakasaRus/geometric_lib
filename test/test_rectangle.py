import unittest

import rectangle

class RectangleAreaTestCase(unittest.TestCase):
    def test_simple(self):
        res = rectangle.area(3, 4)
        self.assertEqual(res, 12)
    
    def test_negative_side(self):
        res = rectangle.area(-3, 4)
        self.assertRaises(Exception, rectangle.area, -3, 4)

    def test_zero_side(self):
        res = rectangle.area(0, 1)
        self.assertRaises(Exception, rectangle.area, 0, 1)

    def test_string_side(self):
        self.assertRaises(Exception, rectangle.area, "hello", 1)

    def test_bool_side(self):
        self.assertRaises(Exception, rectangle.area, True, 1)

class RectanglePerimeterTestCase(unittest.TestCase):
    def test_simple(self):
        res = rectangle.perimeter(3, 4)
        self.assertEqual(res, 14)
    
    def test_negative_side(self):
        self.assertRaises(Exception, rectangle.perimeter, -3, 4)

    def test_zero_side(self):
        self.assertRaises(Exception, rectangle.perimeter, 0, 1)

    def test_string_side(self):
        self.assertRaises(Exception, rectangle.perimeter, "hello", 1)

    def test_bool_side(self):
        self.assertRaises(Exception, rectangle.perimeter, True, 1)
