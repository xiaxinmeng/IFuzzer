
import mmap


with open('test.dat', 'wb') as fh:
    fh.write(b'abcdefghijklmnopqrstuvwxyz')


with open('test.dat', 'rb') as fh:
    mm = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)


with open('test.dat', 'wb') as fh:
    pass  # Note: if something is written, then I get no bus error.


mm[2]
