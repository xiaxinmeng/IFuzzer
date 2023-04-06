def hexlify(b):
    return "%02x"*len(b) % tuple(map(ord, b))