import circle, rectangle, square, triangle

import unittest
import math

class CircleAreaTestCase(unittest.TestCase):
    def test_zero_r(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    
    def test_simple(self):
        res = circle.area(2)
        self.assertEqual(res, math.pi*4)

    def test_huge(self):
        result = circle.area(9999999)
        expected_result = 314159202527129.4
        self.assertEqual(expected_result, result)
    
    def test_neg_r(self):
        res = circle.area(-2)
        self.assertEqual(res, -1)

class CirclePerTestCase(unittest.TestCase):
    def test_zero_r(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_simple(self):
        res = circle.perimeter(2)
        self.assertEqual(res, math.pi*4)
    
    def test_huge(self):
        result = circle.perimeter(9999999)
        expected_result = 62831846.788610555
        self.assertEqual(expected_result, result)
    
    def test_neg_r(self):
        res = circle.perimeter(-2)
        self.assertEqual(res, -1)

class RectangleAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        res = rectangle.area(0, 10)
        self.assertEqual(res, 0)
    
    def test_simple(self):
        res = rectangle.area(2, 3)
        self.assertEqual(res, 6)
    
    def test_huge(self):
        res = rectangle.area(9999999, 9999888)
        exp_res = 99998870000112
        self.assertEqual(res, exp_res)
        
    def test_neg_side(self):
        res = rectangle.area(-2, 2)
        self.assertEqual(res, -1)

class RectanglePerTestCase(unittest.TestCase):
    def test_zero_side(self):
        res = rectangle.perimeter(0, 10)
        self.assertEqual(res, -1)
    
    def test_simple(self):
        res = rectangle.perimeter(2, 3)
        self.assertEqual(res, 10)
    
    def test_huge(self):
        res = rectangle.perimeter(9999999, 9999888)
        exp_res = 39999774
        self.assertEqual(res, exp_res)
    
    def test_neg_side(self):
        res = rectangle.perimeter(-2, 3)
        self.assertEqual(res, -1)

class SquareAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    
    def test_simple(self):
        res = square.area(2)
        self.assertEqual(res, 4)
    
    def test_huge(self):
        result = square.area(9999999)
        expected_result = 99999980000001
        self.assertEqual(expected_result, result)
    
    def test_neg_side(self):
        res = square.area(-2)
        self.assertEqual(res, -1)

class SquarePerTestCase(unittest.TestCase):
    def test_zero_side(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_simple(self):
        res = square.perimeter(3)
        self.assertEqual(res, 12)
    
    def test_huge(self):
        result = square.perimeter(9999999)
        expected_result = 39999996
        self.assertEqual(expected_result, result)
    
    def test_neg_side(self):
        res = square.perimeter(-2)
        self.assertEqual(res, -1)

class TriangleAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        res = triangle.area(0, 3)
        self.assertEqual(res, 0)
    
    def test_zero_height(self):
        res = triangle.area(3, 0)
        self.assertEqual(res, 0)
    
    def test_simple(self):
        res = triangle.area(2, 4)
        self.assertEqual(res, 4)
    
    def test_huge(self):
        res = triangle.area(9999999, 9999888)
        exp_res = 49999435000056.0
        self.assertEqual(exp_res, res)
    
    def test_neg_side(self):
        res = triangle.area(-2, 4)
        self.assertEqual(res, -1)
    
    def test_neg_height(self):
        res = triangle.area(2, -4)
        self.assertEqual(res, -1)
    
class TrianglePerTestCase(unittest.TestCase):
    def test_zero_side(self):
        res = triangle.perimeter(0, 3, 3)
        self.assertEqual(res, -1)
    
    def test_simple(self):
        res = triangle.perimeter(2, 4, 3)
        self.assertEqual(res, 9)
    
    def test_huge(self):
        res = triangle.perimeter(9999999, 9999888, 9999777)
        exp_res = 29999664
        self.assertEqual(exp_res, res)
    
    def test_neg_side(self):
        res = triangle.perimeter(-2, 4, 3)
        self.assertEqual(res, -1)
