import unittest
def area(a, b):
    '''
    Возвращает площадь прямоугольника со сторонами a, b

        Параметры:
            a (float): первая сторона прямоугольника
            b (float): вторая сторона прямоугольника

        Возвращаемое значение:
            a * b  (float): площадь прямоугольника
    '''
    return a * b


def perimeter(a, b):
    '''
    Возвращает площадь периметр со сторонами a, b

        Параметры:
            a (float): первая сторона прямоугольника
            b (float): вторая сторона прямоугольника

        Возвращаемое значение:
            2 * (a * b)  (float): периметр прямоугольника
    '''
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 1)
        self.assertEqual(res, 0)
        res = area(1, 0)
        self.assertEqual(res, 0)
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = area(1, 1)
        self.assertEqual(res, 1)

    def test_two_square_area(self):
        res = area(2, 2)
        self.assertEqual(res, 4)

    def test_half_area(self):
        res = area(0.5, 0.5)
        self.assertEqual(res, 0.25)

    def test_third_area(self):
        res = area(0.332, 3)
        self.assertEqual(res, 0.996)

    def test_big1_area(self):
        res = area(12345, 2)
        self.assertEqual(res, 24690)

    def test_big2_area(self):
        res = area(1020, 1020)
        self.assertEqual(res, 1040400)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
        res = perimeter(0 , 1)
        self.assertEqual(res, 2)
        res = perimeter(1, 0)
        self.assertEqual(res, 2)

    def test_one_perimeter(self):
        res = perimeter(1, 1)
        self.assertEqual(res, 4)

    def test_two_perimeter(self):
        res = perimeter(2, 1)
        self.assertEqual(res, 6)

    def test_half_perimeter(self):
        res = perimeter(0.5, 0.5)
        self.assertEqual(res, 2)

    def test_third_perimeter(self):
        res = perimeter(0.333, 1)
        self.assertEqual(res, 2.666)

    def test_big1_perimeter(self):
        res = perimeter(12345, 1242)
        self.assertEqual(res, 27174)

    def test_big2_perimeter(self):
        res = perimeter(1020, 1021)
        self.assertEqual(res, 4082)