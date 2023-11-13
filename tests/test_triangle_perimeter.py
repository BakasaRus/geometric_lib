import triangle
import unittest


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_zero_side(self):
        res = triangle.perimeter(0, 3, 3)
        self.assertRaises(res, ValueError)

    def test_impossible_sides(self):
        res = triangle.perimeter(1, 10, 2)
        self.assertRaises(res, ValueError)
    
    def test_sample(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_negative(self):
        res = triangle.perimeter(-2, 4, 3)
        self.assertRaises(res, ValueError)

    def test_string(self):
        res = triangle.perimeter("Are str allowed?", 5, 1)
        self.assertRaises(res, ValueError)
