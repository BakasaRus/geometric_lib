import math
import unittest
def area(r):
    '''
    Возвращает площадь круга радиуса r

        Параметры:
            r (float): радиус круга

        Возвращаемое значение:
            math.pi * r * r (float): площадь круга
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Возвращает периметр окружности радиуса r

        Параметры:
            r (float): радиус круга

        Возвращаемое значение:
            2 * math.pi * r  (float): периметр круга
    '''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = area(1)
        self.assertEqual(res, 3.141592653589793)

    def test_two_area(self):
        res = area(2)
        self.assertEqual(res, 12.566370614359172)

    def test_half_area(self):
        res = area(0.5)
        self.assertEqual(res, 0.7853981633974483)

    def test_third_area(self):
        res = area(0.333)
        self.assertEqual(res, 0.3483680677639186)

    def test_big1_area(self):
        res = area(12345)
        self.assertEqual(res, 478775657.3542472)

    def test_big2_area(self):
        res = area(1020)
        self.assertEqual(res, 3268512.9967948208)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = perimeter(1)
        self.assertEqual(res, 6.283185307179586)

    def test_two_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 12.566370614359172)

    def test_half_perimeter(self):
        res = perimeter(0.5)
        self.assertEqual(res, 3.141592653589793)

    def test_third_perimeter(self):
        res = perimeter(0.333)
        self.assertEqual(res, 2.092300707290802)

    def test_big1_perimeter(self):
        res = perimeter(12345)
        self.assertEqual(res, 77565.92261713199)

    def test_big2_perimeter(self):
        res = perimeter(1020)
        self.assertEqual(res, 6408.849013323178)