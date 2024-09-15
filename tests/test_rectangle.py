import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
   def test_zero_mul_a(self):
      res = rectangle.area(10, 0)
      self.assertEqual(res, 0)
   
   def test_zero_mul_b(self):
      res = rectangle.area(0, 10)
      self.assertEqual(res, 0)
       
   def test_square_mul(self):
      res = rectangle.area(10, 10)
      self.assertEqual(res, 100)

   def test_sum(self):
      res = rectangle.perimeter(10, 2)
      self.assertEqual(res, 24)

   def test_negative_area_a(self):
      with self.assertRaises(ValueError):
         rectangle.area(-10, 1)
   
   def test_negative_area_b(self):
      with self.assertRaises(ValueError):
         rectangle.area(10, -1)
   
   def test_negative_perimeter_a(self):
      with self.assertRaises(ValueError):
         rectangle.perimeter(-10, 1)

   def test_negative_perimeter_b(self):
      with self.assertRaises(ValueError):
         rectangle.perimeter(10, -1)

if __name__ == '__main__':
    unittest.main()