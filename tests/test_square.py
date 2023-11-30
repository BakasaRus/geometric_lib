import unittest

import sys
sys.path.append('../')

from lib.square import *


class SquareTestCase(unittest.TestCase):
   def test_zero_mul_0(self):
       res = area(0)
       self.assertEqual(res, 0)

   def test_square_mul_0(self):
       res = area(10)
       self.assertEqual(res, 100)

   def test_square_mul_2(self):
       res = area(1 << 100)
       self.assertEqual(res, 1 << 200)

   def test_perimeter_0(self):
       res = perimeter(10)
       self.assertEqual(res, 40)

   def test_perimeter_1(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

   def test_perimeter_2(self):
       res = perimeter(2 << 100)
       self.assertEqual(res, 8 << 100)
