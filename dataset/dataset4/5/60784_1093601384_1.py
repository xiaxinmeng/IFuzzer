def to_bytes(n, length, order):
    indexes = range(length) if order == 'little' else reversed(range(length))
    return bytes((n >> i*8) & 0xff for i in indexes)