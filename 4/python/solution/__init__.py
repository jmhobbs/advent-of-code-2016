import re

def is_real_room(name, checksum):
    counts = {}
    nameL = list(name.replace('-', ''))
    for letter in set(nameL):
        counts[letter] = nameL.count(letter)

    scored = sorted(counts.items(), key=lambda x: (-1 * x[1], x[0]))
    return checksum == ''.join(map(lambda x: x[0], scored[:5]))

ROOM_STRING_PATTERN = re.compile('^([a-z\-]+)-([0-9]+)\[([a-z]+)')

def split_room_string(room_string):
    result = ROOM_STRING_PATTERN.match(room_string)
    return result.groups()
