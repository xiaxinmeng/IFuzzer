with open(fn, 'rb') as fd:
    with mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_READ) as mm:
        with memoryview(mm)[:2] as data:
            print(data)