fd = os.open("my_file", os.O_DIRECT | os.O_RDWR)
f = os.fdopen(fd, "rb+", 0)
m = mmap.mmap(-1, 4096)
f.readinto(m)