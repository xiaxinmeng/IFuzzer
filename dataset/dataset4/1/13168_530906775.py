import gc
import sys
import _xxsubinterpreters as interpreters

gettotalrefcount = sys.gettotalrefcount

for i in range(14):
    gc.collect()
    refs_before = gettotalrefcount()
    sub = interpreters.create()
    del sub
    gc.collect()
    refs_after = gettotalrefcount()
    if i > 3:
        print(refs_before == refs_after, refs_before, refs_after)