import unittest
from circle import *

class RectangleTestCase(unittest.TestCase):
   def test_zero_mul_0(self):
       res = area(0)
       self.assertEqual(res, 0)
       
   def test_mul_0(self):
       res = area(1)
       self.assertEqual(res, math.pi)

   def test_mul_1(self):
       res = area(11)
       self.assertEqual(round(res, 10), round(121 * math.pi, 10))

   def test_mul_2(self):
       res = area(1 << 100)
       self.assertEqual(round(res, 10), round(math.pi * (1 << 200), 10))

   def test_mul_3(self):
       res = area(1.1)
       self.assertEqual(round(res, 10), round(1.21 * math.pi, 10))

   def test_mul_4(self):
       res = area(1.0000001)
       self.assertEqual(round(res, 10), round(1.0000002000001 * math.pi, 10))
   
   def test_perimeter_0(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

   def test_perimeter_1(self):
       res = perimeter(10)
       self.assertEqual(res, 20 * math.pi)

   def test_perimeter_2(self):
       res = perimeter(1 << 100)
       self.assertEqual(res, math.pi * (2 << 100))

   def test_perimeter_0(self):
       res = perimeter(1.141)
       self.assertEqual(res, 2.282 * math.pi)
