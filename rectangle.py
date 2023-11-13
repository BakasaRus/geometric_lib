import unittest
from typing import Union


def area(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Принимает длины сторон прямоугольника и возвращает площадь прямоугольника

    :param a: длина прямоугольника
    :param b: ширина прямоугольника
    :return: площадь прямоугольника со сторонами a и b
    """
    return a * b


def perimeter(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Принимает длины сторон прямоугольника и возвращает периметр прямоугольника

    :param a: длина прямоугольника
    :param b: ширина прямоугольника
    :return: периметр прямоугольника со сторонами a и b
    """
    return (a + b) * 2


class RectangleTestCase(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_2(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_3(self):
        self.assertEqual(area(100000, 100000), 10000000000)

    def test_area_4(self):
        self.assertNotEqual(area(100, 20), -2000)

    def test_perimeter_1(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_perimeter_2(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_3(self):
        self.assertEqual(perimeter(100000, 100000), 400000)

    def test_perimeter_4(self):
        self.assertNotEqual(perimeter(100, 20), 239)
