import math
import unittest


class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_radius_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


def area(r):
    ''' Принимает радиус окружности r (float), возвращает площадь окружности (float) '''
    return math.pi * r * r


def perimeter(r):
    ''' Принимает радиус окружности r (float), возвращает периметр окружности (float) '''
    return 2 * math.pi * r

