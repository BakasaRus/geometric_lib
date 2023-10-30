import unittest

def area(a):
    '''
    Возвращает площадь квадрата по его стороне
    
        Параметры:
            a (float): сторона квадрата 
            
        Возвращаемое значение:
            a * a (float): площадь квадрата со стороной a
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата по его стороне
    
        Параметры:
            a (float): сторона квадрата 
            
        Возвращаемое значение:
            4 * a (float): периметр квадрата со стороной a
    '''
    return 4 * a

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
