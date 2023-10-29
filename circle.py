import math
import unittest
from typing import Union


def area(r: Union[int, float]) -> Union[int, float]:
    """
    Принимает радиус круга и возвращает площадь круга

    :param r: радиус круга
    :return: площадь круга
    """
    return math.pi * r * r


def perimeter(r: Union[int, float]) -> Union[int, float]:
    """
    Принимает радиус круга и возвращает периметр круга

    :param r: радиус круга
    :return: периметр круга
    """
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(10), 314.1592653589793)

    def test_area_2(self):
        self.assertEqual(area(3), 28.274333882308138)

    def test_area_3(self):
        self.assertEqual(area(100000), 31415926535.89793)

    def test_perimeter_1(self):
        self.assertEqual(perimeter(10), 62.83185307179586)

    def test_perimeter_2(self):
        self.assertEqual(perimeter(20), 125.66370614359172)

    def test_perimeter_3(self):
        self.assertEqual(perimeter(100000), 628318.5307179586)