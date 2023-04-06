import bz2
import sys
import time

if len(sys.argv) != 2:
    exit(1)

total = 0
with bz2.BZ2File(sys.argv[1], 'r', buffering=8192) as input:
    while True:
        bytes = input.read(8192)
        bytes = len(bytes)
        total += bytes
        print('{} {}'.format(total, bytes))
        if bytes < 8192:
            time.sleep(0.5)