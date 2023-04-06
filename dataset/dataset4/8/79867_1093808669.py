with open(fn, 'rb') as fd:
    with mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_READ) as mm:
        with memoryview(mm) as data:
            with data[:2] as theslice:
                print(theslice)