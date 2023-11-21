import rectangle
import unittest


class RectangleAreaTestCase(unittest.TestCase):
    def test_zero_height(self):
        res = rectangle.area(0, 2)
        self.assertEqual(res, 0)

    def test_zero_width(self):
        res = rectangle.area(4, 0)
        self.assertEqual(res, 0)

    def test_zero_both(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_big(self):
        res = rectangle.area(408, 750)
        self.assertEqual(res, 306000)
    
    def test_sample(self):
        res = rectangle.area(2, 87)
        self.assertEqual(res, 174)

    def test_small(self):
        res = rectangle.area(1, 1)
        self.assertEqual(res, 1)
    
    def test_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-3, 1)

    def test_negative_both(self):
        with self.assertRaises(ValueError):
            rectangle.area(-3, -3)

    def test_string(self):
        with self.assertRaises(TypeError):
            rectangle.area(1, "Are str allowed?")
