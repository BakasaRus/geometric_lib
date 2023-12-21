import unittest
from circle import area
from circle import perimeter


class CircleTestCase(unittest.TestCase):
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
        res = area(28)
        expected_result = 2463.0086404143976
        self.assertEqual(res, expected_result)

    def test_random_area_2(self):
        res = area(431)
        expected_result = 583585.3929234936
        self.assertEqual(res, expected_result)

    def test_random_area_3(self):
        res = area(2134879)
        expected_result = 14318463052729.062
        self.assertEqual(res, expected_result)

    # Рандомные числа для периметра
    def test_random_perimeter_1(self):
        res = perimeter(14)
        expected_result = 87.96459430051421
        self.assertEqual(res, expected_result)

    def test_random_perimeter_2(self):
        res = perimeter(192)
        expected_result = 1206.3715789784806
        self.assertEqual(res, expected_result)

    def test_random_perimeter_3(self):
        res = perimeter(132489)
        expected_result = 832452.9381629162
        self.assertEqual(res, expected_result)
