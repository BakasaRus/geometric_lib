import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
   def test_zero_mul_a(self):
      res = triangle.area(10, 0)
      self.assertEqual(res, 0)
   
   def test_zero_mul_h(self):
      res = triangle.area(0, 10)
      self.assertEqual(res, 0)
       
   def test_square_mul(self):
      res = triangle.area(10, 10)
      self.assertEqual(res, 50)

   def test_sum(self):
      res = triangle.perimeter(10, 6, 5)
      self.assertEqual(res, 21)

   def test_negative_area_a(self):
      with self.assertRaises(ValueError):
         triangle.area(-10, 1)
   
   def test_negative_area_h(self):
      with self.assertRaises(ValueError):
         triangle.area(10, -1)

   def test_negative_perimeter_a(self):
      with self.assertRaises(ValueError):
         triangle.perimeter(10, 1, -12)
   
   def test_negative_perimeter_b(self):
      with self.assertRaises(ValueError):
         triangle.perimeter(10, -1, 12)

   def test_negative_perimeter_b(self):
      with self.assertRaises(ValueError):
         triangle.perimeter(-10, 1, 12)

   def test_triangle(self):
      with self.assertRaises(ValueError):
         triangle.perimeter(1, 1, 100)

if __name__ == '__main__':
    unittest.main()