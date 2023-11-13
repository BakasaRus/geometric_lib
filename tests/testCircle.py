import sys
sys.path.append(r"C:\Users\user\Documents\IS-1_semestr\1-semester\DevTools\lab2\geometric_lib")
import circle
import unittest


class CircleTestCaseArea(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(type(circle.area(-1)), Exception)

    def testSimpleRadius(self):
        self.assertEqual(circle.area(3), 28.274333882308138)

    def testZeroRadius(self):
        self.assertEqual(circle.area(0), 0)

    def testBigRadius(self):
        self.assertEqual(circle.area(10_000), 314159265.3589793)


class CircleTestCasePerimeter(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(type(circle.perimeter(-1)), Exception)

    def testSimpleRadius(self):
        self.assertEqual(circle.perimeter(3), 18.84955592153876)

    def testZeroRadius(self):
        self.assertEqual(circle.perimeter(0), 0)

    def testBigRadius(self):
        self.assertEqual(circle.perimeter(10_000), 62831.853071795864)