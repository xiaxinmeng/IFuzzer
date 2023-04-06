# I recommend filling the disk almost full with some better tool.
import os
import errno

fill = 'J:/fill.txt'
try:
    with open(fill, 'wb') as f:
        while True:
            n = f.write(b"\0")
except IOError as e:
    if e.errno == errno.ENOSPC:
        os.remove(fill)