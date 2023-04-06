
from test.support import gc_collect
a = [1, 2, 3]
b = [a]

# Simulate the refcount of "a" being too low (compared to the
# references held on it by live data), but keeping it above zero
# (to avoid deallocating it):
import ctypes
ctypes.pythonapi.Py_DecRef(ctypes.py_object(a))

# The garbage collector should now have a fatal error
# when it reaches the broken object
gc_collect()
