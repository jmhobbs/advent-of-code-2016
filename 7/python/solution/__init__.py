import re


REGEX=re.compile('\[.*?\]')
def split_ip(ip):
    hypernets = []
    supernets = []
    for supernet in ip.split('['):
        split = supernet.split(']')
        if len(split) == 2:
            hypernets.append(split[0])
            supernets.append(split[1])
        else:
            supernets.append(supernet)
    return [supernets, hypernets]

def isABBAString(net):
    for i in xrange(0, len(net)-3):
        if net[i] == net[i+3] and net[i+1] == net[i+2] and net[i] != net[i+1]:
            return True

def isTLSIP(ip):
    result = False
    supernets, hypernets = split_ip(ip)

    for net in supernets:
        if isABBAString(net):
            result = True
            break

    for net in hypernets:
        if isABBAString(net):
            result = False
            break

    return result

def getABAs(net):
    abas = []
    for i in xrange(0, len(net)-2):
        if net[i] == net[i+2] and net[i] != net[i+1]:
            abas.append((net[i], net[i+1]))
    return abas

def isSSLIP(ip):
    supernets, hypernets = split_ip(ip)

    for net in supernets:
        abas = getABAs(net)
        for aba in abas:
            bab = ''.join((aba[1], aba[0], aba[1]))
            for h_net in hypernets:
                if bab in h_net:
                    return True

    return False
