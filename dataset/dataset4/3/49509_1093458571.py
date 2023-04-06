# original version
def encode_plain(user, password):
    return encode_base64("\0%s\0%s" % (user, password))

# fixed version. Note that "eol=''" is given in Python 2.6's smtplib.
def encode_plain(user, password):
    s = "\0%s\0%s" % (user, password)
    return encode_base64(s.encode('ascii'), eol='')