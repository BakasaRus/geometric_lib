import unittest
import sys
sys.path.append("..")
from square import area, perimeter

# класс тестов для функций square.py

class SquareTestCase(unittest.TestCase):
    # проверка на обычных значениях
    def test_area(self):
        self.assertAlmostEqual(area(1.545), 1.545 * 1.545)
    
    def test_prerimetr(self):
        self.assertAlmostEqual(perimeter(34.1234), 4 * 34.1234)

    # проверка нуля

    def test_areanull(self):
        self.assertEqual(area(0), 0)

    def test_perrimetrnull(self):
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