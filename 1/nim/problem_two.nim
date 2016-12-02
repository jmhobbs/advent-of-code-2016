from strutils import split, strip
from taximap import TaxiMap, Intersection, newTaxiMap, step, blocks_away, repeated_points

var
  f: File

if open(f, "../input"):
  var
    map: TaxiMap = newTaxiMap()
    repeats: seq[Intersection]

  let line = readLine(f)
  let instructions = split(line, ',')
  for instruction in instructions:
    map.step(strip(instruction))
  repeats = map.repeated_points()
  echo "Blocks Away: ", repeats[0].blocks
else:
  echo "Couldn't open input file."
