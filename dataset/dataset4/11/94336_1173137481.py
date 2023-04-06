
from test import support
import sys
for i in range(1, 10):
    support.run_in_subinterp("import multiprocessing")
    print("refs:", sys.gettotalrefcount(), "blocks: ", sys.getallocatedblocks())
