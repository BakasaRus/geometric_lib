import rectangle
import unittest

class RectanglePerimeterTestCase(unittest.TestCase):
    def test_zero_height(self):
        res = rectangle.perimeter(0, 4)
        self.assertRaises(res, ValueError)

    def test_zero_width(self):
        res = rectangle.perimeter(8, 0)
        self.assertRaises(res, ValueError)

    def test_zero_both(self):
        res = rectangle.perimeter(0, 0)
        self.assertRaises(res, ValueError)

    def test_big(self):
        res = rectangle.perimeter(408, 750)
        self.assertEqual(res, 2316)
    
    def test_sample(self):
        res = rectangle.perimeter(2, 87)
        self.assertEqual(res, 178)

    def test_small(self):
        res = rectangle.perimeter(1, 1)
        self.assertEqual(res, 4)
    
    def test_negative(self):
        res = rectangle.perimeter(-33, 1)
        self.assertRaises(res, ValueError)

    def test_negative_both(self):
        res = rectangle.perimeter(-1, -33)
        self.assertRaises(res, ValueError)

    def test_string(self):
        res = rectangle.perimeter(1, "Are str allowed?")
        self.assertRaises(res, ValueError)
