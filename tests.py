import unittest
import test_circle
import test_rectangle
import test_square
import test_triangle

circle_test = unittest.TestLoader().loadTestsFromModule(test_circle)
rectangle_test = unittest.TestLoader().loadTestsFromModule(test_rectangle)
square_test = unittest.TestLoader().loadTestsFromModule(test_square)
triangle_test = unittest.TestLoader().loadTestsFromModule(test_triangle)

unittest.TextTestRunner(verbosity=2).run(circle_test)
unittest.TextTestRunner(verbosity=2).run(rectangle_test)
unittest.TextTestRunner(verbosity=2).run(square_test)
unittest.TextTestRunner(verbosity=2).run(triangle_test)

