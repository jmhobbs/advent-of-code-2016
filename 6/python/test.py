import unittest
from solution import MessageCorrector


class TestThing(unittest.TestCase):

    def setUp(self):
        self.mc = MessageCorrector()

    # eedadn
    # drvtee
    # eandsr
    # raavrd
    # atevrs
    # tsrnev
    # sdttsa
    # rasrtv
    # nssdts
    # ntnada
    # svetve
    # tesnvt
    # vntsnd
    # vrdear
    # dvrsen
    # enarar
    # The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.
    def test_sample_1(self):
        messages = [
            'eedadn', 'drvtee', 'eandsr', 'raavrd',
            'atevrs', 'tsrnev', 'sdttsa', 'rasrtv',
            'nssdts', 'ntnada', 'svetve', 'tesnvt',
            'vntsnd', 'vrdear', 'dvrsen', 'enarar'
        ]
        for message in messages:
            self.mc.addMessage(message)
        self.assertEqual(self.mc.getMessage(), 'easter')
