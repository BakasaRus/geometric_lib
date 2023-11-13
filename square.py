import unittest
from typing import Union


def area(a: Union[int, float]) -> Union[int, float]:
    """
    Принимает длину стороны квадрата и возвращает площадь квадрата

    :param a: сторона квадрата
    :return: площадь квадрата со стороной a
    """
    return a * a


def perimeter(a: Union[int, float]) -> Union[int, float]:
    """
    Принимает длину стороны квадрата и возвращает периметр квадрата

    :param a: сторона квадрата
    :return: периметр квадрата со стороной a
    """
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(0), 0)

    def test_area_2(self):
        self.assertEqual(area(10), 100)

    def test_area_3(self):
        self.assertEqual(area(3000), 9000000)

    def test_area_4(self):
        self.assertNotEqual(area(20), -400)

    def test_perimeter_1(self):
        self.assertEqual(perimeter(10), 40)

    def test_perimeter_2(self):
        self.assertEqual(perimeter(50), 200)

    def test_perimeter_3(self):
        self.assertEqual(perimeter(3000), 12000)

    def test_perimeter_4(self):
        self.assertNotEqual(perimeter(100), 399)
