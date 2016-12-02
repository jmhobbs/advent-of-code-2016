from strutils import join
import keypad

var
  kp: Keypad = newKeypad()
  code: seq[char] = @[]

for line in lines "../input":
  code.add(kp.executeRow(line))

echo "Door Code: ", join[char](code)
