import unittest
from keypad import Keypad, InfuriatingKeypad


class KeypadTest(unittest.TestCase):
    def setUp(self):
        self.keypad = Keypad()

    # ULL
    # RRDDD
    # LURDL
    # UUUUD
    #
    # So, in this example, the bathroom code is 1985.
    def test_sample(self):
        self.assertEqual(self.keypad.executeRow('ULL'), '1')
        self.assertEqual(self.keypad.executeRow('RRDDD'), '9')
        self.assertEqual(self.keypad.executeRow('LURDL'), '8')
        self.assertEqual(self.keypad.executeRow('UUUUD'), '5')

class InfuriatingKeypadTest(unittest.TestCase):
    def setUp(self):
        self.keypad = InfuriatingKeypad()

    # ULL
    # RRDDD
    # LURDL
    # UUUUD
    #
    # So, given the actual keypad layout, the code would be 5DB3.
    def test_sample(self):
        self.assertEqual(self.keypad.executeRow('ULL'), '5')
        self.assertEqual(self.keypad.executeRow('RRDDD'), 'D')
        self.assertEqual(self.keypad.executeRow('LURDL'), 'B')
        self.assertEqual(self.keypad.executeRow('UUUUD'), '3')
