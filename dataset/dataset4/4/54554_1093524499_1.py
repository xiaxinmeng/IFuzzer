#!/usr/bin/python
from fcntl import ioctl
EVIOCGID = 1
f = open('/dev/input/mouse0', 'w')
buf = bytes([0]*128)
a = (f.fileno(),)
print(a.__class__, a)
ioctl(a, EVIOCGID, buf, True)
print(buf)