fm = open("5GiB.sparse", "w+b")
fm.truncate(5 * 2**30)
m = mmap(fm.fileno(), 0)
z = compress(m)