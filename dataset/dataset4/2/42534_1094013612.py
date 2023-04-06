fp = open(fn, 'rb')
b = mmap.mmap(fp.fileno(), os.stat(fp.name).st_size,
access=mmap.ACCESS_READ)