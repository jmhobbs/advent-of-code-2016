#!/usr/bin/env python

from solution import TaxiMap


def main():
    taxi_map = TaxiMap()
    with open('input', 'rb') as handle:
        for instruction in map(str.strip, handle.read().split(',')):
            taxi_map.step(instruction)
        print "Blocks Away:", taxi_map.blocks_away()

if __name__ == '__main__':
    main()
