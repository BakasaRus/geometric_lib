import unittest
import config
import circle


class TestCircleMethods(unittest.TestCase):
    def test_circumference_length_typeerror(self):
        self.assertRaises(TypeError, circle.perimeter, 'b')

    def test_circumference_length_valueerror(self):
        self.assertRaises(ValueError, circle.perimeter, -1)

    def test_circumference_length_int(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_circumference_length_float(self):
        self.assertAlmostEqual(circle.perimeter(6.18), 38.8300851983698444, config.kDigitsOfPrecision)

    def test_circle_area_typeerror(self):
        self.assertRaises(TypeError, circle.area, 'b')

    def test_circle_area_valueerror(self):
        self.assertRaises(ValueError, circle.area, -1)

    def test_circle_area_int(self):
        self.assertEqual(circle.area(0), 0)

    def test_circle_area_float(self):
        self.assertAlmostEqual(circle.area(22.8), 1633.12552504211811, config.kDigitsOfPrecision)
