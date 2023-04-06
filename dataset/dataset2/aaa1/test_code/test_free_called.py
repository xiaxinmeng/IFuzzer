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

def test_free_called():
    f = CoExtra.get_func()
    test_code.SetExtra(f.__code__, test_code.FREE_INDEX, ctypes.c_voidp(100))
    del f
    CoExtra.assertEqual(test_code.LAST_FREED, 100)

CoExtra = test_code.CoExtra()
test_free_called()
