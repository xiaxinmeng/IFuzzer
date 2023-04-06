import ctypes

s = 'a'*(0xffffffff/2-0xffff)
sss = 'a'*(0xffffffff/4)
ctypes.set_conversion_mode(s, s)
