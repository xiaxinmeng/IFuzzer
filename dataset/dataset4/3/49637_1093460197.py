import mmap
data = mmap.mmap(-1, 1)
data.move(1,1,-1) # crash