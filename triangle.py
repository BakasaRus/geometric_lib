import unittest
from typing import Union


def area(a: Union[int, float], h: Union[int, float]) -> Union[int, float]:
    """
    Принимает длину основания и высоту, перпендикулярную основанию, треугольника и
    возвращает площадь треугольника

    :param a: основание треугольника
    :param h: высота треугольника
    :return: площадь треугольника
    """
    if not isinstance(a, (int, float)) or a <= 0:
        raise TypeError('Triangle\'s side should be a positive number, not {}'.format(repr(a)))
    if not isinstance(h, (int, float)) or h <= 0:
        raise TypeError('Triangle\'s side should be a positive number, not {}'.format(repr(h)))
    return a * h / 2


def perimeter(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Union[int, float]:
    """
    Принимает длину сторон треугольника и возвращает периметр треугольника

    :param a: 1-ая сторона треугольника
    :param b: 2-ая сторона треугольника
    :param c: 3-ая сторона треугольника
    :return: периметр треугольника
    """
    if not isinstance(a, (int, float)) or a <= 0:
        raise TypeError('Triangle\'s side should be a positive number, not {}'.format(repr(a)))
    if not isinstance(b, (int, float)) or b <= 0:
        raise TypeError('Triangle\'s side should be a positive number, not {}'.format(repr(b)))
    if not isinstance(c, (int, float)) or c <= 0:
        raise TypeError('Triangle\'s side should be a positive number, not {}'.format(repr(c)))
    if not (a < b + c and b < a + c and c < a + b):
        raise TypeError('Triangle\'s sides should satisfy the triangle inequality, not {}'.format((repr(a), repr(b), repr(c))))
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(10, 1), 5)

    def test_area_2(self):
        self.assertEqual(area(10, 10), 50)

    def test_area_3(self):
        self.assertEqual(area(400, 20), 4000)

    def test_area_4(self):
        self.assertNotEqual(area(100, 20), 101)

    def test_area_5(self):
        with self.assertRaises(TypeError):
            area('string', 1)

    def test_area_6(self):
        with self.assertRaises(TypeError):
            area(-10, 1)


    def test_perimeter_1(self):
        self.assertEqual(perimeter(10, 15, 10), 35)

    def test_perimeter_2(self):
        self.assertEqual(perimeter(100, 200, 205), 505)

    def test_perimeter_3(self):
        self.assertEqual(perimeter(100000, 100000, 100000), 300000)

    def test_perimeter_4(self):
        self.assertNotEqual(perimeter(100, 50, 100), 110)

    def test_perimeter_5(self):
        with self.assertRaises(TypeError):
            perimeter('string', 1)

    def test_perimeter_6(self):
        with self.assertRaises(TypeError):
            perimeter(-10, 1)

    def test_perimeter_7(self):
        with self.assertRaises(TypeError):
            perimeter(10, 1, 4)
