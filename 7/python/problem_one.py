from solution import isTLSIP

count = 0

with open('../input', 'rb') as handle:
    for line in handle:
        if isTLSIP(line):
            count += 1

print 'Number of IPs:', count
