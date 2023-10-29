import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):

    def test_area_first(self):
        res = rectangle.area(10, 15)
        self.assertEqual(150, res)

    def test_area_second(self):
        res = rectangle.area(1, 20)
        self.assertEqual(20, res)

    def test_perimeter_first(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(40, res)

    def test_perimeter_second(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(20, res)

    @classmethod
    def setUpClass(cls):
        print(f'Testing {cls.__name__}...')

    @classmethod
    def tearDownClass(cls):
        print(f'Tested {cls.__name__}')


if __name__ == '__main__':
    unittest.main()
