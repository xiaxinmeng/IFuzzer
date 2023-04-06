import mmap

fn = 'issue35686.bin'

with open(fn, 'wb') as fd:
    fd.write(b'x' * 10000)

with open(fn, 'rb') as fd:
    with mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_READ) as mm:
        data = memoryview(mm)
        data = data[1:]
        print("before memoryview release")
        data.release()
        print("before mmap cm exit")
    print("before file cm exit")
