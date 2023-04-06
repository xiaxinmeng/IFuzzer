def stringToLong(s):
    return long(binascii.hexlify(s), 16)

def longToString(n):
    return binascii.unhexlify("%x" % n)