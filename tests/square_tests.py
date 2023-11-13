import unittest, square


class SquareTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_small_sides_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_small_sides_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

    def test_big_sides_area(self):
        res = square.area(1000000)
        self.assertEqual(res, 1000000000000)

    def test_big_sides_perimeter(self):
        res = square.perimeter(1000000)
        self.assertEqual(res, 4000000)

    def test_negative_side_area(self):
        res = square.area(-3)
        self.assertRaises(ArithmeticError, res)

    def test_negative_side_perimeter(self):
        res = square.perimeter(-3)
        self.assertRaises(ArithmeticError, res)
