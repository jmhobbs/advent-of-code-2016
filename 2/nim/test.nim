import unittest, keypad

suite "Problem One":
  setup:
    let kp = newKeypad()

  # ULL
  # RRDDD
  # LURDL
  # UUUUD
  #
  # So, in this example, the bathroom code is 1985.
  test "Sample One":
    check kp.executeRow("ULL") == '1'
    check kp.executeRow("RRDDD") == '9'
    check kp.executeRow("LURDL") == '8'
    check kp.executeRow("UUUUD") == '5'
