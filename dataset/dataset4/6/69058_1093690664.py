_table = [chr(i) for i in range(128)] + [chr(i) for i in range(0xdc80, 0xdd00)]

def decode_surroundescape(s):
    return s.decode('latin1').translate(_table)