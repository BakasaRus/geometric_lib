import unittest
def area(a, h):
    '''
    Возвращает площадь треугольника со стороной a и высотой h, проведенной к этой стороне

        Параметры:
            a (float): сторона треугольника
            h (float): высота треугольника

        Возвращаемое значение:
            a * h / 2  (float): площадь треугольника
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника со сторонами a, b, c

        Параметры:
            a (float): первая сторона треугольника
            b (float): вторая сторона треугольника
            c (float): третья сторона треугольника

        Возвращаемое значение:
            a + b + c  (float): периметр треугольника
    '''
    return a + b + c

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 1)
        self.assertEqual(res, 0)
        res = area(1, 0)
        self.assertEqual(res, 0)
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = area(1, 1)
        self.assertEqual(res, 0.5)

    def test_two_square_area(self):
        res = area(1, 2)
        self.assertEqual(res, 1)

    def test_half_area(self):
        res = area(0.5, 8)
        self.assertEqual(res, 2)

    def test_small_area(self):
        res = area(0.02, 0.1)
        self.assertEqual(res, 0.001)

    def test_big1_area(self):
        res = area(12345, 241)
        self.assertEqual(res, 1487572.5)

    def test_big2_area(self):
        res = area(1020, 20)
        self.assertEqual(res, 10200)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_two_perimeter(self):
        res = perimeter(2, 1, 2)
        self.assertEqual(res, 5)

    def test_half_perimeter(self):
        res = perimeter(0.5, 1, 1.5)
        self.assertEqual(res, 3)

    def test_third_perimeter(self):
        res = perimeter(0.333, 0.1, 0.2)
        self.assertEqual(res, 0.633)

    def test_big1_perimeter(self):
        res = perimeter(12345, 123, 7432)
        self.assertEqual(res, 19900)

    def test_big2_perimeter(self):
        res = perimeter(1020, 1, 10235)
        self.assertEqual(res, 11256)