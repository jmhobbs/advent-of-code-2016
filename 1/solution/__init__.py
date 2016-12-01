#!/usr/bin/env python

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'blocks'])

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class TaxiMap(object):

    def __init__(self):
        self.orientation = NORTH
        self.x = 0
        self.y = 0
        self.history = [Point(0, 0, 0)]

    def __turn(self, direction):
        if direction == 'R':
            self.orientation += 1
        else:
            self.orientation -= 1

        if self.orientation < NORTH:
            self.orientation = WEST
        elif self.orientation > WEST:
            self.orientation = NORTH

    def __move(self):
        if self.orientation == NORTH:
            self.y += 1
        elif self.orientation == EAST:
            self.x += 1
        elif self.orientation == SOUTH:
            self.y -= 1
        elif self.orientation == WEST:
            self.x -= 1

    def step(self, instruction):
        self.__turn(instruction[0])
        for interval in xrange(1, int(instruction[1:])+1):
            self.__move()
            self.history.append(Point(self.x, self.y, abs(self.x) + abs(self.y)))

    def blocks_away(self):
        return self.history[-1].blocks

    def repeated_points(self):
        repeats = []
        for point in self.history:
            if point in repeats:
                continue
            if self.history.count(point) > 1:
                repeats.append(point)
        return repeats
