from ctypes import *
 
i = int('7f94e57c', 16)
cp = pointer(c_int(i))
fp = cast(cp, POINTER(c_float))
print(fp.contents.value) # nan
p = pointer(c_float(fp.contents.value))
ip = cast(p, POINTER(c_int))
print(hex(ip.contents.value)) #'0x7fd4e57c'