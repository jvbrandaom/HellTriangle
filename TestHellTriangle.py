import unittest
from HellTriangle import calculate_maximum_total


class TestHellTriangle(unittest.TestCase):
    def test_hell_triangle(self):
        triangle = [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]
        result = calculate_maximum_total(triangle)
        self.assertEqual(result, 26)

    def test_hell_triangle_2(self):
        triangle = [[6], [5, 3], [9, 7, 1], [10, 6, 8, 4]]
        result = calculate_maximum_total(triangle)
        self.assertEqual(result, 30)

    def test_hell_triangle_3(self):
        triangle = [[6], [5, 3], [9, 7, 1], [10, 6, 8, 4], [1, 7, 5, 6, 7, 8]]
        result = calculate_maximum_total(triangle)
        self.assertEqual(result, 37)

    def test_hell_triangle_with_one_element(self):
        triangle = [[6]]
        result = calculate_maximum_total(triangle)
        self.assertEqual(result, 6)

    def test_empty_hell_triangle(self):
        triangle = []
        with self.assertRaises(IndexError):
            calculate_maximum_total(triangle)

    def test_invalid_input(self):
        triangle = [[6], [3], [9, 7, 1], [4, 6, 8, 4]]
        with self.assertRaises(IndexError):
            calculate_maximum_total(triangle)

if __name__ == '__main__':
    unittest.main()