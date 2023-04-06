# START of refleak.py
import sys, gc, pdb

i = 1
while i:
    pdb.set_trace()
    x = 1
    gc.collect(); print(sys.gettotalrefcount())