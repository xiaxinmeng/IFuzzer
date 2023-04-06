import os

stdin = os.dup(0)
os.close(0)
tty = os.open("/dev/tty", os.O_RDONLY)
assert tty == 0

import readline
print("input:", input())
print("in:", os.read(stdin, 128))