import unittest
from circleTest import CircleTestCase
from rectangleTest import RectangleTestCase
from squareTest import SquareTestCase
from triangleTest import TriangleTestCase

suite = unittest.TestLoader().loadTestsFromTestCase(CircleTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromTestCase(RectangleTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromTestCase(SquareTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromTestCase(TriangleTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)