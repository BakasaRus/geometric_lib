import math
import unittest
from typing import Union


def area(r: Union[int, float]) -> Union[int, float]:
    """
    Принимает радиус круга и возвращает площадь круга

    :param r: радиус круга
    :return: площадь круга
    """
    if not isinstance(r, (int, float)) or r <= 0:
        raise TypeError('Circle\'s radius should be a positive number, not {}'.format(repr(r)))
    return math.pi * r * r


def perimeter(r: Union[int, float]) -> Union[int, float]:
    """
    Принимает радиус круга и возвращает периметр круга

    :param r: радиус круга
    :return: периметр круга
    """
    if not isinstance(r, (int, float)) or r <= 0:
        raise TypeError('Circle\'s radius should be a positive number, not {}'.format(repr(r)))
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_1(self):
        self.assertAlmostEqual(area(10), 314.1592653589793)

    def test_area_2(self):
        self.assertAlmostEqual(area(3), 28.274333882308138)

    def test_area_3(self):
        self.assertAlmostEqual(area(100000), 31415926535.89793)

    def test_area_4(self):
        self.assertNotEqual(area(100), 314)

    def test_area_5(self):
        with self.assertRaises(TypeError):
            area('string')

    def test_area_6(self):
        with self.assertRaises(TypeError):
            area(-10)

    def test_perimeter_1(self):
        self.assertAlmostEqual(perimeter(10), 62.83185307179586)

    def test_perimeter_2(self):
        self.assertAlmostEqual(perimeter(20), 125.66370614359172)

    def test_perimeter_3(self):
        self.assertAlmostEqual(perimeter(100000), 628318.5307179586)

    def test_perimeter_4(self):
        self.assertNotEqual(perimeter(100), 628)

    def test_perimeter_5(self):
        with self.assertRaises(TypeError):
            perimeter('string')

    def test_perimeter_6(self):
        with self.assertRaises(TypeError):
            perimeter(-10)

