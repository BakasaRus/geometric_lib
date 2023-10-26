import unittest
import sys
import math
sys.path.append("..")
from square import area, perimeter

# класс тестов для функций square.py

class SquareTestCase(unittest.TestCase):
    # проверка на обычных значениях
    def test_area(self):
        self.assertEqual(area(10), 10 * 10)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(2.5), 2.5 * 2.5)
        self.assertEqual(area(1.545), 1.545 * 1.545)
    
    def test_prerimetr(self):
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(10), 4 * 10)
        self.assertEqual(perimeter(2.5), 4 * 2.5)
        self.assertEqual(perimeter(34.1234), 4 * 34.1234)

    # проверка на отрицательных значениях
    def test_areaNegative(self):
        self.assertRaises(ValueError, area, -0.2)
        self.assertRaises(ValueError, area, -5)

    def test_perimetrNegative(self):
        self.assertRaises(ValueError, perimeter, -1)
        self.assertRaises(ValueError, perimeter, -5)
        self.assertRaises(ValueError, perimeter, -0.5)

    # проверка на неправильных типах значений
    def test_areaValues(self):
        self.assertRaises(TypeError, area, "qwe")
        self.assertRaises(TypeError, area, 1 + 1j)
    
    def test_perimetrValues(self):
        self.assertRaises(TypeError, perimeter, "qwe")
        self.assertRaises(TypeError, perimeter, 1 + 1j)


if __name__ == '__main__':
    unittest.main()