from rectangle import area, perimeter
import unittest


class Test_rectangle(unittest.TestCase):
    # Сorrectness testing (positive and negative)
    def test_area_correctness_positive(self):
       res = area(10, 15)
       self.assertEqual(res, 150)

       res = area(1, 50)
       self.assertEqual(res, 50)

    def test_perimeter_correctness_positive(self):
        res = perimeter(10, 20)
        self.assertEqual(res, 60)

        res = perimeter(50, 80)
        self.assertEqual(res, 260)

    def test_area_correctness_negative(self):
       res = area(10, 10)
       self.assertNotEqual(res, 50)

       res = area(20, 50)
       self.assertNotEqual(res, 7000)

    def test_perimeter_correctness_negative(self):
        res = perimeter(100, 10)
        self.assertNotEqual(res, 110)

        res = perimeter(1, 1)
        self.assertNotEqual(res, 1)


    # Failsafety
    def test_area_failsafety(self):
        with self.assertRaises(ValueError):
            res = area(-100, 10)

        with self.assertRaises(ValueError):
            res = area(0, -1e+100000000)

    def test_perimeter_failsafety(self):
        with self.assertRaises(ValueError):
            res = perimeter(-1, 1)

        with self.assertRaises(ValueError):
            res = perimeter(50, 0)


    # Speed testing
    def test_area_speed(self):
       res = area(444444444444444444444444, 55555555555555555555555555555)
       self.assertEqual(res, 24691358024691358024691333333086419753086419753086420)

    def test_perimeter_speed(self):
       res = perimeter(999999999999999999999999999999999, 999999999999999999999999999999999)
       self.assertEqual(res, 3999999999999999999999999999999996)
