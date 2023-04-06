import os
import sys

def foo(f, e, o):
    pass
    
sys.settrace(foo)

import __main__
execfile('test_broken.py', __main__.__dict__)