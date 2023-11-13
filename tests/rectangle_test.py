import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):

    def test_area_wrong_arguments(self):
        cases = [["1", 1, 1],
                 [2, "2", 4],
                 [5, 5, "25"]]

        for case in cases:
            res = rectangle.area(case[0], case[1])
            self.assertEqual(res, case[2])

    def test_area_zero(self):
        cases = [[5, 0, 0],
                [0, 0, 0],
                 [0, 20, 0]]

        for case in cases:
            res = rectangle.area(case[0], case[1])
            self.assertEqual(res, case[2])

    def test_area_square(self):
        cases = [[1, 1, 1],
                 [2, 2, 4],
                 [5, 5, 25]]

        for case in cases:
            res = rectangle.area(case[0], case[1])
            self.assertEqual(res, case[2])

    def test_area_rectangle(self):
        cases = [[2, 5, 10],
                 [8, 1, 8],
                 [1000, 1000, 1000000]]

        for case in cases:
            res = rectangle.area(case[0], case[1])
            self.assertEqual(res, case[2])

    def test_perimeter_wrong_arguments(self):
        cases = [["1", 1, 4],
                 [3, "3", 12],
                 [100, 100, "400"]]

        for case in cases:
            res = rectangle.perimeter(case[0], case[1])
            self.assertEqual(res, case[2])

    def test_perimeter_zero(self):
        cases = [[0, 0, 0]]

        for case in cases:
            res = rectangle.perimeter(case[0], case[1])
            self.assertEqual(res, case[2])

    def test_perimeter_square(self):
        cases = [[1, 1, 4],
                 [3, 3, 12],
                 [100, 100, 400]]

        for case in cases:
            res = rectangle.perimeter(case[0], case[1])
            self.assertEqual(res, case[2])

    def test_perimeter_rectangle(self):
        cases = [[1, 2, 6],
                 [5, 3, 16],
                 [9, 17, 52]]

        for case in cases:
            res = rectangle.perimeter(case[0], case[1])
            self.assertEqual(res, case[2])
