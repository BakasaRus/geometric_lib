import unittest
import sys
import math
sys.path.append("..")
from circle import area, perimeter

# класс тестов для функций circle.py

class CircleTestCase(unittest.TestCase):
    # проверка на обычных значениях
    def test_area(self):
        self.assertTrue(math.isclose(area(10), 10 * 10 * math.pi))
        self.assertEqual(area(0), 0)
        self.assertTrue(math.isclose(area(2.5), 2.5 * 2.5 * math.pi))
        self.assertTrue(math.isclose(area(1.545), 1.545 * 1.545 * math.pi))
        
    
    def test_prerimetr(self):
        self.assertTrue(math.isclose(perimeter(1), math.pi * 2 * 1))
        self.assertTrue(math.isclose(perimeter(10), math.pi * 2 * 10))
        self.assertTrue(math.isclose(perimeter(2.5), math.pi * 2 * 2.5))
        self.assertTrue(math.isclose(perimeter(34.1234), math.pi * 2 * 34.1234))

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