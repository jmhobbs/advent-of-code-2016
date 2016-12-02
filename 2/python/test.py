import unittest
from keypad import Keypad


class KeypadTest(unittest.TestCase):
    def setUp(self):
        self.keypad = Keypad()

    # ULL
    # RRDDD
    # LURDL
    # UUUUD
    #
    # So, in this example, the bathroom code is 1985.
    def test_sample_1_1(self):
        self.assertEqual(self.keypad.executeRow('ULL'), 1)
        self.assertEqual(self.keypad.executeRow('RRDDD'), 9)
        self.assertEqual(self.keypad.executeRow('LURDL'), 8)
        self.assertEqual(self.keypad.executeRow('UUUUD'), 5)
