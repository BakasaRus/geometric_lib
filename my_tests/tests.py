import unittest
import circle
import rectangle
import square
import triangle


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


class RectangleTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(rectangle.area(0, 5), -1)
        self.assertEqual(rectangle.area(5, 0), -1)
        self.assertEqual(rectangle.area(0, 0), -1)
        self.assertEqual(rectangle.perimeter(0, 5), -1)
        self.assertEqual(rectangle.perimeter(5, 0), -1)
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

    def test_negative(self):
        self.assertEqual(rectangle.area(-1, 1), -1)
        self.assertEqual(rectangle.area(1, -1), -1)
        self.assertEqual(rectangle.area(-1, -1), -1)
        self.assertEqual(rectangle.perimeter(-1, 1), -1)
        self.assertEqual(rectangle.perimeter(1, -1), -1)
        self.assertEqual(rectangle.perimeter(-1, -1), -1)


class SquareTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(square.area(0), -1)
        self.assertEqual(square.perimeter(0), -1)

    def test_one(self):
        self.assertEqual(square.area(1), 1)
        self.assertEqual(square.perimeter(1), 4)

    def test_two(self):
        self.assertEqual(square.area(2), 4)
        self.assertEqual(square.perimeter(2), 8)

    def test_five(self):
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.perimeter(5), 20)

    def test_big_data(self):
        self.assertEqual(square.area(123_456_789), 15_241_578_750_190_521)
        self.assertEqual(square.perimeter(123_456_789), 493_827_156)

    def test_float(self):
        self.assertEqual(square.area(0.5), 0.25)
        self.assertEqual(square.perimeter(0.5), 2)

    def test_negative(self):
        self.assertEqual(square.area(-1), -1)
        self.assertEqual(square.perimeter(-1), -1)


class TriangleTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(triangle.area(0, 5), -1)
        self.assertEqual(triangle.area(5, 0), -1)
        self.assertEqual(triangle.area(0, 0), -1)
        self.assertEqual(triangle.perimeter(0, 0, 0), -1)
        self.assertEqual(triangle.perimeter(5, 0, 0), -1)

    def test_one(self):
        self.assertEqual(triangle.area(1, 2), 1)
        self.assertEqual(triangle.perimeter(1, 2, 2.5), 5.5)

    def test_two(self):
        self.assertEqual(triangle.area(2, 4), 4)
        self.assertEqual(triangle.perimeter(2, 4, 5), 11)

    def test_five(self):
        self.assertEqual(triangle.area(5, 6), 15)
        self.assertEqual(triangle.perimeter(5, 6, 8), 19)

    def test_big_data(self):
        self.assertEqual(triangle.area(123_456_789, 1_234_567_890), 76_207_893_750_952_605)
        self.assertEqual(triangle.perimeter(123_456_789, 1_234_567_890, 1_234_567_890), 2_592_592_569)

    def test_float(self):
        self.assertEqual(triangle.area(0.5, 0.145), 0.03625)
        self.assertEqual(triangle.perimeter(0.5, 0.145, 0.147), 0.792)

    def test_negative(self):
        self.assertEqual(triangle.area(-1, 1), -1)
        self.assertEqual(triangle.area(1, -1), -1)
        self.assertEqual(triangle.area(-1, -1), -1)
        self.assertEqual(triangle.perimeter(-1, 1, 5), -1)
        self.assertEqual(triangle.perimeter(1, -1, 5), -1)
        self.assertEqual(triangle.perimeter(-1, -1, -5), -1)

    def test_non_existent(self):
        self.assertEqual(triangle.perimeter(1, 5, 7), -1)
        self.assertEqual(triangle.perimeter(3, 4, 8), -1)
        self.assertEqual(triangle.perimeter(17, 7, 9), -1)
        self.assertEqual(triangle.perimeter(3, 28, 17), -1)
