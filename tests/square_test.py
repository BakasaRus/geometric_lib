import unittest
import square


class SquareTestCase(unittest.TestCase):

    def test_area_wrong_arguments(self):
        cases = [["1", 1],
                 [2, "4"],
                 ["3", "9"]]

        for case in cases:
            res = square.area(case[0])
            self.assertEqual(res, case[1])

    def test_area_zero(self):
        cases = [[0, 0]]

        for case in cases:
            res = square.area(case[0])
            self.assertEqual(res, case[1])

    def test_area_square(self):
        cases = [[1, 1],
                 [2, 4],
                 [5, 25]]

        for case in cases:
            res = square.area(case[0])
            self.assertEqual(res, case[1])

    def test_perimeter_wrong_arguments(self):
        cases = [["1", 4],
                 [3, "12"],
                 ["100", "400"]]

        for case in cases:
            res = square.perimeter(case[0])
            self.assertEqual(res, case[1])

    def test_perimeter_zero(self):
        cases = [[0, 0]]

        for case in cases:
            res = square.perimeter(case[0])
            self.assertEqual(res, case[1])

    def test_perimeter_square(self):
        cases = [[1, 4],
                 [3, 12],
                 [100, 400]]

        for case in cases:
            res = square.perimeter(case[0])
            self.assertEqual(res, case[1])
