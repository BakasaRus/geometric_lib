import unittest


def area(a, b):
    """
    Calculates the area of rectangle
    :param a: size of the side of the rectangle (first side)
    :type a: int or float
    :param b: size of the side of the rectangle (adjacent to the first side)
    :type b: int or float
    :rtype: int or float
    :return: a*b - area of the rectangle
    """
    return a * b


def perimeter(a, b):
    """
    Calculates the perimeter of rectangle
    :param a: size of the side of the rectangle (first side)
    :type a: int or float
    :param b: size of the side of the rectangle (adjacent to the first side)
    :type b: int or float
    :rtype: int or float
    :return: 2*(a+b) - perimeter of the rectangle
    """
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_zero_one_perimeter(self):
        res = perimeter(0, 1)
        self.assertEqual(res, 2)

    def test_square_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_negative_argument(self):
        self.assertRaises(Exception, perimeter(-10, 10))

    def test_string_argument(self):
        self.assertRaises(Exception, perimeter("10", 10))
