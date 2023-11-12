import unittest


def area(a, b):
    """Принимает ширину и длину прямоугольника, возвращает площадь соответствующего прямоугольника"""
    return a * b


def perimeter(a, b):
    """Принимает ширину и длину прямоугольника, возвращает периметр соответствующего прямоугольника"""
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 0)

    def test_zero_sides_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_zero_sides_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_small_sides_area(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_small_sides_perimeter(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_big_sides_area(self):
        res = area(1000000, 200000)
        self.assertEqual(res, 200000000000)

    def test_big_sides_perimeter(self):
        res = perimeter(1000000, 200000)
        self.assertEqual(res, 2400000)

    def test_negative_side_area(self):
        res = area(-3, 5)
        self.assertEqual(res, -1)

    def test_negative_side_perimeter(self):
        res = perimeter(-3, 5)
        self.assertEqual(res, -1)
