import unittest

import square

class SquareAreaTestCase(unittest.TestCase):
    def test_simple(self):
        res = square.area(3)
        self.assertEqual(res, 9)
    
    def test_negative_side(self):
        res = square.area(-3)
        self.assertRaises(Exception, square.area, -3)

    def test_zero_side(self):
        res = square.area(0)
        self.assertRaises(Exception, square.area, 0)

    def test_string_side(self):
        self.assertRaises(Exception, square.area, "hello")

    def test_bool_side(self):
        self.assertRaises(Exception, square.area, True)

class SquarePerimeterTestCase(unittest.TestCase):
    def test_simple(self):
        res = square.area(3)
        self.assertEqual(res, 9)
    
    def test_negative_side(self):
        res = square.area(-3)
        self.assertRaises(Exception, square.perimeter, -3)

    def test_zero_side(self):
        res = square.area(0)
        self.assertRaises(Exception, square.perimeter, 0)

    def test_string_side(self):
        self.assertRaises(Exception, square.perimeter, "hello")

    def test_bool_side(self):
        self.assertRaises(Exception, square.perimeter, True)
