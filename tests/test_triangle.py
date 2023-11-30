import unittest
from triangle import *


class TriangleTestCase(unittest.TestCase):
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

   def test_mul_1(self):
       res = area(10, 10)
       self.assertEqual(res, 50)

   def test_mul_2(self):
       res = area(1 << 100, 1 << 100)
       self.assertEqual(res, 1 << 199)

   def test_mul_3(self):
       res = area(1 << 10, 1 << 100)
       self.assertEqual(res, 1 << 109)

   def test_perimeter_0(self):
       res = perimeter(10, 10, 10)
       self.assertEqual(res, 30)

   def test_perimeter_1(self):
       res = perimeter(0, 10, 10)
       self.assertEqual(res, 20)

   def test_perimeter_2(self):
       res = perimeter(0, 0, 0)
       self.assertEqual(res, 0)

   def test_perimeter_3(self):
       res = perimeter(2 << 100, 2 << 100, 3 << 100)
       self.assertEqual(res, 7 << 100)
