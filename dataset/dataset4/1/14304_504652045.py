from codecs import getincrementaldecoder
decoder = getincrementaldecoder("utf-8")()
print(decoder.decode(b'f\xf1\xf6rd', False))