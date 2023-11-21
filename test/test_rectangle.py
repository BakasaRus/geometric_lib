import rectangle
import unittest

class RectangleTest(unittest.TestCase):
    def test_null_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_not_null_perimeter(self):
        res = rectangle.perimeter(23, 7)
        self.assertEqual(res, 60)

    def test_null_area(self):
        res = rectangle.area(12, 0)
        self.assertEqual(res, 0)

    def test_not_null_area(self):
        res = rectangle.area(12, 5)
        self.assertEqual(res, 60)

    def test_if_wrong_params(self):
        try:
            res = rectangle.area([1], 'a')
        except:
            self.fail('Wrong params')
