from strutils import split, strip
from taximap import TaxiMap, newTaxiMap, step, blocks_away 

var
  f: File

if open(f, "../input"):
  var
    map: TaxiMap = newTaxiMap()

  let line = readLine(f)
  let instructions = split(line, ',')

  for instruction in instructions:
    map.step(strip(instruction))

  echo "Blocks Away: ", map.blocks_away()
else:
  echo "Couldn't open input file."
