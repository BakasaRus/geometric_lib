import unittest
import math


def area(r):
    """
    Calculates the area of circle
    :param r: circle radius value
    :type r: int or float
    :rtype: float
    :return: math.pi * r * r - area of a circle
    """
    return math.pi * r * r


def perimeter(r):
    """
    Calculates the perimeter of circle
    :param r: circle radius value
    :type r: int or float
    :rtype: float
    :return: 2 * math.pi * r - perimeter of a circle
    """
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_negative_argument(self):
        self.assertEqual(Exception, area(-10))

    def test_string_argument(self):
        self.assertRaises(Exception, perimeter("10"))
