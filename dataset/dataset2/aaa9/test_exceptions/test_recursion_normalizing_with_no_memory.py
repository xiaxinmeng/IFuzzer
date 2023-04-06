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

@cpython_only
def test_recursion_normalizing_with_no_memory():
    code = 'if 1:\n            import _testcapi\n            class C(): pass\n            def recurse(cnt):\n                cnt -= 1\n                if cnt:\n                    recurse(cnt)\n                else:\n                    _testcapi.set_nomemory(0)\n                    C()\n            recurse(16)\n        '
    with SuppressCrashReport():
        (rc, out, err) = script_helper.assert_python_failure('-c', code)
        ExceptionTests.assertIn(b'Fatal Python error: _PyErr_NormalizeException: Cannot recover from MemoryErrors while normalizing exceptions.', err)

ExceptionTests = test_exceptions.ExceptionTests()
test_recursion_normalizing_with_no_memory()
