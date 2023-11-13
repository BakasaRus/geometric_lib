import triangle
import unittest


class TriangleAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        res = triangle.area(0, 1)
        self.assertEqual(res, 0)
    
    def test_zero_height(self):
        res = triangle.area(1, 0)
        self.assertEqual(res, 0)
    
    def test_sample(self):
        res = triangle.area(2, 4)
        self.assertEqual(res, 4)
    
    def test_negative_side(self):
        res = triangle.area(-42, 4)
        self.assertEqual(res, 0)
    
    def test_negative_height(self):
        res = triangle.area(2, -4)
        self.assertEqual(res, 0)

    def test_string(self):
        with self.assertRaises(TypeError):
            triangle.area("Are str allowed?", 5)