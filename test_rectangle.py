import unittest
from rectangle import area
from rectangle import perimeter


class RectangleTestCase(unittest.TestCase):
    # Проверка на нулевые входные данные для площади
    def test_zero_mul_area(self):
        res = area(0, 0)
        expected_result = 0
        self.assertEqual(res, expected_result)

    # Проверка на нулевые входные данные для периметра
    def test_zero_mul_perimetr(self):
        res = perimeter(0, 0)
        expected_result = 0
        self.assertEqual(res, expected_result)

    # Проверка на корректность входных данных для площади
    def test_correct_mul_area(self):
        self.assertRaises(TypeError, area, -5, 8)

    # Проверка на корректность входных данных для периметра
    def test_correct_mul_perimetr(self):
        self.assertRaises(TypeError, perimeter, -5, 0)

    # Рандомные числа для площади
    def test_random_area_1(self):
        res = area(7, 29)
        expected_result = 203
        self.assertEqual(res, expected_result)

    def test_random_area_2(self):
        res = area(2833, 947)
        expected_result = 2682851
        self.assertEqual(res, expected_result)

    def test_random_area_3(self):
        res = area(2358474, 71934874)
        expected_result = 169656530022276
        self.assertEqual(res, expected_result)

    # Рандомные числа для периметра
    def test_random_perimeter_1(self):
        res = perimeter(38, 129)
        expected_result = 334
        self.assertEqual(res, expected_result)

    def test_random_perimeter_2(self):
        res = perimeter(2893, 12837)
        expected_result = 31460
        self.assertEqual(res, expected_result)

    def test_random_perimeter_3(self):
        res = perimeter(1384198, 7155132)
        expected_result = 17078660
        self.assertEqual(res, expected_result)
