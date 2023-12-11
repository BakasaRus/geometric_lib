import unittest
import triangle

class TriangleTest(unittest.TestCase):
    def test_null_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_not_null_perimeter(self):
        res = triangle.perimeter(23, 7, 10)
        self.assertEqual(res, 40)

    def test_null_area(self):
        res = triangle.area(12, 0)
        self.assertEqual(res, 0)

    def test_not_null_area(self):
        res = triangle.area(12, 5)
        self.assertEqual(res, 30)

    def test_if_wrong_params(self):
        with self.assertRaises(Exception):
            triangle.area([1], 2)
