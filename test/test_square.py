import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_wrong_arguments(self):
        res = perimeter("abc")
        self.assertRaises(ValueError)

    def test_negative_numbers(self):
        res = perimeter(-1)
        self.assertRaises(ValueError)

    def test_none_argument(self):
        res = perimeter(None)
        self.assertRaises(ValueError)
