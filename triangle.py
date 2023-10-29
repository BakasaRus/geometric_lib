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
    return a * h / 2 


def perimeter(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Union[int, float]:
    """
    Принимает длину сторон треугольника и возвращает периметр треугольника

    :param a: 1-ая сторона треугольника
    :param b: 2-ая сторона треугольника
    :param c: 3-ая сторона треугольника
    :return: периметр треугольника
    """
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_2(self):
        self.assertEqual(area(10, 10), 50)

    def test_area_3(self):
        self.assertEqual(area(400, 20), 4000)

    def test_perimeter_1(self):
        self.assertEqual(perimeter(10, 15, 10), 35)

    def test_perimeter_2(self):
        self.assertEqual(perimeter(100, 200, 205), 505)

    def test_perimeter_3(self):
        self.assertEqual(perimeter(100000, 100000, 100000), 300000)
