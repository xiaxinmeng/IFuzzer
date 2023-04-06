import mmap, re

f = open("/tmp/arandomfile", "w+")
f.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxx')
f.flush()
m = mmap.mmap(f.fileno(), 0)
iter = re.finditer(b'a', m)
m.close()
list(iter)
