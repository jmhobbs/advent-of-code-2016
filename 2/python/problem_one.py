from keypad import Keypad

with open('../input') as handle:

    keypad = Keypad()
    code = []

    for row in handle:
        code.append(str(keypad.executeRow(row)))

    print "Door Code:", ''.join(code)
