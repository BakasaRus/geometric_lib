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
    """
    Tests the perimeter and area functions for circle
    """

    def test_zero_area(self):
        """
        Test area if circle has 0 radius
        """
        res = area(0)
        """
        Compares the output and the answer we calculated
        """
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        """
        Test perimeter if circle has 0 radius
        """
        res = area(0)
        """
        Compares the output and the answer we calculated
        """
        self.assertEqual(res, 0)

    def test_negative_argument(self):
        """
        Test if circle has negative argument
        """
        res = area(-10)
        """
        Compares the output and the answer we calculated
        """
        self.assertEqual(res, Exception)

    def test_string_argument(self):
        """
        Test if circle has a string argument
        """
        res = perimeter("10")
        """
        Compares the output and the answer we calculated
        """
        self.assertEqual(res, Exception)
