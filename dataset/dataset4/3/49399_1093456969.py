from ctypes import *

class foo(Structure):
  _fields_ = [ ( "bar", c_char_p ) ]

foofoo = foo()

babar = create_string_buffer(32)

foofoo.bar = babar