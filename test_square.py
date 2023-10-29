from square import area, perimeter
import unittest


class Test_square(unittest.TestCase):
    # Сorrectness testing (positive and negative)
    def test_area_correctness_positive(self):
       res = area(10)
       self.assertEqual(res, 100)

       res = area(45.4851)
       self.assertEqual(res, 2068.8943220100005)

    def test_perimeter_correctness_positive(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

        res = perimeter(50)
        self.assertEqual(res, 200)

    def test_area_correctness_negative(self):
       res = area(40)
       self.assertNotEqual(res, 80)

       res = area(50)
       self.assertNotEqual(res, 5000)

    def test_perimeter_correctness_negative(self):
        res = perimeter(100)
        self.assertNotEqual(res, 25)

        res = perimeter(8)
        self.assertNotEqual(res, 4)


    # Failsafety
    def test_area_failsafety(self):
        with self.assertRaises(ValueError):
            res = area(-100)

        with self.assertRaises(ValueError):
            res = area(1e+100000000)

    def test_perimeter_failsafety(self):
        with self.assertRaises(ValueError):
            res = perimeter(-1)

        with self.assertRaises(ValueError):
            res = perimeter(0)


    # Speed testing
    def test_area_speed(self):
       res = area(999999999999999999999999999999999)
       self.assertEqual(res, 999999999999999999999999999999998000000000000000000000000000000001)

    def test_perimeter_speed(self):
       res = perimeter(999999999999999999999999999999999)
       self.assertEqual(res, 3999999999999999999999999999999996)
