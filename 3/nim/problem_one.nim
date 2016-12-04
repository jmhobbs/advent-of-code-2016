from strutils import split, strip, parseInt
from sequtils import map, keepIf
from triangle import isValidTriangle

var
  valid: int = 0

for line in lines "../input":
  var
    row: seq[string] = line.split
    triangle: seq[int]

  row = row.map(proc(x: string): string = x.strip)
  row.keepIf(proc(x: string): bool = len(x) > 0)
  triangle = row.map(proc(x: string): int = x.parseInt)

  if isValidTriangle(triangle[0], triangle[1], triangle[2]):
    valid = valid + 1

echo("Found ", valid, " valid triangles.")
