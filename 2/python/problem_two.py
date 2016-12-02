from keypad import InfuriatingKeypad

with open('../input') as handle:

    keypad = InfuriatingKeypad()
    code = []

    for row in handle:
        code.append(keypad.executeRow(row))

    print "Door Code:", ''.join(code)
