import bdb
for memory_leak in xrange(10000000):
     b = bdb.Bdb()
     b.run('i=0', {}, {})