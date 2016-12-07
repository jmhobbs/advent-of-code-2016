import unittest
from solution import split_ip, isTLSIP


class TestSplitIP(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(split_ip("abba[mnop]qrst"), [["abba", "qrst"], ["mnop"]])

    def test_sample_2(self):
        self.assertEqual(split_ip("gdlrknrmexvaypu[crqappbbcaplkkzb]vhvkjyadjsryysvj[nbvypeadikilcwg]jwxlimrgakadpxu[dgoanojvdvwfabtt]yqsalmulblolkgsheo"),
                         [[
                             'gdlrknrmexvaypu',
                             'vhvkjyadjsryysvj',
                             'jwxlimrgakadpxu',
                             'yqsalmulblolkgsheo',
                         ],
                             [
                             'crqappbbcaplkkzb',
                             'nbvypeadikilcwg',
                             'dgoanojvdvwfabtt']
                         ])


class TestIsTLSIP(unittest.TestCase):

    # abba[mnop]qrst supports TLS (abba outside square brackets).
    def test_sample_1(self):
        self.assertTrue(isTLSIP("abba[mnop]qrst"))

    # abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
    def test_sample_2(self):
        self.assertFalse(isTLSIP("abcd[bddb]xyyx"))

    # aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
    def test_sample_3(self):
        self.assertFalse(isTLSIP("aaaa[qwer]tyui"))

    # ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
    def test_sample_3(self):
        self.assertTrue(isTLSIP("ioxxoj[asdfgh]zxcvbn"))
