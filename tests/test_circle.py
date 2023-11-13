import unittest

from circle import *


class CircleTestCase(unittest.TestCase):
    '''
        Test with null values for area
    '''

    def test_zero_area_1(self):
        result = area(0)
        self.assertEqual(result, 0)

    '''
        Test with small values for area
    '''

    def test_small_area_1(self):
        result = area(19)
        self.assertEqual(result, 1134.1149479459152)

    '''
        Test with big values for area
    '''

    def test_big_area_1(self):
        result = area(19555842)
        self.assertEqual(result, 1201442282908392.2)

    '''
        Tests with incorrect values for area
    '''

    def test_incorrect_area_1(self):
        with self.assertRaises(Exception):
            perimeter("sdfsd")

    def test_incorrect_area_2(self):
        with self.assertRaises(Exception):
            perimeter(-10000)

    def test_incorrect_area_3(self):
        with self.assertRaises(Exception):
            perimeter({"sd", 90})

    '''
        Test with null values for perimeter
    '''

    def test_zero_perimeter_1(self):
        result = perimeter(0)
        self.assertEqual(result, 0)

    '''
        Test with small values for perimeter
    '''

    def test_small_perimeter_1(self):
        result = perimeter(14)
        self.assertEqual(result, 87.96459430051421)

    '''
        Test with big values for perimeter
    '''

    def test_big_perimeter_1(self):
        result = perimeter(19555842)
        self.assertEqual(result, 122872979.12392545)

    '''
        Tests with incorrect values for perimeter
    '''

    def test_incorrect_perimeter_1(self):
        with self.assertRaises(Exception):
            perimeter("IWWEd")

    def test_incorrect_perimeter_2(self):
        with self.assertRaises(Exception):
            perimeter(-10000)

    def test_incorrect_perimeter_3(self):
        with self.assertRaises(Exception):
            perimeter({"sd", 90})
