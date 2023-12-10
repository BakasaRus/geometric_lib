import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_zero1(self):
        self.assertEqual(rectangle.area(0, 5), -1)
        self.assertEqual(rectangle.perimeter(0, 5), -1)

    def test_zero2(self):
        self.assertEqual(rectangle.area(5, 0), -1)
        self.assertEqual(rectangle.perimeter(5, 0), -1)

    def test_zero3(self):
        self.assertEqual(rectangle.area(0, 0), -1)
        self.assertEqual(rectangle.perimeter(0, 0), -1)

    def test_one(self):
        self.assertEqual(rectangle.area(1, 1), 1)
        self.assertEqual(rectangle.perimeter(1, 1), 4)

    def test_two(self):
        self.assertEqual(rectangle.area(2, 4), 8)
        self.assertEqual(rectangle.perimeter(2, 4), 12)

    def test_five(self):
        self.assertEqual(rectangle.area(5, 6), 30)
        self.assertEqual(rectangle.perimeter(5, 6), 22)

    def test_big_data(self):
        self.assertEqual(rectangle.area(123_456_789, 1_234_567_890), 152_415_787_501_905_210)
        self.assertEqual(rectangle.perimeter(123_456_789, 1_234_567_890), 2_716_049_358)

    def test_float(self):
        self.assertEqual(rectangle.area(0.5, 0.145), 0.0725)
        self.assertEqual(rectangle.perimeter(0.5, 0.145), 1.29)

    def test_negative1(self):
        self.assertEqual(rectangle.area(-1, 1), -1)
        self.assertEqual(rectangle.perimeter(-1, 1), -1)

    def test_negative2(self):
        self.assertEqual(rectangle.area(1, -1), -1)
        self.assertEqual(rectangle.perimeter(1, -1), -1)

    def test_negative3(self):
        self.assertEqual(rectangle.area(-1, -1), -1)
        self.assertEqual(rectangle.perimeter(-1, -1), -1)
