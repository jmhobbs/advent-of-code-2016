class Keypad(object):

    pad = (('1', '2', '3'),
           ('4', '5', '6'),
           ('7', '8', '9'))

    def __init__(self):
        self.row = 1
        self.column = 1

    def move(self, direction):
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
            self.move(direction)

        return self.pad[self.row][self.column]


class InfuriatingKeypad(Keypad):

    pad = ((' ', ' ', '1', ' ', ' '),
           (' ', '2', '3', '4', ' '),
           ('5', '6', '7', '8', '9'),
           (' ', 'A', 'B', 'C', ' '),
           (' ', ' ', 'D', ' ', ' '))

    def __init__(self):
        super(Keypad, self).__init__()
        self.row = 2
        self.column = 0

    def move(self, direction):
        d_row = self.row
        d_column = self.column

        if direction == 'U':
            d_row = max(0, self.row - 1)
        elif direction == 'L':
            d_column = max(0, self.column - 1)
        elif direction == 'D':
            d_row = min(4, self.row + 1)
        elif direction == 'R':
            d_column = min(4, self.column + 1)

        if self.pad[d_row][d_column] != ' ':
            self.row = d_row
            self.column = d_column
