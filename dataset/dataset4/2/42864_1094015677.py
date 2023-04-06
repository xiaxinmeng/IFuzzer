import sys, os, mmap

for i in xrange(2000):
  f = os.open('/dev/zero', os.O_RDWR)
  m = mmap.mmap(f, 10000)
  os.close(f)
  a = m[0:100]
  m[100:200] = 'F' * 100
  m.close()