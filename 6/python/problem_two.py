from solution import ModifiedMessageCorrector


mc = ModifiedMessageCorrector(8)

with open('../input', 'rb') as handle:
    for line in handle:
        mc.addMessage(line.strip())

print "Message:", mc.getMessage()
