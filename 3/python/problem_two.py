from triangle import is_possible_triangle

valid = 0

with open('../input', 'rb') as handle:
    rows = []
    for line in handle:
        rows.append(map(int, filter(None, map(str.strip, line.split(' ')))))
        if len(rows) == 3:
            for i in xrange(0, 3):
                if is_possible_triangle(rows[0][i], rows[1][i], rows[2][i]):
                    valid += 1
            rows = []

print "Found %d valid triangles." % valid
