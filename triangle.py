import unittest
def area(a, h):
    """
    Calculates the area of triangle
    :param a: size of the side of the triangle to which the height is build
    :type a: int or float
    :param h: height of triangle
    :type h: int or float
    :rtype: int or float
    :return: a * h / 2 - area of triangle
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Calculates the perimeter of triangle
    :param a: size of the first side of the triangle
    :type a: int or float
    :param b: size of the second side of the triangle
    :type b: int or float
    :param c: size of the third side of the triangle
    :type c : int or float
    :rtype: int or float
    :return: a + b + c - perimeter of triangle
    """
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(1, 0)
        self.assertEqual(res, 0)


    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_zero_two_perimeter(self):
        res = perimeter(1, 0, 0)
        self.assertEqual(res, 2)


    def test_negative_argument(self):
        self.assertRaises(Exception, perimeter(-10, 10, 10))

    def test_string_argument(self):
        self.assertRaises(Exception, perimeter("10", 10, 10))