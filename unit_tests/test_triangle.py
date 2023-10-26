import unittest
import sys
sys.path.append("..")
from triangle import area, perimeter

# класс тестов для функций triangle.py

class TriangleTestCase(unittest.TestCase):
    # проверка на обычных значениях
    def test_area(self):
        self.assertEqual(area(10, 10), 10 * 10 / 2)
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(2.5, 2), 2.5)
        self.assertEqual(area(1.5, 3.21), 1.5*3.21 / 2)
    
    def test_prerimetr(self):
        self.assertEqual(perimeter(10, 10, 10), 30)
        self.assertEqual(perimeter(10, 0, 2), 12)
        self.assertEqual(perimeter(2.5, 2, 1.3), 5.8)
        self.assertEqual(perimeter(1.5, 3.21, 3.123), 1.5 + 3.21 + 3.123)

    # проверка на отрицательных значениях
    def test_areaNegative(self):
        self.assertRaises(ValueError, area, 2, -1)
        self.assertRaises(ValueError, area, -5, 2)
        self.assertRaises(ValueError, area, -1, -0.5)

    def test_perimetrNegative(self):
        self.assertRaises(ValueError, perimeter, 2, -1, 0)
        self.assertRaises(ValueError, perimeter, -5, 2, -5)
        self.assertRaises(ValueError, perimeter, -1, -0.5, -1.3)

    # проверка на неправильных типах значений
    def test_areaValues(self):
        self.assertRaises(TypeError, area, "qwe", 10)
        self.assertRaises(TypeError, area, 1, 1 + 1j)
    
    def test_perimetrValues(self):
        self.assertRaises(TypeError, perimeter, "qwe", 10, "q")
        self.assertRaises(TypeError, perimeter, 1, 1 + 1j, -2)


if __name__ == '__main__':
    unittest.main()