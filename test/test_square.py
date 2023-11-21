import unittest
import square

class SquareTest(unittest.TestCase):
    def test_null_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_not_null_perimeter(self):
        res = square.perimeter(23)
        self.assertEqual(res, 92)

    def test_null_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_not_null_area(self):
        res = square.area(12)
        self.assertEqual(res, 144)

    def test_if_wrong_params(self):
        with self.assertRaises(Exception):
            square.area('a')
