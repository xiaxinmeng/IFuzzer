for i in range(0x10000, 0x40000, 32):
    chars = ''.join(chr(i+j) for j in range(32))
    print(hex(i), chars)