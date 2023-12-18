import unittest
import sys
import math
sys.path.append("..")
from circle import area, perimeter

# класс тестов для функций circle.py

class CircleTestCase(unittest.TestCase):
    # проверка на обычных значениях
    def test_area(self):
        self.assertAlmostEqual(area(10), 10 * 10 * math.pi)
    
    def test_prerimetr(self):
        self.assertAlmostEqual(perimeter(34.1234), math.pi * 2 * 34.1234)
    
    # проверка нуля
    def test_areanull(self):
        self.assertEqual(area(0), 0)    
    
    def test_perimetrnull(self):
        self.assertEqual(perimeter(0), 0)

    # проверка на отрицательных значениях
    def test_areaNegative(self):
        self.assertRaises(ValueError, area, -0.2)

    def test_perimetrNegative(self):
        self.assertRaises(ValueError, perimeter, -1)

    # проверка на неправильных типах значений
    def test_areaValues(self):
        self.assertRaises(TypeError, area, "qwe")
    
    def test_perimetrValues(self):
        self.assertRaises(TypeError, perimeter, 1 + 1j)


if __name__ == '__main__':
    unittest.main()