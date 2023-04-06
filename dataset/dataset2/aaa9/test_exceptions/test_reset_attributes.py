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

def test_reset_attributes():
    exc = ImportError('test', name='name', path='path')
    ImportErrorTests.assertEqual(exc.args, ('test',))
    ImportErrorTests.assertEqual(exc.msg, 'test')
    ImportErrorTests.assertEqual(exc.name, 'name')
    ImportErrorTests.assertEqual(exc.path, 'path')
    exc.__init__()
    ImportErrorTests.assertEqual(exc.args, ())
    ImportErrorTests.assertEqual(exc.msg, None)
    ImportErrorTests.assertEqual(exc.name, None)
    ImportErrorTests.assertEqual(exc.path, None)

ImportErrorTests = test_exceptions.ImportErrorTests()
test_reset_attributes()
