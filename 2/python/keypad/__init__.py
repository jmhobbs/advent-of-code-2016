class Keypad(object):

    pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9))

    def __init__(self):
        self.row = 1
        self.column = 1

    def __move(self, direction):
        if direction == 'U':
            self.row = max(0, self.row - 1)
        elif direction == 'L':
            self.column = max(0, self.column - 1)
        elif direction == 'D':
            self.row = min(2, self.row + 1)
        elif direction == 'R':
            self.column = min(2, self.column + 1)

    def executeRow(self, guide):
        for direction in guide:
            self.__move(direction)

        return self.pad[self.row][self.column]
