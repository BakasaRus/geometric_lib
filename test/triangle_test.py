import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    """Provides tests for triangle module
       Tests contains check for area and perimeter functions
    """
    def test_area_first(self):
        res = triangle.area(10, 20)
        self.assertEqual(100, res)

    def test_area_second(self):
        res = triangle.area(5, 1)
        self.assertEqual(2.5, res)

    def test_perimeter_first(self):
        res = triangle.perimeter(10, 20, 30)
        self.assertEqual(60, res)

    def test_perimeter_second(self):
        res = triangle.perimeter(1, 2, 3)
        self.assertEqual(6, res)

    @classmethod
    def setUpClass(cls):
        print(f'Testing {cls.__name__}...')

    @classmethod
    def tearDownClass(cls):
        print(f'Tested {cls.__name__}')


if __name__ == '__main__':
    unittest.main()
