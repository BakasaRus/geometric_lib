import unittest

def area(a):
    '''Принимает число a, возвращает площадь квадрата со стороной a'''
    return a * a


def perimeter(a):
    '''Принимает число a, возвращает периметр квадрата со стороной a'''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    testDelta = 0.000000000001

    def test_zero_side_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = perimeter(0);
        self.assertEqual(res, 0)

    def test_one_side_area(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_one_side_perimeter(self):
        res = perimeter(1);
        self.assertEqual(res, 4)

    def test_small_side_area(self):
        res = area(0.00000000001)
        self.assertAlmostEqual(res, 9.999999999999999e-23, delta=self.testDelta)

    def test_small_side_perimeter(self):
        res = perimeter(0.00000000001);
        self.assertAlmostEqual(res, 4e-11, delta=self.testDelta)

    def test_large_side_area(self):
        res = area(10000000000000)
        self.assertEqual(res, 100000000000000000000000000)

    def test_large_side_perimeter(self):
        res = perimeter(10000000000000);
        self.assertEqual(res, 40000000000000)

    def test_larger_aprox_one_side_area(self):
        res = area(1.00000000001)
        self.assertAlmostEqual(res, 1.00000000002, delta=self.testDelta)

    def test_larger_aprox_one_side_perimeter(self):
        res = perimeter(1.00000000001)
        self.assertAlmostEqual(res, 4.00000000004, delta=self.testDelta)

    def test_smaller_aprox_one_side_area(self):
        res = area(0.999999999999)
        self.assertAlmostEqual(res, 0.999999999998, delta=self.testDelta)

    def test_smaller_aprox_one_side_perimeter(self):
        res = perimeter(0.999999999999);
        self.assertAlmostEqual(res, 3.999999999996, delta=self.testDelta)

