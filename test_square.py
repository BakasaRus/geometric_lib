import unittest
from square import area
from square import perimeter


class SquareTestCase(unittest.TestCase):
    # Проверка на нулевые входные данные для площади
    def test_zero_mul_area(self):
        res = area(0)
        expected_result = 0
        self.assertEqual(res, expected_result)

    # Проверка на нулевые входные данные для периметра
    def test_zero_mul_perimetr(self):
        res = perimeter(0)
        expected_result = 0
        self.assertEqual(res, expected_result)

    # Проверка на корректность входных данных для площади
    def test_correct_mul_area(self):
        self.assertRaises(TypeError, area, -5)

    # Проверка на корректность входных данных для периметра
    def test_correct_mul_perimetr(self):
        self.assertRaises(TypeError, perimeter, -5)

    # Рандомные числа для площади
    def test_random_area_1(self):
        res = area(10)
        expected_result = 100
        self.assertEqual(res, expected_result)

    def test_random_area_2(self):
        res = area(238)
        expected_result = 56644
        self.assertEqual(res, expected_result)

    def test_random_area_3(self):
        res = area(9384)
        expected_result = 88059456
        self.assertEqual(res, expected_result)

    # Рандомные числа для периметра
    def test_random_perimeter_1(self):
        res = perimeter(10)
        expected_result = 100
        self.assertEqual(res, expected_result)

    def test_random_perimeter_2(self):
        res = perimeter(238)
        expected_result = 56644
        self.assertEqual(res, expected_result)

    def test_random_perimeter_3(self):
        res = perimeter(9384)
        expected_result = 88059456
        self.assertEqual(res, expected_result)
