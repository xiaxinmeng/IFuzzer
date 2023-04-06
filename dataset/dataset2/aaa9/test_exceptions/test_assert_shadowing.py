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

@unittest.skipUnless(__debug__, "Won't work if __debug__ is False")
def test_assert_shadowing():
    global AssertionError
    AssertionError = TypeError
    try:
        assert False, 'hello'
    except BaseException as e:
        del AssertionError
        ExceptionTests.assertIsInstance(e, AssertionError)
        ExceptionTests.assertEqual(str(e), 'hello')
    else:
        del AssertionError
        ExceptionTests.fail('Expected exception')

ExceptionTests = test_exceptions.ExceptionTests()
test_assert_shadowing()
