from solution import isSSLIP

count = 0

with open('../input', 'rb') as handle:
    for line in handle:
        if isSSLIP(line):
            count += 1

print 'Number of SSL IPs:', count
