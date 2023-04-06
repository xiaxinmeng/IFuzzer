from ctypes import *
libc = CDLL("libc.so.6")
print(libc.printf(c_char_p("An int %d, a double %f\n"), 1234,
c_double(3.14)))