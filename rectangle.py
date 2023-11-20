import unittest


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 1)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = area(1, 0)
        self.assertEqual(res, 0)

    def test_square(self):
        res = area(2, 2)
        self.assertEqual(res, 4)


def area(a, b):
    ''' Принимает значения a и b -- длины сторон прямоугольника, возвращает площадь '''
    return a * b


def perimeter(a, b):
    ''' Принимает значения a и b -- длинны сторон прямоугольника, возвращает периметр '''
    return 2 * (a + b)
