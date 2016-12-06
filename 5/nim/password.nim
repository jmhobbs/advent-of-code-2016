import md5
from strutils import format, join
from sequtils import filter

proc parseIntHex(c: char): int =
  let map = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
  for i, v in map.pairs():
    if v == c:
      return i
  return -1


proc findPassword*(prefix: string): string =
  var
    i: int = 0
    password: seq[char] = @[]
  
  while true:
    var str = $toMD5("$1$2".format(prefix, i))
    if str[0..4] == "00000":
      password.add(str[5])
      if len(password) == 8:
        break
    i = i + 1

  join(password)

proc findSecondPassword*(prefix: string): string =
  var
    i: int = 0
    password: seq[char] = @['_', '_', '_', '_', '_', '_', '_', '_']
  
  while true:
    var str = $toMD5("$1$2".format(prefix, i))
    if str[0..4] == "00000":
      var pos = parseIntHex(str[5])
      if pos <= 7 and password[pos] == '_':
        password[pos] = str[6]
        var filtered = password.filter do (c: char) -> bool : c == '_'
        if len(filtered) == 0:
          break

    i = i + 1

  join(password)

if isMainModule:
  echo findSecondPassword("abc")
