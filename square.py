
def area(a):
    '''
    Принимает одно число: длину стороны квадрата.
    
    Возвращает площадь фигуры
    '''
    return a * a


def perimeter(a):
    '''
    Принимает одно число: длину стороны квадрата.
    
    Возвращает периметр фигуры
    '''
    return 4 * a

import unittest
class SquareTestCase(unittest.TestCase):
   def test_zero_area(self):
       res = area(00)
       self.assertEqual(res, 0)
       
   def test_square_area(self):
       res = area(10)
       self.assertEqual(res, 100)
       
   def test_one_area(self):
       res = area(1)
       self.assertEqual(res, 1)
    #--------------------------
   def test_zero_perimeter(self):
       res = perimeter(0)
       self.assertEqual(res, 0)
       
   def test_square_perimeter(self):
       res = perimeter(10)
       self.assertEqual(res, 40)
       
   def test_one_perimeter(self):
       res = perimeter(1)
       self.assertEqual(res, 4)
