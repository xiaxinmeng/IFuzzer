f = open('test.x', 'w+b')
f.write(b'\x00' * 10)
f.flush()

fm = mmap.mmap(f.fileno(), 0)
fm.close()
f.truncate(5 * 1024 ** 3)

# mmap only 1GiB of the 5GiB file
fm = mmap.mmap(f.fileno(), 1024**3)
fm.close()

f.close()