const
  pad = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
  ]

type
  Keypad* = ref object of RootObj
    row: int
    column: int

proc newKeypad*(): Keypad =
  Keypad(row: 1, column: 1)

proc move(kp: Keypad, direction: char) {.raises: [ValueError].} =
  if direction == 'U':
    kp.row = max(0, kp.row - 1)
  elif direction == 'L':
    kp.column = max(0, kp.column - 1)
  elif direction == 'D':
    kp.row = min(2, kp.row + 1)
  elif direction == 'R':
    kp.column = min(2, kp.column + 1)
  else:
    raise newException(ValueError, "Invalid Direction")
#
proc executeRow*(kp: Keypad, row: string): char =
  for direction in row:
    kp.move(direction)

  pad[kp.row][kp.column]

# /// Problem 2 ////

const
  diamond_pad = [
    [' ', ' ', '1', ' ', ' '],
    [' ', '2', '3', '4', ' '],
    ['5', '6', '7', '8', '9'],
    [' ', 'A', 'B', 'C', ' '],
    [' ', ' ', 'D', ' ', ' ']
  ]

type
  InfuriatingKeypad* = ref object of Keypad

proc newInfuriatingKeypad*(): InfuriatingKeypad =
  InfuriatingKeypad(row: 2, column: 0)

proc move(kp: InfuriatingKeypad, direction: char) {.raises: [ValueError].} =
  var
    d_row: int = kp.row
    d_column: int = kp.column

  if direction == 'U':
    d_row = max(0, kp.row - 1)
  elif direction == 'L':
    d_column = max(0, kp.column - 1)
  elif direction == 'D':
    d_row = min(4, kp.row + 1)
  elif direction == 'R':
    d_column = min(4, kp.column + 1)
  else:
    raise newException(ValueError, "Invalid Direction")

  if diamond_pad[d_row][d_column] != ' ':
    kp.row = d_row
    kp.column = d_column

proc executeRow*(kp: InfuriatingKeypad, row: string): char =
  for direction in row:
    kp.move(direction)

  diamond_pad[kp.row][kp.column]
