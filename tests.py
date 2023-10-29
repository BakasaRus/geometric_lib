import unittest
import rectangle
import square
import circle
import triangle

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
        Блок тестов для периметра, где одна из сторон
        прямоугольника равна 0, а другая не равна 0
        (вырожденный случай: длина отрезка).
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_degenerate_perimeter_1(self):
        res = rectangle.perimeter(5, 0)
        self.assertEqual(res, 5)
    
    def test_degenerate_perimeter_2(self):
        res = rectangle.perimeter(0, 7345)
        self.assertEqual(res, 7345)
        
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
        Блок тестов для периметра, где входными данными для perimeter(a, b)
        являются большие числа.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_large_numbers_perimeter_1(self):
        res = rectangle.perimeter(123456789000, 88888888000)
        self.assertEqual(res, 424691354000)
    
    def test_large_numbers_perimeter_2(self):
        res = rectangle.perimeter(10973936690260632, 2)
        self.assertEqual(res, 21947873380521268)
    
    def test_large_numbers_perimeter_3(self):
        res = rectangle.perimeter(123456789, 21947873380521264)
        self.assertEqual(res, 43895747007956106)  
        
        
        
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
    
    def test_small_numbers_area_2(self):
        res = circle.area(100)
        self.assertAlmostEqual(res, 31415.926535897932)
    
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
        Блок тестов для периметра вырожденного случая: длина отрезка.
        
        Параметры:
                self: ссылка на экземпляр класса RectangleTestCase
        
    '''
    
    def test_degenerate_perimeter_1(self):
        res = triangle.perimeter(5, 1, 4)
        self.assertEqual(res, 5)
    
    def test_degenerate_perimeter_2(self):
        res = triangle.perimeter(7, 13, 6)
        self.assertEqual(res, 13)
        
    def test_degenerate_perimeter_3(self):
        res = triangle.perimeter(10, 10, 20)
        self.assertEqual(res, 20)
        
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
   