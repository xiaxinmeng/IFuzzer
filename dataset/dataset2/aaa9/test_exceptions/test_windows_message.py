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

@unittest.skipUnless(sys.platform == 'win32', 'test specific to Windows')
def test_windows_message():
    """Should fill in unknown error code in Windows error message"""
    ctypes = import_module('ctypes')
    code = 3765269347
    with ExceptionTests.assertRaisesRegex(OSError, 'Windows Error 0x%x' % code):
        ctypes.pythonapi.PyErr_SetFromWindowsErr(code)

ExceptionTests = test_exceptions.ExceptionTests()
test_windows_message()
