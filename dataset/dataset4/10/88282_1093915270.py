import sys
import gc

for i in range(10):
    import csv
    del sys.modules['_csv']
    del sys.modules['csv']
    del csv
    gc.collect()

    print(sys.gettotalrefcount())