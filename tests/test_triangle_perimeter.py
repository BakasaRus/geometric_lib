import triangle
import unittest


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_zero_side(self):
        res = triangle.perimeter(0, 3, 3)
        self.assertEqual(res, 0)

    def test_impossible_sides(self):
        res = triangle.perimeter(1, 10, 2)
        self.assertEqual(res, 0)
    
    def test_sample(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_negative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-2, 4, 3)

    def test_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("Are str allowed?", 5, 1)
