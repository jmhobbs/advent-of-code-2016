import unittest
from solution import is_real_room, split_room_string, decrypt


class RoomParseTest(unittest.TestCase):

    # aaaaa-bbb-z-y-x-123[abxyz]
    def test_sample_1(self):
        self.assertEqual(("aaaaa-bbb-z-y-x", "123", "abxyz"), split_room_string("aaaaa-bbb-z-y-x-123[abxyz]"))


class RoomChecksumTest(unittest.TestCase):

    # aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
    def test_sample_1(self):
        self.assertTrue(is_real_room("aaaaa-bbb-z-y-x", "abxyz"))

    # a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
    def test_sample_2(self):
        self.assertTrue(is_real_room("a-b-c-d-e-f-g-h", "abcde"))

    # not-a-real-room-404[oarel] is a real room.
    def test_sample_3(self):
        self.assertTrue(is_real_room("not-a-real-room", "oarel"))

    # totally-real-room-200[decoy] is not.
    def test_sample_4(self):
        self.assertFalse(is_real_room("totally-real-room", "decoy"))


class ShiftCipherTest(unittest.TestCase):

    # For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.
    def test_sample_1(self):
        self.assertEqual("very encrypted name", decrypt("qzmt-zixmtkozy-ivhz", 343))
