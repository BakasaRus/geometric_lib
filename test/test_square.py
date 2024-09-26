import unittest
import square

'''
    Класс тестов для модуля square.py
'''
class SquareTestCase(unittest.TestCase):
    '''
        Тест для площади, где результатом является 0.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_0_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)
        
    '''
        Блок тестов для площади, где входными данными для area(a)
        являются малые числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_small_numbers_area_1(self):
        res = square.area(23)
        self.assertEqual(res, 529)
    
    def test_small_numbers_area_2(self):
        res = square.area(100)
        self.assertEqual(res, 10000)
    
    def test_small_numbers_area_3(self):
        res = square.area(3)
        self.assertEqual(res, 9)
    
    '''
        Блок тестов для площади, где входными данными для area(a)
        являются большие числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_large_numbers_area_1(self):
        res = square.area(123456789000)
        self.assertEqual(res, 15241578750190521000000)
    
    def test_large_numbers_area_2(self):
        res = square.area(10973936690260632)
        self.assertEqual(res, 120427286481848474234844089039424)
    
    def test_large_numbers_area_3(self):
        res = square.area(1000000000)
        self.assertEqual(res, 1000000000000000000)  
        
    '''
        Тест для периметра, где результатом является 0.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_0_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
        
    '''
        Блок тестов для периметра, где входными данными для perimeter(a)
        являются малые числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_small_numbers_perimeter_1(self):
        res = square.perimeter(70)
        self.assertEqual(res, 280)
    
    def test_small_numbers_perimeter_2(self):
        res = square.perimeter(100)
        self.assertEqual(res, 400)
    
    def test_small_numbers_perimeter_3(self):
        res = square.perimeter(3)
        self.assertEqual(res, 12)
    
    '''
        Блок тестов для периметра, где входными данными для perimeter(r)
        являются большие числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_large_numbers_perimeter_1(self):
        res = square.perimeter(123456789000)
        self.assertEqual(res, 493827156000)
    
    def test_large_numbers_perimeter_2(self):
        res = square.perimeter(10973936690260632)
        self.assertEqual(res, 43895746761042528)
    
    def test_large_numbers_perimeter_3(self):
        res = square.perimeter(1234567893984385555555)
        self.assertEqual(res, 4938271575937542222220)  

if __name__ == '__main__':
    unittest.main()
