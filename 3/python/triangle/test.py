import unittest
from triangle import is_possible_triangle


class TriangleTest(unittest.TestCase):

    # For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.
    def test_sample(self):
        self.assertFalse(is_possible_triangle(5, 10, 25))
