import sys, os
from ctypes import *

if len(sys.argv) != 2:
    sys.exit('Error: the symbol name is required.')
symbol = sys.argv[1]
libdl = CDLL('libdl.so')
libdl.dlopen.restype = c_void_p
libdl.dlsym.restype = c_void_p
hdle = libdl.dlopen(None, os.RTLD_NOW | RTLD_GLOBAL)
if hdle is None:
    print('Cannot get a handle on the global symbol object.')
else:
    v = libdl.dlsym(c_void_p(hdle), symbol.encode())
    _not = 'not ' if v is None else ''
    print('The symbol "%s" is %sresolved.' % (symbol, _not))