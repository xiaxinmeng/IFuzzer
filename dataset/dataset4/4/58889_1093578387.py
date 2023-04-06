import zlib
zdict = b"thequickbrownfoxjumped\x00"
c = zlib.compressobj()
c.set_dictionary (zdict)
cd = c.compress (b"the quick brown fox jumped over the candlestick")
cd += c.flush()
d = zlib.decompressobj()
try:
    print (d.decompress (cd))
except zlib.error as what:
    if what.args[0].startswith ('Error 2 '):
        d.set_dictionary (zdict)
        print (d.flush())