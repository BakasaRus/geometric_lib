from lib.triangle import *
import unittest

class TriangleTestCase(unittest.TestCase):
   def test_zero_area(self):
       res = area(0, 0)
       self.assertEqual(res, 0)
       
   def test_square_area(self):
       res = area(10, 10)
       self.assertEqual(res, 50)
       
   def test_one_area(self):
       res = area(1, 1)
       self.assertEqual(res, 0.5)
    #--------------------------
   def test_zero_perimeter(self):
       res = perimeter(0, 0, 0)
       self.assertEqual(res, 0)
       
   def test_perimeter(self):
       res = perimeter(10, 20, 30)
       self.assertEqual(res, 60)
       
   def test_one_perimeter(self):
       res = perimeter(1, 1, 1)
       self.assertEqual(res, 3)
