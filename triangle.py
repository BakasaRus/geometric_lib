import unittest, random
def area(a, h):
    '''
    Вычисление площади треугольника
    Параметры:
        h, a(int/float) - высота и сторона(основание)
    Возвращаемое значение:
        a * h / 2(int/float) - площадь треугольника
    Пример вызова:
        area(2, 4) = 4
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Вычисление периметра треугольника
    Параметры:
        a, b, c(int/float) - 3 стороны треугольника
    Возвращаемое значение:
        a + b + c(int/float) - площадь треугольника
    Пример вызова:
        perimeter(3, 4, 5) = 12
    ''' 
    return a + b + c 

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
    def test_small_numbers_area(self):
        res = area(15, 2)
        self.assertEqual(res, 15*2/2)