import unittest
from solution import find_password


class TestFindPassword(unittest.TestCase):

    # The first index which produces a hash that starts with five zeroes is 3231929, which we find by hashing abc3231929; the sixth character of the hash, and thus the first character of the password, is 1.
    # 5017308 produces the next interesting hash, which starts with 000008f82..., so the second character of the password is 8.
    # The third time a hash starts with five zeroes is for abc5278568, discovering the character f.
    # In this example, after continuing this search a total of eight times, the password is 18f47a30.
    def test_sample_1(self):
        self.assertEqual(find_password("abc"), "18f47a30")
