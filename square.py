import unittest


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


def area(a):
    ''' Принимает значение длины стороны квадрата a, возвращает площадь '''
    return a * a


def perimeter(a):
    ''' Принимает значение длины стороны квадрата a, возвращает периметр '''
    return 4 * a
