import unittest


def area(a):
    """
    Calculates the area of a square
    :param a: square side size
    :type a: int or float
    :rtype: int or float
    :return: a*a - area of the square
    """
    return a * a


def perimeter(a):
    """
    Calculates the perimeter of a square
    :param a: square side size
    :type a: int or float
    :rtype: int or float
    :return: 4*a - perimeter of the square
    """
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_negative_argument(self):
        self.assertRaises(Exception, area(-10))

    def test_string_argument(self):
        self.assertRaises(Exception, perimeter("10"))
