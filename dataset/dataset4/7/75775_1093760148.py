def mymaketrans(mapping):
    table = bytearray(range(256))
    for x, y in mapping.items():
        table[x] = y
    return table