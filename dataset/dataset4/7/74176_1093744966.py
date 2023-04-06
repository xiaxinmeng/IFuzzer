# legal sequence b'\x81\x31\x81\x30' is decoded to U+060A, it's fine.
uchar = b'\x81\x31\x81\x30'.decode('gb18030')
print(hex(ord(uchar)))

# illegal sequence 0x8130FF30 can be decoded to U+060A as well, this should not happen.
uchar = b'\x81\x30\xFF\x30'  .decode('gb18030')
print(hex(ord(uchar)))