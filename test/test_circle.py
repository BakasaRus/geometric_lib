import unittest
import circle

'''
    Класс тестов для модуля circle.py
'''
class CircleTestCase(unittest.TestCase):
    '''
        Тест для площади, где результатом является 0.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_0_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
        
    '''
        Блок тестов для площади, где входными данными для area(r)
        являются малые числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_small_numbers_area_1(self):
        res = circle.area(23)
        self.assertAlmostEqual(res, 1661.9025137490005)
    
    def test_small_numbers_area_3(self):
        res = circle.area(3)
        self.assertAlmostEqual(res, 28.274333882308138)
    
    '''
        Блок тестов для площади, где входными данными для area(r)
        являются большие числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_large_numbers_area_1(self):
        res = circle.area(123456789000)
        self.assertAlmostEqual(res, 4.788283183070884e+22)
    
    def test_large_numbers_area_2(self):
        res = circle.area(10973936690260632)
        self.assertAlmostEqual(res, 3.783334785031286e+32)
    
    def test_large_numbers_area_3(self):
        res = circle.area(1000000000)
        self.assertAlmostEqual(res, 3.1415926535897933e+18)  
        
    '''
        Тест для периметра, где результатом является 0.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_0_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
        
    '''
        Блок тестов для периметра, где входными данными для perimeter(r)
        являются малые числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_small_numbers_perimeter_1(self):
        res = circle.perimeter(70)
        self.assertAlmostEqual(res, 439.822971502571)
    
    def test_small_numbers_perimeter_2(self):
        res = circle.perimeter(100)
        self.assertAlmostEqual(res, 628.3185307179587)
    
    def test_small_numbers_perimeter_3(self):
        res = circle.perimeter(3)
        self.assertAlmostEqual(res, 18.84955592153876)
    
    '''
        Блок тестов для периметра, где входными данными для perimeter(r)
        являются большие числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_large_numbers_perimeter_1(self):
        res = circle.perimeter(123456789000)
        self.assertAlmostEqual(res, 775701882716.3704)
    
    def test_large_numbers_perimeter_2(self):
        res = circle.perimeter(10973936690260632)
        self.assertAlmostEqual(res, 6.8951277774164584e+16)
    
    def test_large_numbers_perimeter_3(self):
        res = circle.perimeter(123456789)
        self.assertAlmostEqual(res, 775701882.7163703)  

if __name__ == '__main__':
    unittest.main()
