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

def test_capi2():
    import _testcapi
    try:
        _testcapi.raise_exception(BadException, 0)
    except RuntimeError as err:
        (exc, err, tb) = sys.exc_info()
        co = tb.tb_frame.f_code
        ExceptionTests.assertEqual(co.co_name, '__init__')
        ExceptionTests.assertTrue(co.co_filename.endswith('test_exceptions.py'))
        co2 = tb.tb_frame.f_back.f_code
        ExceptionTests.assertEqual(co2.co_name, 'test_capi2')
    else:
        ExceptionTests.fail('Expected exception')

ExceptionTests = test_exceptions.ExceptionTests()
test_capi2()
