import os
os.utime('foo.txt', ns=(BadInt(), 1))