from ctypes import *

testlib = windll.LoadLibrary('testlib')
testfun = testlib.test

class objid(Structure):
    _fields_ = [('bytes', c_ubyte*16)]

print('Calling...')
testfun(objid(), c_wchar_p('test'))
print('Done.')