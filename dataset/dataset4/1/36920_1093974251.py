# example - with a webcam on /dev/video0:
import os, mmap
fd = os.open("/dev/video0",os.O_RDONLY)
mm = mmap.mmap(fd, 1024, mmap.MAP_SHARED)