import unittest
from triangle import area
from triangle import perimeter


class TriangleTestCase(unittest.TestCase):
    # Проверка на нулевые входные данные для площади
    def test_zero_mul_area(self):
        res = area(0, 0)
        expected_result = 0
        self.assertEqual(res, expected_result)

    # Проверка на нулевые входные данные для периметра
    def test_zero_mul_perimetr(self):
        res = perimeter(0, 0, 0)
        expected_result = 0
        self.assertEqual(res, expected_result)

    # Проверка на корректность входных данных для площади
    def test_correct_mul_area(self):
        self.assertRaises(TypeError, area, -5, 8)

    # Проверка на корректность входных данных для периметра
    def test_correct_mul_perimetr(self):
        self.assertRaises(TypeError, perimeter, 8, 8, 88)

    # Рандомные числа для площади
    def test_random_area_1(self):
        res = area(10, 39)
        expected_result = 195
        self.assertEqual(res, expected_result)

    def test_random_area_2(self):
        res = area(2134, 23924)
        expected_result = 25526908
        self.assertEqual(res, expected_result)

    def test_random_area_3(self):
        res = area(53284139, 95123231)
        expected_result = 2534279731366554.5
        self.assertEqual(res, expected_result)

    # Рандомные числа для периметра
    def test_random_perimeter_1(self):
        res = perimeter(92, 28, 119)
        expected_result = 239
        self.assertEqual(res, expected_result)

    def test_random_perimeter_2(self):
        res = perimeter(6232, 1857, 5412)
        expected_result = 13501
        self.assertEqual(res, expected_result)

    def test_random_perimeter_3(self):
        res = perimeter(417925, 148375, 314285)
        expected_result = 880585
        self.assertEqual(res, expected_result)
