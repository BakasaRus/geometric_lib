import unittest
import circle


class CircleTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(circle.area(0), -1)
        self.assertEqual(circle.perimeter(0), -1)

    def test_one(self):
        self.assertEqual(circle.area(1), 3.141592653589793)
        self.assertEqual(circle.perimeter(1), 6.283185307179586)

    def test_two(self):
        self.assertEqual(circle.area(2), 12.566370614359172)
        self.assertEqual(circle.perimeter(2), 12.566370614359172)

    def test_five(self):
        self.assertEqual(circle.area(5), 78.53981633974483)
        self.assertEqual(circle.perimeter(5), 31.41592653589793)

    def test_big_data(self):
        self.assertEqual(circle.area(123_456_789), 47_882_831_830_708_839.579653330952153)
        self.assertEqual(circle.perimeter(123_456_789), 775_701_882.7163703)

    def test_float(self):
        self.assertEqual(circle.area(0.5), 0.7853981633974483)
        self.assertEqual(circle.perimeter(0.5), 3.141592653589793)

    def test_negative(self):
        self.assertEqual(circle.area(-1), -1)
        self.assertEqual(circle.perimeter(-1), -1)
