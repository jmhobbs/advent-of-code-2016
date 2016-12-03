from triangle import is_possible_triangle

valid = 0

with open('../input', 'rb') as handle:
    for line in handle:
        triangle = map(int, filter(None, map(str.strip, line.split(' '))))

        if is_possible_triangle(triangle[0], triangle[1], triangle[2]):
            valid += 1

print "Found %d valid triangles." % valid
