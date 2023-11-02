import math
import unittest
import circle


class CircleTestCase(unittest.TestCase):

    def test_area_zero(self):
        cases = [[0, 0]]

        for case in cases:
            res = circle.area(case[0])
            self.assertEqual(res, case[1])

    def test_area_circle(self):
        cases = [[1, math.pi],
                 [2, 4 * math.pi],
                 [5, 25 * math.pi]]

        for case in cases:
            res = circle.area(case[0])
            self.assertEqual(res, case[1])

    def test_perimeter_zero(self):
        cases = [[0, 0]]

        for case in cases:
            res = circle.perimeter(case[0])
            self.assertEqual(res, case[1])

    def test_perimeter_circle(self):
        cases = [[1, 2 * math.pi],
                 [5, 10 * math.pi],
                 [9, 18 * math.pi]]

        for case in cases:
            res = circle.perimeter(case[0])
            self.assertEqual(res, case[1])
