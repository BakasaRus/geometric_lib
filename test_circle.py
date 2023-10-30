from circle import area, perimeter
import unittest


class Test_circe(unittest.TestCase):
    # Сorrectness testing (positive and negative)
    def test_area_correctness_positive(self):
       res = area(10)
       self.assertAlmostEqual(res, 314.159265359)

       res = area(1.5)
       self.assertAlmostEqual(res, 7.068583471)

    def test_perimeter_correctness_positive(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 6.283185307)

        res = perimeter(158.852)
        self.assertAlmostEqual(res, 998.096552416)

    def test_area_correctness_negative(self):
       res = area(20)
       self.assertNotAlmostEqual(res, 1200)

       res = area(1)
       self.assertNotAlmostEqual(res, 0.1)

    def test_perimeter_correctness_negative(self):
        res = perimeter(1e+100)
        self.assertNotAlmostEqual(res, 0)

        res = perimeter(1)
        self.assertNotAlmostEqual(res, 3.14)


    # Failsafety
    def test_area_failsafety(self):
        with self.assertRaises(ValueError):
            res = area(-100)

        with self.assertRaises(ValueError):
            res = area(-1e+100000000)

    def test_perimeter_failsafety(self):
        with self.assertRaises(ValueError):
            res = perimeter(0)

        with self.assertRaises(ValueError):
            res = perimeter(-1e+100000000)


    # Speed testing
    def test_area_speed(self):
       res = area(999999999999999999999999999999999)
       self.assertAlmostEqual(res, 3.1415926535897927e+66)

       res = area(45214562145214562147521451)
       self.assertAlmostEqual(res, 6.422535770073654e+51)

    def test_perimeter_speed(self):
       res = perimeter(999999999999999999999999999999999)
       self.assertAlmostEqual(res, 6.283185307179586e+33)

       res = perimeter(45214562145214562147521451)
       self.assertAlmostEqual(res, 2.840914725413704e+26)
