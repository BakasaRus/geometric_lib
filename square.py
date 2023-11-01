import unittest
def area(a):
    '''
    Возвращает площадь квадрата со стороной a

        Параметры:
            a (float): сторона квадрата

        Возвращаемое значение:
            a * a  (float): площадь квадрата
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата со стороной a

        Параметры:
            a (float): сторона квадрата

        Возвращаемое значение:
            4 * a  (float): периметр квадрата
    '''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_two_square_area(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_half_area(self):
        res = area(0.5)
        self.assertEqual(res, 0.25)

    def test_small_area(self):
        res = area(0.02)
        self.assertEqual(res, 0.0004)

    def test_big1_area(self):
        res = area(12345)
        self.assertEqual(res, 152399025)

    def test_big2_area(self):
        res = area(1020)
        self.assertEqual(res, 1040400)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_two_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

    def test_half_perimeter(self):
        res = perimeter(0.5)
        self.assertEqual(res, 2)

    def test_third_perimeter(self):
        res = perimeter(0.333)
        self.assertEqual(res, 1.332)

    def test_big1_perimeter(self):
        res = perimeter(12345)
        self.assertEqual(res, 49380)

    def test_big2_perimeter(self):
        res = perimeter(1020)
        self.assertEqual(res, 4080)