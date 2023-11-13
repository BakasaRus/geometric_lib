import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 1)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(10, 2)
        self.assertEqual(res, 10)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)

    def test_wrong_arguments(self):
        res = perimeter("abc", "q", 8)
        self.assertEqual(res, ValueError)

    def test_negative_numbers(self):
        res = perimeter(-1, -8, 2)
        self.assertEqual(res, ValueError)

    def test_none_argument(self):
        res = perimeter(None, None, None)
        self.assertEqual(res, ValueError)
