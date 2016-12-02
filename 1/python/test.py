import unittest
from taximap import TaxiMap


class TaxiMapTest(unittest.TestCase):
    def setUp(self):
        self.taxi_map = TaxiMap()

    # Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
    def test_sample_1_1(self):
        self.taxi_map.step('R2')
        self.taxi_map.step('L3')
        self.assertEqual(self.taxi_map.blocks_away(), 5)

    # R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
    def test_sample_1_2(self):
        self.taxi_map.step('R2')
        self.taxi_map.step('R2')
        self.taxi_map.step('R2')
        self.assertEqual(self.taxi_map.blocks_away(), 2)

    # R5, L5, R5, R3 leaves you 12 blocks away.
    def test_sample_1_3(self):
        self.taxi_map.step('R5')
        self.taxi_map.step('L5')
        self.taxi_map.step('R5')
        self.taxi_map.step('R3')
        self.assertEqual(self.taxi_map.blocks_away(), 12)

    # //////// Part Two //////// #

    # For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.
    def test_sample_2_1(self):
        self.taxi_map.step('R8')
        self.taxi_map.step('R4')
        self.taxi_map.step('R4')
        self.taxi_map.step('R8')
        print self.taxi_map.history
        self.assertEqual(self.taxi_map.repeated_points()[0].blocks, 4)
