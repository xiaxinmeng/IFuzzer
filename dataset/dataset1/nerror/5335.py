import mmap, tempfile
f = tempfile.TemporaryFile()
m1 = mmap.mmap(f.fileno(), 1000, tagname="foo")
m2 = mmap.mmap(f.fileno(), 5000, tagname="foo") # use same tagname, but

print(len(m2[:])) # crash
