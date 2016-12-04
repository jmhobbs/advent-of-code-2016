proc indexOf[T](a: seq[T], b: T): int =
  for i, v in a.pairs():
    if v == b:
      return i
  return -1

proc remove[T](a: var seq[T], b: T): bool =
  var
    index: int = a.indexOf(b)

  if index >= 0:
    a.delete(index)
    return true

  false

proc isValidTriangle*(a: int, b: int, c: int): bool =
  var
    largest: int = max(a, max(b, c))
    remaining: seq[int] = @[a, b, c]

  discard remaining.remove(largest)
  remaining[0] + remaining[1] > largest


if isMainModule:
  assert(isValidTriangle(3, 5, 4) == true)
  assert(isValidTriangle(3, 5, 9) == false)
