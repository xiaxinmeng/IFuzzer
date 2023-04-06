# legal sequence 0x81319130 is decoded to U+060A, it's fine.
b = bytes([0x81, 0x31, 0x81, 0x30])
uchar = b.decode('gb18030')
print(ord(uchar))

# illegal sequence 0x8130FF30 can be decoded to U+060A as well.
b = bytes([0x81, 0x30, 0xFF, 0x30])  
uchar = b.decode('gb18030')
print(ord(uchar))