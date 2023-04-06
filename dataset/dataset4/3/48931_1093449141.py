import mmap

f = open('test.x', 'w+b')
f.write(b'\x00' * 10)
f.flush()

fm = mmap.mmap(f.fileno(), 0)
fm.resize(5 * 1024 ** 3)
fm.close()

f.close()