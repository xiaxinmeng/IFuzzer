import mmap
m = mmap.mmap(-1, 5)
try:
    m.resize(-1)
except WindowsError:
    pass
m[0] = '1' # crash
