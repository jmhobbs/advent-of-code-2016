from solution import split_room_string, is_real_room, decrypt

with open('../input', 'rb') as handle:
    for line in handle:
        name, sector, checksum = split_room_string(line)
        if is_real_room(name, checksum):
            plaintext = decrypt(name, int(sector))
            if "north" in plaintext:
                print "[%s] %s" % (sector, plaintext)
