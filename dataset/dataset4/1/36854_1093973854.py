f = open('in.txt', 'rb')
m = mmap.mmap(f.fileno(), 0, 
access=mmap.ACCESS_READ)
f.close()