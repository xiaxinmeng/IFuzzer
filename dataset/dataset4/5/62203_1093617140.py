import lzma, io
filename = "pacman.log.xz"  # 256206 lines; 389 kB -> 13 MB

# Basic case
reader = lzma.LZMAFile(filename)  # 3.2 s

# Add __iter__() optimization
def lzma_iter(self):
    self._check_can_read()
    return iter(self._buffer)
lzma.LZMAFile.__iter__ = lzma_iter  # 1.31 s

# Add “closed” optimization
def decompressor_closed(self):
    return self._decompressor is None
import _compression
_compression.DecompressReader.closed = property(decompressor_closed)  # 0.53 s