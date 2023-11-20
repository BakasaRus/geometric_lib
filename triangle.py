import unittest


class TriangleTestCase(unittest.TestCase):
    def test_zero_height_area(self):
        res = area(0, 2)
        self.assertEqual(res, 0)

    def test_zero_side_area(self):
        res = area(2, 0)
        self.assertEqual(res, 0)


def area(a, h):
    ''' Принимает значения длины стороны a и высоты h треугольника, возвращает площадь '''
    return a * (h / 2)


def perimeter(a, b, c):
    ''' Принимает значение длины всех сторон треугольника a, b и c, возвращает периметр '''
    return a + b + c
