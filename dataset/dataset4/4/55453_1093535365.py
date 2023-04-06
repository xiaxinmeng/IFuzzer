# test.py
from dis import dis

def x(var): return var in {1,2,3} # Note curly braces.  These are sets.
def y(var): return var in {1,-2,3}