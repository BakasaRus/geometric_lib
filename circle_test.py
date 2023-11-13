import importlib
import unittest
import circle


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = circle.area(1)
        self.assertAlmostEqual(res, 3.141592653589793, 0.000001)

    def test_two_area(self):
        res = circle.area(2)
        self.assertAlmostEqual(res, 12.566370614359172, 0.000001)

    def test_half_area(self):
        res = circle.area(0.5)
        self.assertAlmostEqual(res, 0.7853981633974483, 0.000001)

    def test_third_area(self):
        res = circle.area(0.333)
        self.assertAlmostEqual(res, 0.3483680677639186, 0.000001)

    def test_big1_area(self):
        res = circle.area(12345)
        self.assertAlmostEqual(res, 478775657.3542472, 0.000001)

    def test_big2_area(self):
        res = circle.area(1020)
        self.assertAlmostEqual(res, 3268512.9967948208, 0.000001)
    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = circle.perimeter(1)
        self.assertAlmostEqual(res, 6.283185307179586, 0.000001)

    def test_two_perimeter(self):
        res = circle.perimeter(2)
        self.assertAlmostEqual(res, 12.566370614359172, 0.000001)

    def test_half_perimeter(self):
        res = circle.perimeter(0.5)
        self.assertAlmostEqual(res, 3.141592653589793, 0.000001)

    def test_third_perimeter(self):
        res = circle.perimeter(0.333)
        self.assertEqual(res, 2.092300707290802, 0.000001)

    def test_big1_perimeter(self):
        res = circle.perimeter(12345)
        self.assertAlmostEqual(res, 77565.92261713199, 0.000001)

    def test_big2_perimeter(self):
        res = circle.perimeter(1020)
        self.assertAlmostEqual(res, 6408.849013323178, 0.000001)


if __name__ == '__main__':
    unittest.main()
