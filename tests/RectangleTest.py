import sys
sys.path.append("../")

from lib.rectangle import *
import unittest

class RectangleTestCase(unittest.TestCase):
   def test_zero_area(self):
       res = area(0, 0)
       self.assertEqual(res, 0)
       
   def test_square_area(self):
       res = area(10, 10)
       self.assertEqual(res, 100)
       
   def test_rect_area(self):
       res = area(5, 10)
       self.assertEqual(res, 50)
    #--------------------------
   def test_zero_perimeter(self):
       res = perimeter(0, 0)
       self.assertEqual(res, 0)
       
   def test_square_perimeter(self):
       res = perimeter(10, 10)
       self.assertEqual(res, 40)
       
   def test_rect_perimeter(self):
       res = perimeter(5, 10)
       self.assertEqual(res, 30)
