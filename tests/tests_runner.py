import unittest, setup
import circle_tests, rectangle_tests, square_tests, triangle_tests

suite1 = unittest.TestLoader().loadTestsFromModule(circle_tests)
suite2 = unittest.TestLoader().loadTestsFromModule(rectangle_tests)
suite3 = unittest.TestLoader().loadTestsFromModule(square_tests)
suite4 = unittest.TestLoader().loadTestsFromModule(triangle_tests)

unittest.TextTestRunner(verbosity=2).run(suite1)
unittest.TextTestRunner(verbosity=2).run(suite2)
unittest.TextTestRunner(verbosity=2).run(suite3)
unittest.TextTestRunner(verbosity=2).run(suite4)
