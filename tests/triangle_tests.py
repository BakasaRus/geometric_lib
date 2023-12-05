import unittest
import triangle

class TriangleAreaTestCase(unittest.TestCase):
    # def test_zero_side(self):
    #     self.assertRaises(ValueError, triangle.area, 0, 2)
    
    # def test_zero_height(self):
    #     self.assertRaises(ValueError, triangle.area, 2, 0)
    
    def test_simple(self):
        res = triangle.area(2, 4)
        self.assertEqual(res, 4)
    
    # def test_huge(self):
    #     res = triangle.area(9999999, 9999888)
    #     exp_res = 49999435000056.0
    #     self.assertEqual(exp_res, res)
    
    # def test_neg_side(self):
    #     self.assertRaises(ValueError, triangle.area, -2, 2)
    
    # def test_neg_height(self):
    #     self.assertRaises(ValueError, triangle.area, 2, -2)
    
    # def test_invalid_type(self):
    #     self.assertRaises(TypeError, triangle.area, "100", 3)
    
class TrianglePerTestCase(unittest.TestCase):
    # def test_zero_side(self):
    #     self.assertRaises(ValueError, triangle.perimeter, 0, 2, 3)
    
    def test_simple(self):
        res = triangle.perimeter(2, 4, 3)
        self.assertEqual(res, 9)
    
    # def test_huge(self):
    #     res = triangle.perimeter(9999999, 9999888, 9999777)
    #     exp_res = 29999664
    #     self.assertEqual(exp_res, res)
    
    # def test_neg_side(self):
    #     self.assertRaises(ValueError, triangle.perimeter, -2, 2, 3)
    
    # def test_invalid_type(self):
    #     self.assertRaises(TypeError, triangle.perimeter, "100", 3, 4)
