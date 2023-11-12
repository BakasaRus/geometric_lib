import unittest


def area(a):
    """Принимает длину стороны квадрата, возвращает площадь соответсвующего квадрата"""
    return a * a


def perimeter(a):
    """Принимает длину стороны квадрата, возвращает периметр соответсвующего квадрата"""
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_small_sides_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_small_sides_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_big_sides_area(self):
        res = area(1000000)
        self.assertEqual(res, 1000000000000)

    def test_big_sides_perimeter(self):
        res = perimeter(1000000)
        self.assertEqual(res, 4000000)

    def test_negative_side_area(self):
        res = area(-3)
        self.assertEqual(res, -1)

    def test_negative_side_perimeter(self):
        res = perimeter(-3)
        self.assertEqual(res, -1)