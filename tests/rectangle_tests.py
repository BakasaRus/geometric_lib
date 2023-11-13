import unittest
import rectangle

class RectangleAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        rectangle.area(2, 0)
        raise Exception("Zero side!")
    
    def test_simple(self):
        res = rectangle.area(2, 3)
        self.assertEqual(res, 6)
    
    def test_huge(self):
        res = rectangle.area(9999999, 9999888)
        exp_res = 99998870000112
        self.assertEqual(res, exp_res)
        
    def test_neg_side(self):
        rectangle.area(-2, 2)
        raise Exception("Negative side!")

class RectanglePerTestCase(unittest.TestCase):
    def test_zero_side(self):
        rectangle.perimeter(0, 2)
        raise Exception("Zero side!")
    
    def test_simple(self):
        res = rectangle.perimeter(2, 3)
        self.assertEqual(res, 10)
    
    def test_huge(self):
        res = rectangle.perimeter(9999999, 9999888)
        exp_res = 39999774
        self.assertEqual(res, exp_res)
    
    def test_neg_side(self):
        rectangle.perimeter(2, -2)
        raise Exception("Negative side!")
