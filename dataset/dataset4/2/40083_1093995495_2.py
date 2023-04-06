def stringToLong(s):
    return long('\0'+s, 256)

def longToString(n):
    s = n.tostring()
    if s[0] == '\0' and s != '\0':
        s = s[1:]
    return s