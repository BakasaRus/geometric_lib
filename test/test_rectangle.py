import unittest
import rectangle

'''
    Класс тестов для модуля rectangle.py
'''
class RectangleTestCase(unittest.TestCase):
    '''
        Блок тестов для площади, где результатом является 0.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_0_area_1(self):
        res = rectangle.area(12, 0)
        self.assertEqual(res, 0)
    
    def test_0_area_2(self):
        res = rectangle.area(0, 21)
        self.assertEqual(res, 0)
    
    def test_0_area_3(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)
        
    '''
        Блок тестов для площади, где входными данными для area(a, b)
        являются малые числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_small_numbers_area_1(self):
        res = rectangle.area(23, 2)
        self.assertEqual(res, 46)
    
    def test_small_numbers_area_2(self):
        res = rectangle.area(100, 5)
        self.assertEqual(res, 500)
    
    def test_small_numbers_area_3(self):
        res = rectangle.area(3, 3)
        self.assertEqual(res, 9)
    
    '''
        Блок тестов для площади, где входными данными для area(a, b)
        являются большие числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_large_numbers_area_1(self):
        res = rectangle.area(123456789, 88888888)
        self.assertEqual(res, 10973936690260632)
    
    def test_large_numbers_area_2(self):
        res = rectangle.area(10973936690260632, 2)
        self.assertEqual(res, 21947873380521264)
    
    def test_large_numbers_area_3(self):
        res = rectangle.area(123456789, 21947873380521264)
        self.assertEqual(res, 2709613972937730399661296)  
        
    '''
        Тест для периметра, где результатом является 0.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_0_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)
    
    '''
        Блок тестов для периметра, где входными данными для perimeter(a, b)
        являются малые числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_small_numbers_perimeter_1(self):
        res = rectangle.perimeter(70, 2)
        self.assertEqual(res, 144)
    
    def test_small_numbers_perimeter_2(self):
        res = rectangle.perimeter(100, 5)
        self.assertEqual(res, 210)
    
    def test_small_numbers_perimeter_3(self):
        res = rectangle.perimeter(3, 3)
        self.assertEqual(res, 12)
    
    '''
        Тест для периметра, где входными данными для perimeter(a, b)
        являются большие числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_large_numbers_perimeter_1(self):
        res = rectangle.perimeter(123456789, 21947873380521264)
        self.assertEqual(res, 43895747007956106)  
        
if __name__ == '__main__':
    unittest.main()
