def area(a, h):
    '''
    Возвращает площадь треугольника по длинам стороны и высоты отложенной от этой стороны.
    
        Параметры:
            a (int/float): длина стороны треугольнка
            h (int/float): длина высоты треугольника отложенной от стороны a
    
        Возвращаемое значение:
            area (int/float): результат
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Возвращает периметр треугольника по длинам трех сторон.
    
        Параметры:
            a (int/float): длина первой стороны треугольнка
            b (int/float): длина второй стороны треугольнка
            c (int/float): длина третей стороны треугольнка
    
        Возвращаемое значение:
            perimeter (int/float): результат
    '''
    return a + b + c 


import unittest
class TriangleTestCase(unittest.TestCase):
   def test_zero_area(self):
       res = area(0, 0)
       self.assertEqual(res, 0)
       
   def test_square_area(self):
       res = area(10, 10)
       self.assertEqual(res, 50)
       
   def test_one_area(self):
       res = area(1, 1)
       self.assertEqual(res, 0.5)
    #--------------------------
   def test_zero_perimeter(self):
       res = perimeter(0, 0, 0)
       self.assertEqual(res, 0)
       
   def test_perimeter(self):
       res = perimeter(10, 20, 30)
       self.assertEqual(res, 60)
       
   def test_one_perimeter(self):
       res = perimeter(1, 1, 1)
       self.assertEqual(res, 3)
