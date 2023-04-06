import marshal
import sys

f = open('data.bin', 'rb')
t = marshal.load(f)
print('Python version:', sys.version)
print('Object just loaded was:\n%r' % (t,))
print('File position is now at %d' % f.tell())
t = marshal.load(f)
print('Object just loaded was:\n%r' % (t,))
print('File position is now at %d' % f.tell())