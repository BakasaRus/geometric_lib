import unittest

def area(a, b):
    '''Принимает 2 числа - a, b, возвращает площадь прямоугольника со сторонами a, b'''
    return a * b

def perimeter(a, b):
    '''Принимает 2 числа - a, b, возвращает периметр прямоугольника со сторонами a, b'''
    return a * 2 + b * 2

class RectangleTestCase(unittest.TestCase):
    testDelta = 0.000000000001

    def test_zero_side_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
        res = area(0, 1)
        self.assertEqual(res, 0)
        res = area(1, 0)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = perimeter(0, 0);
        self.assertEqual(res, 0)
        res = perimeter(0, 1);
        self.assertEqual(res, 2)
        res = perimeter(1, 0);
        self.assertEqual(res, 2)

    def test_one_side_area(self):
        res = area(1, 1)
        self.assertEqual(res, 1)

    def test_one_side_perimeter(self):
        res = perimeter(1, 1);
        self.assertEqual(res, 4)

    def test_small_side_area(self):
        res = area(0.00000000001, 0.00000000001)
        self.assertAlmostEqual(res, 9.999999999999999e-23, delta=self.testDelta)
        res = area(0.00000000001, 1)
        self.assertAlmostEqual(res, 0.00000000001, delta=self.testDelta)
        res = area(1, 0.00000000001)
        self.assertAlmostEqual(res, 0.00000000001, delta=self.testDelta)

    def test_small_side_perimeter(self):
        res = perimeter(0.00000000001, 0.00000000001)
        self.assertAlmostEqual(res, 0.00000000004, delta=self.testDelta)
        res = perimeter(0.00000000001, 1)
        self.assertAlmostEqual(res, 2.00000000002, delta=self.testDelta)
        res = perimeter(1, 0.00000000001)
        self.assertAlmostEqual(res, 2.00000000002, delta=self.testDelta)

    def test_large_side_area(self):
        res = area(10000000000000, 10000000000000)
        self.assertEqual(res, 100000000000000000000000000)
        res = area(10000000000000, 1)
        self.assertEqual(res, 10000000000000)
        res = area(1, 10000000000000)
        self.assertEqual(res, 10000000000000)

    def test_large_side_perimeter(self):
        res = perimeter(10000000000000, 10000000000000)
        self.assertEqual(res, 40000000000000)
        res = perimeter(10000000000000, 1)
        self.assertEqual(res, 20000000000002)
        res = perimeter(1, 10000000000000)
        self.assertEqual(res, 20000000000002)

    def test_larger_aprox_one_side_area(self):
        res = area(1.00000000001, 1.00000000001)
        self.assertAlmostEqual(res, 1.00000000002, delta=self.testDelta)
        res = area(1.00000000001, 1)
        self.assertAlmostEqual(res, 1.00000000001, delta=self.testDelta)
        res = area(1, 1.00000000001)
        self.assertAlmostEqual(res, 1.00000000001, delta=self.testDelta)

    def test_larger_aprox_one_side_perimeter(self):
        res = perimeter(1.00000000001, 1.00000000001)
        self.assertAlmostEqual(res, 4.00000000004, delta=self.testDelta)
        res = perimeter(1.00000000001, 1)
        self.assertAlmostEqual(res, 4.00000000002, delta=self.testDelta)
        res = perimeter(1, 1.00000000001)
        self.assertAlmostEqual(res, 4.00000000002, delta=self.testDelta)

    def test_smaller_aprox_one_side_area(self):
        res = area(0.999999999999, 0.999999999999)
        self.assertAlmostEqual(res, 0.999999999998, delta=self.testDelta)
        res = area(0.999999999999, 1)
        self.assertAlmostEqual(res, 0.999999999999, delta=self.testDelta)
        res = area(1, 0.999999999999)
        self.assertAlmostEqual(res, 0.999999999999, delta=self.testDelta)

    def test_smaller_aprox_one_side_perimeter(self):
        res = perimeter(0.999999999999, 0.999999999999)
        self.assertAlmostEqual(res, 3.999999999996, delta=self.testDelta)
        res = perimeter(0.999999999999, 1)
        self.assertAlmostEqual(res, 3.999999999998, delta=self.testDelta)
        res = perimeter(1, 0.999999999999)
        self.assertAlmostEqual(res, 3.999999999998, delta=self.testDelta)

