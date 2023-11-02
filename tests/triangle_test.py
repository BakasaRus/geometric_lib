import unittest
import triangle


class TriangleTestCase(unittest.TestCase):

    def test_area_zero(self):
        cases = [[5, 0, 0],
                [0, 0, 0],
                 [0, 20, 0]]

        for case in cases:
            res = triangle.area(case[0], case[1])
            self.assertEqual(res, case[2])

    def test_area_rectangular(self):
        cases = [[2, 1, 1],
                 [4, 2, 4],
                 [10, 5, 25]]

        for case in cases:
            res = triangle.area(case[0], case[1])
            self.assertEqual(res, case[2])

    def test_area_triangle(self):
        cases = [[2, 5, 5],
                 [8, 1, 4],
                 [1000, 1000, 500000]]

        for case in cases:
            res = triangle.area(case[0], case[1])
            self.assertEqual(res, case[2])

    def test_perimeter_zero(self):
        cases = [[0, 0, 0, 0]]

        for case in cases:
            res = triangle.perimeter(case[0], case[1], case[2])
            self.assertEqual(res, case[3])

    def test_perimeter_rectangular(self):
        cases = [[3, 4, 5, 12],
                 [8, 6, 10, 24],
                 [25, 15, 20, 60]]

        for case in cases:
            res = triangle.perimeter(case[0], case[1], case[2])
            self.assertEqual(res, case[3])

    def test_perimeter_triangle(self):
        cases = [[1, 2, 6, 9],
                 [5, 3, 16, 24],
                 [9, 17, 52, 78]]

        for case in cases:
            res = triangle.perimeter(case[0], case[1], case[2])
            self.assertEqual(res, case[3])
