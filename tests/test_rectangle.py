import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
   def test_zero_mul_0(self):
       res = area(10, 0)
       self.assertEqual(res, 0)

   def test_zero_mul_1(self):
       res = area(0, 1000)
       self.assertEqual(res, 0)

   def test_zero_mul_2(self):
       res = area(2 << 100, 0)
       self.assertEqual(res, 0)

   def test_zero_mul_3(self):
       res = area(0, 0)
       self.assertEqual(res, 0)

   def test_zero_mul_4(self):
       res = area(0, 2 << 100)
       self.assertEqual(res, 0)
       
   def test_square_mul_0(self):
       res = area(0, 0)
       self.assertEqual(res, 0)

   def test_square_mul_1(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

   def test_square_mul_2(self):
       res = area(1 << 100, 1 << 100)
       self.assertEqual(res, 1 << 200)

   def test_not_square_mul_0(self):
       res = area(1 << 10, 1 << 100)
       self.assertEqual(res, 1 << 110)

   def test_perimeter_0(self):
       res = perimeter(10, 10)
       self.assertEqual(res, 40)

   def test_perimeter_1(self):
       res = perimeter(0, 10)
       self.assertEqual(res, 20)

   def test_perimeter_2(self):
       res = perimeter(0, 0)
       self.assertEqual(res, 0)

   def test_perimeter_3(self):
       res = perimeter(2 << 100, 2 << 100)
       self.assertEqual(res, 8 << 100)
