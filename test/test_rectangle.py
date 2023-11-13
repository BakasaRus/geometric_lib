import unittest

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_wrong_arguments(self):
        res = perimeter("abc", None)
        sself.assertRaises(ValueError)

    def test_negative_numbers(self):
        res = perimeter(-1, -2)
        self.assertRaises(ValueError)

    def test_none_argument(self):
        res = perimeter(None, None)
        self.assertRaises(ValueError)
