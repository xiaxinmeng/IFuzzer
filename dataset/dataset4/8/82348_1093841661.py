import mmap
import os

fd = os.open(path_to_file, os.O_DIRECT | os.O_RDWR)
fo = os.fdopen(fd, 'rb+')
m = mmap.mmap(-1, 4096)
fo.readinto(m)