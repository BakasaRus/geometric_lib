import rectangle
import unittest

class RectanglePerimeterTestCase(unittest.TestCase):
    def test_zero_height(self):
        res = rectangle.perimeter(0, 4)
        self.assertEqual(0, 4)

    def test_zero_width(self):
        res = rectangle.perimeter(8, 0)
        self.assertEqual(res, 0)

    def test_zero_both(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

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

        with self.assertRaises(ValueError):
            rectangle.perimeter(-33, 1)

    def test_negative_both(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-1, -33)

    def test_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(1, "Are str allowed?")
