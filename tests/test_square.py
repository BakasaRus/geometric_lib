import unittest
import square
class SquareTestCase(unittest.TestCase):
   def test_zero_mul(self):
      res = square.area(0)
      self.assertEqual(res, 0)
       
   def test_mul(self):
      res = square.area(10)
      self.assertEqual(res, 100)

   def test_sum(self):
      res = square.perimeter(10)
      self.assertEqual(res, 40)

   def test_negative_perimeter(self):
      with self.assertRaises(ValueError):
         square.area(-10)

   def test_negative_perimeter(self):
      with self.assertRaises(ValueError):
         square.perimeter(-10)

if __name__ == '__main__':
    unittest.main()