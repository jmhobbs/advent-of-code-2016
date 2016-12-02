#!/usr/bin/env python

from taximap import TaxiMap


def main():
    taxi_map = TaxiMap()
    with open('../input', 'rb') as handle:
        for instruction in map(str.strip, handle.read().split(',')):
            taxi_map.step(instruction)
        first_repeat = taxi_map.repeated_points()[0]
        print "Blocks Away:", first_repeat.blocks

if __name__ == '__main__':
    main()
