import inspect
import sys
import threading
import unittest
import weakref
import ctypes
from test.support import run_doctest, run_unittest, cpython_only, check_impl_detail
import _testcapi
from types import FunctionType
from test import test_code
import test_code

def test_get_set():
    f = CoExtra.get_func()
    extra = ctypes.c_voidp()
    test_code.SetExtra(f.__code__, test_code.FREE_INDEX, ctypes.c_voidp(200))
    test_code.SetExtra(f.__code__, test_code.FREE_INDEX, ctypes.c_voidp(300))
    CoExtra.assertEqual(test_code.LAST_FREED, 200)
    extra = ctypes.c_voidp()
    test_code.GetExtra(f.__code__, test_code.FREE_INDEX, extra)
    CoExtra.assertEqual(extra.value, 300)
    del f

CoExtra = test_code.CoExtra()
test_get_set()
