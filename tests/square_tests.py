import unittest
import square

class SquareAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertRaises(ValueError, square.area, 0)

    def test_simple(self):
        res = square.area(2)
        self.assertEqual(res, 4)
    
    def test_huge(self):
        result = square.area(9999999)
        expected_result = 99999980000001
        self.assertEqual(expected_result, result)
    
    def test_neg_side(self):
        self.assertRaises(ValueError, square.area, -2)

class SquarePerTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertRaises(ValueError, square.perimeter, 0)
    
    def test_simple(self):
        res = square.perimeter(3)
        self.assertEqual(res, 12)
    
    def test_huge(self):
        result = square.perimeter(9999999)
        expected_result = 39999996
        self.assertEqual(expected_result, result)
    
    def test_neg_side(self):
         self.assertRaises(ValueError, square.perimeter, -2)