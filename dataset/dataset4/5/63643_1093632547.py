fd = os.open(...)
mmap = mmap.mmap(fd, size)
# do some stuff
os.close(fd)