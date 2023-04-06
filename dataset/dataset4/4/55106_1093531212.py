with open("hello.txt", "r+b") as f:
    # memory-map the file, size 0 means whole file
    map = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(map.readline())  # prints b"Hello Python!\n"
    # read content via slice notation
    print(map[:5])  # prints b"Hello"
    # update content using slice notation;
    # note that new content must have same size
    map[6:] = b" world!\n"
    # ... and read again using standard file methods
    map.seek(0)
    print(map.readline())  # prints b"Hello  world!\n"
    # close the map
    map.close()