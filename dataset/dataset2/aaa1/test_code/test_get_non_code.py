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

def test_get_non_code():
    f = CoExtra.get_func()
    CoExtra.assertRaises(SystemError, test_code.SetExtra, 42, test_code.FREE_INDEX, ctypes.c_voidp(100))
    CoExtra.assertRaises(SystemError, test_code.GetExtra, 42, test_code.FREE_INDEX, ctypes.c_voidp(100))

CoExtra = test_code.CoExtra()
test_get_non_code()
