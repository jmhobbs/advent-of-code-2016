from solution import split_room_string, is_real_room

sector_sum = 0
with open('../input', 'rb') as handle:
    for line in handle:
        name, sector, checksum = split_room_string(line)
        if is_real_room(name, checksum):
            sector_sum = sector_sum + int(sector)

print "Sum of valid room sectors is %d." % sector_sum
