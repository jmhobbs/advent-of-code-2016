import unittest
from solution import split_ip, isTLSIP, isSSLIP


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


class TestIsSSLIP(unittest.TestCase):

    # aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
    def test_sample_1(self):
        self.assertTrue(isSSLIP("aba[bab]xyz"))

    # xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
    def test_sample_1(self):
        self.assertFalse(isSSLIP("xyx[xyx]xyx"))

    # aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
    def test_sample_1(self):
        self.assertTrue(isSSLIP("aaa[kek]eke"))

    # zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
    def test_sample_1(self):
        self.assertTrue(isSSLIP("zazbz[bzb]cdb"))

