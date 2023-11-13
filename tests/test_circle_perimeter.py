import circle
import unittest, math


class CirclePerimeterTestCase(unittest.TestCase):
    def test_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_big(self):
        res = circle.perimeter(408750)
        self.assertEqual(res, math.pi * 817500)

    def test_sample(self):
        res = circle.perimeter(34)
        self.assertEqual(res, math.pi * 68)
    
    def test_small(self):
        res = circle.perimeter(7)
        self.assertEqual(res, math.pi * 14)
    
    def test_negative(self):
        res = circle.perimeter(-2)
        self.assertRaises(res, ValueError)

    def test_string(self):
        res = circle.perimeter("Are str allowed?")
        self.assertRaises(res, ValueError)