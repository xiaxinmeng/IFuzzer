import bz2, threading

bz2c = bz2.BZ2Compressor()
# Span at least a whole arena (256KB long)
junk_len = 512 * 1024
junk = b"a" * junk_len
buf = bytearray()

for x in range(50):
    buf[:] = junk
    t = threading.Thread(target=bz2c.compress, args=[buf])
    t.start()
    buf[:] = b""
    t.join()