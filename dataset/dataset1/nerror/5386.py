import mmap
m = mmap.mmap(-1, 1)
for i in range(10000): # enough?
    print(i)
    m.write_byte('1') # crash
