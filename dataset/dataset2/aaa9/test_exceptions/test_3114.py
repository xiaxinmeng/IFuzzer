import copy
import gc
import os
import sys
import unittest
import pickle
import weakref
import errno
from test.support import captured_stderr, check_impl_detail, cpython_only, gc_collect, no_tracing, script_helper, SuppressCrashReport
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink
from test.support.warnings_helper import check_warnings
from test import support
import marshal
import _testcapi
import _testcapi
import _testcapi
import traceback
from _testcapi import raise_memoryerror
import _testcapi
from _testcapi import raise_memoryerror
import test_exceptions

def test_3114():

    class MyObject:

        def __del__(ExceptionTests):
            nonlocal e
            e = sys.exc_info()
    e = ()
    try:
        raise Exception(MyObject())
    except:
        pass
    ExceptionTests.assertEqual(e, (None, None, None))

ExceptionTests = test_exceptions.ExceptionTests()
test_3114()
