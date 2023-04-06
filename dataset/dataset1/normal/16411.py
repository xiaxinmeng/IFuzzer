import zlib

data = zlib.compress(b'abcdefghijklmnopqrstuvwxyz')
d = zlib.decompressobj()
d.decompress(data, 1)
del data
data = zlib.compress(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# Should be a prefix of b'bcdefghijklmnopqrstuvwxyz',
# but I get b'bcDEFGHIJKLMNOPQRSTUVWXYZ' instead:
print(repr(d.flush()))
