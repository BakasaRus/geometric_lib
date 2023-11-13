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
    """
    Tests the perimeter and area functions for square
    """

    def test_zero_area(self):
        """
        Test area if square has zero as an argument
        """
        res = area(0)
        """
        Compares the output and the answer we calculated
        """
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        """
        Test perimeter if square has zero as an argument
        """
        res = area(0)
        """
        Compares the output and the answer we calculated
        """
        self.assertEqual(res, 0)

    def test_negative_argument(self):
        """
        Test if square has a negative argument
        """
        res = area(-10)
        """
        Compares the output and the answer we calculated
        """
        self.assertEqual(res, Exception)

    def test_string_argument(self):
        """
        Test if square has a string argument
        """
        res = perimeter("10")
        """
        Compares the output and the answer we calculated
        """
        self.assertEqual(res, Exception)
