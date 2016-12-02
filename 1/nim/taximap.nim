from strutils import parseInt

const
  NORTH = 0
  EAST = 1
  SOUTH = 2
  WEST = 3

type
  Intersection* = tuple[x: int, y: int, blocks: int]
  TaxiMap* = ref object of RootObj
    history: seq[Intersection]
    orientation: int
    x: int
    y: int

proc newTaxiMap*(): TaxiMap =
  var
    intersection: Intersection = (x: 0, y: 0, blocks: 0)
  TaxiMap(orientation: NORTH, x: 0, y: 0, history: @[intersection])

proc turn(taxi_map: TaxiMap, direction: char) {.raises: [ValueError].} =
  case direction
  of 'R':
    taxi_map.orientation = taxi_map.orientation + 1
  of 'L':
    taxi_map.orientation = taxi_map.orientation - 1
  else:
    raise newException(ValueError, "Invalid Direction")

  if taxi_map.orientation < NORTH:
    taxi_map.orientation = WEST
  elif taxi_map.orientation > WEST:
    taxi_map.orientation = NORTH

proc move(taxi_map: TaxiMap) {.raises: [ValueError].} =
  case taxi_map.orientation
  of NORTH:
    taxi_map.y = taxi_map.y + 1
  of EAST:
    taxi_map.x = taxi_map.x + 1
  of SOUTH:
    taxi_map.y = taxi_map.y - 1
  of WEST:
    taxi_map.x = taxi_map.x - 1
  else:
    raise newException(ValueError, "Invalid Orientation")

proc blocks_away*(taxi_map: TaxiMap): int =
  abs(taxi_map.x) + abs(taxi_map.y)

proc step*(taxi_map: TaxiMap, instruction: string) =
  taxi_map.turn(instruction[0])
  var blocks = parseInt(instruction[1..len(instruction)])
  for i in 1..blocks:
    taxi_map.move()
    var
      point: Intersection = (x: taxi_map.x, y: taxi_map.y, blocks: blocks_away(taxi_map))
    taxi_map.history.add(point)

proc repeated_points*(taxi_map: TaxiMap): seq[Intersection] =
  var
    repeats: seq[Intersection]

  repeats = @[]

  for i, point in taxi_map.history:
    if point in repeats:
      continue

    for j, sub_point in taxi_map.history:
      if i >= j:
        continue
      if sub_point == point:
        repeats.add(point)
        break

  return repeats

if isMainModule:
  var taxi_map = newTaxiMap()
  step(taxi_map, "R8")
  step(taxi_map, "R4")
  step(taxi_map, "R4")
  step(taxi_map, "R8")
