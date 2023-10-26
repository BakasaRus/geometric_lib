import unittest
import sys
sys.path.append("..")
from rectangle import area, perimeter

# класс тестов для функций rectangle.py

class RectangleTestCase(unittest.TestCase):
    # проверка на обычных значениях
    def test_area(self):
        self.assertEqual(area(10, 10), 100)
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(2.5, 2), 5)
        self.assertEqual(area(1.5, 3.21), 1.5*3.21)
    
    def test_prerimetr(self):
        self.assertEqual(perimeter(10, 10), 40)
        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(2.5, 2), 9)
        self.assertEqual(perimeter(1.5, 3.21), 2*1.5 + 2*3.21)

    # проверка на отрицательных значениях
    def test_areaNegative(self):
        self.assertRaises(ValueError, area, 2, -1)
        self.assertRaises(ValueError, area, -5, 2)
        self.assertRaises(ValueError, area, -1, -0.5)

    def test_perimetrNegative(self):
        self.assertRaises(ValueError, perimeter, 2, -1)
        self.assertRaises(ValueError, perimeter, -5, 2)
        self.assertRaises(ValueError, perimeter, -1, -0.5)

    # проверка на неправильных типах значений
    def test_areaValues(self):
        self.assertRaises(TypeError, area, "qwe", 10)
        self.assertRaises(TypeError, area, 1, 1 + 1j)
    
    def test_perimetrValues(self):
        self.assertRaises(TypeError, perimeter, "qwe", 10)
        self.assertRaises(TypeError, perimeter, 1, 1 + 1j)


if __name__ == '__main__':
    unittest.main()