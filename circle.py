import math, unittest


def area(r):
    """Принимает радиус круга, возвращает площадь круга переданного радиуса"""
    return math.pi * r * r


def perimeter(r):
    """Принимает радиус круга, возвращает периметр круга переданного радиуса"""
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_radius_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_small_radius_area(self):
        res = area(3)
        self.assertEqual(res, 28.274333882308138)

    def test_small_perimeter_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_big_radius_area(self):
        res = area(100000)
        self.assertEqual(res, 31415926535.89793)

    def test_big_radius_perimeter(self):
        res = perimeter(100000)
        self.assertEqual(res, 628318.5307179586)

    def test_negative_radius_area(self):
        res = area(-2)
        self.assertEqual(res, -1)

    def test_negative_radius_perimeter(self):
        res = perimeter(-2)
        self.assertEqual(res, -1)
