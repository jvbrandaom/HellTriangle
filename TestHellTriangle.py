import unittest
import HellTriangle


class TestHellTriangle(unittest.TestCase):
    def test_hell_triangle(self):
        triangle = [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]
        result = HellTriangle.calculate_maximum_total(triangle)
        self.assertEqual(result, 26)

    def test_invalid_input(self):
        triangle = [[6], [3], [9, 7, 1], [4, 6, 8, 4]]
        with self.assertRaises(IndexError):
            HellTriangle.calculate_maximum_total(triangle)