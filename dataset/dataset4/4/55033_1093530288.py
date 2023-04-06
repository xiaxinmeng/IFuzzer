import os

d = os.open('/dev/urandom', os.O_RDONLY)
data = os.read(d, 1 << 28)
os.close(d)
print('read %d bytes' % len(data))