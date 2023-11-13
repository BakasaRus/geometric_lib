import unittest

from square import *


class SquareTestCase(unittest.TestCase):
    '''
        Test with small values for area
    '''

    def test_zero_area_1(self):
        result = area(0)
        self.assertEqual(result, 0)

    '''
        Test with small values for area
    '''

    def test_small_area_1(self):
        result = area(19)
        self.assertEqual(result, 361)

    '''
        Test with big values for area
    '''

    def test_big_area_1(self):
        result = area(19555842)
        self.assertEqual(result, 382430956328964)

    '''
        Test with incorrect values for area
    '''

    def test_incorrect_area_1(self):
        with self.assertRaises(Exception):
            perimeter(-10000)

    def test_incorrect_area_2(self):
        with self.assertRaises(Exception):
            perimeter("sdfsfd")

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
        self.assertEqual(result, 56)

    '''
        Test with big values for perimeter
    '''

    def test_big_perimeter_1(self):
        result = perimeter(19555842)
        self.assertEqual(result, 78223368)

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
