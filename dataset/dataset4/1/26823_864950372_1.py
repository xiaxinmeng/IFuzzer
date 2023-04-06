
import _testcapi
import faulthandler
import gc
import sys

faulthandler.enable()

class RefCycle:
    def __del__(self):
        _testcapi.fatal_error(b'bug')

# create a reference cycle which triggers a fatal
# error in a destructor
a = RefCycle()
b = RefCycle()
a.b = b
b.a = a

# Delete the objects, not the cycle
a = None
b = None

# Break the reference cycle: call __del__()
gc.collect()

# Should not reach this line
print("exit", file=sys.stderr)
