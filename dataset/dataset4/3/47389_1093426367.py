import bz2, threading
bz2c = bz2.BZ2Compressor()
b = bytearray(b"a" * 1000000)
def f():
    for x in range(10):
        b[:] = b""
        b[:] = bytearray(b"a" * 1000000)
threading.Thread(target=f).start()
for x in range(10):
    bz2c.compress(b)