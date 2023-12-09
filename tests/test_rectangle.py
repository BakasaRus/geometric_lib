import unittest

from rectangle import *


class RectangleTestCase(unittest.TestCase):
    '''
        Test with null values for area
    '''

    def test_zero_area_3(self):
        result = area(0, 0)
        self.assertEqual(result, 0)

    '''
        Test with small values for area
    '''

    def test_small_area_1(self):
        result = area(19, 14)
        self.assertEqual(result, 266)

    '''
        Test with big values for area
    '''

    def test_big_area_1(self):
        result = area(19555842, 98888453)
        self.assertEqual(result, 1933846962492426)

    '''
        Tests with incorrect values for area
    '''

    def test_incorrect_area_1(self):
        with self.assertRaises(Exception):
            perimeter(-10000, 2)

    def test_incorrect_area_2(self):
        with self.assertRaises(Exception):
            perimeter("sdfsfd", 222)

    def test_incorrect_area_3(self):
        with self.assertRaises(Exception):
            perimeter({"sd", 90}, "sd")

    '''
        Test with null values for perimeter
    '''

    def test_zero_perimeter_1(self):
        result = perimeter(0, 0)
        self.assertEqual(result, 0)

    '''
        Test with small values for perimeter
    '''

    def test_small_perimeter_1(self):
        result = perimeter(19, 14)
        self.assertEqual(result, 66)

    '''
        Test with big values for perimeter
    '''

    def test_big_perimeter_1(self):
        result = perimeter(19555842, 98888453)
        self.assertEqual(result, 236888590)

    '''
        Tests with incorrect values for perimeter
    '''

    def test_incorrect_perimeter_1(self):
        with self.assertRaises(Exception):
            perimeter("IWWEd", -12)

    def test_incorrect_perimeter_2(self):
        with self.assertRaises(Exception):
            perimeter(-10000, [11, 1, 122])

    def test_incorrect_perimeter_3(self):
        with self.assertRaises(Exception):
            perimeter({"sd", 90}, "dd")
