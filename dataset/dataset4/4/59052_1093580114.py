import sys
b'x'.decode('utf-8')
import locale; del locale.encodings   # Not necessary with python2
del sys.modules['encodings.utf_8'], sys.modules['encodings']
b'x'.decode('utf-8')