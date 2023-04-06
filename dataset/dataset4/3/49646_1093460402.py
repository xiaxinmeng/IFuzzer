import mmap
import os

fd = os.open('/dev/dm-2', os.O_DIRECT | os.O_RDWR)  # mapped block device
fo = os.fdopen(fd, 'rb+')
m = mmap.mmap(-1, 4096)
fo.readinto(m)