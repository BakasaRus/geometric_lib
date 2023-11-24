import unittest
import triangle

'''
    Класс тестов для модуля triangle.py
'''
class TriangleTestCase(unittest.TestCase):
    '''
        Блок тестов для площади, где результатом является 0.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_0_area_1(self):
        res = triangle.area(12, 0)
        self.assertEqual(res, 0)
    
    def test_0_area_2(self):
        res = triangle.area(0, 21)
        self.assertEqual(res, 0)
    
    def test_0_area_3(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)
        
    '''
        Блок тестов для площади, где входными данными для area(a, h)
        являются малые числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_small_numbers_area_1(self):
        res = triangle.area(23, 2)
        self.assertEqual(res, 23)
    
    def test_small_numbers_area_2(self):
        res = triangle.area(100, 5)
        self.assertEqual(res, 250)
    
    def test_small_numbers_area_3(self):
        res = triangle.area(3, 3)
        self.assertEqual(res, 4.5)
    
    '''
        Блок тестов для площади, где входными данными для area(a, h)
        являются большие числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_large_numbers_area_1(self):
        res = triangle.area(123456789, 88888888)
        self.assertEqual(res, 5486968345130316.0)
    
    def test_large_numbers_area_2(self):
        res = triangle.area(10973936690260632, 2)
        self.assertEqual(res, 10973936690260632.0)
    
    def test_large_numbers_area_3(self):
        res = triangle.area(123456789, 21947873380521264)
        self.assertEqual(res, 1.3548069864688651e+24)  
        
    '''
        Тест для периметра, где результатом является 0.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_0_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
     
    '''
        Блок тестов для периметра, где входными данными для perimeter(a, b, c)
        являются малые числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_small_numbers_perimeter_1(self):
        res = triangle.perimeter(39, 2, 40)
        self.assertEqual(res, 81)
    
    def test_small_numbers_perimeter_2(self):
        res = triangle.perimeter(60, 25, 50)
        self.assertEqual(res, 135)
    
    def test_small_numbers_perimeter_3(self):
        res = triangle.perimeter(3, 3, 4)
        self.assertEqual(res, 10)
    
    '''
        Блок тестов для периметра, где входными данными для perimeter(a, b, c)
        являются большие числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_large_numbers_perimeter_1(self):
        res = triangle.perimeter(123456789000, 88888888000, 34567901019)
        self.assertEqual(res, 246913578019)
    
    def test_large_numbers_perimeter_2(self):
        res = triangle.perimeter(10973936690260632, 2, 10973936690260631)
        self.assertEqual(res, 21947873380521265)
    
    def test_large_numbers_perimeter_3(self):
        res = triangle.perimeter(123456789, 21947873380521264, 21947873257064480)
        self.assertEqual(res, 43895746761042533)  

if __name__ == '__main__':
    unittest.main()
   