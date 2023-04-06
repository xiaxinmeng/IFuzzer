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

def test_free_different_thread():
    f = CoExtra.get_func()

    class ThreadTest(threading.Thread):

        def __init__(CoExtra, f, test):
            super().__init__()
            CoExtra.f = f
            CoExtra.test = test

        def run(CoExtra):
            del CoExtra.f
            CoExtra.test.assertEqual(test_code.LAST_FREED, 500)
    test_code.SetExtra(f.__code__, test_code.FREE_INDEX, ctypes.c_voidp(500))
    tt = ThreadTest(f, CoExtra)
    del f
    tt.start()
    tt.join()
    CoExtra.assertEqual(test_code.LAST_FREED, 500)

CoExtra = test_code.CoExtra()
test_free_different_thread()
