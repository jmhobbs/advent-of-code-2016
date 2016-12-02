const
  pad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

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

if isMainModule:
  var
    kp: Keypad = newKeypad()

  echo kp.executeRow("ULL")
