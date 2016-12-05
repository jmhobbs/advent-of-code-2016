from hashlib import md5


def find_password(prefix):
    i = 0
    password = []
    while True:
        hash = md5()
        hash.update("%s%d" % (prefix, i))
        hash = hash.hexdigest()
        if hash[:5] == '00000':
            password.append(hash[5])
            if len(password) == 8:
                return ''.join(password)
        i += 1


def find_second_password(prefix):
    i = 0
    password = [None, None, None, None, None, None, None, None]
    while True:
        hash = md5()
        hash.update("%s%d" % (prefix, i))
        hash = hash.hexdigest()
        if hash[:5] == '00000':
            pos = int(hash[5], 16)
            if pos <= 7:
                if password[pos] is None:
                    password[pos] = hash[6]
                    if len(filter(None, password)) == 8:
                        return ''.join(password)
        i += 1
