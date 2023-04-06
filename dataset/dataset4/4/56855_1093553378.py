c = zlib.compressobj()
s = c.compress(b'This is just a test string.')
s += c.flush(zlib.Z_FULL_FLUSH)