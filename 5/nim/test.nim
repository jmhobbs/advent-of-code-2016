import unittest
from password import findPassword, findSecondPassword

suite "Problem One":

  # The first index which produces a hash that starts with five zeroes is 3231929, which we find by hashing abc3231929; the sixth character of the hash, and thus the first character of the password, is 1.
  # 5017308 produces the next interesting hash, which starts with 000008f82..., so the second character of the password is 8.
  # The third time a hash starts with five zeroes is for abc5278568, discovering the character f.
  # In this example, after continuing this search a total of eight times, the password is 18f47a30.
  test "Sample One":
    check findPassword("abc") == "18f47a30"

  # The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______.
  # In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an invalid position (8).
  # The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___.
  # You almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3.
  test "Sample Two":
    check findSecondPassword("abc") == "05ace8e3"
