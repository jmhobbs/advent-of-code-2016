import re


REGEX=re.compile('\[.*?\]')
def split_ip(ip):
    hypernets = []
    groups = []
    for group in ip.split('['):
        split = group.split(']')
        if len(split) == 2:
            hypernets.append(split[0])
            groups.append(split[1])
        else:
            groups.append(group)
    return [groups, hypernets]

def isABBAString(seq):
    for i in xrange(0, len(seq)-3):
        if seq[i] == seq[i+3] and seq[i+1] == seq[i+2] and seq[i] != seq[i+1]:
            return True

def isTLSIP(ip):
    result = False
    seqs, hypernets = split_ip(ip)

    for seq in seqs:
        if isABBAString(seq):
            result = True
            break

    for seq in hypernets:
        if isABBAString(seq):
            result = False
            break

    return result
