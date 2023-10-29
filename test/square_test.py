import unittest
import square


class SquareTestCase(unittest.TestCase):

    def test_area_first(self):
        res = square.area(10)
        self.assertEqual(100, res)

    def test_area_second(self):
        res = square.area(1)
        self.assertEqual(1, res)

    def test_perimeter_first(self):
        res = square.perimeter(10)
        self.assertEqual(40, res)

    def test_perimeter_second(self):
        res = square.perimeter(700)
        self.assertEqual(2800, res)

    @classmethod
    def setUpClass(cls):
        print(f'Testing {cls.__name__}...')

    @classmethod
    def tearDownClass(cls):
        print(f'Tested {cls.__name__}')


if __name__ == '__main__':
    unittest.main()
