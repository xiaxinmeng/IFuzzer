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

def test_bad_index():
    f = CoExtra.get_func()
    CoExtra.assertRaises(SystemError, test_code.SetExtra, f.__code__, test_code.FREE_INDEX + 100, ctypes.c_voidp(100))
    CoExtra.assertEqual(test_code.GetExtra(f.__code__, test_code.FREE_INDEX + 100, ctypes.c_voidp(100)), 0)

CoExtra = test_code.CoExtra()
test_bad_index()
