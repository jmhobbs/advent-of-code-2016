import unittest, taximap

suite "Problem One":
  setup:
    let map = newTaxiMap()

  # Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
  test "Sample One":
    map.step("R2")
    map.step("L3")
    check map.blocks_away() == 5

  # R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
  test "Sample Two":
    map.step("R2")
    map.step("R2")
    map.step("R2")
    check map.blocks_away() == 2

  # R5, L5, R5, R3 leaves you 12 blocks away.
  test "Sample Three":
    map.step("R5")
    map.step("L5")
    map.step("R5")
    map.step("R3")
    check map.blocks_away() == 12

suite "Problem Two":
  setup:
    let map = newTaxiMap()

  # For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.
  test "Sample One":
    map.step("R8")
    map.step("R4")
    map.step("R4")
    map.step("R8")
    var repeats = map.repeated_points()
    check len(repeats) > 0
    check repeats[0].blocks == 4
