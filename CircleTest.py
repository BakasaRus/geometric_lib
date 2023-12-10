from circle import *
import unittest

class testsCircleTest(unittest.TestCase):
   def test_zero_area(self):
       res = area(0)
       self.assertEqual(res, 0)
       
   def test_area(self):
       res = area(10)
       self.assertEqual(res, math.pi * 100)
       
   def test_one_area(self):
       res = area(1)
       self.assertEqual(res, math.pi)
    #--------------------------
   def test_zero_perimeter(self):
       res = perimeter(0)
       self.assertEqual(res, 0)
       
   def test_square_perimeter(self):
       res = perimeter(10)
       self.assertEqual(res, 20 *  math.pi)
       
   def test_one_perimeter(self):
       res = perimeter(1)
       self.assertEqual(res, 2 *  math.pi)
