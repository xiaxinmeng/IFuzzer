from ctypes import *
import struct

i = int('7f94e57c', 16)
cp = pointer(c_int(i))
fp = cast(cp, POINTER(c_float))
print(fp.contents.value) # nan
print(struct.pack(">f", fp.contents.value).hex()) # 7fd4e57c