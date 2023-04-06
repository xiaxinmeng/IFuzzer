def to_bytes(n, length, order):
    if order == 'little':
        return bytes((n >> i*8) & 0xff for i in range(length))
    elif order == 'big':
        return bytes((n >> i*8) & 0xff for i in reversed(range(length)))