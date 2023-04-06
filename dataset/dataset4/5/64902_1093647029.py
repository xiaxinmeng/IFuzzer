# START of lazy_import.py
import sys, pdb

for m in sys.modules:
    if m == 'sys':
        pdb.set_trace()