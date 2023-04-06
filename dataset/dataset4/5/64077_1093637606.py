import bz2
obj = bz2.BZ2File('bla.bz2')
for loop in range(1024*10):
    obj.__init__('bla.bz2')