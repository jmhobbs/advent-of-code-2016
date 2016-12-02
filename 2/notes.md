# nim

Trying to use a `case` for `proc move(kp: Keypad, direction: char)` throws an AST error I can't figure out.

I used the same syntax in problem 1, so I'm unsure what happened here.  I relaced it with if/elif/else.

    proc move(kp: Keypad, direction: char) {.raises: [ValueError].} =
      case direction
      on 'U':
        kp.row = max(0, kp.row - 1)
      else:
        raise newException(ValueError, "Invalid Direction")

nim check shows:

     keypad.nim(17, 3) Error: illformed AST: case direction
