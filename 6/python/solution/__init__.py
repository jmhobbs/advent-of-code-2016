class MessageCorrector(object):

    def __init__(self, length=6):
        self.counters = []
        for i in xrange(0, length):
            self.counters.append({})

    def addMessage(self, message):
        length = len(message)
        for i in xrange(0, length):
            if message[i] not in self.counters[i]:
                self.counters[i][message[i]] = 0
            self.counters[i][message[i]] += 1

    def getMessage(self):
        message = []
        for letter in self.counters:
            scored = sorted(letter.items(), key=lambda x: (-1 * x[1], x[0]))
            message.append(scored[0][0])
        return ''.join(message)
