import unittest
import HellTriangle


class TestHellTriangle(unittest.TestCase):
    def test_hell_triangle(self):
        triangle = [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]
        result = HellTriangle.sum_triangle(triangle)
        self.assertEqual(result, 26)
