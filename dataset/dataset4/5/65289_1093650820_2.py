import os
read, write = os.openpty()
os.write(write, b'ok\n')
os.close(write)
print("read: %r" % os.read(read, 4096))
print("read: %r" % os.read(read, 4096))