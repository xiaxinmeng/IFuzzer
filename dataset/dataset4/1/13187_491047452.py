
import _testcapi
import sys

def hook_func(*args):
    raise Exception("hook_func failed")

sys.unraisablehook = hook_func
_testcapi.write_unraisable(ValueError(42), None)
