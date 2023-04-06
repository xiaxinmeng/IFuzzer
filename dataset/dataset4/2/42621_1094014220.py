from mmap import mmap
f = open('test.out', 'ab+')
f.write('ABCDEabcde')
f.flush()
m = mmap(f.fileno(), 10)
m.move(5, 0, 5)
m.read(10)