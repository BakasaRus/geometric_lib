import unittest
import square

class TestSquare(unittest.TestCase):
    # Correct testing (positive numbers)
    def test_area_positive(self):
        res = square.area(150)
        self.assertEqual(res, 22500)

        res = square.area(27.3983)
        self.assertEqual(res, 750.66684289)

    def test_perimeter_positive(self):
        res = square.perimeter(2573)
        self.assertEqual(res, 10292)

        res = square.perimeter(98394)
        self.assertEqual(res, 393576)

    def test_area_negative(self):
        res = square.area(6278)
        self.assertNotEqual(res, 29830)

        res = square.area(289374)
        self.assertNotEqual(res, 86794)

    def test_perimeter_negative(self):
        res = square.perimeter(2689321)
        self.assertNotEqual(res, 921340325)

        res = square.perimeter(8273)
        self.assertNotEqual(res, 45678)

    # Failure (negative, zero and strings)
    def test_area_failure(self):
        with self.assertRaises(ValueError):
            res = square.area(-10008)

        with self.assertRaises(ValueError):
            res = square.area(0)

        with self.assertRaises(ValueError):
            res = square.area("1e+13849000")

    def test_perimeter_failure(self):
        with self.assertRaises(ValueError):
            res = square.perimeter(-14567)

        with self.assertRaises(ValueError):
            res = square.perimeter(0)

        with self.assertRaises(ValueError):
            res = square.area("287364")

    # Speed testing
    def test_area_speed(self):
        res = square.area(1827364981239847982374987239874982734829834789273872384)
        self.assertEqual(res, 3339262774661709968568640839588132724875442688405789442349249032418067598291974796128047897054140034717843456)

    def test_perimeter_speed(self):
        res = square.perimeter(72394792384028309480293840923094809283409823094)
        self.assertEqual(res, 289579169536113237921175363692379237133639292376)
