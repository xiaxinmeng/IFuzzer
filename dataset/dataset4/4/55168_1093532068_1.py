with open("/tmp/rnd", "wb") as f:
    f.write(b"X" * 115699)

with open("/tmp/rnd", "w+b") as f:
    with mmap.mmap(f.fileno(), 0, offset=2147479552) as m:
        print(len(m))
        for i in m:
            print(m[i])