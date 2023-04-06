import os, io
fd = os.open( "./4841.py", os.O_RDONLY)
s1 = os.fdopen(fd)
s2 = io.open(fd)
os.close(fd)
s1.close()
s2.close()
