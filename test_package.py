from test import RectangleTestCase, SquareTestCase, CircleTestCase, TriangleTestCase
import unittest


def suite():
    suite_test = unittest.TestSuite()

    suite_rectangle = unittest.TestLoader().loadTestsFromTestCase(RectangleTestCase)
    suite_square = unittest.TestLoader().loadTestsFromTestCase(SquareTestCase)
    suite_circle = unittest.TestLoader().loadTestsFromTestCase(CircleTestCase)
    suite_triangle = unittest.TestLoader().loadTestsFromTestCase(TriangleTestCase)

    suite_test.addTest(suite_rectangle)
    suite_test.addTest(suite_square)
    suite_test.addTest(suite_circle)
    suite_test.addTest(suite_triangle)

    return suite_test


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
