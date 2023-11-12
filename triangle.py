import unittest

def area(a, h):
    '''Принимает 2 числа - a, h, возвращает площадь треугольника с высотой h и основанием a'''
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает 3 числа - a, b, c, возвращает площадь треугольника со сторонами a, b, c'''
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    testDelta = 0.000000000001

    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
        res = area(1, 0)
        self.assertEqual(res, 0)
        res = area(0, 1)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0);
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = area(1, 1)
        self.assertAlmostEqual(res, 0.5, delta=self.testDelta)

    def test_one_perimeter(self):
        res = perimeter(1, 1, 1);
        self.assertEqual(res, 3)

    def test_small_area(self):
        res = area(0.00000000001, 0.00000000001)
        self.assertAlmostEqual(res, 4.9999999999999997e-23, delta=self.testDelta)
        res = area(1, 0.00000000001)
        self.assertAlmostEqual(res, 5e-12, delta=self.testDelta)
        res = area(0.00000000001, 1)
        self.assertAlmostEqual(res, 5e-12, delta=self.testDelta)

    def test_small_perimeter(self):
        res = perimeter(0.00000000001, 0.00000000001, 0.00000000001);
        self.assertAlmostEqual(res, 0.00000000003, delta=self.testDelta)
        res = perimeter(1, 0.00000000001, 0.00000000001);
        self.assertAlmostEqual(res, 1.00000000002, delta=self.testDelta)
        res = perimeter(0.00000000001, 1, 0.00000000001);
        self.assertAlmostEqual(res, 1.00000000002, delta=self.testDelta)
        res = perimeter(0.00000000001, 0.00000000001, 1);
        self.assertAlmostEqual(res, 1.00000000002, delta=self.testDelta)
        res = perimeter(1, 1, 0.00000000001);
        self.assertAlmostEqual(res, 2.00000000001, delta=self.testDelta)
        res = perimeter(0.00000000001, 1, 1);
        self.assertAlmostEqual(res, 2.00000000001, delta=self.testDelta)
        res = perimeter(1, 0.00000000001, 1);
        self.assertAlmostEqual(res, 2.00000000001, delta=self.testDelta)

    def test_large_area(self):
        res = area(10000000000000, 10000000000000)
        self.assertAlmostEqual(res, 50000000000000000000000000.0, delta=self.testDelta)
        res = area(1, 10000000000000)
        self.assertAlmostEqual(res, 5000000000000.0, delta=self.testDelta)
        res = area(10000000000000, 1)
        self.assertAlmostEqual(res, 5000000000000.0, delta=self.testDelta)

    def test_large_perimeter(self):
        res = perimeter(10000000000000, 10000000000000, 10000000000000);
        self.assertAlmostEqual(res, 30000000000000, delta=self.testDelta)
        res = perimeter(1, 10000000000000, 10000000000000);
        self.assertAlmostEqual(res, 20000000000001, delta=self.testDelta)
        res = perimeter(10000000000000, 1, 10000000000000);
        self.assertAlmostEqual(res, 20000000000001, delta=self.testDelta)
        res = perimeter(10000000000000, 10000000000000, 1);
        self.assertAlmostEqual(res, 20000000000001, delta=self.testDelta)
        res = perimeter(1, 1, 10000000000000);
        self.assertAlmostEqual(res, 10000000000002, delta=self.testDelta)
        res = perimeter(10000000000000, 1, 1);
        self.assertAlmostEqual(res, 10000000000002, delta=self.testDelta)
        res = perimeter(1, 10000000000000, 1);
        self.assertAlmostEqual(res, 10000000000002, delta=self.testDelta)

    def test_larger_aprox_one_area(self):
        res = area(1.00000000001, 1.00000000001)
        self.assertAlmostEqual(res, 0.50000000001, delta=self.testDelta)
        res = area(1.00000000001, 1)
        self.assertAlmostEqual(res, 0.500000000005, delta=self.testDelta)
        res = area(1, 1.00000000001)
        self.assertAlmostEqual(res, 0.500000000005, delta=self.testDelta)

    def test_larger_aprox_one_perimeter(self):
        res = perimeter(1.00000000001, 1.00000000001, 1.00000000001);
        self.assertAlmostEqual(res, 3.00000000003, delta=self.testDelta)
        res = perimeter(1, 1.00000000001, 1.00000000001);
        self.assertAlmostEqual(res, 3.00000000002, delta=self.testDelta)
        res = perimeter(1.00000000001, 1, 1.00000000001);
        self.assertAlmostEqual(res, 3.00000000002, delta=self.testDelta)
        res = perimeter(1.00000000001, 1.00000000001, 1);
        self.assertAlmostEqual(res, 3.00000000002, delta=self.testDelta)
        res = perimeter(1, 1, 1.00000000001);
        self.assertAlmostEqual(res, 3.00000000001, delta=self.testDelta)
        res = perimeter(1.00000000001, 1, 1);
        self.assertAlmostEqual(res, 3.00000000001, delta=self.testDelta)
        res = perimeter(1, 1.00000000001, 1);
        self.assertAlmostEqual(res, 3.00000000001, delta=self.testDelta)

    def test_smaller_aprox_one_area(self):
        res = area(0.999999999999, 0.999999999999)
        self.assertAlmostEqual(res, 0.499999999999, delta=self.testDelta)
        res = area(1, 0.999999999999)
        self.assertAlmostEqual(res, 0.4999999999995, delta=self.testDelta)
        res = area(0.999999999999, 1)
        self.assertAlmostEqual(res, 0.4999999999995, delta=self.testDelta)

    def test_smaller_aprox_one_perimeter(self):
        res = perimeter(0.999999999999, 0.999999999999, 0.999999999999);
        self.assertAlmostEqual(res, 2.999999999997, delta=self.testDelta)
        res = perimeter(1, 0.999999999999, 0.999999999999);
        self.assertAlmostEqual(res, 2.999999999998, delta=self.testDelta)
        res = perimeter(0.999999999999, 1, 0.999999999999);
        self.assertAlmostEqual(res, 2.999999999998, delta=self.testDelta)
        res = perimeter(0.999999999999, 0.999999999999, 1);
        self.assertAlmostEqual(res, 2.999999999998, delta=self.testDelta)
        res = perimeter(1, 1, 0.999999999999);
        self.assertAlmostEqual(res, 2.999999999999, delta=self.testDelta)
        res = perimeter(0.999999999999, 1, 1);
        self.assertAlmostEqual(res, 2.999999999999, delta=self.testDelta)
        res = perimeter(1, 0.999999999999, 1);
        self.assertAlmostEqual(res, 2.999999999999, delta=self.testDelta)

