
import zlib


hello = b'hello'

# Compress data using deflate and shared/predefined dict.
co = zlib.compressobj(wbits=-zlib.MAX_WBITS, zdict=hello)
data = co.compress(hello) + co.flush()

# Decompress deflate by providing same dict.
do = zlib.decompressobj(wbits=-zlib.MAX_WBITS, zdict=hello)
data = do.decompress(data)

print(data)
