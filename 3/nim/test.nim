import unittest, triangle

suite "Problem One":
  # For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.
  test "Sample One":
    check isValidTriangle(5, 10, 25) == false
