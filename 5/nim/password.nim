import md5
from strutils import format, join

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

if isMainModule:
  echo findPassword("abc")
