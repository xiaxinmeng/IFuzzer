import sys
foo = b''

for i in range (0,10):
    foo += bytes(i)

sys.stdout.buffer.write(foo)